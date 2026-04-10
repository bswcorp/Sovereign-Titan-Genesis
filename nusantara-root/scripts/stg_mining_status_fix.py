cat << 'EOF' > scripts/stg_mining_status.py
#!/usr/bin/env python3
import time
import random
import sys

def show_status():
    units = ["16-Psyche (Gold)", "TOI-1452b (Water)", "Bank-007 (Liquidity)"]
    print("\n==================================================")
    print("      🚀 STG MINING STATUS: ARUS KEDAULATAN       ")
    print("==================================================")
    
    try:
        while True:
            for unit in units:
                load = random.randint(85, 99)
                hash_rate = random.uniform(150.5, 450.8)
                status = "✅ STABLE" if load < 98 else "⚠️  HIGH LOAD"
                
                print(f" UNIT   : {unit}")
                print(f" STATUS : {status}")
                print(f" POWER  : {load}% | RATE: {hash_rate:.2f} TH/s")
                print(f" LOG    : Synchronizing with Nusantara-Root...")
                print("-" * 30)
            
            print(f"\n[TIME: {time.strftime('%H:%M:%S')}] Menunggu detak jantung berikutnya...")
            print("Tekan Ctrl+C untuk kembali ke Markas.\n")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\n[!] Monitoring dihentikan. Kembali ke Operasi Senyap.")

if __name__ == "__main__":
    show_status()
EOF
