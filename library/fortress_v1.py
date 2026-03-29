import os
def run():
    print("\n" + "🛡️"*15)
    print("🏛️  STG FORTRESS - AUDIT & SCAN LOG")
    print("🛡️"*15)
    print("1. 🕵️  SCAN LOG SRIGALA (PROFILING)")
    print("2. 🔍 AUDIT INTERNAL (LEAK & BUG)")
    print("3. 🪓 GUILLOTINE (CUTTING OFF)")
    c = input("👉 PILIH EKSEKUSI: ")
    if c == '1': os.system("python3 ~/Sovereign-Titan-Genesis/library/wolf_scanner_v1.py")
    elif c == '2': os.system("python3 ~/Sovereign-Titan-Genesis/library/system_audit_v2.py")
    elif c == '3': os.system("python3 ~/Sovereign-Titan-Genesis/library/guillotine_v1.py")
if __name__ == "__main__": run()
