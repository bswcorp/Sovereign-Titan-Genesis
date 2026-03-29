import os, time, random

def run_bank():
    print("\n" + "🏛️"*15)
    print("      STG BANK & COLD WALLET [GENESIS]")
    print("      STATUS: VAULT LOCKED (1T ASSET)")
    print("🏛️"*15)
    print("💳 [VISA] [MASTERCARD] [STG-PAY] ENABLED")
    print("------------------------------------------")
    print("1. 💸 TRANSFER INTERNAL (COLD TO HOT)")
    print("2. 🔍 SCAN INTEGRITY (BANK AUDIT)")
    print("3. 📇 GENERATE VIRTUAL CARD (VISA/MC)")
    print("4. 🚪 KELUAR KE MENU UTAMA")
    
    c = input("\n👉 EKSEKUSI NOMOR: ")
    
    if c == '1':
        amt = input("💰 JUMLAH TRANSFER: ")
        print(f"⏳ PROSESING... {amt} $QSTATE DILUNCURKAN.")
        time.sleep(1); print("✅ TRANSFER SELESAI.")
    elif c == '2':
        os.system("python3 ~/Sovereign-Titan-Genesis/library/system_audit_v2.py")
    elif c == '3':
        print(f"💳 CARD ISSUED: 4242 **** **** {random.randint(1000,9999)}")
        print("🏛️  BANKER STATUS: VERIFIED BY STG")
    elif c == '4':
        return
    else:
        print("⚠️ PILIHAN SALAH, DRO!")

if __name__ == "__main__":
    run_bank()
