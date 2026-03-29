import os, time, random
try:
    from notification_hub_v1 import send_tembako_alert
except:
    def send_tembako_alert(a, d): print(f"📡 ALERT: {a} to {d}")

def run_hot():
    os.system('clear')
    print("==================================================")
    print("🔥  STG HOT WALLET - v2.2 COMMERCIAL SEED")
    print("🛡️  STATUS: READY TO SHOOT (100M TARGET)")
    print("==================================================")
    print("1. 🚀 [SHOT] INJEKSI KE BURSA (10% DARI HOT)")
    print("2. 🦊 [SYNC] SINKRONISASI METAMASK")
    print("3. 💹 [MARK] CEK HARGA PASAR LIVE")
    print("4. 🚪 [EXIT] KEMBALI KE MENU UTAMA")
    
    c = input("\n👉 PILIH EKSEKUSI [1-4]: ")
    
    if c == '1':
        amt = input("💰 JUMLAH UNTUK BURSA: ")
        print(f"⏳ PROSESING... {amt} $QSTATE DILUNCURKAN.")
        time.sleep(1)
        send_tembako_alert(amt, 'BURSA_MAINNET')
        print("✅ INJEKSI SELESAI. HARGA TERANGKAT!")
    elif c == '2':
        os.system("python3 ~/Sovereign-Titan-Genesis/library/metamask_info_v1.py")
    elif c == '3':
        os.system("python3 ~/Sovereign-Titan-Genesis/library/market_info_v1.py")
    elif c == '4':
        return
    else:
        print("⚠️ PILIHAN SALAH, DRO!")
    input("\n[ENTER] Kembali...")

if __name__ == "__main__":
    run_hot()
