import time
import random

def monitor_galerai():
    print("==========================================")
    print("🏛️  GALERAI MOTION SENSOR - STG GOV")
    print("🛡️  STATUS: SCANNING SEKTOR ALUTSISTA...")
    print("==========================================")
    
    try:
        while True:
            # Simulasi deteksi gerakan di halaman luas
            detection = random.random()
            timestamp = time.strftime("%H:%M:%S")
            
            if detection > 0.8:
                print(f"[{timestamp}] ⚠️ ALERT: PERGERAKAN TERDETEKSI DI SEKTOR 2 (ALUTSISTA REBORN)!")
            elif detection < 0.1:
                print(f"[{timestamp}] 🛸 INFO: WAHANA UDARA (SONAR) MELINTAS - STATUS: CLEAR.")
            else:
                print(f"[{timestamp}] 🟢 STATUS: AMAN - HALAMAN TERPANTAU.")
            
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n[!] MONITORING DIHENTIKAN OLEH ARCHITECT.")

if __name__ == "__main__":
    monitor_galerai()
