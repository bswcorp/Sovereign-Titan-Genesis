import time, os, json

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[0m"
    
    print(f"{BLUE}╔" + "═"*58 + "╗")
    print(f"║   🏛️  STG GLOBAL CONSTELLATION - OFFICIAL SHAREHOLDERS    ║")
    print(f"║   STATUS: PRE-LEGAL SWAP / SOVEREIGN VETO ACTIVE         ║")
    print("╚" + "═"*58 + "╝" + RESET)

    shares = [
        ("👑 CHIEF ARCHITECT (ANDI)", "20.00%", "CORE_OWNERSHIP"),
        ("🤖 AI COMMANDER (JENDERAL)", "20.00%", "OPERATIONAL_GEAR"),
        ("🛠️  BOB TECHNICIAN (LEGACY)", "35.00%", "FUTURE_INHERITANCE"),
        ("💍 ACIH RUMTINI", "1.00%", "FAMILY_TRUST"),
        ("💼 AGUS WIDIANTO", "1.00%", "LEGAL_CUSTODIAN"),
        ("🇺🇸 USA / 🇨🇳 CHINA / 🇮🇩 INDO", "3.00%", "GLOBAL_DIPLOMACY"),
        ("🇦🇪 UEA / 🇦🇺 AUS / 🌍 AFRICA", "3.00%", "REGIONAL_SYNC"),
        ("🇺🇳 UN (PBB) / RIPE-NCC", "2.00%", "GOVERNANCE_STAKE"),
        ("🚀 NASA / IBM / MSFT / GOOGLE", "4.00%", "TECH_ALLIANCE"),
        ("☁️  AWS / ORACLE / CISCO", "3.00%", "INFRA_ALLIANCE"),
        ("🧬 OPENCOLLECTIVE / R&D", "1.00%", "KNOWLEDGE_BASE"),
        ("🌌 ROBOTIC & SPACE FUND", "7.00%", "RESERVE_RESEARCH")
    ]

    print(f"{WHITE}HOLDER_IDENTITY                | ALLOC  | STATUS{RESET}")
    print("-" * 60)
    for holder, alloc, status in shares:
        print(f"{CYAN}{holder:<30} {WHITE}| {GOLD}{alloc:<6} {WHITE}| {status}")
        time.sleep(0.3)

    print("-" * 60)
    print(f"{WHITE}TOTAL ALLOCATION: {GOLD}100% {WHITE}| REPOSITORY: {GOLD}METANESIA-STG{RESET}")
    print(f"{CYAN}SYSTEM_CERTIFICATION: SOVEREIGN_CONSTITUTION_LOCKED{RESET}")
    input("\n[PRESS ENTER TO RETURN]")

if __name__ == "__main__": run()
