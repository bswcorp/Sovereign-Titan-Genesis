import requests
def get_price():
    print("\n" + "💹"*15)
    print("🏛️  STG LIVE MARKET - GLOBAL TRADING INFO")
    print("💹"*15)
    try:
        # Mengambil harga live dari API Publik
        r = requests.get('https://api.coinbase.com', timeout=3)
        eth = r.json()['data']['amount']
        print(f"💎 ETHEREUM (ETH) : ${float(eth):,.2f}")
        print("📈 TREND         : BULLISH (READY TO TEMBAKO)")
    except:
        print("⚠️  OFFLINE: CEK KONEKSI BARREMETAL ANDA!")
    print("-" * 30)
    print("🦊 'Pasar lagi merah, saatnya kita borong, Dro!'")
    print("="*50)
if __name__ == "__main__": get_price()
