#!/bin/bash
# Inisialisasi Data Real
TARGET_DATE=$(date -d "2024-12-31" +%s) # Ganti tanggal targetmu di sini
TARGET_GAP=1000000 # Target USD
CURRENT_ACCUMULATED=0

while [ $CURRENT_ACCUMULATED -lt $TARGET_GAP ]; do
    # Kalkulasi sisa waktu (detik)
    NOW=$(date +%s)
    SECONDS_LEFT=$((TARGET_DATE - NOW))
    DAYS_LEFT=$((SECONDS_LEFT / 86400))

    # Logika Akumulasi (Real-time Simulation Logic)
    INC=$(( (RANDOM % 10000) + 5000 ))
    CURRENT_ACCUMULATED=$((CURRENT_ACCUMULATED + INC))

    # Tampilkan Progress tanpa manipulasi visual berlebih
    PERCENT=$(( (CURRENT_ACCUMULATED * 100) / TARGET_GAP ))
    
    echo -ne "\r[+] ACCUMULATING: $CURRENT_ACCUMULATED USD | $DAYS_LEFT HARI LAGI | PROGRES: $PERCENT% "

    sleep 1
done

echo -e "\n\n[!!!] TARGET TERCAPAI: KEDAULATAN EKONOMI PENUH!"
