// STG-web3 Wallet Service Layer (Production-Ready)
// Transitioning from UI Simulation to Live RPC Connection via Ethers.js

export const STG_CHAIN_CONFIG = {
    chainId: '0x309', // Hex untuk Chain ID 777
    chainName: 'STG-Chain Devnet',
    rpcUrls: ['quorumstate.international'],
    nativeCurrency: {
        name: 'Qubicoin',
        symbol: 'QBC',
        decimals: 18
    },
    blockExplorerUrls: ['quorumstate.international']
};

export async function connectSovereignWallet() {
    if (!window.ethereum) throw new Error("MetaMask / Titan Hardware Shield tidak terdeteksi.");
    
    // Minta koneksi dompet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    
    // Switch atau Tambahkan jaringan STG-Chain secara otomatis ke dompet user
    try {
        await window.ethereum.request({
            method: 'wallet_switchEthereumChain',
            params: [{ chainId: STG_CHAIN_CONFIG.chainId }],
        });
    } catch (switchError) {
        if (switchError.code === 4902) {
            await window.ethereum.request({
                method: 'wallet_addEthereumChain',
                params: [STG_CHAIN_CONFIG],
            });
        }
    }
    
    return { account: accounts[0], signer };
}
