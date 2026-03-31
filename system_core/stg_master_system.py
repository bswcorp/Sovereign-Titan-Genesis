import os, time, sys

def draw_tsc_header():
    os.system('clear')
    G, B, W, R = "\033[1;32m", "\033[1;34m", "\033[1;37m", "\033[0m"
    print(f"{W}┌" + "─"*48 + "┐")
    print(f"│ {G}● ACTIVE {W}│ {B}  THE SOVEREIGN CORE - TSC v1.0       {W}│")
    print(f"├" + "─"*12 + "┬" + "─"*35 + "┤")
    print(f"│ {W}ARCHT: ANDI {W}│ {W}SYSTEM: STG-UNIFIED INFRASTRUCTURE  {W}│")
    print(f"└" + "─"*12 + "┴" + "─"*35 + "┘")
    print(f"{B}INDUSTRIAL STATUS: [0xd914 / 0x5836 SYNCED]{R}")
    print("-" * 50)

def run():
    while True:
        draw_tsc_header()
        print("001. [CORE] PRIMARY ENGINE INITIALIZATION")
        print("110. [AUDT] CONSOLIDATED ASSET AUDIT")
        print("111. [BILL] QUANTUM INVOICE GENERATOR")
        print("505. [SPEC] TECHNICAL DATASHEET & MANUAL")
        print("555. [FLOW] LIQUIDITY EMISSION (1MQ)")
        print("808. [LINK] QUANTUM METAPORTASI BRIDGE")
        print("810. [EXIT] SECURE SYSTEM TERMINATION")
        print("-" * 50)
        
        choice = input("ENTER COMMAND CODE: ").strip()
        p = "/home/userland/Sovereign-Titan-Genesis/library/"
        
        if choice == '001': os.system(f"python3 {p}stg_primary_engine.py")
        elif choice == '110': os.system(f"python3 {p}system_audit_v2.py")
        elif choice == '111': os.system(f"python3 {p}stg_invoice_v1.py")
        elif choice == '505': os.system(f"cat {p}manual_book/MANUAL_BOOK_v1.md; read")
        elif choice == '555': os.system(f"python3 {p}stg_homeschooling_v1.py")
        elif choice == '808': os.system(f"python3 {p}metaportasi_v1.py")
        elif choice == '810': sys.exit()
        else: print("\nERR: INVALID_INPUT"); time.sleep(1)

if __name__ == "__main__":
    try: run()
    except KeyboardInterrupt: sys.exit()
