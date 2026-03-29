import time, os

def draw_liquidity_flow():
    print("\n" + "🌊"*15)
    print("      STG QUORUM-STATE LIQUIDITY FLOW")
    print("      STATUS: SOVEREIGN INJECTION MODE")
    print("🌊"*15)
    print("  [🏛️ GENESIS VAULT] ----> [🧊 COLD STORAGE]")
    print("          |                      |")
    print("  [🔥 HOT WALLET  ] <---- [⚡ QUORUM HUB  ]")
    print("-" * 45)
    print("💡 SYSTEM: NO INTERMEDIARIES. NO DEFI SCANDALS.")

def run():
    os.system('clear')
    print("🏦"*20)
    print("🏛️  STG INTERNAL BANK & COLD WALLET")
    print("💰 VAULT BALANCE: 1,000,000,000,000 (1T) $QSTATE")
    print("🏦"*20)
    
    draw_liquidity_flow()
    
    try:
        amt = input("\n💸 AMOUNT TO INJECT INTO MARKET (QUORUM-STATE): ")
        if not amt.isdigit():
            print("⚠️ INVALID INPUT!"); return
            
        print(f"\n⏳ INJECTING {int(amt):,} $QSTATE VIA QUORUM-STATE...")
        time.sleep(1.5)
        
        print("\n" + "="*55)
        print("✅ SUCCESS: MARKET LIQUIDITY INCREASED.")
        print("🏛️  STATUS: UNIFIED SYSTEM PILLARS SECURED.")
        print("="*55)
        
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    run()
