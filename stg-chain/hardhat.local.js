require("@nomicfoundation/hardhat-toolbox");
const path = require('path');

module.exports = {
  solidity: "0.8.20",
  networks: {
    localhost: {
      url: "http://127.0.0.1:8545",
      // Mengaktifkan fitur persistence cache untuk merekam histori state transaksi local node
      accounts: {
        mnemonic: "test test test test test test test test test test test junk",
        path: "m/44'/60'/0'/0",
        initialIndex: 0,
        count: 20,
        passphrase: "",
      }
    }
  },
  paths: {
    cache: path.join(__dirname, "database/hardhat_cache"),
    artifacts: path.join(__dirname, "database/hardhat_artifacts")
  }
};
