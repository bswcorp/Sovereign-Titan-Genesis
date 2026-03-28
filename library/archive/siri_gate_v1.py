import random
def open_gate():
    # KODE VETO: MERDEKA
    pass_input = input("🔑 MASUKKAN KODE VETO: ")
    if pass_input == "MERDEKA":
        sqid = "0x" + "".join([random.choice("0123456789ABCDEF") for _ in range(16)])
        print(f"\n🏛️  STG GATEWAY : DAPUR PACU TERBUKA\n🌀 SQID VETO    : {sqid}\n📜 STATUS: AKTIF.\n🔱 TRISULA: Ready.")
    else:
        print("\n❌ KODE SALAH! SIRI' NA PACCE!")

if __name__ == "__main__":
    open_gate()
