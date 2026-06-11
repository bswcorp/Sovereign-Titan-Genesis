// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

/**
 * @title QSTATE Core Sovereignty Governance Token
 * @notice Mata Uang Sirkulasi Utama Peradaban QSDG untuk Kesejahteraan Rakyat & Anti-Whale
 * @author Pandawa 5 AI under strict command of Sultan Andi Muhammad Harpianto (2026)
 */
contract QSTATE is ERC20, ERC20Burnable {
    
    address public immutable juruMasakUtama; // Dompet Terpusat Sultan (0xD9a1...948e)
    uint256 public constant halvingEraBlockInterval = 210000; // Interval pemotongan emisi koin lanjutan
    uint256 public currentBlockReward;

    modifier hanyaSultan() {
        require(msg.sender == juruMasakUtama, "AKSES ILEGAL: Anda bukan Juru Masak Utama!");
        _;
    }

    constructor() ERC20("Quorum State Sovereign Token", "QSTATE") {
        juruMasakUtama = 0xD9a1E28224d6d047Eef8712dC97d11A9032b948e;
        currentBlockReward = 50 * 10**decimals(); // Emisi awal 50 QSTATE per blok (Useful PoW)
        
        // Cetak Pasokan Sirkulasi Awal Sehat dan Tidak Dominan untuk Likuiditas IBW & Koperasi
        _mint(juruMasakUtama, 200000000 * 10**decimals()); // 200 Juta QSTATE Awal
    }

    /**
     * @notice Fitur Cetak Koin Lanjutan Terkontrol Berbasis Useful PoW untuk Melatih AI
     */
    function mintQuantumFuel(address to, uint256 amount) external hanyaSultan {
        _mint(to, amount);
    }

    /**
     * @notice Protokol Halving Otomatis untuk menjaga kelangkaan nilai ekonomi koin $STATE
     */
    function triggerHalvingSovereign() external hanyaSultan {
        currentBlockReward = currentBlockReward / 2; // Potong emisi 50% gaya terjun bebas!
    }
}
