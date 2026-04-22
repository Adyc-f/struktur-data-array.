# struktur-data-array.

## Penjelasan Konsep Array

Array adalah struktur data yang digunakan untuk menyimpan beberapa data dalam satu variabel dengan tipe yang sama. Dalam Python, array dapat direpresentasikan menggunakan list.

Pada program ini, saya menggunakan array (list) untuk menyimpan 10 nilai mahasiswa yang diinput oleh user. Data tersebut kemudian diolah untuk mencari nilai tertinggi, terendah, rata-rata, dan jumlah mahasiswa yang lulus.

Penggunaan array memudahkan dalam pengolahan data secara berulang menggunakan perulangan (loop).

## Screenshot Hasil Program

Berikut adalah hasil eksekusi program:

<img width="949" height="373" alt="Screenshot 2026-04-22 195228" src="https://github.com/user-attachments/assets/01afe54a-baad-4be3-825b-cc9b3d86bb1f" />

## Analisis Kompleksitas

Berikut analisis kompleksitas dari program:

1. Input nilai:
   Menggunakan perulangan sebanyak n kali.
   Kompleksitas: O(n)

2. Mencari nilai tertinggi:
   Melakukan pengecekan seluruh elemen array.
   Kompleksitas: O(n)

3. Mencari nilai terendah:
   Sama seperti nilai tertinggi.
   Kompleksitas: O(n)

4. Menghitung rata-rata:
   Menjumlahkan seluruh elemen array.
   Kompleksitas: O(n)

5. Menghitung jumlah lulus:
   Mengecek setiap nilai apakah >= 60.
   Kompleksitas: O(n)

6. Akses elemen array:
   Mengakses elemen langsung seperti nilai[0].
   Kompleksitas: O(1)

Kesimpulan:
Sebagian besar operasi dalam program ini memiliki kompleksitas O(n) karena menggunakan perulangan untuk mengakses seluruh data.

## Refleksi Pembelajaran

Dari tugas ini, saya belajar bagaimana menggunakan array (list) untuk menyimpan dan mengolah data dalam jumlah banyak.

Saya juga memahami bahwa untuk mendapatkan nilai seperti maksimum, minimum, dan rata-rata, diperlukan proses perulangan untuk mengecek setiap elemen.

Selain itu, saya belajar membuat visualisasi sederhana menggunakan matplotlib untuk menampilkan data dalam bentuk grafik.

Kesulitan yang saya alami adalah memahami cara kerja perulangan dan memastikan logika program berjalan dengan benar. Namun, dengan mencoba dan memperbaiki kesalahan, saya menjadi lebih paham.

Ke depannya, saya ingin mempelajari cara yang lebih efisien dalam mengolah data serta memahami struktur data lainnya.

Menurut saya, latihan ini membantu saya berpikir lebih sistematis dalam menyelesaikan masalah menggunakan logika pemrograman.
