import os

def check_vibe():
    # Cek kapasitas memori (Proporsional)
    try:
        with open('/proc/meminfo', 'r') as f:
            mem = f.readline().split()[1]
            mem_gb = round(int(mem) / 1024 / 1024, 2)
    except:
        mem_gb = "Unknown"

    print("\n" + "="*50)
    print("🏛️  STG MACHINE STATUS: [VERSION CONTROL READY]")
    print(f"📠 ALAT KERJA : USERLAND-ANDROID (KENTANG MODE)")
    print(f"🧠 RAM TOTAL  : {mem_gb} GB")
    print("------------------------------------------")
    if float(mem_gb) < 4:
        print("⚠️  STATUS: MODE STEALTH (TEXT ONLY) AKTIF.")
        print("💡 PESAN: TUNGGU LISTING UNTUK MODE EMPIRE!")
    else:
        print("🚀 STATUS: MESIN GAHAR TERDETEKSI!")
    print("="*50)

if __name__ == "__main__":
    check_vibe()
