# QSDG Dual-Layer Asset Architecture Specification (v1.0)
Document Name: dual-layer-asset-spec.md
Repository: STG-Chain
Category: ARCHITECTURE-LAYER
Version: DUAL-V1-2026
Status: Core Core Approved
Chain ID Target: 31337 (Hardhat Engine)

---

## 1. Executive Summary
Spesifikasi ini menegaskan pemisahan mutlak antara Layer Cadangan Historis (AKSA Ledger) dan Layer Ekonomi Sirkulasi Aktif (QSTATE Token) di bawah payung besar Quorum Sovereign Digital Generation.

## 2. Structural Layer Parameters
1. **AKSA Layer (Historical Reserve)**:
   - Supply: 1.498 Triliun Koin.
   - Peran: Backing asset internal (Aksara Nusantara Ledger) yang merepresentasikan legasi kekayaan awal. Dikunci eksklusif pada dompet Sultan `0xD9a1E28224d6d047Eef8712dC97d11A9032b948e`.
2. **QSTATE Layer (Main Economic Engine)**:
   - Supply: Genesis Target Initial Circulation (Feeless, 15.5M+ TPS Capable).
   - Peran: Alat tukar sirkulasi, pembayaran gas fee hibrida, tata kelola proposal, dan pemicu transfer otomatis BI-FAST di `banking_bridge.py`.

## 3. Threat Mitigation Layer
Jika salah satu layer wallet terindikasi mengalami penyitaan atau pembekuan oleh otoritas luar ("Serigala"), sirkulasi ekonomi akan otomatis dialihkan oleh Jenderal Sadewa ke layer cadangan dalam waktu 300 mikrodetik menggunakan interaksi saklar hibrida, menjaga ekosistem tetap Antifragile.
