# Program pengelolaan nilai mahasiswa

nilai = []

print("=== Input Nilai Mahasiswa ===")

for i in range(10):
    n = int(input(f"Masukkan nilai ke-{i+1}: "))
    nilai.append(n)

print("\nData nilai:", nilai)

# mencari nilai tertinggi
maks = nilai[0]
for n in nilai:
    if n > maks:
        maks = n

# mencari nilai terendah
minim = nilai[0]
for n in nilai:
    if n < minim:
        minim = n

print("\nNilai tertinggi:", maks)
print("Nilai terendah:", minim)
