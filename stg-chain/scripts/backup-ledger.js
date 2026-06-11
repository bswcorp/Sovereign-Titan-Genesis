const fs = require('fs-extra');
const path = require('path');

async function runBackup() {
    const sourceDir = path.join(__dirname, '../database/stg_ledger_db');
    // Menempatkan folder cadangan di luar repositori Git agar aman dari pembersihan (git clean)
    const targetDir = path.join(process.env.HOME, 'STG_LEDGER_BACKUPS', `backup-${Date.now()}`);

    console.log("🛰️ INITIALIZING BACKUP SEQUENCE FOR UNIT 008 LEDGER STORE...");
    
    try {
        if (!fs.existsSync(sourceDir)) {
            console.log("⚠️ Database LevelDB lokal belum terbentuk. Lakukan transaksi terlebih dahulu.");
            return;
        }

        // Melakukan penyalinan folder database secara utuh (Hot-backup simulator)
        await fs.copy(sourceDir, targetDir);
        console.log(`[💾 SUKSES] Database berhasil diekspor secara eksternal ke:`);
        console.log(`➡️ ${targetDir}`);
        
        // Mempertahankan log historis ringkas
        const logPath = path.join(process.env.HOME, 'STG_LEDGER_BACKUPS', 'backup_registry.log');
        fs.appendFileSync(logPath, `[${new Date().toISOString()}] Exported successfully to ${targetDir}\n`);

    } catch (err) {
        console.error("❌ Gagal mengekspor database LevelDB:", err);
    }
}

// Menginstal dependency fs-extra jika belum tersedia sebelum menjalankan fungsi
try {
    require('fs-extra');
    runBackup();
} catch (e) {
    console.log("Installing missing fs-extra backup utility...");
    const { execSync } = require('child_process');
    execSync('npm install fs-extra');
    runBackup();
}
