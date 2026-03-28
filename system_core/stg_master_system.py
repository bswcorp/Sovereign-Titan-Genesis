import os
import sys

def menu():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SOVEREIGN SUPREME SYSTEM v81.0 (CAPACITY)")
    print("🛡️  ARCHITECT: ANDI M. HARPIANTO | THE 81 PILLARS")
    print("==================================================")
    print("1. [🔐] DAPUR PACU (SIRI GATE)")
    print("2. [🚀] WARP SPEED (SWISS HUB)")
    print("3. [📡] AUDIT KEDAULATAN (RIPE ATLAS)")
    print("4. [🛡️] SCAN LOG SRIGALA (PROFILING)")
    print("5. [🫀] REAL-WORK KERNEL MONITOR")
    print("6. [📠] CEK KAPASITAS ALAT KERJA")
    print("7. [📘] BACA MANUAL BOOK (INDUSTRIAL)")
    print("8. [🏦] JURUSAN BANK & DOMPET MANDIRI")
    print("...")
    print("81. [🚪] KELUAR SISTEM")
    print("==================================================")

def run():
    while True:
        menu()
        choice = input("👉 PILIH OPERASI [1-81]: ")
        
        # LOGIKA NAVIGASI ELASTIS
        if choice == '1': os.system('python3 ../library/siri_gate_v2.py')
        elif choice == '2': os.system('python3 ../library/warp_drive_v2.py')
        elif choice == '3': os.system('python3 ../library/log_kedaulatan_v1.py')
        elif choice == '4': os.system('python3 ../library/wolf_scanner_v1.py')
        elif choice == '5': os.system('python3 ../library/wolf_realwork_v1.py')
        elif choice == '6': os.system('python3 ../library/machine_status_v1.py')
        elif choice == '7': os.system('cat ../library/manual_book/MANUAL_BOOK_v1.md')
        elif choice == '8': os.system("python3 ../library/bank_genesis_v1.py")
        elif choice == '81': 
            print("\n👋 Sistem Standby. Merdeka!")
            break
        else:
            print("\n⚠️ PILIHAN BELUM AKTIF ATAU SALAH, DRO!")
        
        input("\n[ENTER] Kembali ke System...")

if __name__ == "__main__":
    run()
