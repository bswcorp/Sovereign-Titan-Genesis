import os, time, sys

def run():
    os.system('clear')
    GOLD = "\033[1;33m"
    BLUE = "\033[1;34m"
    RESET = "\033[0m"

    print(f"{BLUE}==================================================")
    print("🏛️  STG SUPREME AUDITOR COMMAND - MOBILE v82.9")
    print(f"🛡️  CHIEF ARCHITECT: {GOLD}CAPO ANDI M. HARPIANTO{BLUE}")
    print("==================================================" + RESET)

    print(f"{GOLD}001.{RESET} 🇮🇩 [MRDK] MERDEKA (PRIMARY COMMAND)")
    print(f"{GOLD}505.{RESET} 🆘 [HELP] SOS, FAQ, MANUAL BOOK")
    print(f"{GOLD}555.{RESET} ⛏️  [MINE] MINING OPERATIONS (STEALTH)")
    print(f"{GOLD}808.{RESET} 🏛️  [ABUT] ABOUT STG / MAKRONESIA / METAPORTASI")
    print(f"{GOLD}810.{RESET} 🚪 [GATE] EXIT / PINTU KELUAR")
    print(f"{BLUE}--------------------------------------------------{RESET}")

    choice = input(f"{GOLD}👉 ENTER CODE: {RESET}").strip()

    if choice == '001':
        print("\n🇮🇩 MERDEKA! SOVEREIGN AUTHORITY ACTIVE."); time.sleep(1.2)
    elif choice == '505':
        print("\n🆘 LOADING MANUAL BOOK & FAQ..."); time.sleep(1.2)
    elif choice == '555':
        # Simulasi Mining Ringan agar HP tidak panas
        os.system('clear')
        print(f"{GOLD}⛏️  MINING METANESIA ASSETS (STEALTH)...{RESET}")
        for i in range(3):
            print(f"🛰️  SCANNING DATA... [BLOCK {i+555}] CONFIRMED")
            time.sleep(0.5)
        print(f"\n✅ STATUS: DATA MINED. ASSETS SECURED.")
        input("\n[ENTER] Back...")
    elif choice == '808':
        print("\n🏛️  STG: SOVEREIGN TITAN GENESIS - MAKRONESIA ARK."); time.sleep(1.2)
    elif choice == '810':
        print("\n🚪 CLOSING SECURE GATE..."); time.sleep(1); sys.exit()
    else:
        print("\n⚠️ INVALID AUDITOR CODE."); time.sleep(1)

if __name__ == "__main__":
    while True:
        try: run()
        except KeyboardInterrupt: sys.exit()
