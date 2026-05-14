const express = require('express');
const { Pool } = require('pg');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());

const pool = new Pool({
    connectionString: process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/qubicoin_db'
});

const JWT_SECRET = process.env.JWT_SECRET || 'STG_SUPER_SECRET_CORE_KEY_2026';

// Middleware: Otentikasi Token Keamanan Session
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; // Membaca format Bearer Token
    if (!token) return res.status(401).json({ error: 'Sesi akses kadaluarsa atau tidak sah.' });

    jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) return res.status(403).json({ error: 'Tanda tangan token ilegal.' });
        req.user = user;
        next();
    });
};

// --- AUTH ROUTING PORTALS ---
app.post('/api/auth/register', async (req, res) => {
    const { username, email, password, walletAddress } = req.body;
    try {
        const hashedPassword = await bcrypt.hash(password, 10);
        const client = await pool.connect();
        try {
            await client.query('BEGIN');
            const userRes = await client.query(
                'INSERT INTO users (username, email, password_hash, wallet_address) VALUES ($1, $2, $3, $4) RETURNING id, username',
                [username, email, hashedPassword, walletAddress ? walletAddress.toLowerCase() : null]
            );
            const newUser = userRes.rows[0];

            // Memberikan modal awal saldo simulasi bank sebesar Rp 1.500.000,00 secara otomatis
            await client.query(
                'INSERT INTO internal_balances (user_id, currency, fiat_balance, qbc_offchain_balance) VALUES ($1, $2, $3, $4)',
                [newUser.id, 'IDR', 1500000.00, 0.00]
            );

            await client.query('COMMIT');
            res.status(201).json({ message: 'Registrasi Berhasil', user: newUser });
        } catch (err) {
            await client.query('ROLLBACK');
            throw err;
        } finally {
            client.release();
        }
    } catch (err) {
        res.status(500).json({ error: 'Registrasi Gagal.', detail: err.message });
    }
});

app.post('/api/auth/login', async (req, res) => {
    const { email, password } = req.body;
    try {
        const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
        if (result.rows.length === 0) return res.status(400).json({ error: 'Email atau password tidak akurat.' });

        const user = result.rows[0];
        const validPassword = await bcrypt.compare(password, user.password_hash);
        if (!validPassword) return res.status(400).json({ error: 'Email atau password tidak akurat.' });

        const token = jwt.sign({ id: user.id, username: user.username }, JWT_SECRET, { expiresIn: '24h' });
        res.json({ token, user: { id: user.id, username: user.username, wallet: user.wallet_address } });
    } catch (err) {
        res.status(500).json({ error: 'Kegagalan otentikasi internal.' });
    }
});

app.get('/api/banking/dashboard', authenticateToken, async (req, res) => {
    try {
        const balanceRes = await pool.query('SELECT * FROM internal_balances WHERE user_id = $1', [req.user.id]);
        const historyRes = await pool.query(
            `SELECT * FROM transactions WHERE sender_id = $1 OR recipient_id = $1 ORDER BY created_at DESC LIMIT 10`, [req.user.id]
        );
        res.json({ balances: balanceRes.rows, activityLogs: historyRes.rows });
    } catch (err) {
        res.status(500).json({ error: 'Gagal mengambil data akuntansi server.' });
    }
});

// --- ENGINE UTAMA: SISTEM PEMBAYARAN VIA QR CODES (OFF-CHAIN LEDGER DEBIT) ---
app.post('/api/banking/qr-pay', authenticateToken, async (req, res) => {
    const { merchantId, amount } = req.body;
    
    if (!amount || amount <= 0) return res.status(400).json({ error: 'Jumlah transfer pembayaran wajib bernilai positif.' });

    const client = await pool.connect();
    try {
        await client.query('BEGIN');

        // 1. Periksa ketersediaan likuiditas / saldo pembayar (IDR)
        const balanceCheck = await client.query(
            'SELECT fiat_balance FROM internal_balances WHERE user_id = $1 AND currency = $2 FOR UPDATE',
            [req.user.id, 'IDR']
        );
        
        if (balanceCheck.rows.length === 0) return res.status(404).json({ error: 'Dompet mata uang IDR tidak aktif.' });
        
        const currentBalance = parseFloat(balanceCheck.rows[0].fiat_balance);
        if (currentBalance < amount) return res.status(400).json({ error: 'Gagal Transaksi: Likuiditas saldo IDR Anda tidak mencukupi.' });

        // 2. Kurangi saldo pembayar
        await client.query(
            'UPDATE internal_balances SET fiat_balance = fiat_balance - $1 WHERE user_id = $2 AND currency = $3',
            [amount, req.user.id, 'IDR']
        );

        // 3. Catat entri riwayat ke tabel audit transaksi ekosistem
        await client.query(
            `INSERT INTO transactions (sender_id, recipient_id, tx_type, amount, currency, status) 
             VALUES ($1, NULL, $2, $3, $4, $5)`,
            [req.user.id, `QR_PAYMENT:${merchantId}`, amount, 'IDR', 'COMPLETED']
        );

        await client.query('COMMIT');
        res.json({ message: 'Pembayaran QR diproses instan dengan status sukses.' });
    } catch (err) {
        await client.query('ROLLBACK');
        res.status(500).json({ error: 'Pemrosesan mesin QR perbankan gagal.', detail: err.message });
    } finally {
        client.release();
    }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🛰️ STG Core Hub Engine & Perbankan QR Aktif di Port: ${PORT}`));
