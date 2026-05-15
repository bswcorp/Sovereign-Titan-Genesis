#!/bin/bash
# 🏛️ PROTOTYPE BANK STG - LIVE LEDGER STREAM TERMINAL MONITOR
# Purpose: High-Frequency Continuous Terminal View for Transaction Clearings

DB_URL="postgresql://postgres:postgres@localhost:5432/stg_unified"

# Trap exit commands cleanly
cleanup() {
    echo -e "\n🛑 [MONITOR]: Ledger telemetry interception halted."
    exit 0
}
trap cleanup SIGINT SIGTERM

clear
while true; do
    echo "============================================================"
    echo "📊 PROTOTYPE BANK STG: LIVE CENTRAL CLEARING HOUSE LEDGER"
    echo "🌐 Environment: Native Baremetal Interface | Time: $(date +%H:%M:%S)"
    echo "============================================================"
    
    # Query top 10 most recent double-entry ledger mutations via psql
    PGPASSWORD=postgres psql -d stg_unified -h localhost -U postgres -c "
    SELECT tx_id, from_account, to_account, amount_aksa, tx_type, timestamp 
    FROM bank_ledger 
    ORDER BY timestamp DESC 
    LIMIT 10;" 2>/dev/null

    if [ $? -ne 0 ]; then
        echo "🚨 Connection Error: Unable to scan stg_unified baremetal database pipeline."
    fi

    echo "------------------------------------------------------------"
    echo "💡 Continuous Stream Mode Active. Press [CTRL+C] to close window loop."
    sleep 2
    clear
done
