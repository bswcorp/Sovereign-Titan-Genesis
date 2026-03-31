import os, time, sys

def run():
    os.system('clear')
    GOLD, BLUE, RESET = "\033[1;33m", "\033[1;34m", "\033[0m"
    
    print(f"{BLUE}==================================================")
    print("🏛️  STG SUPREME AUDITOR COMMAND - MOBILE v84.1")
    print(f"🛡️  CHIEF ARCHITECT: {GOLD}CAPO ANDI M. HARPIANTO{BLUE}")
    print("==================================================" + RESET)
    
    print(f"{GOLD}001.{RESET} 🇮🇩 [MRDK] MERDEKA (PRIMARY COMMAND)")
    print(f"{GOLD}505.{RESET} 🆘 [HELP] SOS, FAQ, MANUAL BOOK")
    print(f"{GOLD}555.{RESET} 🌊 [MINE] THE GREAT MINING TSUNAMI (1MQ)")
    print(f"{GOLD}808.{RESET} 🔮 [META] METAPORTASI (SPACE-TIME FOLDING)")
    print(f"{GOLD}810.{RESET} 🚪 [GATE] EXIT / PINTU KELUAR")
    print(f"{BLUE}--------------------------------------------------{RESET}")
    
    choice = input(f"{GOLD}👉 ENTER CODE: {RESET}").strip()
    p = "/home/userland/Sovereign-Titan-Genesis/library/"
    
    if choice == '001':
        os.system(f"python3 {p}stg_primary_engine.py")
    elif choice == '505':
        os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md")
    elif choice == '555':
        os.system(f"python3 {p}stg_homeschooling_v1.py")
    elif choice == '808':
        os.system(f"python3 {p}metaportasi_v1.py")
    elif choice == '810':
        print("\n🚪 CLOSING SECURE GATE..."); sys.exit()
    else:
        print("\n⚠️ CODE INVALID."); time.sleep(1)

if __name__ == "__main__":
    while True:
        try: run()
        except KeyboardInterrupt: sys.exit()
