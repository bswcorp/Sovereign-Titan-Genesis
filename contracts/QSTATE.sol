// SPDX-License-Identifier: STG-Sovereign-License
pragma solidity ^0.8.0;

import "./openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./openzeppelin/contracts/access/Ownable.sol";

/**
 * @title QuorumStateToken
 * @dev Suplai Sovereign Scale: 100.000 Triliun (100 Quadrillion)
 * Mencerminkan nilai sejarah Nusantara yang tak terukur.
 */
contract QuorumStateToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 100000000000000000 * 10**18;

    constructor() ERC20("Quorum State Token", "QSTATE") Ownable(msg.sender) {
        _mint(msg.sender, MAX_SUPPLY);
    }

    function emergencyMint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Kedaulatan maksimal tercapai.");
        _mint(to, amount);
    }
}
