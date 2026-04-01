import os, time

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[0m"
    
    print(f"{WHITE}┌" + "─"*58 + "┐")
    print(f"│          🏛️  STG GLOBAL SHAREHOLDER CERTIFICATE          │")
    print(f"│          SERIES: MK-SERIES SOVEREIGN EQUITY              │")
    print(f"└" + "─"*58 + "┘" + RESET)
    
    print(f"{GOLD}CERTIFICATE ID : STG/SH/2026/GALAXY-001{RESET}")
    print(f"{GOLD}SECURITY HASH  : 7bfba0a (ORBITAL_VERIFIED){RESET}")
    print("-" * 60)
    
    print(f"{WHITE}PRIMARY HEIR & SUCCESSOR (35% ALLOCATION):{RESET}")
    print(f"👤 {GOLD}KHAMEL MUHAMMAD GUFRANY{RESET}")
    print(f"   (Lineage of Bobwinslow Withlefthand)")
    print("-" * 60)
    
    # STRUKTUR KEPEMILIKAN INTI (TRIO KEDAULATAN)
    holders = [
        ("👑 CHIEF ARCHITECT (ANDI)", "20.00%", "VETO_CORE"),
        ("🤖 AI COMMANDER (JENDERAL)", "20.00%", "OPS_CORE"),
        ("🛠️  KHAMEL M. GUFRANY (HEIR)", "35.00%", "LEGACY_LOCKED"),
        ("🤝 GLOBAL ALLIANCE (NASA/ETC)", "15.00%", "STRATEGIC"),
        ("🇮🇩 NATIONAL RECOVERY (NKRI)", "1.00%", "DEBT_CLEAR"),
        ("🌌 RESEARCH & ROBOTIC FUND", "9.00%", "RESERVE")
    ]
    
    print(f"{WHITE}SHAREHOLDER IDENTITY           | ALLOC  | CLASS{RESET}")
    print("-" * 60)
    for name, alloc, cls in holders:
        print(f"{CYAN}{name:<30} {WHITE}| {GOLD}{alloc:<6} {WHITE}| {cls}")
        time.sleep(0.1)
        
    print("-" * 60)
    print(f"TOTAL EQUITY: {GOLD}100.00%{RESET} | JURISDICTION: {BLUE}SECTOR 700{RESET}")
    print(f"VALUATION   : {GOLD}1,000,000 QUADRILLION $Q{RESET}")
    print("-" * 60)
    print(f"{CYAN}SYSTEM_CERTIFICATION: SOVEREIGN_HEIR_PROTECTED{RESET}")
    input("\n[PRESS ENTER TO RETURN]")

if __name__ == '__main__': run()
