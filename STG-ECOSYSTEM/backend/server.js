const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const pool = require('./db');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const profilePath = path.join(__dirname, 'incubator_profile.json');

// 📡 REST API: Fetch Master Incubator and Database Synced Telemetry Data
app.get('/api/incubator/profile', async (fileReq, fileRes) => {
    try {
        const rawData = fs.readFileSync(profilePath, 'utf8');
        const jsonProfile = JSON.parse(rawData);

        // Fetch live state block counts from your Chainstack node endpoint with Master Key Auth
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

        // Commit network logs into persistent PostgreSQL database tracking logs
        await pool.query(
            "INSERT INTO node_telemetry (node_id, block_height) VALUES ($1, $2)",
            [process.env.CHAINSTACK_NODE_ID, currentBlock]
        );

        jsonProfile.monitoring_metrics.live_chainstack_block = currentBlock;
        jsonProfile.system_id = process.env.CHAINSTACK_NODE_ID;
        
        return fileRes.json(jsonProfile);
    } catch (err) {
        return fileRes.status(500).json({ error: "Failed to bridge and archive authenticated data." });
    }
});

app.listen(PORT, () => {
    console.log(`📡 STG PERSISTENT BACKEND GATEWAY: Operational on port :${PORT}`);
});
