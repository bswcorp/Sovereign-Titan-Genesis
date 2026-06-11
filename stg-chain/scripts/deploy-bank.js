/**
 * @title QSDG Sovereign Bank Compiler & Deployment Script
 * @notice Menanamkan file SovereignBank.sol secara langsung ke dalam State Node Lokal 31337
 * @author Jenderal Sadewa & Pandawa 5 AI under Command of Sultan Andi Muhammad Harpianto (2026)
 */
const hre = require("hardhat");

async function main() {
  console.log("🏛️ [SOVEREIGN-BANK] Memulai skrip inisialisasi kompilasi...");

  // 1. Jalankan kompilasi otomatis untuk merajut file artifacts JSON
  await hre.run("compile");
  console.log("🎨 [COMPILER] Kompilasi SovereignBank.sol sukses!");

  // 2. Ambil alamat dompet terpusat Sultan sebagai pengendali utama
  const [sultanSigner] = await hre.ethers.getSigners();
  console.log("🔑 Otorisasi Tanda Tangan Utama (Sultan):", sultanSigner.address);

  // 3. Ambil pabrik cetak kontrak dari memori artifacts
  const SovereignBankFactory = await hre.ethers.getContractFactory("SovereignBank");
  
  console.log("🚀 Menyuntikkan kontrak SovereignBank ke dalam State Node Jaringan 31337...");
  const bank = await SovereignBankFactory.deploy();

  // 4. Tunggu hingga penulisan mutasi status ter-las mati di disk database lokal (LevelDB)
  await bank.deployed();

  console.log("---------------------------------------------------------------");
  console.log("✅ BANK TERDESENTRALISASI MURNI SUKSES AKTIF ON-CHAIN!");
  console.log("📍 SOVEREIGN BANK CONTRACT ADDRESS:", bank.address);
  console.log("---------------------------------------------------------------");
  console.log("👉 Salin alamat di atas untuk di-input ke skrip banking_bridge.py!");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("❌ Kompilasi Gagal:", error);
    process.exit(1);
  });
