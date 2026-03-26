# Konsep Array dalam Program

Dalam Python, konsep Array diimplementasikan menggunakan tipe data List.
•Penyimpanan Data: List digunakan untuk menampung sekumpulan nilai mahasiswa (nilai = []) dalam satu variabel tunggal.
•Akses Elemen: Kita mengakses data menggunakan indeks (misalnya nilai[0] untuk mahasiswa pertama).
•Iterasi: Program menggunakan List Comprehension [n for n in nilai if n >= 60] untuk menyaring data secara efisien tanpa memerlukan banyak baris kode.
•Dinamis: List di Python bersifat dinamis, sehingga kita bisa menambah data menggunakan fungsi .append() saat melakukan perulangan input.

# Input Nilai & Output teks di terminal
<img width="624" height="652" alt="image" src="https://github.com/user-attachments/assets/778423f1-d074-4785-a5d6-e1201a412639" />

# Grafik (Nilai Minimum/NilaiRata-Rata/Nilai Maksimum)
<img width="1351" height="1006" alt="image" src="https://github.com/user-attachments/assets/c4a065b0-12ba-4b0c-80cc-ec983ed0fa94" />

| Operasi | Metode yang Digunakan | Kompleksitas Waktu | Kompleksitas Ruang | Keterangan |
|---------|-----------------------|--------------------|--------------------|------------|
| Input 10 Nilai | while loop + append() | $O(1)$ | $O(n)$ | $n=10$ (Tetap/Konstan) |
|---------|-----------------------|--------------------|--------------------|------------|
| Mencari Nilai Maksimum | max(nilai) | $O(n)$ | $O(1)$ | Melakukan traversal seluruh elemen |
|---------|-----------------------|--------------------|--------------------|------------|
| Mencari Nilai Minimum | min(nilai) | $O(n)$ | $O(1)$ | Melakukan traversal seluruh elemen |
|---------|-----------------------|--------------------|--------------------|------------|
| Menghitung Rata-rata | sum(nilai) / len() | $O(n)$ | $O(1)$ | Memerlukan akumulasi seluruh data |
|---------|-----------------------|--------------------|--------------------|------------|
| Filter Kelulusan | list comprehension | $O(n)$ | $O(n)$ | Membuat list baru untuk filter data |
|---------|-----------------------|--------------------|--------------------|------------|
| Menampilkan Output | print() f-string | $O(1)$ | $O(1)$ | Operasi I/O standar |
|---------|-----------------------|--------------------|--------------------|------------|
| Visualisasi Grafik | matplotlib.pyplot | $O(1)$ | $O(1)$ | Untuk data kecil, rendering sangat cepat |
|---------|-----------------------|--------------------|--------------------|------------|
| Keseluruhan Program | — | $O(n)$ | $O(n)$ | Efisien secara Linear |
|---------|-----------------------|--------------------|--------------------|------------|

# Refleksi PembelajaranSetelah menyelesaikan proyek kecil ini, berikut adalah poin-poin penting yang saya pelajari:
•Validasi Data yang Kuat: Menggunakan blok try-except sangat krusial dalam Python untuk mencegah program force close saat user memasukkan data non-numerik.
•Visualisasi Data: Saya memahami bagaimana menerjemahkan data mentah menjadi informasi visual menggunakan matplotlib. Penentuan batas sumbu Y (plt.ylim) dan pelabelan angka di atas grafik      sangat membantu audiens dalam membaca data.
•Efisiensi Fungsi Bawaan: Penggunaan fungsi built-in seperti max(), min(), dan sum() terbukti lebih efisien dan membuat kode lebih bersih (clean code) dibandingkan menulis perulangan manual.
•Skalabilitas: Meskipun program ini diatur untuk 10 mahasiswa, strukturnya sudah siap untuk menangani jumlah data yang lebih besar ($n$) dengan kompleksitas linear.
