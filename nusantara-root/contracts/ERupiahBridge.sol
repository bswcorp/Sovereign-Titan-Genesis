// SPDX-License-Identifier: MIT
// Modul: Hybrid CBDC Bridge (e-Rp to AKSA)
// Arsitek Utama: Andi Muhammad Harpianto
// Framework: Sovereign Titan Genesis (STG)

pragma solidity ^0.8.22;

import "./QStateToken.sol";

contract HybridBridge is Ownable {
    QStateToken public aksaToken;
    
    // Mapping untuk melacak e-Rp yang dikunci (Locked Asset) di Sovereign Vault
    mapping(address => uint256) public lockedERupiah;

    event AssetBridged(address indexed user, uint256 amount, string targetCurrency);
    event AssetReleased(address indexed user, uint256 amount, string targetCurrency);

    // Perbaikan: Ownable sekarang butuh msg.sender di constructor
    constructor(address _aksaAddress) Ownable(msg.sender) {
        aksaToken = QStateToken(_aksaAddress);
    }

    /**
     * @dev Mekanisme Integrasi e-Rp ke AKSA (Swap)
     * 1. Terima e-Rp Digital dari Bank Sentral/Gateway STG
     * 2. Kunci nilai e-Rp di Sovereign Vault (Swiss/Singapore)
     * 3. Kirim AKSA ke dompet pengguna secara instan via H2K
     */
    function bridgeToAksa(uint256 amountERp) public {
        // Validasi identitas biologis (H2K) dari kontrak utama
        require(aksaToken.isH2KVerified(msg.sender), "H2K Auth Required: Jantung Tidak Terdeteksi.");
        
        // Pencatatan aset yang dikunci (Sovereign Vault Storage)
        lockedERupiah[msg.sender] += amountERp;
        
        // Eksekusi pengiriman AKSA (Pastikan kontrak ini punya saldo AKSA untuk dikirim)
        // Jika AKSA di-minting baru, gunakan fungsi mint (jika tersedia di QStateToken)
        bool success = aksaToken.transfer(msg.sender, amountERp);
        require(success, "Transfer AKSA Gagal: Likuiditas Vault Tidak Cukup.");
        
        emit AssetBridged(msg.sender, amountERp, "AKSA");
    }

    /**
     * @dev Update alamat kontrak AKSA jika terjadi migrasi dahan
     */
    function updateAksaAddress(address _newAddress) public onlyOwner {
        aksaToken = QStateToken(_newAddress);
    }
}
// Fungsi Penerbitan Mandiri (Sovereign Minting)
// Digunakan untuk prototipe e-Rp sebelum otoritas resmi bergabung.
mapping(address => uint256) public sovereignIDRBalance;

event SovereignMinted(address indexed to, uint256 amount, string reason);

function mintSovereignIDR(address to, uint256 amount) public onlyOwner {
    require(aksaToken.isH2KVerified(to), "H2K Auth Required for Minting");
    
    // Mencetak unit Rupiah Digital STG (sIDR) sebagai aset underlying
    sovereignIDRBalance[to] += amount;
    
    emit SovereignMinted(to, amount, "STG Prototype e-Rupiah");
}

