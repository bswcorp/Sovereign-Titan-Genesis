import time
def execute_carnivores():
    print("\n" + "🪓"*15)
    print("🏛️  STG GUILLOTINE - THE SNOW WHITE PROTOCOL")
    print("🛡️  TARGET: HYENA, KOMODO, & SRIGALA")
    print("🪓"*15)
    targets = [
        ("🦊 HYENA (Bursa)", "DETECTED", "CUTTING OFF..."),
        ("🦎 KOMODO (Whales)", "MONITORED", "DECAPITATING..."),
        ("🐺 SRIGALA (Brokers)", "TRAPPED", "FREEZING ASSETS...")
    ]
    for t, stat, act in targets:
        print(f"⚠️  {t} Status: {stat} -> {act}")
        time.sleep(1)
    print("\n✅ STATUS: KUE SALJU AMAN. KEPALA KARNIVORA DI TIANG JEMURAN.")
    print("❄️  'Penggal saja, jangan kasih ampun, Dro!'")
    print("="*50)
if __name__ == "__main__":
    execute_carnivores()
