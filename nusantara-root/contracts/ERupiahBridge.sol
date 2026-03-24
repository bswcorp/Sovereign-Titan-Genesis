// SPDX-License-Identifier: MIT
// Modul: Hybrid CBDC Bridge & Sovereign Minting (e-Rp to AKSA)
// Arsitek Utama: Andi Muhammad Harpianto
// Framework: Sovereign Titan Genesis (STG)

pragma solidity ^0.8.22;

import "./QStateToken.sol";

contract HybridBridge is Ownable {
    QStateToken public aksaToken;
    
    // Mapping untuk melacak e-Rp yang dikunci di Sovereign Vault
    mapping(address => uint256) public lockedERupiah;
    
    // Mapping untuk Penerbitan Mandiri (sIDR)
    mapping(address => uint256) public sovereignIDRBalance;

    event AssetBridged(address indexed user, uint256 amount, string targetCurrency);
    event SovereignMinted(address indexed to, uint256 amount, string reason);

    constructor(address _aksaAddress) Ownable(msg.sender) {
        aksaToken = QStateToken(_aksaAddress);
    }

    /**
     * @dev Mekanisme Integrasi e-Rp ke AKSA (Swap)
     */
    function bridgeToAksa(uint256 amountERp) public {
        require(aksaToken.isH2KVerified(msg.sender), "H2K Auth Required: Jantung Tidak Terdeteksi.");
        
        lockedERupiah[msg.sender] += amountERp;
        
        // Transfer AKSA dari likuiditas Vault ke pengguna
        bool success = aksaToken.transfer(msg.sender, amountERp);
        require(success, "Transfer AKSA Gagal: Likuiditas Vault Tidak Cukup.");
        
        emit AssetBridged(msg.sender, amountERp, "AKSA");
    }

    /**
     * @dev Fungsi Penerbitan Mandiri (Sovereign Minting)
     * Digunakan untuk prototipe e-Rp (sIDR) sebelum otoritas resmi bergabung.
     */
    function mintSovereignIDR(address to, uint256 amount) public onlyOwner {
        require(aksaToken.isH2KVerified(to), "H2K Auth Required: Calon Pemegang sIDR harus terverifikasi H2K.");
        
        // Mencetak unit Rupiah Digital STG (sIDR) sebagai aset underlying
        sovereignIDRBalance[to] += amount;
        
        emit SovereignMinted(to, amount, "STG Prototype e-Rupiah Deployment");
    }

    /**
     * @dev Update alamat kontrak AKSA jika terjadi migrasi dahan
     */
    function updateAksaAddress(address _newAddress) public onlyOwner {
        aksaToken = QStateToken(_newAddress);
    }

    /**
     * @dev Cek saldo sIDR pengguna
     */
    function getSIDRBalance(address account) public view returns (uint256) {
        return sovereignIDRBalance[account];
    }
}
