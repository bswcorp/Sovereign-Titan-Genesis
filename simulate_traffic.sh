#!/bin/bash
# STG-Chain Automated Background Traffic Generator

NODE_URL="http://localhost:8545"
echo "🚀 Memulai Generator Trafik STG-Chain..."
echo "Menyerang $NODE_URL dengan transaksi otomatis setiap 4 detik. Tekan [CTRL+C] untuk berhenti."

while true; do
    # Generate nilai transaksi acak antara 10 hingga 50 (dalam format Hex)
    HEX_VAL=$(printf '0x%x' $((RANDOM % 40 + 10)))
    
    echo -n "Sending Tx... "
    RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" \
        --data "{\"jsonrpc\":\"2.0\",\"method\":\"eth_sendTransaction\",\"params\":[{\"from\":\"0xgenesis\",\"to\":\"0xalice\",\"value\":\"$HEX_VAL\"}],\"id\":$(date +%s)}" \
        $NODE_URL)
    
    TX_HASH=$(echo $RESPONSE | grep -o '"result":"[^"]*' | grep -o '[^"]*$')
    echo "Mined! Hash: ${TX_HASH:0:20}..."
    
    sleep 4
done
