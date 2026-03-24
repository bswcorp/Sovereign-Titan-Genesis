import serial, sqlite3

def start_engine():
    conn = sqlite3.connect('quorum_state.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS aksa_vault (signature TEXT, amount INTEGER)')
    
    try:
        # Port USB ESP32 Anda
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) 
        print(">>> Mendengarkan Detak Jantung Titan...")
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if "QS_MINTED_KEY:" in line:
                sig = line.split(":")[1]
                cursor.execute("INSERT INTO aksa_vault (signature, amount) VALUES (?, ?)", (sig, 1000))
                conn.commit()
                print(f"[MINTED] 1000 AKSA Tersimpan di Brankas.")
    except Exception as e: print(f"Error: {e}")
    finally: conn.close()

if __name__ == "__main__":
    start_engine()
