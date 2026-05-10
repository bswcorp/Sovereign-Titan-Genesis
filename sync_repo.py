import subprocess
import os

# Konfigurasi: Masukkan URL repositori yang ingin digabungkan
REPOS_TO_MERGE = {
    "Titan-Legacy": "https://github.com/username/titan-legacy.git",
    "Genesis-Core": "https://github.com/username/genesis-core.git",
    "Sovereign-Auth": "https://github.com/username/sovereign-auth.git"
}

def run_cmd(cmd):
    """Menjalankan perintah terminal."""
    print(f"Menjalankan: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result

def merge_repositories():
    # Inisialisasi jika belum ada git
    if not os.path.exists(".git"):
        run_cmd(["git", "init"])
        run_cmd(["git", "commit", "--allow-empty", "-m", "Initial monorepo commit"])

    for repo_name, repo_url in REPOS_TO_MERGE.items():
        print(f"\n--- Menggabungkan {repo_name} ---")
        
        # 1. Tambahkan remote dan ambil data
        run_cmd(["git", "remote", "add", repo_name, repo_url])
        run_cmd(["git", "fetch", repo_name])
        
        # 2. Gabungkan sejarah (history) commit
        # Gunakan --allow-unrelated-histories untuk menggabungkan dua repo berbeda
        run_cmd(["git", "merge", f"{repo_name}/main", "--allow-unrelated-histories", "-m", f"Merge {repo_name}"])
        
        # 3. Pindahkan file ke sub-folder agar tidak bentrok
        os.makedirs(repo_name, exist_ok=True)
        files = [f for f in os.listdir('.') if f not in [repo_name, ".git"]]
        for f in files:
            run_cmd(["git", "mv", f, repo_name])
            
        run_cmd(["git", "commit", "-m", f"Organisasi folder untuk {repo_name}"])
        run_cmd(["git", "remote", "remove", repo_name])

    print("\n[SUKSES] Semua repositori telah digabungkan ke Sovereign-Titan-Genesis.")

if __name__ == "__main__":
    merge_repositories()
  
