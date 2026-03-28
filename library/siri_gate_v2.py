import random
def open_gate():
    # VERSI 2: LOGIKA LEBIH BERSIH & STABIL
    pass_input = input("🔑 MASUKKAN KODE VETO: ")
    if pass_input == "MERDEKA":
        sqid = "0x" + "".join([random.choice("0123456789ABCDEF") for _ in range(16)])
        print(f"\n🏛️  STG GATEWAY v2.0 : OPEN\n🌀 SQID: {sqid}\n📜 STATUS: DATA SECURED.")
    else:
        print("\n❌ KODE SALAH! SIRI' NA PACCE!")
if __name__ == "__main__": open_gate()
