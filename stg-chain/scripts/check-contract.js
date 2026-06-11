const hre = require("hardhat");

async function main() {

 const address = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512";

 const code = await hre.ethers.provider.getCode(address);

 console.log("Code length:", code.length);

}
main();
