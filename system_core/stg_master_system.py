import os
import sys

def menu():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SOVEREIGN MASTER SYSTEM v2.0")
    print("🛡️  ARCHITECT: ANDI M. HARPIANTO")
    print("==================================================")
    print("1. 🔐 MASUK DAPUR PACU (SIRI GATE)")
    print("2. 🚀 LUNCURKAN WARP SPEED (SWISS HUB)")
    print("3. 📡 AUDIT KEDAULATAN (RIPE ATLAS)")
    print("4. 📦 BONGKAR-MUAT LIBRARY (SYNC GITHUB)")
    print("5. 🚪 KELUAR SISTEM")
    print("==================================================")

def run():
    while True:
        menu()
        choice = input("👉 PILIH OPERASI [1-5]: ")
        
        if choice == '1':
            os.system('python3 library/siri_gate_v2.py')
            input("\n[ENTER] Kembali ke System...")
        elif choice == '2':
            os.system('python3 library/warp_drive_v2.py')
            input("\n[ENTER] Kembali ke System...")
        elif choice == '3':
            os.system('python3 library/log_kedaulatan_v2.py')
            input("\n[ENTER] Kembali ke System...")
        elif choice == '4':
            print("🔄 Sinkronisasi Hulu-Hilir...")
            os.system('git add . && git commit -m "SYSTEM: Auto-Sync via Master Control" && git push origin main')
            input("\n[ENTER] Selesai...")
        elif choice == '5':
            print("👋 Sistem Standby. Merdeka!")
            break
        else:
            print("⚠️ Pilihan Salah, Dro!")
            time.sleep(1)

if __name__ == "__main__":
    run()
