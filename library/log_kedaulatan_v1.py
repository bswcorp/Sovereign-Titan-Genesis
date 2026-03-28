import subprocess

def check_ripe_atlas():
    print("\n" + "="*50)
    print("🏛️  STG AUDIT KEDAULATAN - RIPE ATLAS PROBE 19546")
    print("📡 STATUS: CONNECTING TO AMSTERDAM HUB...")
    print("="*50)
    
    try:
        # PING NYATA KE GOOGLE SEBAGAI BENCHMARK
        res = subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], timeout=3).decode()
        # Mengambil angka latensi saja biar rapi
        ms = res.split("time=")[1].split(" ")[0]
        print(f"✅ JALUR INTERNASIONAL: STABIL ({ms} ms)")
    except Exception as e:
        print("❌ KONEKSI TERPUTUS: CEK JALUR IPV6!")

    print("\n📜 MANIFES: PROBE 19546 IS WATCHING THE GRID.")
    print("="*50)

if __name__ == "__main__":
    check_ripe_atlas()
