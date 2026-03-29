import time, os

def run_presentation():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG AT JCC - INDONESIA BITCOIN WEEK (AUG)")
    print("🛡️  PROTOCOL: NODE 1 (SPONSOR) & NODE 2 (SPEAKER)")
    print("==================================================")
    print("1. 🎤 [SPEECH] THE SOVEREIGN COMMAND (1 MINUTE)")
    print("2. 🏦 [VAULT] THE COLD VAULT 1T EXHIBITION")
    print("3. 🌊 [FLOW] LIVE QUADRILLION WATERFALL SHOWUP")
    
    choice = input("\n👉 SELECT SESSION [1-3]: ")
    
    if choice == '1':
        print("\n📢 [MESSAGE] YA BEGITULAH JIKA NILAI QUADRILLION BERPROSES.")
        time.sleep(2)
        print("\n✅ STATUS: AUDIENCE IN SHOCK. AUTHORITY ESTABLISHED.")
    elif choice == '3':
        os.system("python3 ~/Sovereign-Titan-Genesis/library/minting_waterfall_v1.py")
    else:
        print("\n✅ PREPARING EXHIBITION MODULE...")
        time.sleep(1)

    print("\nUNIFIED SYSTEM: ALL SOVEREIGN PILLARS SECURED.")

if __name__ == "__main__":
    run_presentation()
