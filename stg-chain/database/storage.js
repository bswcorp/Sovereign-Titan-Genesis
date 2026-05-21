const { ClassicLevel } = require('classic-level');
const path = require('path');

// Menginisialisasi database LevelDB pada sub-direktori fisik stg_ledger_db
const db = new ClassicLevel(path.join(__dirname, 'stg_ledger_db'), { valueEncoding: 'json' });

async function saveWalletBalance(address, balance) {
    try {
        await db.put(`balance:${address.toLowerCase()}`, {
            balance: balance.toString(),
            updatedAt: Date.now()
        });
        console.log(`[💾 LEVELDB] Berhasil mengamankan saldo permanen untuk: ${address}`);
    } catch (err) {
        console.error('❌ Gagal menulis data ke LevelDB:', err);
    }
}

async function getWalletBalance(address) {
    try {
        const data = await db.get(`balance:${address.toLowerCase()}`);
        return data.balance;
    } catch (err) {
        if (err.code === 'LEVEL_NOT_FOUND') {
            return "0"; // Default jika data alamat belum terdaftar di disk
        }
        console.error('❌ Gagal membaca data dari LevelDB:', err);
        return "0";
    }
}

module.exports = { saveWalletBalance, getWalletBalance, db };
