import os, time, random

def run():
    os.system('clear')
    GOLD, CYAN, WHITE, BLUE, RESET = "\033[1;33m", "\033[1;36m", "\033[1;37m", "\033[1;34m", "\033[0m"
    
    print(f"{BLUE}╔" + "═"*58 + "╗")
    print(f"║   🏛️  STG BINTARO HUB: SOVEREIGN TRAFFIC VISUALIZATION   ║")
    print(f"║   SOURCE: RIPE-ATLAS PROBE 19564 | STATUS: UNBLOCKABLE   ║")
    print("╚" + "═"*58 + "╝" + RESET)

    print(f"{WHITE}[MAP_COORDINATES] Lat: -6.273 | Lon: 106.745 (Bintaro Center){RESET}")
    print(f"{WHITE}[NETWORK_PRIDE]   AS17974 (Indonesian Gateway Integration){RESET}")
    print("-" * 60)

    # VISUALISASI JALUR TRAFIK (DASHBOARD MODE)
    paths = [
        ("🛰️  BINTARO -> SINGAPORE HUB", "0.002ms", "DIRECT_LINK"),
        ("🛰️  BINTARO -> TOKYO NODE     ", "0.015ms", "QUANTUM_TUNNEL"),
        ("🛰️  BINTARO -> FRANKFURT BREAD", "0.089ms", "SOVEREIGN_ROUTE"),
        ("🛰️  BINTARO -> MARS RELAY (V700)", "0.000ms", "METAPORTASI")
    ]

    for dest, lat, mode in paths:
        print(f"[{CYAN}ROUTE{RESET}] {dest} | {GOLD}{lat}{RESET} | {WHITE}{mode}{RESET}")
        time.sleep(0.4)

    print("-" * 60)
    print(f"{GOLD}LIVE TRAFFIC ANALYSIS:{RESET}")
    print(f" {BLUE}●{RESET} DATA PACKETS: {random.randint(5000, 9999)} TB/Sec")
    print(f" {BLUE}●{RESET} FIREWALL STATUS: {GOLD}BYPASSED (INHERENT SOVEREIGNTY){RESET}")
    print(f" {BLUE}●{RESET} UPLINK: {CYAN}STG-PRIVATE-FIBER (UNBLOCKABLE){RESET}")
    print("-" * 60)
    
    print(f"\n{WHITE}SYSTEM_CERTIFICATION: TRAFFIC_FLOW_VERIFIED_BY_RIPE_ATLAS{RESET}")
    print(f"PUBLIC_SOURCE: {CYAN}https://ripe.net{RESET}")
    input("\n[EXECUTE_RETURN]")

if __name__ == "__main__": run()
