// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title QuorumStateCoin
 * @dev Versi Sempurna dari kode lama Anda.
 * Menambahkan fitur Ownable untuk keamanan dan batas 1.000T.
 */
contract QuorumStateCoin is ERC20, Ownable {
    // Batas Maksimal Suplai Global: 1.000 Triliun (1.000T)
    uint256 public constant MAX_SUPPLY = 1000000000000000 * 10**18;

    constructor() ERC20("Quorum State", "QSTATE") Ownable(msg.sender) {
        // Fase Genesis: Cetak 1 Triliun pertama langsung ke dompet Anda
        _mint(msg.sender, 1000000000000 * 10**18);
    }

    /**
     * @dev Fungsi khusus untuk mencetak koin fase berikutnya (H2K Mining).
     * Hanya bisa dipanggil oleh Anda (Owner).
     */
    function mintNextPhase(address to, uint256 amountInTrillions) public onlyOwner {
        uint256 amountToMint = amountInTrillions * 1000000000000 * 10**18;
        require(totalSupply() + amountToMint <= MAX_SUPPLY, "Melebihi batas maksimal 1000T!");
        _mint(to, amountToMint);
    }
}
