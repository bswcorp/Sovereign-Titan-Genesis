import os
import sys

def menu():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG SOVEREIGN APP v81.0 (ULTIMATE EDITION)")
    print("🛡️  ARCHITECT: ANDI M. HARPIANTO | 81 PILLARS")
    print("==================================================")
    print("1.  🔐 [SIRI] DAPUR PACU (SIRI GATE)")
    print("2.  🚀 [WARP] LONCATAN PHINISI (SWISS)")
    print("3.  📡 [RIPE] AUDIT KEDAULATAN (AMSTERDAM)")
    print("4.  🕵️ [SCAN] SCAN LOG SRIGALA (PROFILING)")
    print("5.  🫀 [KERN] REAL-WORK KERNEL MONITOR")
    print("6.  📠 [MACH] CEK KAPASITAS ALAT KERJA")
    print("7.  📘 [MANL] BACA MANUAL BOOK (INDUSTRIAL)")
    print("8.  🏦 [BANK] BANK & DOMPET GENESIS (1T)")
    print("9.  🔥 [OMG!] PRESENTASI 1 MENIT (AUG)")
    print("10. 🕵️ [AUDT] AUDIT INTERNAL (IBW READY)")
    print("11. ⚓ [BAHT] RENCANA BAHTERA (2028)")
    print("12. 💹 [GTE ] GLOBAL TRADING ENGINE (BOT)")
    print("13. 📊 [180V] DASHBOARD MONITORING 180")
    print("14. 🔥 [HOT ] DOMPET HOT (100M BURSA)")
    print("15. 🦊 [META] METAMASK INFO & CUSTODY")
    print("16. 💹 [MARK] LIVE MARKET & TRADING INFO")
    print("...")
    print("81. 🚪 [EXIT] KELUAR SISTEM (VETO)")
    print("==================================================")

def run():
    while True:
        menu()
        choice = input("👉 PILIH OPERASI [1-81]: ")
        p = "~/Sovereign-Titan-Genesis/library/"
        if choice == '1': os.system(f'python3 {p}siri_gate_v2.py')
        elif choice == '2': os.system(f'python3 {p}warp_drive_v2.py')
        elif choice == '3': os.system(f'python3 {p}log_kedaulatan_v1.py')
        elif choice == '4': os.system(f'python3 {p}wolf_scanner_v1.py')
        elif choice == '5': os.system(f'python3 {p}wolf_realwork_v1.py')
        elif choice == '6': os.system(f'python3 {p}machine_status_v1.py')
        elif choice == '7': os.system(f'cat {p}manual_book/MANUAL_BOOK_v1.md')
        elif choice == '8': os.system(f'python3 {p}bank_genesis_v1.py')
        elif choice == '9': os.system(f'python3 {p}presentation_v1.py')
        elif choice == '10': os.system(f'python3 {p}system_audit_v1.py')
        elif choice == '11': os.system(f'cat {p}BAHTERA_STG_OS_2028.md')
        elif choice == '12': os.system(f'python3 {p}gte_engine_v1.py')
        elif choice == '13': os.system(f'python3 {p}dashboard_180_v1.py')
        elif choice == '14': os.system(f'python3 {p}hot_wallet_v1.py')
        elif choice == '15': os.system(f'python3 {p}metamask_info_v1.py')
        elif choice == '16': os.system(f'python3 {p}market_info_v1.py')
        elif choice == '81': 
            print("\n👋 Sistem Standby. Merdeka!"); break
        else: print("\n⚠️ PILIHAN BELUM AKTIF, DRO!")
        input("\n[ENTER] Kembali...")

if __name__ == "__main__": run()
