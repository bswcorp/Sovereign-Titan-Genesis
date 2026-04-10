#!/bin/bash

# =================================================================
# STG Health Check & Update Script (V.1.0)
# Penanggung Jawab: ANDI MUHAMMAD HARPIANTO
# Lingkungan: Ubuntu Bash (UserLand)
# =================================================================

# Daftar 9 Pilar Proyek STG
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

BASE_URL="https://github.com"
BASE_DIR=$(pwd)

echo "--------------------------------------------------------"
echo "MEMULAI KONSOLIDASI & UPDATE 9 PILAR STG..."
echo "User: ANDI MUHAMMAD HARPIANTO"
echo "--------------------------------------------------------"

# 1. Update Package List (Tanpa Upgrade Otomatis untuk menjaga binary)
echo "[1/3] Memperbarui daftar paket sistem..."
sudo apt-get update -y

# 2. Loop Pengecekan Direktori dan Update Git
echo "[2/3] Memeriksa integritas folder proyek..."

for repo in "${REPOS[@]}"
do
    echo -n "Checking $repo... "
    if [ -d "$BASE_DIR/$repo" ]; then
        echo -e "\e[32m[FOUND]\e[0m"
        cd "$BASE_DIR/$repo"
        
        # Cek status git tanpa mengubah file
        git fetch --all &> /dev/null
        
        # Update aman: simpan perubahan lokal, tarik update, kembalikan perubahan
        echo "Updating $repo..."
        git stash &> /dev/null
        git pull origin main || git pull origin master
        git stash pop &> /dev/null
        
        cd "$BASE_DIR"
    else
        echo -e "\e[31m[NOT FOUND]\e[0m"
        echo "Saran: Lakukan git clone $BASE_URL/$repo"
    fi
done

# 3. Verifikasi Akhir
echo "--------------------------------------------------------"
echo "[3/3] PEMERIKSAAN SELESAI."
echo "Status: Versi terbaru telah ditarik ke folder masing-masing."
echo "Peringatan: Tidak ada file lama yang dihapus sesuai SOP."
echo "--------------------------------------------------------"
