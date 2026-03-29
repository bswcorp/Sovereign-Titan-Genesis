import os
def run():
    print("\n" + "🛠️"*15)
    print("🏛️  STG MAINTENANCE & EXECUTIONER")
    print("🛠️"*15)
    print("1. 🛡️ AUDIT INTERNAL")
    print("2. 🪓 GUILLOTINE (PENGGAL HYENA)")
    choice = input("👉 PILIH EKSEKUSI: ")
    if choice == '1': os.system("python3 ~/Sovereign-Titan-Genesis/library/system_audit_v2.py")
    elif choice == '2': os.system("python3 ~/Sovereign-Titan-Genesis/library/guillotine_v1.py")
if __name__ == "__main__": run()
