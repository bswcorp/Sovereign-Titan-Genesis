import time, os, random, sys

def run():
    os.system('clear')
    GOLD = "\033[1;33m"
    CYAN = "\033[1;36m"
    BLUE = "\033[1;34m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    
    print(f"{GOLD}╔" + "═"*58 + "╗")
    print(f"║  ⛏️  MAKRONESIA: LIQUIDITY EMISSION TSUNAMI (1MQ)        ║")
    print(f"║  📊 STATUS: CONTINUOUS INJECTION ACTIVE                  ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    try:
        count = 0
        while True:
            val = random.randint(1000, 9999)
            # LOGIKA VISUAL: NILAI KOIN DALAM WARNA BIRU (BLUE)
            sys.stdout.write(f"\r{CYAN}[BLOCK {count+2462}] {WHITE}INJECTED: {BLUE}+{val:,}.00 $QSTATE {WHITE}| {GOLD}CONFIRMED ✓{RESET}")
            sys.stdout.flush()
            time.sleep(0.01) # Ultra-Fast Industrial Stream
            print("") 
            count += 1
    except KeyboardInterrupt:
        print(f"\n{GOLD}SYSTEM_CERTIFICATION: SOVEREIGN_ASSET_VERIFIED{RESET}")
        input("\n[EXECUTE_RETURN]")

if __name__ == "__main__":
    run()
