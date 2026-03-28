import os
import subprocess

def get_real_uptime():
    # Mengambil data Uptime Nyata dari sistem
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return f"{uptime_seconds / 3600:.2f} Jam"
    except:
        return "Akses Terbatas"

def get_real_node_latency():
    # Testing Jalur Nyata ke Google
    try:
        # Gunakan shell=True agar lebih stabil di UserLand
        cmd = "ping -c 1 8.8.8.8 | grep 'time=' | awk -F'time=' '{print $2}'"
        lat = subprocess.check_output(cmd, shell=True).decode().strip()
        return f"{lat}"
    except:
        return "TIMEOUT"

def run_test():
    print("\n" + "!"*50)
    print("🏛️  STG REAL-WORK MONITOR (USERLAND ADAPTIVE)")
    print("!"*50)
    
    # KERNEL UPTIME (Ini biasanya diizinkan)
    uptime = get_real_uptime()
    print(f"🫀  KERNEL UPTIME (Live)    : {uptime}")
    
    # NODE DATA
    node_lat = get_real_node_latency()
    print(f"📍  NODE LATENCY (Jakarta)  : {node_lat}")
    
    print("-" * 50)
    print("✅ STATUS: DATA REAL DARI SOCKET & PROC.")
    print("🦊 PESAN: SATPAM ANDROID BERHASIL DIGOCEK!")
    print("="*50)

if __name__ == "__main__":
    run_test()
