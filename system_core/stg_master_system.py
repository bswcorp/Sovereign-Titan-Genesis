import os, sys, time

def execute_pillar(cmd, path):
    try:
        os.system(f"python3 {path}{cmd}")
    except:
        print(f"\n❌ ERROR IN PILAR: {cmd}")

def menu():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SUPREME COMMAND - AUDIT COMPLETED")
    print("🛡️  CHIEF ARCHITECT: ANDI M. HARPIANTO")
    print("==================================================")
    # PILAR UTAMA (DIRECT JEPRET)
    print("1.  🔐 [SEC ] PRIMARY COMMAND (1-16)")
    print("5.  💰 [MINT] MINTING WATERFALL (EYE-BLINK)")
    print("6.  📠 [MACH] MACHINE CAPACITY")
    print("7.  📘 [MANL] INDUSTRIAL MANUAL")
    print("8.  🏦 [BANK] GENESIS VAULT (1T)")
    print("21. 🔴 [QDAY] GLOBAL RESET (OFFICIAL)")
    print("24. 🤝 [ALLY] GUEST LEDGER (MASTER PLAN)")
    print("25. ⚔️  [WAR ] WAR PROJECT (INITIATE)")
    print("81. 🚪 [EXIT] SYSTEM STANDBY")
    print("==================================================")

def run():
    while True:
        menu()
        c = input("👉 SELECT PILLAR: ").strip()
        p = "/home/userland/Sovereign-Titan-Genesis/library/"
        
        if c == '1': execute_pillar("stg_primary_engine.py", p)
        elif c == '5': execute_pillar("minting_waterfall_v1.py", p)
        elif c == '6': execute_pillar("machine_status_v1.py", p)
        elif c == '7': os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md")
        elif c == '8': execute_pillar("bank_internal_v1.py", p)
        elif c == '21': execute_pillar("qday_doomsday_v1.py", p)
        elif c == '24': execute_pillar("web4_guest_ledger_v1.py", p)
        elif c == '25': execute_pillar("war_room_v1.py", p)
        elif c == '81': break
        else: print("\n⚠️ COMMAND UNAVAILABLE."); time.sleep(1)
        
        if c != '81': input("\n[ENTER] Back to Center...")

if __name__ == "__main__": run()
