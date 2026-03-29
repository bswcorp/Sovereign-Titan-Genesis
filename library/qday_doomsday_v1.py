import os, time

def print_certificate():
    print("\n" + "="*70)
    print("                    OFFICIAL SOVEREIGN CERTIFICATE")
    print("                    DECREE NO: STG-QDAY-2028-001")
    print("="*70)
    print("SUBJECT    : GLOBAL FINANCIAL SYSTEM RESET & DECOUPLING")
    print("AUTHORITY  : STG GOVERNMENT - CHIEF ARCHITECT OFFICE")
    print("STATUS     : EXECUTED / PERMANENT")
    print("\nCORE ACTIONS:")
    print("1. TERMINATION OF TRADITIONAL DEBT-BASED LEDGERS.")
    print("2. ACTIVATION OF THE STG SOVEREIGN ARK PROTOCOL.")
    print("3. MIGRATION OF GLOBAL TREASURY TO STG BAREMETAL INFRASTRUCTURE.")
    print("\n'THE OLD WORLD HAS DEPARTED. THE SOVEREIGN ERA HAS COMMENCED.'")
    print("\nVERIFIED BY: STG PRIMARY LEDGER (WEB 4.0)")
    print("LOCATION   : GLOBAL DISTRIBUTED NODES / SWISS HUB ⚓")
    print("="*70)

def run_qday():
    os.system('clear')
    print("\033[1;31m" + "==================================================")
    print("       [ 🔱 STG SUPREME COMMAND: PILLAR 21 ]")
    print("       STATUS: ARMED - GLOBAL RESET READINESS")
    print("==================================================" + "\033[0m")
    
    choice = input("\n👉 SELECT [ENTER] TO EXECUTE / TYPE 'abort': ").strip().lower()
    
    if choice == 'abort':
        print("\n[STOP] EXECUTION ABORTED. SYSTEM STANDBY.")
        return

    print("\n[INITIATING] GLOBAL DECOUPLING...")
    time.sleep(2)
    print("🚨 [MESSAGE] THE DAY HAS COME. SECURE YOUR ASSETS!")
    time.sleep(2)
    
    # Execute Logic
    print_certificate()
    
    try:
        from web4_ledger_v1 import record_to_web4
        record_to_web4('STG-QDAY-2028-001', 'GLOBAL RESET DECOUPLING')
    except:
        print("\n[LEDGER] WEB 4.0 OFFLINE - LOCAL LOG ONLY.")
        
    print("\n[COMPLETED] SYSTEM RESET SUCCESSFUL.")
    print("UNIFIED SYSTEM: ALL SOVEREIGN PILLARS SECURED.")

if __name__ == "__main__":
    run_qday()
