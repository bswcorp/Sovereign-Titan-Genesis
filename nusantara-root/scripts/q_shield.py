import os
import hashlib

def generate_quantum_key(seed):
    # Simulasi Lattice-based key generation
    return hashlib.sha3_512(seed.encode()).hexdigest()

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    
    # XOR dengan Quantum Key (Simulasi)
    encrypted = bytearray([b ^ ord(key[i % len(key)]) for i, b in enumerate(data)])
    
    with open(filename + ".qshield", 'wb') as f:
        f.write(encrypted)
    print(f"[*] File {filename} telah dibungkus Perisai Kuantum (1Ai).")

# Eksekusi untuk file sensitifmu
seed = "Bourbon-Sovereign-Titan-1Ai" # Ini kunci rahasiamu
key = generate_quantum_key(seed)

files_to_shield = ['cold_vault_dna.txt', 'kedaulatan_mandiri.sho']
for f in files_to_shield:
    if os.path.exists(f):
        encrypt_file(f, key)
