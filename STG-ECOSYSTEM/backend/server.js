const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const pool = require('./db');
const { uploadToIPFS } = require('./ipfs');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const profilePath = path.join(__dirname, 'incubator_profile.json');

// ==========================================
// 🏦 PROTOTYPE BANK STG ENDPOINTS EXECUTIVE
// ==========================================

// API BANK 1: Ambil Status Akun Finansial Sultan
app.get('/api/bank/account/:accountNumber', async (req, res) => {
    try {
        const result = await pool.query("SELECT * FROM bank_accounts WHERE account_number = $1", [req.params.accountNumber]);
        if (result.rows.length === 0) return res.status(404).json({ error: "Bank account parameters trace failed." });
        return res.json(result.rows[0]);
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
});

// API BANK 2: Eksekusi Transfer Kliring Finansial Internal Bank STG (Double-Entry Protection)
app.post('/api/bank/transfer-clearing', async (req, res) => {
    const { fromAccount, toAccount, amount, note } = req.body;
    
    if (!fromAccount || !toAccount || amount <= 0) {
        return res.status(400).json({ error: "Invalid financial transaction input matrix." });
    }

    const client = await pool.connect();
    try {
        await client.query('BEGIN'); // Mulai Transaksi SQL Terisolasi

        // Check kecukupan dana pengirim
        const checkBal = await client.query("SELECT balance_aksa FROM bank_accounts WHERE account_number = $1 FOR UPDATE", [fromAccount]);
        if (checkBal.rows.length === 0 || parseFloat(checkBal.rows[0].balance_aksa) < parseFloat(amount)) {
            throw new Error("Liquidity Check Refused: Insufficient balance pool inside account.");
        }

        // Jalankan Mutasi Pengurangan Dana
        await client.query("UPDATE bank_accounts SET balance_aksa = balance_aksa - $1 WHERE account_number = $2", [amount, fromAccount]);
        
        // Buat rekening penerima otomatis jika belum terdaftar (Auto-Onboarding Unit 012)
        await client.query(`
            INSERT INTO bank_accounts (account_number, account_name, account_type, balance_aksa)
            VALUES ($1, 'Unit-012 Automated Onboard Account', 'PUBLIC', 0)
            ON CONFLICT DO NOTHING;
        `, [toAccount]);

        // Jalankan Mutasi Penambahan Dana
        await client.query("UPDATE bank_accounts SET balance_aksa = balance_aksa + $1 WHERE account_number = $2", [amount, toAccount]);

        // Catat ke Ledger Pembukuan Abadi Bank
        await client.query(`
            INSERT INTO bank_ledger (from_account, to_account, amount_aksa, tx_type, reference_note)
            VALUES ($1, $2, $3, 'TRANSFER', $4)
        `, [fromAccount, toAccount, amount, note || "STG Internal Settlement Link"]);

        await client.query('COMMIT'); // Eksekusi Permanen
        return res.json({ status: "BANK_SETTLEMENT_SUCCESSFUL", sent_amount: amount });
    } catch (err) {
        await client.query('ROLLBACK'); // Batalkan mutasi total jika ada satu saja kegagalan
        return res.status(500).json({ error: err.message });
    } finally {
        client.release();
    }
});

// API BANK 3: Tarik Riwayat Pembukuan Abadi Ledger Bank
app.get('/api/bank/ledger-history', async (req, res) => {
    try {
        const result = await pool.query("SELECT * FROM bank_ledger ORDER BY timestamp DESC LIMIT 50");
        return res.json(result.rows);
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
});

// ==========================================
// 🌐 DECENTRALIZED ASSETS & TELEMETRY PATHS
// ==========================================
app.post('/api/assets/mint-sovereign-nft', async (req, res) => {
    const { ownerAddress } = req.body;
    if (!ownerAddress) return res.status(400).json({ error: "Wallet address required." });
    const nftName = "Titan Guard Access Token #008";
    const svgPath = path.join(__dirname, 'temp_nft.svg');
    const metaPath = path.join(__dirname, 'temp_meta.json');
    const svgContent = `<svg xmlns="http://w3.org" viewBox="0 0 400 400" width="400" height="400"><rect width="100%" height="100%" fill="#050505"/><polygon points="200,40 320,100 320,260 200,360 80,260 80,100" fill="none" stroke="#d4af37" stroke-width="8"/><text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" fill="#00ff00" font-family="monospace" font-size="24" font-weight="bold">TITAN GUARD</text><text x="50%" y="58%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="monospace" font-size="32" font-weight="bold">UNIT 008</text><circle cx="200" cy="200" r="140" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="10"/></svg>`;
    try {
        fs.writeFileSync(svgPath, svgContent);
        const imageCid = await uploadToIPFS(svgPath);
        const metadata = { name: nftName, description: "Sovereign Access Token to Unit 008 Secured Dashboard Network", image: `https://ipfs.io{imageCid}` };
        fs.writeFileSync(metaPath, JSON.stringify(metadata));
        const metaCid = await uploadToIPFS(metaPath);
        fs.unlinkSync(svgPath); fs.unlinkSync(metaPath);
        await pool.query("INSERT INTO sovereign_nfts (name, cid, owner) VALUES ($1, $2, $3)", [nftName, metaCid, ownerAddress]);
        return res.json({ status: "MINT_SUCCESS", cid: metaCid });
    } catch (err) { return res.status(500).json({ error: err.message }); }
});

app.get('/api/assets/my-nfts', async (req, res) => {
    try {
        const result = await pool.query("SELECT * FROM sovereign_nfts ORDER BY id DESC");
        return res.json(result.rows);
    } catch (err) { return res.status(500).json({ error: err.message }); }
});

app.get('/api/incubator/profile', async (fileReq, fileRes) => {
    try {
        const rawData = fs.readFileSync(profilePath, 'utf8');
        const jsonProfile = JSON.parse(rawData);
        const rpcResponse = await fetch(process.env.CHAINSTACK_HTTP_ENDPOINT, {
            method: "POST",
            headers: { "Content-Type": "application/json", "Authorization": `Bearer ${process.env.CHAINSTACK_API_KEY}` },
            body: JSON.stringify({ jsonrpc: "2.0", method: "eth_blockNumber", params: [], id: 1 })
        });
        const rpcData = await rpcResponse.json();
        const currentBlock = rpcData.result || "0x0";
        await pool.query("INSERT INTO node_telemetry (node_id, block_height) VALUES ($1, $2)", [process.env.CHAINSTACK_NODE_ID, currentBlock]).catch(()=>{});
        jsonProfile.monitoring_metrics.live_chainstack_block = currentBlock;
        jsonProfile.system_id = process.env.CHAINSTACK_NODE_ID;
        return fileRes.json(jsonProfile);
    } catch (err) { return fileRes.status(500).json({ error: "Failed to bridge data from Chainstack Node." }); }
});

app.listen(PORT, () => console.log(`STG Core Unified Server deployed on port ${PORT}`));
