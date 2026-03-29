import os
import shutil
import time

def archive_file(filename, folder_dest):
    if os.path.exists(filename):
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        new_name = f"{filename.split('.')[0]}_{timestamp}.{filename.split('.')[1]}"
        shutil.copy(filename, f"{folder_dest}/{new_name}")
        print(f"📦 BERHASIL: {filename} TELAH DIARSIPKAN KE {new_name}")
    else:
        print("⚠️ FILE TIDAK DITEMUKAN UNTUK DIARSIPKAN.")

if __name__ == "__main__":
    archive_file("../index.html", "../archive/naskah_web")
