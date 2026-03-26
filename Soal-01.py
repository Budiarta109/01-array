import matplotlib.pyplot as plt

# Input 10 nilai mahasiswa
print("Masukkan 10 nilai mahasiswa:")
nilai = []

for i in range(10): 
    while True:
        try:
            input_user = input(f"Nilai mahasiswa ke-{i+1}: ")
            if input_user.strip() == "": 
                 print("Input tidak boleh kosong.")
                 continue
                 
            n = float(input_user)
            if 0 <= n <= 100: 
                nilai.append(n)
                break
            else:
                print("Masukkan nilai antara 0 - 100.")
        except ValueError:
            print("Input harus berupa angka.")

# Hitung statistik dasar
nilai_max = max(nilai)
nilai_min = min(nilai)
rata_rata = sum(nilai) / len(nilai)

# Hitung data kelulusan (>= 60)
mhs_lulus = [n for n in nilai if n >= 60]
jumlah_lulus = len(mhs_lulus)
jumlah_tidak_lulus = len(nilai) - jumlah_lulus
persentase_lulus = (jumlah_lulus / len(nilai)) * 100

# Output Ringkasan di Terminal
print("\n" + "="*45)
print(f"{'RINGKASAN NILAI MAHASISWA':^45}")
print("="*45)
print(f"Skor Tertinggi        : {nilai_max}")
print(f"Skor Terendah         : {nilai_min}")
print(f"Rata-rata Kelas       : {rata_rata:.2f}")
print("-" * 45)
print(f"Jumlah Lulus (>=60)   : {jumlah_lulus} Mahasiswa")
print(f"Jumlah Tidak Lulus    : {jumlah_tidak_lulus} Mahasiswa")
print(f"Persentase Kelulusan  : {persentase_lulus:.1f}%")
print("="*45 + "\n")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Analisis Hasil Studi Mahasiswa', fontsize=18, fontweight='bold', y=0.98)

# GRAFIK 1: Statistik Nilai 
kategori_stats = ['Minimum', 'Rata-rata', 'Maksimum']
nilai_stats = [nilai_min, rata_rata, nilai_max]
warna_stats = ['#e74c3c', '#f1c40f', '#2ecc71'] 

bars = ax1.bar(kategori_stats, nilai_stats, color=warna_stats, edgecolor='black', alpha=0.8)


ax1.set_ylim(0, 110) 
ax1.set_title('Statistik Nilai Kelas', fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel('Skor (0 - 100)', fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.5)
ax1.set_axisbelow(True) 

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval:.1f}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')
    
#GRAFIK 2: Data Kelulusan
label_kelulusan = ['Lulus (>=60)', 'Tidak Lulus']
data_pie = [jumlah_lulus, jumlah_tidak_lulus]
warna_pie = ['#2ecc71', '#e74c3c'] 
explode = (0.05, 0) 

if jumlah_lulus == 0 or jumlah_tidak_lulus == 0:
    explode = (0, 0)

wedges, texts, autotexts = ax2.pie(data_pie, labels=label_kelulusan, autopct='%1.1f%%', 
                                  startangle=90, colors=warna_pie, explode=explode,
                                  shadow=True, textprops=dict(color="black"))

plt.setp(texts, fontsize=12, fontweight='bold')
plt.setp(autotexts, fontsize=12, fontweight='bold', color='white') 

ax2.set_title('Proporsi Kelulusan', fontsize=14, fontweight='bold', pad=15)
ax2.axis('equal') 

ax2.legend(wedges, [f"{label_kelulusan[0]}: {jumlah_lulus} Mhs", 
                    f"{label_kelulusan[1]}: {jumlah_tidak_lulus} Mhs"],
           title="Detail", loc="lower right", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.show()
