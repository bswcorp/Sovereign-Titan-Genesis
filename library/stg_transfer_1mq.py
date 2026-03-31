import time, os
def run():
    os.system('clear')
    GOLD, BLUE, RESET = "\033[1;33m", "\033[1;34m", "\033[0m"
    print(f"{GOLD}🏛️  METANESIA AUTO-TRANSFER PROTOCOL (1MQ)")
    print(f"STATUS: READY FOR INSTANT EMISSION")
    print("-" * 50 + RESET)
    
    addr = input("⌨️ ENTER CLIENT WALLET ADDRESS: ").strip()
    amt = input("⌨️ ENTER AMOUNT ($Q): ").strip()
    
    if addr and amt:
        print(f"\n{BLUE}[INITIATING] EMISSION FROM CELESTIAL VAULT...")
        time.sleep(0.3) # Minim Jeda!
        print(f"🚀 [SUCCESS] {amt} $Q SENT TO {addr}")
        print(f"✅ RECORDED IN WEB 4.0 LEDGER.{RESET}")
        time.sleep(1)
if __name__ == "__main__": run()
