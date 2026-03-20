from web3 import Web3
import json

# 1. KONEKSI KE JARINGAN (Pegasus Lightlink)
RPC_URL = "https://1891.rpc.thirdweb.com"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# 2. IDENTITAS SANG PELOPOR (Ganti dengan data Anda)
MY_ADDRESS = "0xD9a1E28224d6d047Eef8712dC97d11A9032b948e"
PRIVATE_KEY = "MASUKKAN_PRIVATE_KEY_ANDA_DI_SINI" # Simpan rahasia!

# 3. BYTECODE & ABI (Data dari Remix tadi)
# Saya masukkan ringkasannya agar mesin mengenali QSTATE
ABI = [...] # (Diisi otomatis dari hasil compile)
BYTECODE = "0x60806040..." # (Bytecode panjang yang Anda kirim tadi)

def deploy():
    print(f">>> Memulai Auto-Deploy $QSTATE untuk: ANDI MUHAMMAD HARPIANTO")
    
    # Cek Koneksi
    if not w3.is_connected():
        print("![ERROR] Gagal konek ke jaringan Pegasus.")
        return

    # Siapkan Transaksi
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = {
        'from': MY_ADDRESS,
        'nonce': nonce,
        'gas': 3000000,
        'gasPrice': w3.to_wei('0.15', 'gwei'),
        'data': BYTECODE,
        'chainId': 1891
    }

    # Tanda Tangan & Kirim
    signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print(f">>> TRANSAKSI TERKIRIM! Hash: {tx_hash.hex()}")
    print(">>> Menunggu Konfirmasi Jaringan...")
    
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f">>> BERHASIL! Alamat Kontrak $QSTATE: {tx_receipt.contractAddress}")

if __name__ == "__main__":
    deploy()
  
