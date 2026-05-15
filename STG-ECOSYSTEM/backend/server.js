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

// 🌐 ROUTE 3: Automated IPFS Metadata Registry Anchor
app.post('/api/assets/mint-metadata', async (req, res) => {
    const { assetName, description, imageUrl } = req.body;
    
    if (!assetName || !imageUrl) {
        return res.status(400).json({ error: "Missing required parameter mappings." });
    }

    const tempMetadataPath = path.join(__dirname, 'temp_nft_metadata.json');
    
    // Construct standard ERC-721 metadata structure format specifications
    const nftMetadata = {
        name: assetName,
        description: description || "Sovereign Titan Genesis Decentralized Ecosystem Asset",
        image: imageUrl,
        attributes: [
            { "trait_type": "Origin", "value": "Nusantara Core" },
            { "trait_type": "Security", "value": "Quantum-Shielded" }
        ],
        compiled_at: new Date().toISOString()
    };

    try {
        fs.writeFileSync(tempMetadataPath, JSON.stringify(nftMetadata, null, 2));
        
        // Push metadata package out to the IPFS network stream mapping node
        const cidHash = await uploadToIPFS(tempMetadataPath);
        fs.unlinkSync(tempMetadataPath); // Clear temporary disk files cleanly

        return res.json({
            status: "METADATA_DECENTRALIZED_PIN_SUCCESS",
            ipfs_uri: `ipfs://${cidHash}`,
            gateway_url: `https://ipfs.io{cidHash}`
        });
    } catch (err) {
        return res.status(500).json({ error: "Failed to anchor metadata object parameters onto IPFS." });
    }
});

app.get('/api/incubator/profile', async (fileReq, fileRes) => {
    try {
        const rawData = fs.readFileSync(profilePath, 'utf8');
        const jsonProfile = JSON.parse(rawData);

        const rpcResponse = await fetch(process.env.CHAINSTACK_HTTP_ENDPOINT, {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Authorization": `Bearer ${process.env.CHAINSTACK_API_KEY}`
            },
            body: JSON.stringify({ jsonrpc: "2.0", method: "eth_blockNumber", params: [], id: 1 })
        });
        const rpcData = await rpcResponse.json();
        const currentBlock = rpcData.result || "0x0";

        await pool.query(
            "INSERT INTO node_telemetry (node_id, block_height) VALUES ($1, $2) ON CONFLICT DO NOTHING",
            [process.env.CHAINSTACK_NODE_ID, currentBlock]
        ).catch(() => {});

        jsonProfile.monitoring_metrics.live_chainstack_block = currentBlock;
        jsonProfile.system_id = process.env.CHAINSTACK_NODE_ID;
        
        return fileRes.json(jsonProfile);
    } catch (err) {
        return fileRes.status(500).json({ error: "Failed to bridge data from Chainstack Node." });
    }
});

app.listen(PORT, () => {
    console.log(`📡 STG PERSISTENT PROXY GATEWAY: Active on port :${PORT}`);
});
