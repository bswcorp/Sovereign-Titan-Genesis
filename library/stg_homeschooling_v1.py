import time, os, random, sys

def run():
    os.system('clear')
    GOLD = "\033[1;33m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    
    print(f"{GOLD}⛏️  PROJECT MAKRONESIA: ASTEROID MINING ACTIVE")
    print(f"🚀 PROTOCOL: INFINITE LIQUIDITY EMISSION (1MQ)")
    print("-" * 55 + RESET)
    time.sleep(1)

    try:
        # TSUNAMI ANGKA DIMULAI!
        count = 0
        while True:
            val = random.randint(1000, 9999)
            # Menampilkan aliran deras koin layaknya bursa raksasa
            sys.stdout.write(f"\r{CYAN}[BLOCK {count+555}] {WHITE}INJECTED: +{val:,}.00 $QSTATE | STATUS: {GOLD}CONFIRMED ✓{RESET}")
            sys.stdout.flush()
            # Tidak pakai sleep lama, biar mengalir deras!
            time.sleep(0.01) 
            print("") # Baris baru untuk efek waterfall
            count += 1
    except KeyboardInterrupt:
        print(f"\n{GOLD}✅ MINING PAUSED. TOTAL ASSETS SECURED IN LEDGER.{RESET}")
        print("UNIFIED SYSTEM: ALL SOVEREIGN PILLARS SECURED.")
        input("\n[ENTER] Back to Command Center...")

if __name__ == "__main__": run()
