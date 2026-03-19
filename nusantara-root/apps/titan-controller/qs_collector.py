import serial
import sqlite3
import time

# Konfigurasi Koneksi (Sesuaikan port jika perlu, biasanya /dev/ttyACM0)
SERIAL_PORT = '/dev/ttyACM0' 
BAUD_RATE = 115200

# 1. Inisialisasi Database Quorum-State
def init_db():
    conn = sqlite3.connect('quorum_state.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS minted_keys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aksara_signature TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn

def start_collector():
    conn = init_db()
    cursor = conn.cursor()
    
    print(f">>> QS-Collector: Menunggu Signature dari Sovereign Titan...")
    
    try:
        # Membuka koneksi serial
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                
                # Cek apakah baris mengandung Signature hasil Minting
                if "QS_MINTED_KEY:" in line:
                    signature = line.split(":")[1]
                    
                    # Simpan ke Database
                    cursor.execute("INSERT INTO minted_keys (aksara_signature) VALUES (?)", (signature,))
                    conn.commit()
                    
                    print(f"[SAVED] Quorum-State Updated: {signature}")
                    
    except KeyboardInterrupt:
        print("\n>>> Collector Dihentikan.")
    finally:
        conn.close()

if __name__ == "__main__":
    start_collector()
