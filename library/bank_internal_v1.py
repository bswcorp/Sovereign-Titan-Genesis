import time, os, sys, threading

running = True

def live_dashboard():
    while running:
        t = time.localtime()
        clock_wib = time.strftime("%H:%M:%S", t)
        clock_ny = "09:22:15" # INTEL STEALTH LOCK
        CYAN, WHITE, GREY, RESET = "\033[38;5;81m", "\033[38;5;255m", "\033[38;5;244m", "\033[0m"
        sys.stdout.write("\033[s\033[H")
        print(f"{GREY}╒" + "═"*62 + "╕")
        print(f"{CYAN}│  [ STG SUPREME BANKING HUB ]{WHITE}{' '*(11)}WIB: {clock_wib}  │")
        print(f"{GREY}├" + "─"*31 + "┬" + "─"*30 + "┤")
        print(f"{GREY}│ {CYAN}NY-TIME: {clock_ny}          {GREY}│ {WHITE}DATE: {time.strftime('%A | %d-%m-%Y').upper()}  │")
        print(f"{GREY}╘" + "═"*31 + "╧" + "═"*30 + "╛" + RESET)
        sys.stdout.write("\033[u\033[K")
        sys.stdout.flush()
        time.sleep(1)

def run():
    global running
    running = True
    os.system('clear')
    threading.Thread(target=live_dashboard, daemon=True).start()
    print("\n" * 7)
    WHITE, CYAN, GREEN, GOLD, RESET = "\033[38;5;255m", "\033[38;5;81m", "\033[38;5;46m", "\033[38;5;214m", "\033[0m"
    print(f"  {WHITE}▶ VAULT CAP    : {GOLD}1,000,000,000,000 $QSTATE{RESET}")
    print(f"  {WHITE}▶ STATUS       : {GREEN}SOVEREIGN INJECTION READY{RESET}")
    print("  " + "—" * 60)
    try:
        while True:
            amt = input(f"\n  {WHITE}💸 ENTER AMOUNT: {RESET}").strip()
            if amt.lower() == 'q': running = False; break
            if amt.isdigit():
                # EFEK VISUAL TOMBOL SEND (FLASH GREEN)
                print(f"\n  {GREEN} [ SENDING... ] {RESET}", end="")
                sys.stdout.flush()
                time.sleep(0.5)
                # ANIMASI INJEKSI
                print(f"\r  {GOLD}🚀 [ INJECTED: {int(amt):,} $QSTATE ] {RESET}")
                with open('last_transfer.tmp', 'w') as f: f.write(amt)
                time.sleep(1.5)
            print("\033[A\033[K\033[A\033[K\033[A\033[K") 
    except KeyboardInterrupt: running = False

if __name__ == "__main__": run()
