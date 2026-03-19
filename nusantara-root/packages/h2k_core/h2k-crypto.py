
import hashlib
import time

class H2KCrypto:
    def __init__(self, aksara_base="hanacaraka"):
        # Map sederhana untuk simulasi representasi Aksara
        self.aksara_map = {
            '0': 'ha', '1': 'na', '2': 'ca', '3': 'ra', '4': 'ka',
            '5': 'da', '6': 'ta', '7': 'sa', '8': 'wa', '9': 'la'
        }
        self.genesis_stg = "SOVEREIGN-TITAN-GENESIS-V1"

    def process_heartbeat(self, raw_signal):
        """
        Mengubah sinyal detak jantung mentah (Kinetic) menjadi entropy.
        Di ESP32, ini diambil dari nilai ADC (Analog-to-Digital Converter).
        """
        # Simulasi ekstraksi fitur unik dari ritme jantung
        entropy = hashlib.sha256(str(raw_signal).encode()).hexdigest()
        return entropy

    def generate_nusantara_key(self, entropy):
        """
        Mengonversi entropy menjadi deretan Aksara Nusantara (Private Key).
        """
        # Mengambil 10 digit pertama dari hash untuk identitas unik
        numeric_key = str(int(entropy, 16))[:10]
        aksara_key = "".join([self.aksara_map[d] for d in numeric_key])
        return aksara_key

    def sign_state(self, message, private_aksara):
        """
        Menandatangani 'State' agar divalidasi oleh Quorum-State.
        """
        signature = hashlib.sha256(f("{message}{private_aksara}{self.genesis_stg}").encode()).hexdigest()
        return signature

# --- Simulasi Penggunaan oleh ESP32-S3 Node ---
h2k = H2KCrypto()

# 1. Mendapatkan input kinetik (misal: interval antar detak jantung)
raw_pulse = [72, 75, 71, 74] # Input dari sensor biometrik

# 2. Membuat Private Key Aksara
entropy_data = h2k.process_heartbeat(raw_pulse)
my_private_aksara = h2k.generate_nusantara_key(entropy_data)

print(f"Sinyal Kinetik: {raw_pulse}")
print(f"Private Key Aksara: {my_private_aksara}")

# 3. Minting State (Contoh: Validasi Transaksi/Data)
state_data = "VALIDATE_BLOCK_001"
signature = h2k.sign_state(state_data, my_private_aksara)

print(f"Signature Quorum: {signature}")
