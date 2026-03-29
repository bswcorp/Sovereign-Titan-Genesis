import time, os

def run():
    os.system('clear')
    print("🏦"*20)
    print("🏛️  STG INTERNAL BANK & COLD WALLET")
    print("💰 VAULT BALANCE: 1,000,000,000,000 (1T) $QSTATE")
    print("🏦"*20)
    
    try:
        amt = input("\n💸 ENTER AMOUNT TO TRANSFER TO HOT WALLET: ")
        if not amt.isdigit():
            print("⚠️ INVALID AMOUNT, ARCHITECT!")
            return
            
        print(f"\n⏳ PROCESSING: TRANSFERRING {int(amt):,} $QSTATE...")
        time.sleep(1.5)
        
        print("\n" + "="*50)
        print(f"✅ INTERNAL TRANSFER SUCCESSFUL!")
        print(f"📈 HOT WALLET BALANCE INCREASED BY: {int(amt):,} $QSTATE")
        print("="*50)
        print("🦊 'Status: Saldo masuk dan tuntas, Dro!'")
        
    except Exception as e:
        print(f"❌ SYSTEM ERROR: {e}")

if __name__ == "__main__":
    run()
