const fs = require('fs');
const path = require('path');

async function uploadToIPFS(localFilePath) {
    try {
        const fileBuffer = fs.readFileSync(localFilePath);
        const fileName = path.basename(localFilePath);
        const boundary = '----STGTrisulaBoundary' + Date.now();
        
        let payload = `--${boundary}\r\n`;
        payload += `Content-Disposition: form-data; name="file"; filename="${fileName}"\r\n`;
        payload += `Content-Type: application/json\r\n\r\n`;
        const footer = `\r\n--${boundary}--`;
        const totalLength = payload.length + fileBuffer.length + footer.length;

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
        if (!data.Hash) throw new Error("IPFS Gateway failed.");
        return data.Hash;
    } catch (err) {
        console.error("🚨 IPFS Error:", err.message);
        throw err;
    }
}

module.exports = { uploadToIPFS };
