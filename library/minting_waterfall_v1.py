import time, random, sys, os

def run_waterfall():
    # DAFTAR KAMAR RESMI (Whitelist Dompet Kedaulatan STG)
    # Ini simulasi 22.000 dompet yang terkunci ke identitas Arsitek
    stg_vault_prefix = ["0xSTG", "0xGEN", "0xTITAN", "0xAMH"]

    try:
        os.system('clear')
        print("\033[38;5;214m" + "⚓"*25)
        print("      🏛️  STG PRECISION MINTING - VOL 5")
        print("      ✨  STATUS: ADDRESS VALIDATION ACTIVE")
        print("      🔒  SECURITY: NO WRONG ROOM PROTOCOL")
        print("⚓"*25 + "\033[0m")
        time.sleep(1.5)
        
        while True:
            amount = random.randint(1000000, 9999999)
            # Generator Alamat Ber-Identitas (Bukan Acak Srigala)
            prefix = random.choice(stg_vault_prefix)
            suffix = "".join([random.choice("0123456789ABCDEF") for _ in range(30)])
            wallet = f"{prefix}{suffix}"
            
            # Output: MINTING DONE dengan Verifikasi Alamat
            sys.stdout.write(f"\r\033[38;5;121m💎 MINTING DONE: {amount:,.0f} $QSTATE | TO: {wallet[:12]}... [VERIFIED] | SUCCESS\033[0m")
            sys.stdout.flush()
            time.sleep(0.015) 
            print("") 

    except KeyboardInterrupt:
        print("\n" + "="*60)
        print("\033[38;5;214m✅ MINTING TERMINATED. ALL ASSETS SECURED IN SOVEREIGN VAULTS.\033[0m")
        print("🌹 'Ya begitulah jika nilai Quadrillion berproses, Dro!'")
        print("="*60)

if __name__ == "__main__":
    run_waterfall()
