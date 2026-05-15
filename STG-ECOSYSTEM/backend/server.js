const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');
const { uploadToIPFS } = require('./ipfs');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const pool = new Pool({
    connectionString: process.env.DATABASE_URL || "postgresql://postgres:postgres@stg-db:5432/stg_unified"
});

// Inisialisasi Tabel NFT di PostgreSQL
pool.query(`
    CREATE TABLE IF NOT EXISTS sovereign_nfts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        cid VARCHAR(100),
        owner VARCHAR(100),
        minted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
`).catch(err => console.error(err));

// API 1: Generate dan Mint NFT Tameng Kedaulatan
app.post('/api/assets/mint-sovereign-nft', async (req, res) => {
    const { ownerAddress } = req.body;
    if (!ownerAddress) return res.status(400).json({ error: "Wallet address required." });

    const nftName = "Titan Guard Access Token #008";
    const svgPath = path.join(__dirname, 'temp_nft.svg');
    const metaPath = path.join(__dirname, 'temp_meta.json');

    // 🛡️ Generator Seni Digital SVG (Tameng Emas Unit 008)
    const svgContent = `
    <svg xmlns="http://w3.org" viewBox="0 0 400 400" width="400" height="400">
        <rect width="100%" height="100%" fill="#050505"/>
        <polygon points="200,40 320,100 320,260 200,360 80,260 80,100" fill="none" stroke="#d4af37" stroke-width="8"/>
        <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" fill="#00ff00" font-family="monospace" font-size="24" font-weight="bold">TITAN GUARD</text>
        <text x="50%" y="58%" dominant-baseline="middle" text-anchor="middle" fill="#ffffff" font-family="monospace" font-size="32" font-weight="bold">UNIT 008</text>
        <circle cx="200" cy="200" r="140" fill="none" stroke="#d4af37" stroke-width="2" stroke-dasharray="10"/>
    </svg>`;

    try {
        // 1. Amankan gambar ke IPFS
        fs.writeFileSync(svgPath, svgContent);
        const imageCid = await uploadToIPFS(svgPath);

        // 2. Buat Metadata ERC-721 Standard
        const metadata = {
            name: nftName,
            description: "Sovereign Access Token to Unit 008 Secured Dashboard Network",
            image: `https://ipfs.io{imageCid}`,
            attributes: [{ "trait_type": "Security_Level", "value": "Maximum" }]
        };
        fs.writeFileSync(metaPath, JSON.stringify(metadata));
        const metaCid = await uploadToIPFS(metaPath);

        // Hapus file sampah lokal
        fs.unlinkSync(svgPath);
        fs.unlinkSync(metaPath);

        // 3. Catat Kepemilikan Permanen ke PostgreSQL
        await pool.query("INSERT INTO sovereign_nfts (name, cid, owner) VALUES ($1, $2, $3)", [nftName, metaCid, ownerAddress]);

        return res.json({ status: "MINT_SUCCESS", cid: metaCid, metadata: metadata });
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
});

// API 2: Ambil Semua Koleksi NFT dari Database
app.get('/api/assets/my-nfts', async (req, res) => {
    try {
        const result = await pool.query("SELECT * FROM sovereign_nfts ORDER BY id DESC");
        return res.json(result.rows);
    } catch (err) {
        return res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => console.log(`Backend server active on port ${PORT}`));
