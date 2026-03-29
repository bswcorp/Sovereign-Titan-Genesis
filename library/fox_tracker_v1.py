import time, os, random

def run():
    os.system('clear')
    print("\033[38;5;214m" + "🦊 [FOX TRACKER: ACTIVE SURVEILLANCE]")
    print("STATUS: MONITORING EXTERNAL SCAN & INTRUSION")
    print("-" * 45 + "\033[0m")
    
    # Simulasi Deteksi Scan Intelijen
    wolf_regions = ["US-EAST", "EU-CENTRAL", "CN-NORTH", "UNKNOWN-PROXY"]
    
    try:
        while True:
            t = time.strftime("%H:%M:%S")
            region = random.choice(wolf_regions)
            # Log Pendek & Irit Space (Industrial English)
            print(f"[{t}] ALERT: SCAN DETECTED FROM {region} | ACTION: [SHADOW_BLOCK]")
            time.sleep(random.randint(2, 5))
    except KeyboardInterrupt:
        print("\n\033[38;5;81m✅ TRACKER STANDBY. LOGS ENCRYPTED IN WEB 4.0\033[0m")

if __name__ == "__main__": run()
