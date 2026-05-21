// STG-web3 Wallet & Contract Service Layer (Production-Grade)
// Connecting directly to localhost Hardhat node on port 8545

export const STG_CHAIN_CONFIG = {
    chainId: '0x309', // Chain ID 777
    chainName: 'STG Local Hardhat Node',
    rpcUrls: ['http://127.0.0.1:8545'],
    nativeCurrency: { name: 'Ethereum', symbol: 'ETH', decimals: 18 }
};

const CONTRACT_ADDRESS = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0";
const CONTRACT_ABI = [
    "function name() view returns (string)",
    "function symbol() view returns (string)",
    "function totalSupply() view returns (uint256)",
    "function balanceOf(address) view returns (uint256)",
    "function transfer(address, uint256) returns (bool)"
];

export async function fetchTokenData() {
    if (!window.ethereum) throw new Error("MetaMask not detected");
    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);
    
    try {
        const name = await contract.name();
        const symbol = await contract.symbol();
        const supply = await contract.totalSupply();
        return { name, symbol, supply: supply.toString() };
    } catch (error) {
        console.error("Failed fetching live contract metadata:", error);
        return null;
    }
}

export async function fetchUserBalance(userAddress) {
    if (!window.ethereum) throw new Error("MetaMask not detected");
    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, provider);
    
    try {
        const balance = await contract.balanceOf(userAddress);
        return ethers.utils.formatUnits(balance, 18);
    } catch (error) {
        console.error("Failed fetching live user balance:", error);
        return "0";
    }
}

// Alamat Kontrak Timelock (Pastikan diisi dengan alamat hasil deploy Anda)
const TIMELOCK_ADDRESS = "MASUKKAN_ALAMAT_TIMELOCK_ANDA_DISINI";

export async function proposeVaultRelease(targetAddress, amount) {
    if (!window.ethereum) throw new Error("MetaMask tidak terdeteksi!");
    
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    
    // ABI minimal untuk berinteraksi dengan fungsi pengajuan proposal di Timelock
    const timelockAbi = [
        "function schedule(address target, uint256 value, bytes data, bytes32 predecessor, bytes32 salt, uint256 delay) public"
    ];
    
    const timelockContract = new ethers.Contract(TIMELOCK_ADDRESS, timelockAbi, signer);
    
    // Mengonversi jumlah QUBI ke unit WEI/Kripto (18 desimal)
    const parsedAmount = ethers.utils.parseUnits(amount.toString(), 18);
    
    // Membuat payload data transaksi mutasi transfer token Qubicoin
    const qubiInterface = new ethers.utils.Interface([
        "function transfer(address to, uint256 value)"
    ]);
    const txData = qubiInterface.encodeFunctionData("transfer", [targetAddress, parsedAmount]);
    
    // Parameter enkripsi unik untuk keamanan internal (Salt & Predecessor)
    const salt = ethers.utils.hexZeroPad(ethers.utils.hexlify(Math.floor(Math.random() * 100000)), 32);
    const predecessor = ethers.utils.hexZeroPad("0x0", 32);
    const delay = 172800; // Wajib menunggu jeda waktu aman 2 hari (172800 detik)

    try {
        console.log("Mengirim pengajuan kunci multi-sig ke MetaMask...");
        const tx = await timelockContract.schedule(
            CONTRACT_ADDRESS, // Kontrak target yang akan dieksekusi (Qubicoin)
            0,                // Nilai ETH (0 karena kita mengirim token)
            txData,           // Data mutasi transfer
            predecessor,
            salt,
            delay
        );
        
        const receipt = await tx.wait();
        return { success: true, txHash: receipt.transactionHash };
    } catch (error) {
        console.error("Gagal mengesahkan transaksi di MetaMask:", error);
        return { success: false, error: error.message };
    }
}
