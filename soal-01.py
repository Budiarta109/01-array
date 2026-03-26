import matplotlib.pyplot as plt

# 1. Input 10 nilai mahasiswa
print("Masukkan 10 nilai mahasiswa:")
nilai = []
for i in range(10):
    while True:
        try:
            n = float(input(f"Nilai mahasiswa ke-{i+1}: "))
            if 0 <= n <= 100: 
                nilai.append(n)
                break
            else:
                print("Masukkan nilai antara 0 - 100.")
        except ValueError:
            print("Input harus berupa angka.")

# Statistik dasar
nilai_max = max(nilai)
nilai_min = min(nilai)
rata_rata = sum(nilai) / len(nilai)

# Jumlah mahasiswa lulus (>= 60)
mhs_lulus = [n for n in nilai if n >= 60]
jumlah_lulus = len(mhs_lulus)
jumlah_tidak_lulus = len(nilai) - jumlah_lulus
persentase_lulus = (jumlah_lulus / len(nilai)) * 100

# Output Ringkasan
print("\n" + "="*40)
print(f"{'RINGKASAN NILAI MAHASISWA':^40}")
print("="*40)
print(f"Skor Tertinggi       : {nilai_max}")
print(f"Skor Terendah        : {nilai_min}")
print(f"Rata-rata Kelas      : {rata_rata:.2f}")
print(f"Jumlah Lulus (>=60)  : {jumlah_lulus} Mahasiswa")
print(f"Jumlah Tidak Lulus   : {jumlah_tidak_lulus} Mahasiswa")
print(f"Persentase Kelulusan : {persentase_lulus:.1f}%")
print("="*40 + "\n")

# 5. GRAFIK
plt.figure(figsize=(9, 6))

kategori = ['Nilai Minimum', 'Rata-rata Nilai', 'Nilai Maksimum']
nilai_grafik = [nilai_min, rata_rata, nilai_max]
warna_grafik = ['#e74c3c', '#f1c40f', '#2ecc71'] 

bars = plt.bar(kategori, nilai_grafik, color=warna_grafik, edgecolor='black', alpha=0.8)

plt.ylim(0, 110) 
plt.title('Analisis Statistik Nilai Mahasiswa', fontsize=15, fontweight='bold', pad=20)
plt.ylabel('Skor (0 - 100)', fontsize=12)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gca().set_axisbelow(True) 

plt.tight_layout()
plt.show()
