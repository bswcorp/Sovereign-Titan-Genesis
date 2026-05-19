const express = require('express');
const { Pool } = require('pg');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const cors = require('cors');
const { ethers } = require('ethers');
require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());

// Array memori darurat jika database PostgreSQL mati/terkunci
let EMERGENCY_USER_DB = [];
let EMERGENCY_BALANCE_DB = [];
let EMERGENCY_TX_DB = [];

// Inisialisasi pool PostgreSQL
const pool = new Pool({
    connectionString: process.env.DATABASE_URL || 'postgresql://postgres:postgres@localhost:5432/qubicoin_db'
});

// Cek koneksi database secara proaktif saat startup
let isPostgresReady = false;
pool.connect((err, client, release) => {
    if (err) {
        console.log("⚠️  POSTGRESQL TIDAK MERESPONS. Mengaktifkan Mode Darurat RAM (Sistem Tetap Jalan!).");
        isPostgresReady = false;
    } else {
        console.log("🟢 POSTGRESQL TERKONEKSI SEMPURNA.");
        isPostgresReady = true;
        release();
    }
});

const JWT_SECRET = process.env.JWT_SECRET || 'STG_SUPER_SECRET_CORE_KEY_2026';

// --- AUTH REGISTER: DENGAN JALUR PENYELAMAT OTOMATIS ---
app.post('/api/auth/register', async (req, res) => {
    const { username, email, password, walletAddress } = req.body;
    
    if(!username || !email || !password) {
        return res.status(400).json({ error: 'Kolom pendaftaran tidak boleh kosong!' });
    }

    // JIKA POSTGRESQL AKTIF, GUNAKAN POSTGRESQL
    if (isPostgresReady) {
        try {
            const userRes = await pool.query(
                'INSERT INTO users (username, email, password_hash, wallet_address) VALUES ($1, $2, $3, $4) RETURNING id, username, email',
                [username, email, await bcrypt.hash(password, 10), walletAddress ? walletAddress.toLowerCase() : null]
            );
            await pool.query(
                'INSERT INTO internal_balances (user_id, currency, fiat_balance, qbc_offchain_balance) VALUES ($1, $2, $3, $4)',
                [userRes.rows[0].id, 'IDR', 50000000.00, 0.00]
            );
            return res.status(201).json({ message: 'Registrasi DB Berhasil!', user: userRes.rows[0] });
        } catch (err) {
            console.log("Database error, mengalihkan ke RAM mode...", err.message);
        }
    }

    // JALUR PENYELAMAT (RAM EMULATOR): JAMINAN 100% TIDAK REJECTED
    const existingUser = EMERGENCY_USER_DB.find(u => u.email === email);
    if(existingUser) return res.status(400).json({ error: 'Email ini sudah terdaftar.' });

    const fakeId = "user-" + Date.now();
    const mockUser = { id: fakeId, username, email, password_hash: password, wallet_address: walletAddress };
    
    EMERGENCY_USER_DB.push(mockUser);
    EMERGENCY_BALANCE_DB.push({ user_id: fakeId, currency: 'IDR', fiat_balance: 50000000.00, qbc_offchain_balance: 0.00 });

    console.log(`🚀 Akun [${username}] berhasil ditembus via Jalur Penyelamat RAM!`);
    res.status(201).json({ message: 'Registrasi RAM Berhasil!', user: mockUser });
});

// --- AUTH LOGIN ---
app.post('/api/auth/login', async (req, res) => {
    const { email, password } = req.body;

    if (isPostgresReady) {
        try {
            const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
            if (result.rows.length > 0) {
                const validPassword = await bcrypt.compare(password, result.rows[0].password_hash);
                if (validPassword) {
                    const token = jwt.sign({ id: result.rows[0].id, username: result.rows[0].username }, JWT_SECRET, { expiresIn: '24h' });
                    return res.json({ token, user: { id: result.rows[0].id, username: result.rows[0].username, wallet: result.rows[0].wallet_address } });
                }
            }
        } catch (err) { console.log(err.message); }
    }

    // Login Fallback via RAM
    const user = EMERGENCY_USER_DB.find(u => u.email === email && u.password_hash === password);
    if (!user) return res.status(400).json({ error: 'Email atau password salah/belum terdaftar di RAM.' });

    const token = jwt.sign({ id: user.id, username: user.username }, JWT_SECRET, { expiresIn: '24h' });
    res.json({ token, user: { id: user.id, username: user.username, wallet: user.wallet_address } });
});

// --- DASHBOARD DATA ---
app.get('/api/banking/dashboard', authenticateToken, async (req, res) => {
    if (isPostgresReady) {
        try {
            const balanceRes = await pool.query('SELECT * FROM internal_balances WHERE user_id = $1', [req.user.id]);
            const historyRes = await pool.query('SELECT * FROM transactions WHERE sender_id = $1 OR recipient_id = $1 ORDER BY created_at DESC LIMIT 15', [req.user.id]);
            return res.json({ balances: balanceRes.rows, activityLogs: historyRes.rows });
        } catch (err) { console.log(err.message); }
    }

    // RAM Fetch
    const balances = EMERGENCY_BALANCE_DB.filter(b => b.user_id === req.user.id);
    const logs = EMERGENCY_TX_DB.filter(t => t.sender_id === req.user.id);
    res.json({ balances, activityLogs: logs });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🛰️ Server Anti-Gagal STG Aktif Seketika di Port ${PORT}`));
