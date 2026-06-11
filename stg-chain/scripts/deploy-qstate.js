const hre = require("hardhat");

async function main() {
  await hre.run("compile");
  
  const QSTATEFactory = await hre.ethers.getContractFactory("QSTATE");
  const qstate = await QSTATEFactory.deploy();
  await qstate.deployed();
  
  console.log("===============================================================");
  console.log("✅ KOIN UTAMA $QSTATE SUKSES AKTIF ON-CHAIN GEGAP GEMPITA!");
  console.log("📍 QSTATE CONTRACT ADDRESS:", qstate.address);
  console.log("===============================================================");
}

main()
  .then(() => process.exit(0))
  .catch((error) => { 
    console.error(error); 
    process.exit(1); 
  });

