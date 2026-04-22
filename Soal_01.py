# Program pengelolaan nilai mahasiswa

nilai = []

print("=== Input Nilai Mahasiswa ===")

for i in range(10):
    n = int(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

print("\nData nilai:", nilai)
