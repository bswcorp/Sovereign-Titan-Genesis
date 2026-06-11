// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";

contract AKSA is ERC20, ERC20Burnable {
    address public immutable juruMasakUtama;

    modifier hanyaSultan() {
        require(msg.sender == juruMasakUtama, "Akses Ilegal: Anda bukan Juru Masak!");
        _;
    }

    constructor() ERC20("Aksa Kedaulatan Sovereign Asset", "AKSA") {
        juruMasakUtama = 0xD9a1E28224d6d047Eef8712dC97d11A9032b948e;
        _mint(juruMasakUtama, 1498000000000 * 10**decimals());
    }

    function mintSovereign(address to, uint256 amount)
        external
        hanyaSultan
    {
        _mint(to, amount);
    }
}
