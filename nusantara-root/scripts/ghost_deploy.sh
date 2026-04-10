#!/bin/bash
# 1Ai Ghost Deployer - Quadrius Edition
REPO_URL="https://github.com/bswcorp/STG-1AI"

echo "Distilling system... [Bourbon Mode]"
git remote remove origin 2>/dev/null
git remote add origin $REPO_URL

# Membersihkan file ilegal (titik dua) sebelum push
if [ -f "stg_mining_status.py:" ]; then
    mv "stg_mining_status.py:" stg_mining_status_fix.py
fi

git add .
git commit -m "STG-1A1: Deployment of Sovereign Assets"
git push -u origin main
echo "Sovereign-Titan-Genesis: MISSION ACCOMPLISHED."
