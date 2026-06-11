const hre = require("hardhat");

async function main() {
  const minDelay = 172800; // 2 Hari jeda waktu aman
  const [deployer] = await hre.ethers.getSigners();
  const proposers = [deployer.address];
  const executors = [deployer.address];
  const admin = deployer.address;

  console.log("Deploying Unit 008 Treasury Timelock...");
  const Timelock = await hre.ethers.getContractFactory("TimelockController");
  const timelock = await Timelock.deploy(minDelay, proposers, executors, admin);

  await timelock.waitForDeployment();
  console.log(`Treasury Timelock successfully deployed to: ${await timelock.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
