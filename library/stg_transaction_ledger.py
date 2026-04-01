import time, os, json

def record_transaction(sender, receiver, amount, category):
    tx_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tx_id": f"STG-TX-{int(time.time())}",
        "from": sender,
        "to": receiver,
        "amount": f"{amount:,} $Q",
        "category": category,
        "status": "VERIFIED_AUDIT"
    }
    with open('internal_cashflow.json', 'a') as f:
        f.write(json.dumps(tx_data) + "\n")
    print(f"✅ TRANSACTION {tx_data['tx_id']} RECORDED SUCCESSFULLY.")

if __name__ == "__main__":
    print("--- INTERNAL TRANSACTION ROUTING ---")
    record_transaction("BFN_VAULT", "INVESTOR_NODE_01", 1000, "COMMERCIAL_LICENSE")
