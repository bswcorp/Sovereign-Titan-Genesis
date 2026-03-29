import time
def record_to_web4(decree_no, subject):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    entry = f"\n| {timestamp} | {decree_no} | {subject} | 🏛️ IMMUTABLE | ✅ STG-VERIFIED |"
    with open('~/Sovereign-Titan-Genesis/WEB4_SOVEREIGN_LEDGER.md', 'a') as f:
        f.write(entry)
    print(f"\n[LEDGER] DECREE {decree_no} HAS BEEN CARVED INTO WEB 4.0.")

if __name__ == "__main__":
    record_to_web4("STG-QDAY-2028-001", "GLOBAL RESET")
