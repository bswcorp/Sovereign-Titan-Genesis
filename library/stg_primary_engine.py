import os, requests, random, time

def get_live_data():
    try:
        r = requests.get('https://api.coinbase.com', timeout=2)
        eth = f"💎 ETH: ${float(r.json()['data']['amount']):,.2f}"
    except: eth = "⚠️ MARKET OFFLINE"
    try:
        with open('/proc/uptime', 'r') as f:
            up = f"{float(f.readline().split())/3600:.2f} Jam"
    except: up = "USERLAND-ACTIVE"
    return eth, up

def run():
    os.system('clear')
    print("==================================================")
    print("🏛️  STG PRIMARY ENGINE v2.0 (THE ARCHITECT CORE)")
    print("==================================================")
    pwd = input("🔑 KODE VETO: ")
    if pwd == "MERDEKA":
        sqid = "0x" + "".join([random.choice("0123456789ABCDEF") for _ in range(16)])
        eth, up = get_live_data()
        print(f"\n✅ AKSES DITERIMA | SQID: {sqid}")
        print("-" * 40)
        print(eth)
        print(f"📠 UPTIME: {up}")
        print(f"🔥 HOT WALLET: 100,000,000 $QSTATE (READY)")
        print("-" * 40)
        print("🦊 'Satu mesin, semua pilar terjaga, Dro!'")
    else:
        print("\n❌ KODE SALAH! SIRI' NA PACCE!")
    input("\n[ENTER] Kembali ke System...")

if __name__ == "__main__":
    run()
