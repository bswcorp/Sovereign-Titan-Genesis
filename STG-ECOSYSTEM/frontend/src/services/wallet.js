// STG UNIFIED - Framework Compilation Layer
// Dynamic RPC Provider integration for local devnet environment port 8545

export const TRISULA_NETWORK_CONFIG = {
    chainId: "0x309", // Chain ID 777 in Hexadecimal
    chainName: "STG-Chain TRISULA",
    rpcUrls: ["http://localhost:8545"],
    nativeCurrency: { name: "Qubicoin", symbol: "QBC", decimals: 18 }
};

export async function connectSovereignWallet() {
    if (!window.ethereum) throw new Error("MetaMask or Titan Guard not found.");
    const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
    return accounts[0];
}
