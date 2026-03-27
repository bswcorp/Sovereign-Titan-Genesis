import time
import os
import random

def play_alert():
    for _ in range(3):
        os.system('echo -e "\a"')
        time.sleep(0.2)

def generate_predator_id():
    names = ["WOLF", "SNAKE", "DINO", "NAGA", "HYENA", "VULTURE", "SHARK"]
    regions = ["WEST", "EAST", "DARK_WEB", "OFFSHORE", "SHADOW"]
    p_name = random.choice(names)
    p_reg = random.choice(regions)
    p_id = f"{p_name}-{random.randint(1000, 9999)}-{p_reg}"
    return p_id

def anti_dump_gate():
    print("==========================================")
    print("🛡️  BENTENG ANTI-DUMP SOVEREIGN TITAN")
    print("💀 STATUS: SKULL MODE [ARMED]")
    print("==========================================")
    
    TOTAL_SUPPLY = 1000000000000
    LIMIT = TOTAL_SUPPLY * 0.001 
    
    try:
        amount = float(input("MASUKKAN JUMLAH JUAL ($QSTATE): "))
        print("\n⏳ SCANNING PREDATOR SIGNATURE...")
        time.sleep(1)
        
        if amount > LIMIT:
            play_alert()
            p_identity = generate_predator_id()
            print("\n" + "!"*45)
            print(f"🚨 DUMP DETECTED! [RED SKULL ALERT]")
            print(f"🆔 TARGET ID : {p_identity}")
            print(f"❌ VETO      : TRANSAKSI {amount:,.0f} DIBLOKIR!")
            print(">>> STATUS   : TARGET BLACKLISTED.")
            print("!"*45)
            
            # Simpan ke Buku Hitam GPFS
            with open('/home/userland/GPFS_TITAN/metadata/ALUTSISTA_COMMAND/blacklist.log', 'a') as f:
                f.write(f"{time.ctime()} | ID: {p_identity} | AMT: {amount:,.0f}\n")
        else:
            print("\n✅ TRANSAKSI AMAN. HARGA TERJAGA.")
    except:
        print("Input error, Capo!")

if __name__ == "__main__":
    anti_dump_gate()
