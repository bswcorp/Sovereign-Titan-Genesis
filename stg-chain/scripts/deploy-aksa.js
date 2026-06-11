const hre = require("hardhat");

async function main() {
    const AKSA = await hre.ethers.getContractFactory("AKSA");

    const aksa = await AKSA.deploy();

    await aksa.deployed();

    console.log("AKSA deployed to:", aksa.address);
}

main()
.then(() => process.exit(0))
.catch((error) => {
    console.error(error);
    process.exit(1);
});
