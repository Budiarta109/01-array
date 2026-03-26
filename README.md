# Created by I Nyoman Budiarta

# 1. Konsep Array dalam Program

Dalam Python, konsep Array diimplementasikan menggunakan tipe data List.
* Penyimpanan Data: List digunakan untuk menampung sekumpulan nilai mahasiswa (nilai = []) dalam satu variabel tunggal.

* Akses Elemen: Kita mengakses data menggunakan indeks (misalnya nilai[0] untuk mahasiswa pertama).

* Iterasi: Program menggunakan List Comprehension [n for n in nilai if n >= 60] untuk menyaring data secara efisien tanpa memerlukan banyak baris kode.

* Dinamis: List di Python bersifat dinamis, sehingga kita bisa menambah data menggunakan fungsi .append() saat melakukan perulangan input.

# Screenshoot Hasil Eksekusi
1. Input Nilai & Output teks di terminal
<img width="868" height="626" alt="image" src="https://github.com/user-attachments/assets/e4be9ed8-d73a-49c7-ac84-5f2d33c42d73" />

2. Grafik (Nilai Minimum/NilaiRata-Rata/Nilai Maksimum) & Grafik Proporsi Kelulusan
<img width="2098" height="995" alt="image" src="https://github.com/user-attachments/assets/f046901b-f6ea-4dad-9d35-53a2d1ee62ee" />

# 3. Analisis Kompleksitas

| Operasi | Metode yang Digunakan | Kompleksitas Waktu | Kompleksitas Ruang | Keterangan |
|---------|-----------------------|--------------------|--------------------|------------|
| Input 10 Nilai | while loop + append() | $O(1)$ | $O(n)$ | $n=10$ (Tetap/Konstan) |
| Mencari Nilai Maksimum | max(nilai) | $O(n)$ | $O(1)$ | Melakukan traversal seluruh elemen |
| Mencari Nilai Minimum | min(nilai) | $O(n)$ | $O(1)$ | Melakukan traversal seluruh elemen |
| Menghitung Rata-rata | sum(nilai) / len() | $O(n)$ | $O(1)$ | Memerlukan akumulasi seluruh data |
| Filter Kelulusan | list comprehension | $O(n)$ | $O(n)$ | Membuat list baru untuk filter data |
| Menampilkan Output | print() f-string | $O(1)$ | $O(1)$ | Operasi I/O standar |
| Visualisasi Grafik | matplotlib.pyplot | $O(1)$ | $O(1)$ | Untuk data kecil, rendering sangat cepat |
| Keseluruhan Program | — | $O(n)$ | $O(n)$ | Efisien secara Linear |

# 4. Refleksi PembelajaranSetelah menyelesaikan proyek kecil ini, berikut adalah poin-poin penting yang saya pelajari:
* Validasi Data yang Kuat: Menggunakan blok try-except sangat krusial dalam Python untuk mencegah program force close saat user memasukkan data non-numerik.

* Visualisasi Data: Saya memahami bagaimana menerjemahkan data mentah menjadi informasi visual menggunakan matplotlib. Penentuan batas sumbu Y (plt.ylim) dan pelabelan angka di atas grafik sangat membantu audiens dalam membaca data.

* Efisiensi Fungsi Bawaan: Penggunaan fungsi built-in seperti max(), min(), dan sum() terbukti lebih efisien dan membuat kode lebih bersih (clean code) dibandingkan menulis perulangan manual.

* Skalabilitas: Meskipun program ini diatur untuk 10 mahasiswa, strukturnya sudah siap untuk menangani jumlah data yang lebih besar ($n$) dengan kompleksitas linear.
