// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title QSDG Sovereign Decentralized Bank Core
 * @notice Menegakkan hibah komunitas, kesejahteraan warga, dan pakan/obat hewan tanpa perantara bank terpusat
 * @author Jenderal Sadewa & Pandawa 5 AI under strict command of Sultan Andi Muhammad Harpianto (2026)
 */
contract SovereignBank {
    
    address public immutable juruMasakUtama; // Dompet Terpusat Sultan (0xD9a1...948e)
    uint256 public constant aksaMicroUnit = 14890; // Angka dasar ukuran recehan koin

    struct GrantProposal {
        uint256 id;
        string category;       // "Warga", "Anak_Bayi", "Hewan_Peliharaan", "Eco_Funding"
        string targetAccount;  // No Rekening atau Wallet tujuan
        uint256 amountIdr;     // Nilai Rupiah berbasis nilai penunjuk AKSA
        bool isApproved;
        bool isDispatched;
        uint256 timestamp;
    }

    mapping(uint256 => GrantProposal) public proposals;
    uint256 public proposalCount;

    event GrantProposed(uint256 indexed id, string category, uint256 amountIdr);
    event GrantApproved(uint256 indexed id, address indexed auditor);
    event GrantDispatched(uint256 indexed id, string targetAccount, uint256 amountIdr);

    modifier hanyaSultan() {
        require(msg.sender == juruMasakUtama, "HAK AKSES DITOLAK: Hanya Juru Masak Utama!");
        _;
    }

    constructor() {
        juruMasakUtama = 0xD9a1E28224d6d047Eef8712dC97d11A9032b948e;
    }

    /**
     * @notice Mengajukan hibah darurat untuk komunitas tertindas atau kesejahteraan alam
     */
    function proposeGrant(string memory _category, string memory _targetAccount, uint256 _amountIdr) external hanyaSultan {
        require(_amountIdr >= aksaMicroUnit, "Nilai hibah di bawah batas minimum receh AKSA!");
        
        proposalCount++;
        proposals[proposalCount] = GrantProposal({
            id: proposalCount,
            category: _category,
            targetAccount: _targetAccount,
            amountIdr: _amountIdr,
            isApproved: false,
            isDispatched: false,
            timestamp: block.timestamp
        });

        emit GrantProposed(proposalCount, _category, _amountIdr);
    }

    /**
     * @notice Menyetujui hibah secara mutlak (Otorisasi On-Chain)
     */
    function approveAndLockGrant(uint256 _id) external hanyaSultan {
        require(_id <= proposalCount, "Proposal tidak ditemukan!");
        require(!proposals[_id].isApproved, "Proposal sudah disetujui!");
        
        proposals[_id].isApproved = true;
        emit GrantApproved(_id, msg.sender);
    }

    /**
     * @notice Mengubah status menjadi sukses disalurkan setelah banking_bridge memproses BI-FAST
     */
    function finalizeDispatch(uint256 _id) external hanyaSultan {
        require(proposals[_id].isApproved, "Proposal belum disetujui!");
        require(!proposals[_id].isDispatched, "Dana sudah disalurkan!");
        
        proposals[_id].isDispatched = true;
        emit GrantDispatched(_id, proposals[_id].targetAccount, proposals[_id].amountIdr);
    }
}
