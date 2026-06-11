const hre = require("hardhat");

async function main() {
  const token = await hre.ethers.getContractAt(
    "AKSA",
    "0x5FbDB2315678afecb367f032d93F642f64180aa3"
  );

  const supply = await token.totalSupply();

  console.log(
    hre.ethers.utils.formatUnits(supply, 18)
  );
}

main();
