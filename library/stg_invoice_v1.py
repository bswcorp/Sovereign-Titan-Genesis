import os, time, random

def generate_invoice():
    os.system('clear')
    GOLD, CYAN, WHITE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[0m"
    
    # DATA INVOICE STANDAR INDUSTRI
    inv_num = f"INV-TSC-{random.randint(1000, 9999)}"
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"{GOLD}╔" + "═"*58 + "╗")
    print(f"║  🏛️  THE SOVEREIGN CORE (TSC) - OFFICIAL INVOICE         ║")
    print(f"║  📄 SERIAL: {inv_num} | DATE: {date}    ║")
    print("╚" + "═"*58 + "╝" + RESET)
    
    print(f"{WHITE}BILL TO    : [ SOVEREIGN ALLY / CLIENT ]")
    print(f"ISSUED BY  : OFFICE OF THE CHIEF ARCHITECT (STG)")
    print("-" * 60)
    
    # DAFTAR LAYANAN KOMERSIAL
    print(f"1. TSC-v1.0 SOFTWARE LICENSE (OEM)   : 1,000.00 $Q")
    print(f"2. QUANTUM METAPORTASI BRIDGE        : 500.00 $Q")
    print(f"3. INDUSTRIAL SECURITY AUDIT (V110)  : 250.00 $Q")
    print("-" * 60)
    print(f"{CYAN}TOTAL SETTLEMENT REQUIRED            : 1,750.00 $QSTATE{RESET}")
    print("-" * 60)
    
    print(f"{WHITE}PAYMENT ADDRESS (TSC VAULT):{RESET}")
    print(f"{GOLD}0x5836c7a5eb31975b51c76a205aaba4c01f0eb3e8{RESET}")
    print(f"\n{CYAN}SYSTEM_CERTIFICATION: SOVEREIGN_ASSET_VERIFIED{RESET}")
    print("=" * 60)
    input("\n[PRESS ENTER TO SAVE & RETURN]")

if __name__ == "__main__":
    generate_invoice()
