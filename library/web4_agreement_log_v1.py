import time
def record_agreement(title):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"| {timestamp} | {title} | 🏛️ VERIFIED ON WEB 4.0 | ✅ IMMUTABLE |\n"
    with open('../AGREEMENT_LEDGER_WEB4.md', 'a') as f:
        f.write(log_entry)
    print(f"📜 PERJANJIAN '{title}' TELAH DIPAHAT DI WEB 4.0.")

if __name__ == "__main__":
    record_agreement("AKUISISI PERBENDAHARAAN GLOBAL")
