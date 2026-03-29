import shutil
import os
import time

def upgrade_with_safe(filename):
    if os.path.exists(filename):
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        archive_path = f"archive/version_control/{filename}_{timestamp}.bak"
        shutil.copy(filename, archive_path)
        print(f"📦 [SROT!] {filename} LAMA DIARSIPKAN KE: {archive_path}")
    else:
        print(f"🆕 MEMULAI PEMBUATAN {filename} VERSI BARU.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        upgrade_with_safe(sys.argv[1])
