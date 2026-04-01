import os, time, sys

def draw_tsc_header():
    os.system('clear')
    G, B, W, R = "\033[1;32m", "\033[1;34m", "\033[1;37m", "\033[0m"
    print(f"{W}┌" + "─"*48 + "┐")
    print(f"│ {G}● ACTIVE {W}│ {B}  THE SOVEREIGN CORE - TSC v1.0       {W}│")
    print(f"├" + "─"*12 + "┬" + "─"*35 + "┤")
    print(f"│ {W}ARCHT: ANDI {W}│ {W}SYSTEM: STG-UNIFIED INFRASTRUCTURE  {W}│")
    print(f"└" + "─"*12 + "┴" + "─"*35 + "┘")
    print(f"{B}INDUSTRIAL STATUS: [HEIR_PROTECTION_ACTIVE v99.0]{R}")
    print("-" * 50)

def run():
    while True:
        draw_tsc_header()
        print("001. [CORE] BFN ROUTING & TRANSACTION HUB")
        print("110. [AUDT] CONSOLIDATED ASSET AUDIT")
        print("111. [BILL] QUANTUM INVOICE GENERATOR")
        print("112. [PASS] BINTARO TRAFFIC VISUALIZATION")
        print("113. [LOYL] FUTURE LOYALTY & REWARD LOG")
        print("114. [CERT] E-CERTIFICATE: KHAMEL M. GUFRANY")
        print("212. [RBOT] TACTICAL ROBOT & MINING MAP")
        print("505. [SPEC] 3-MINUTE PITCH & TECH MANUAL")
        print("555. [FLOW] LIQUIDITY TSUNAMI (1MQ)")
        print("808. [LINK] QUANTUM METAPORTASI BRIDGE")
        print("810. [EXIT] SECURE SYSTEM TERMINATION")
        print("-" * 50)
        
        choice = input("ENTER COMMAND CODE: ").strip()
        p = "/home/userland/Sovereign-Titan-Genesis/library/"
        
        if choice == '001': os.system(f"python3 {p}stg_primary_engine.py")
        elif choice == '110': os.system(f"python3 {p}system_audit_v2.py")
        elif choice == '111': os.system(f"python3 {p}stg_invoice_v1.py")
        elif choice == '112': os.system(f"python3 {p}stg_epass_card.py")
        elif choice == '113': os.system(f"python3 {p}stg_loyalty_ledger.py")
        elif choice == '114': os.system(f"python3 {p}stg_shareholder_cert.py")
        elif choice == '212': os.system(f"python3 {p}stg_robot_dash_v1.py")
        elif choice == '505': 
            os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md")
            input("\n[ENTER] TO RETURN...")
        elif choice == '555': os.system(f"python3 {p}stg_homeschooling_v1.py")
        elif choice == '808': os.system(f"python3 {p}metaportasi_v1.py")
        elif choice == '810': sys.exit()
        else: print("\nERR: INVALID_INPUT"); time.sleep(1)

if __name__ == "__main__":
    try: run()
    except KeyboardInterrupt: sys.exit()
