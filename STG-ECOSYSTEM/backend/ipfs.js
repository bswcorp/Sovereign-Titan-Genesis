// 🌐 STG UNIFIED - IPFS DECENTRALIZED STORAGE INTERFACE
// Purpose: Permanent, Content-Addressed Storage Layer for Sovereign Assets

const fs = require('fs');
const path = require('path');

/**
 * Uploads a local file stream directly to a public IPFS node gateway.
 * @param {string} localFilePath - Path to the asset file on the baremetal disk.
 * @returns {Promise<string>} - Returns the unique Content Identifier (CID).
 */
async function uploadToIPFS(localFilePath) {
    try {
        const fileBuffer = fs.readFileSync(localFilePath);
        const fileName = path.basename(localFilePath);

        // Building raw multipart form boundary manually to maintain environmental efficiency
        const boundary = '----STGTrisulaBoundary' + Date.now();
        let payload = `--${boundary}\r\n`;
        payload += `Content-Disposition: form-data; name="file"; filename="${fileName}"\r\n`;
        payload += `Content-Type: application/octet-stream\r\n\r\n`;

        const footer = `\r\n--${boundary}--`;
        const totalLength = payload.length + fileBuffer.length + footer.length;

        // Channeling payload stream to public IPFS cluster endpoint API
        const response = await fetch('https://subspace.network', {
            method: 'POST',
            headers: {
                'Content-Type': `multipart/form-data; boundary=${boundary}`,
                'Content-Length': totalLength
            },
            body: Buffer.concat([
                Buffer.from(payload, 'utf8'),
                fileBuffer,
                Buffer.from(footer, 'utf8')
            ])
        });

        const data = await response.json();
        if (!data.Hash) throw new Error("IPFS Gateway failed to output content hash hash mapping.");
        
        console.log(`🌐 IPFS: Asset locked successfully. Hash Link: ipfs://${data.Hash}`);
        return data.Hash;
    } catch (err) {
        console.error("🚨 IPFS Core Error:", err.message);
        throw err;
    }
}

module.exports = { uploadToIPFS };
