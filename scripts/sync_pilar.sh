#!/bin/bash
# Script Sinkronisasi Otomatis Hub Pimpinan Sovereign-Titan-Genesis

# Definisikan daftar pilar repositori bawah payung STG
# Format: "nama_folder_tujuan|URL_repositori_lama"
REPOS=(
    "src/legacy-qubic|https://github.com"
    "src/aigarth-q|https://github.com"
    "src/bsw-nodes|https://github.com"
)

echo "=== MEMULAI SINKRONISASI SUBTREE KE PAYUNG STG ==="

for repo_data in "${REPOS[@]}"; do
    IFS="|" read -r TARGET_DIR REPO_URL <<< "$repo_data"
    
    # Deteksi nama remote unik berdasarkan folder tujuan
    REMOTE_NAME=$(echo "$TARGET_DIR" | tr '/' '_')
    
    echo "------------------------------------------------"
    echo "Menghubungkan ke pilar: $REPO_URL -> Folder: $TARGET_DIR"
    
    # Tambahkan remote jika belum terdaftar
    if ! git remote | grep -q "^$REMOTE_NAME$"; then
        git remote add -f "$REMOTE_NAME" "$REPO_URL"
    fi
    
    # Ambil data terbaru dari remote
    git fetch "$REMOTE_NAME"
    
    # Lakukan penggabungan dengan Git Subtree (menggunakan branch main)
    if [ ! -d "$TARGET_DIR" ]; then
        echo "[NEW] Membuat subtree baru untuk $TARGET_DIR..."
        git subtree add --prefix="$TARGET_DIR" "$REMOTE_NAME" main --squash
    else
        echo "[UPDATE] Memperbarui kode di $TARGET_DIR..."
        git subtree pull --prefix="$TARGET_DIR" "$REMOTE_NAME" main --squash
    fi
done

echo "------------------------------------------------"
echo "=== SINKRONISASI PILAR SELESAI ==="
