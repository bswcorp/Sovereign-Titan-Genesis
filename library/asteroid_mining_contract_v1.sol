// SPDX-License-Identifier: STG-SOVEREIGN
pragma solidity ^0.8.0;

contract ProjectMacronesia {
    string public project = "MACRONESIA_SPACE_MINING";
    uint256 public collateral_value = 1_000_000 * 10**15; // 1 Juta Quadrillion
    uint256 public repayment_period = 20 * 365 days; // 20 Tahun
    
    mapping(string => uint256) public global_allocation;

    constructor() {
        // Alokasi 1% (Biar Gak Diboikot Srigala Global)
        global_allocation["CHINA"] = collateral_value / 100;
        global_allocation["USA"]   = collateral_value / 100;
        global_allocation["UEA"]   = collateral_value / 100;
        global_allocation["AFRICA"] = collateral_value / 100;
    }

    function status() public view returns (string memory) {
        return "SOVEREIGN_DEBT_REPLACEMENT_ACTIVE";
    }
}
