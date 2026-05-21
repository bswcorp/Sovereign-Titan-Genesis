const hre = require("hardhat");

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
    console.log("🚀 STARTING STG-CHAIN BACKGROUND TRAFFIC SIMULATOR...");
    const [deployer, user1, user2] = await hre.ethers.getSigners();
    
    // Alamat kontrak Qubicoin yang aktif
    const qubicoinAddress = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
    const Qubicoin = await hre.ethers.getContractAt("Qubicoin", qubicoinAddress);

    const targets = [user1.address, user2.address];
    let txCount = 0;

    while (true) {
        try {
            txCount++;
            const randomTarget = targets[Math.floor(Math.random() * targets.length)];
            // Membuat jumlah transfer acak antara 1 hingga 50 QUBI
            const randomAmount = (Math.random() * 49 + 1).toFixed(2);
            const parsedAmount = hre.ethers.parseUnits(randomAmount, 18);

            console.log(`[Tx #${txCount}] Mengirim ${randomAmount} QUBI ke alamat target: ${randomTarget}`);
            
            const tx = await Qubicoin.transfer(randomTarget, parsedAmount);
            // Menunggu konfirmasi blok lokal secara instan
            await tx.wait();
            
            console.log(`[SUKSES] Tx #${txCount} berhasil masuk blok memori.`);
            
        } catch (error) {
            console.error("⚠️ Kegagalan simulasi transaksi:", error.message);
        }

        // Jeda waktu acak antara 4 sampai 8 detik sebelum transaksi berikutnya
        const delay = Math.floor(Math.random() * 4000) + 4000;
        await sleep(delay);
    }
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
