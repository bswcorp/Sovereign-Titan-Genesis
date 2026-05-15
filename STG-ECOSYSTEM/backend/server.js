const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const profilePath = path.join(__dirname, 'incubator_profile.json');

app.get('/api/incubator/profile', async (fileReq, fileRes) => {
    try {
        const rawData = fs.readFileSync(profilePath, 'utf8');
        const jsonProfile = JSON.parse(rawData);

        // Eksekusi jabat tangan otentik menggunakan Master API Key Sultan
        const rpcResponse = await fetch(process.env.CHAINSTACK_HTTP_ENDPOINT, {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                "Authorization": `Bearer ${process.env.CHAINSTACK_API_KEY}`
            },
            body: JSON.stringify({
                jsonrpc: "2.0",
                method: "eth_blockNumber",
                params: [],
                id: 1
            })
        });
        const rpcData = await rpcResponse.json();

        jsonProfile.monitoring_metrics.live_chainstack_block = rpcData.result || "0x0";
        jsonProfile.system_id = process.env.CHAINSTACK_NODE_ID;
        
        return fileRes.json(jsonProfile);
    } catch (err) {
        return fileRes.status(500).json({ error: "Failed to bridge authenticated data from Chainstack Node." });
    }
});

app.listen(PORT, () => {
    console.log(`📡 STG AUTHENTICATED BACKEND PROXY: Active on endpoint port :${PORT}`);
});
