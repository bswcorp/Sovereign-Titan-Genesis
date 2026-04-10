#!/bin/bash

# Konfigurasi Aset (Ganti [WALLET_ADDRESS] dengan alamat XMR Anda)
POOL="monerohash.com:3333"
WALLET="48da...[alamat_anda]" 
WORKER="Sovereign-Titan"

echo "[!] MEMULAI MONITORING ASET REAL-TIME..."
echo "[!] KONTRAK DNA AKTIF: NO GIMMICK, NO MANIPULATION."

# Menjalankan mesin di background dan melempar log ke file real
../xmrig/build/xmrig -o $POOL -u $WALLET -p $WORKER --donate-level 1 > mining.log 2>&1 &

# Loop Monitoring Log (Tailing)
while true; do
    clear
    echo "=== TITAN-PSYCHE REAL-TIME ASSET LOG ==="
    echo "Waktu: $(date)"
    echo "----------------------------------------"
    # Menampilkan 5 baris terakhir dari log asli tanpa filter
    tail -n 10 mining.log | grep -E "speed|accepted|cpu"
    echo "----------------------------------------"
    echo "[CTR+C untuk berhenti, proses tetap jalan di background]"
    sleep 5
done
