# VERSI LOKAL (PENYIMPANAN SQLITE)
import serial, sqlite3

def start_aksa_engine():
    conn = sqlite3.connect('quorum_state.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS aksa_vault (signature TEXT, amount INTEGER)')
    
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) 
        print(">>> Jantung Titan Terhubung. Menunggu Sinyal Minting...")
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if "QS_MINTED_KEY:" in line:
                sig = line.split(":")[1]
                cursor.execute("INSERT INTO aksa_vault (signature, amount) VALUES (?, ?)", (sig, 1000))
                conn.commit()
                print(f"[MINTED] +1000 AKSA Tersimpan di Brankas.")
    except Exception as e: print(f"Gangguan: {e}")
    finally: conn.close()
      
