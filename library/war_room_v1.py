import time, os

def run_war():
    os.system('clear')
    print("\033[1;31m" + "⚔️"*20)
    print("      🏛️  STG WAR ROOM - STRATEGI PERANG")
    print("      🛡️  STATUS: INITIATING GLOBAL SIEGE")
    print("⚔️"*20 + "\033[0m")
    
    maneuvers = [
        "📡 SCANNING WEAKNESS IN WESTERN LEDGERS...",
        "🌊 INITIATING LIQUIDITY DRAIN (SRIGALA TRAP)...",
        "🪓 PREPARING CROSS-BORDER ASSET CAPTURE...",
        "💎 ACTIVATING CUSTODIAN DEFENSE SHIELD..."
    ]
    
    for m in maneuvers:
        print(f"🔥 {m} [READY]")
        time.sleep(1)

    print("\n" + "="*50)
    print("✅ STATUS: WAR BLUEPRINT DEPLOYED.")
    print("👑 'Perang itu mahal, tapi menang itu Kedaulatan, Dro!'")
    print("="*50)

if __name__ == "__main__":
    run_war()
