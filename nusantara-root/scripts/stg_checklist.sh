#!/bin/bash

# =================================================================
# STG OPERATIONAL CHECKLIST (Sederhana & Logis)
# Penanggung Jawab: ANDI MUHAMMAD HARPIANTO
# Fungsi: Memantau Kesiapan 9 Pilar STG
# =================================================================

REPOS=(
    "Sovereign-Titan-Genesis"
    "METAPORTATION"
    "Quorum-State"
    "qs-guardian-search"
    "TITAN-PSYCHE-MONO"
    "STG-METAPORTATION-EVENT"
    "Qubicoin"
    "Makronesia-Act-Ark"
    "Garage"
)

BASE_DIR=$(pwd)
DATE=$(date '+%Y-%m-%d %H:%M:%S')

clear
echo "=========================================================="
echo "         CHECKLIST OPERASIONAL PILAR STG"
echo "         Waktu: $DATE"
echo "         Admin: ANDI MUHAMMAD HARPIANTO"
echo "=========================================================="
echo " STATUS  |  NAMA PILAR           |  FUNGSI ALUR"
echo "----------------------------------------------------------"

for repo in "${REPOS[@]}"
do
    if [ -d "$BASE_DIR/$repo" ]; then
        # Cek jika ada file di dalamnya (tidak kosong)
        if [ "$(ls -A $BASE_DIR/$repo)" ]; then
            STATUS="\e[32m[ READY ]\e[0m"
        else
            STATUS="\e[33m[ EMPTY ]\e[0m"
        fi
    else
        STATUS="\e[31m[ MISSING]\e[0m"
    fi
    
    # Menampilkan fungsi singkat berdasarkan pilar
    case $repo in
        "Sovereign-Titan-Genesis") FUNC="Core Engine/Ledger" ;;
        "METAPORTATION") FUNC="Value Transmission" ;;
        "Quorum-State") FUNC="Governance/Consensus" ;;
        "qs-guardian-search") FUNC="Security/OS Mandiri" ;;
        "TITAN-PSYCHE-MONO") FUNC="Identity & Asset" ;;
        "STG-METAPORTATION-EVENT") FUNC="Event Synchronization" ;;
        "Qubicoin") FUNC="Quantum-Proof Asset" ;;
        "Makronesia-Act-Ark") FUNC="Regional Sovereignty" ;;
        "Garage") FUNC="R&D / Maintenance" ;;
    esac

    printf " %-17b | %-21s | %s\n" "$STATUS" "$repo" "$FUNC"
done

echo "----------------------------------------------------------"
echo "SOP: Jalankan './stg_health_update.sh' jika status MISSING."
echo "=========================================================="

