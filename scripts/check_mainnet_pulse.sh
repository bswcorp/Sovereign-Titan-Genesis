#!/bin/bash
# STG-UNIFIED: MAINNET INFRASTRUCTURE PULSE CHECK
# Purpose: Real-time diagnostic monitor for the Trisula Stack

echo "============================================================"
echo "📡 TELEMETRY DIAGNOSTIC: TESTING THE GIANT'S HEARTBEAT"
echo "============================================================"

# 1. Cek Status Kontainer Docker
echo -n "🐳 Docker Containers: "
if command -v docker-compose &> /dev/null; then
    docker-compose ps
else
    echo "Baremetal mode execution detected."
fi

# 2. Cek Koneksi Endpoint HTTP Chainstack Riil
echo -e "\n📡 Testing Chainstack HTTP Link..."
curl -s -X POST https://chainstack.com \
-H "Content-Type: application/json" \
-d '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":1}'

# 3. Cek Sinkronisasi Blok BSC Mainnet Riil via Master API Key
echo -e "\n\n📊 Querying Live Mainnet Block Height..."
curl -s -X POST https://chainstack.com \
-H "Content-Type: application/json" \
-H "Authorization: Bearer i7GWskB6.cf5aunZeiuLRqH8RCtYd56A9wxPkAKSW" \
-d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

echo -e "\n============================================================"
echo "🏁 STATUS: DIAGNOSTIC CYCLE COMPLETE. VIVA AUTHENTIC!"
echo "============================================================"
