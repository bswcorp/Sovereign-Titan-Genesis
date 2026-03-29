import time, os

def draw_map():
    print("\n" + "🌐"*15)
    print("      STG ALLIANCE NETWORK - THE MASTER PLAN")
    print("🌐"*15)
    print("   [🏛️ STG ARCHITECT] <---> [🤝 TRUSTED ALLIES]")
    print("          |                      |")
    print("   [🏦 SWISS HUB]         [🏢 GLOBAL ASSETS]")
    print("-" * 45)

def run():
    os.system('clear')
    print("================================================")
    print("🏛️  STG SOVEREIGN ALLY - GUEST LEDGER v24")
    print("🛡️  STATUS: MASTER PLAN INTEGRATION")
    print("================================================")
    
    # Tunjukkan Peta Dulu buat Gaya
    draw_map()
    
    agree = input("\n📜 AGREE TO PRIVACY POLICY? (YAY/NAY): ").lower()
    if agree == 'yay':
        name = input("✍️  ALLIANCE NAME: ").upper()
        position = input("🏢 INSTITUTION/POSITION: ").upper()
        
        # SIMPAN KE LEDGER WEB 4.0 (PRASASTI)
        ledger_path = "/home/userland/Sovereign-Titan-Genesis/WEB4_SOVEREIGN_LEDGER.md"
        with open(ledger_path, 'a') as f:
            f.write(f"| {time.strftime('%Y-%m-%d %H:%M:%S')} | {name} | {position} | 🤝 ALLY | ✅ VERIFIED |\n")
        
        print(f"\n✅ SUCCESS! '{name}' CARVED INTO WEB 4.0 LEDGER")
        print("\n[📜] GENERATING SOVEREIGN ALLIANCE CERTIFICATE...")
        time.sleep(1.5)
        print("------------------------------------------------")
        print(f"        CERTIFICATE OF SOVEREIGN ALLIANCE")
        print(f"        NAME  : {name}")
        print(f"        OFFICE: {position}")
        print(f"        STATUS: OFFICIALLY LINKED TO THE ARK")
        print("------------------------------------------------")
    else:
        print("\n🛑 ACCESS ABORTED. THE GATES ARE CLOSED.")
    
    input("\n[ENTER] Back to Command Center...")

if __name__ == "__main__":
    run()
