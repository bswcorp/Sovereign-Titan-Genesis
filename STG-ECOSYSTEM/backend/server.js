const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

// Enable secure cross-origin queries for public interface dashboard integration
app.use(cors());
app.use(express.json());

const profilePath = path.join(__dirname, 'incubator_profile.json');

// Route 1: Retrieve complete structural incubation metrics
app.get('/api/incubator/profile', (fileReq, fileRes) => {
    fs.readFile(profilePath, 'utf8', (err, data) => {
        if (err) {
            return fileRes.status(500).json({ error: "Failed to read data center record metadata." });
        }
        return fileRes.json(JSON.parse(data));
    });
});

// Route 2: Isolated search query for active funding tiers
app.get('/api/incubator/tiers', (tierReq, tierRes) => {
    fs.readFile(profilePath, 'utf8', (err, data) => {
        if (err) {
            return tierRes.status(500).json({ error: "Configuration indexing lookup failure." });
        }
        const parsedData = JSON.parse(data);
        return tierRes.json(parsedData.incubation_tiers || []);
    });
});

app.listen(PORT, () => {
    console.log(`📡 STG INCUBATOR ENGINE: Active on secure gateway port :${PORT}`);
});
