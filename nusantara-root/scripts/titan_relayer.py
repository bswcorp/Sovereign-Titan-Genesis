from web3 import Web3

# 1. KONEKSI PUSAT KOMANDO (Bensin ditanggung Pusat)
w3 = Web3(Web3.HTTPProvider("https://1891.rpc.thirdweb.com"))

# 2. BRANKAS BENSIN (Akun Pusat yang bayar semua Gas Fee)
# Di sinilah Bapak simpan saldo ETH Faucet yang banyak
CENTRAL_PAYMASTER_ADDR = "0xD9a1E28224d6d047Eef8712dC97d11A9032b948e"
PAYMASTER_PRIVATE_KEY = "PRIVATE_KEY_BAPAK_YANG_RAHASIA"

# 3. KONTRAK QSTATE
CONTRACT_ADDRESS = "0x70a64d8216e91077B2C36695596482Be068640c1"
ABI = [...] # (ABI Standar Transfer)

def kirim_tanpa_bensin(pengirim_addr, penerima_addr, jumlah_aksa):
    print(f">>> [SIRKUS AKTIF] Memproses pengiriman {jumlah_aksa} Aksa...")
    print(f">>> Biaya bensin ditanggung oleh Otoritas: ANDI MUHAMMAD HARPIANTO")

    # Pusat Komando yang menandatangani transaksi
    nonce = w3.eth.get_transaction_count(CENTRAL_PAYMASTER_ADDR)
    
    # Perintah Transfer dikirim oleh Pusat atas nama Pengirim
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
    
    # Eksekusi (Gas Fee diambil dari CENTRAL_PAYMASTER_ADDR)
    tx = contract.functions.transfer(penerima_addr, jumlah_aksa).build_transaction({
        'from': CENTRAL_PAYMASTER_ADDR,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.to_wei('0.1', 'gwei')
    })

    signed_tx = w3.eth.account.sign_transaction(tx, PAYMASTER_PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print(f">>> BERHASIL! Transaksi Selesai. Hash: {tx_hash.hex()}")
    print(">>> Penonton hanya melihat saldo mereka terpotong. Beres!")

if __name__ == "__main__":
    # Contoh: Pusat kirim koin ke seseorang tanpa orang itu bayar bensin
    kirim_tanpa_bensin(CENTRAL_PAYMASTER_ADDR, "0xALAMAT_PENERIMA", 1000000)
