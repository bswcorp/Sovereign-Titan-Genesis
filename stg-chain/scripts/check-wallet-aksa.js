const hre = require("hardhat");

async function main() {

 const token = await hre.ethers.getContractAt(
   "AKSA",
   "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"
 );

 const balance = await token.balanceOf(
   "0xD9a1E28224d6d047Eef8712dC97d11A9032b948e"
 );

 console.log(
   hre.ethers.formatUnits(balance,18)
 );
}

main();
