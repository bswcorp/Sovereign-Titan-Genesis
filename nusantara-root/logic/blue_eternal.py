# BLUE ETERNAL ENGINE V5.0 - "THE SOVEREIGN BLUE"
# Dilengkapi dengan fitur Eternal Backup ke GitHub.
import hashlib
import time
import requests # Pastikan instal: pip install requests
import base64

class BlueEternalEngine:
    def __init__(self, key="NUSANTARA_ETERNAL", github_token=None, repo=None):
        self.genesis_hash = hashlib.sha256(key.encode()).hexdigest()
        self.BLUE_MARKER = "᨞ ᨅᨆᨑᨘ ᨞" 
        self.github_token = github_token
        self.repo = repo # Format: "username/repo"

    def oceanic_encrypt(self, data):
        """Mode Samudra: Enkripsi Spiral Berliku (Deep Archives)"""
        raw = f"{self.genesis_hash[:4]}{data}{int(time.time())}".lower().replace(" ", "x")
        blocks = [raw[i:i+5] for i in range(0, len(raw), 5)]
        cipher = []
        for i, b in enumerate(blocks):
            b = b[::-1] if i % 2 == 0 else b[1:] + b[0]
            cipher.append(b) 
        return f"{self.BLUE_MARKER} OCEANIC-DEEP ᨞ {'-'.join(cipher)}"

    def eternal_backup(self, file_path, content):
        """Otomatisasi Pencadangan ke GitHub (Pesan untuk Masa Depan)"""
        if not self.github_token or not self.repo:
            return "Backup Skip: Token/Repo tidak diatur."
        
        url = f"https://api.github.com/repos/{self.repo}/contents/{file_path}"
        headers = {
            "Authorization": f"token {self.github_token}", 
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Ambil SHA file jika sudah ada untuk update
        res = requests.get(url, headers=headers)
        sha = res.json().get('sha') if res.status_code == 200 else None
        
        payload = {
            "message": f"Eternal Backup: {time.ctime()}",
            "content": base64.b64encode(content.encode()).decode(),
            "sha": sha
        }
        
        put_res = requests.put(url, headers=headers, json=payload)
        return "Backup Sukses" if put_res.status_code in [200, 201] else f"Gagal: {put_res.text}"

if __name__ == "__main__":
    # MASUKKAN TOKEN GITHUB HASIL PANDUAN DI BAWAH KE SINI:
    MY_TOKEN = "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" # Ganti dengan token asli Anda
    MY_REPO = "bswcorp/Sovereign-Titan-Genesis"
    
    be = BlueEternalEngine(github_token=MY_TOKEN, repo=MY_REPO)
    log_data = "Kedaulatan Biru Nusantara - Sesi Cadangan Abadi"
    print(be.eternal_backup("backups/blue_log.txt", be.oceanic_encrypt(log_data)))
