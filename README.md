# Muhafidz Ahmad Halim - Technical Test IT Automation Officer Dicoding

Semua solusi otomasi dibuat menggunakan bahasa pemrograman python.

- [Muhafidz Ahmad Halim - Technical Test IT Automation Officer Dicoding](#muhafidz-ahmad-halim---technical-test-it-automation-officer-dicoding)
  - [Case 1 : Meringkas informasi pada sebuah website](#case-1--meringkas-informasi-pada-sebuah-website)
    - [Tentang Program](#tentang-program)
  - [Case 2 : Membuat folder secara otomatis dan dinamis](#case-2--membuat-folder-secara-otomatis-dan-dinamis)
    - [Tentang program](#tentang-program-1)
    - [Cara menggunakan program](#cara-menggunakan-program)
  - [Case 3 : Membuat calendar event dan mengirim email undangan](#case-3--membuat-calendar-event-dan-mengirim-email-undangan)
    - [Tentang Program](#tentang-program-2)
    - [Cara menggunakan program](#cara-menggunakan-program-1)
  - [Case 4 : Mengolah Sheet](#case-4--mengolah-sheet)
    - [Tentang Program](#tentang-program-3)
    - [Cara menggunakan program](#cara-menggunakan-program-2)

## Case 1 : Meringkas informasi pada sebuah website
### Tentang Program
Program otomasi 

## Case 2 : Membuat folder secara otomatis dan dinamis
### Tentang program
Pada case ini, digunakan Google Sheets API untuk membaca [Google Sheets](https://docs.google.com/spreadsheets/d/1TGj2Q-3geoRAdhZfjGfUaeadA0YUpUY7S5yYsR3r-k8/edit#gid=0), dan Google Drive API untuk membuat folder di [Google Drive](https://drive.google.com/drive/folders/1G0VCBSSGo1gLDLrGGoK106ESBlhmEgdK).

Terdapat 2 file:
1. main2.py: program utama. Jalankan file ini untuk menjalankan program.
2. Google.py: berisi fungsi-fungsi untuk melakukan berbagai aksi yang diperlukan untuk mengerjakan tugas.

Fungsi-fungsi yang tersedia antara lain:
* Membuat service dari Google Workspace API
* Membaca [Google Sheet](https://docs.google.com/spreadsheets/d/1TGj2Q-3geoRAdhZfjGfUaeadA0YUpUY7S5yYsR3r-k8/edit#gid=0), 
* Membuat folder di [Google Drive](https://drive.google.com/drive/folders/1G0VCBSSGo1gLDLrGGoK106ESBlhmEgdK), hingga
* Mengatasi folder yang memiliki nama yang sama atau nama yang telah dipakai.

Program ini bisa membuat folder dengan fleksibel berdasarkan nama-nama folder yang ditulis di [Google Sheet](https://docs.google.com/spreadsheets/d/1TGj2Q-3geoRAdhZfjGfUaeadA0YUpUY7S5yYsR3r-k8/edit#gid=0).

### Cara menggunakan program
- Sebelum menjalankan file main2.py, siapkan file *credentials.json* yang didapatkan dari Google Cloud Project yang telah mengaktifkan Google Sheets API dan Google Drive API. 
- Simpan file tersebut di folder yang sama dengan file main2.py.
- Kemudian jalankan file main2.py. Running pertama akan diminta beberapa akses ke akun Google Anda.
- Program akan membuat folder dengan nama-nama folder dari [Google Sheets ini](https://docs.google.com/spreadsheets/d/1TGj2Q-3geoRAdhZfjGfUaeadA0YUpUY7S5yYsR3r-k8/edit#gid=0) ke dalam folder [Google Drive ini](https://drive.google.com/drive/folders/1G0VCBSSGo1gLDLrGGoK106ESBlhmEgdK).

## Case 3 : Membuat calendar event dan mengirim email undangan
### Tentang Program
Program pada case ini menggunakan Google Calendar API untuk membuat event di Google Calendar dan library smtplib untuk mengirim email.

Terdapat 2 file:
1. main3.py: program utama. Jalankan file ini untuk menjalankan program.
2. Google.py: berisi fungsi-fungsi untuk melakukan berbagai aksi yang diperlukan untuk mengerjakan tugas.

Fungsi-fungsi yang tersedia antara lain:
* Membuat service dari Google Workspace API.
* Membuat event di Google Calendar. Informasi event yang dapat diedit pada program ini (untuk saat ini) adalah judul event, waktu pelaksanaan event, lokasi, dan partisipan event. Event yang dibuat pada program ini tidak akan mengirim email secara langsung dari Google Calendar.
* Mengirim email secara terpisah. Perlu memasukan email dan password, dimana email yang digunakan untuk mengirim harus mengaktifkan "Akses aplikasi yang kurang aman" pada akunnya.

Program ini akan membuat event di Google Calendar pada email yang dimasukan sebagai partisipan event.

### Cara menggunakan program
- Sebelum menjalankan file main3.py, siapkan file *credentials.json* yang didapatkan dari Google Cloud Project yang telah mengaktifkan Google Calendar API.
- Simpan file *credentials.json* di folder yang sama dengan file main3.py.
- Isi detail event dan email dengan mengedit variabel-variabel yang bersangkutan di file main3.py, seperti judul event, partisipan, hingga isi email.
- Jalankan file main3.py. Running pertama akan diminta beberapa akses ke akun Google Anda.
- Kemudian akan diminta untuk memasukan email beserta passwordnya untuk keperluan mengirim email.
- Setelah itu, event akan muncul di Google Calendar setiap partisipan dan email juga akan terkirim.

## Case 4 : Mengolah Sheet
### Tentang Program
Program pada case ini menggunakan Google Sheets API untuk membaca dan mengedit [Google Sheets](https://docs.google.com/spreadsheets/d/1JSgfzgXzJ3zYwITGuBiHlCh56GZUE0uLV-vGBrVTS4Q/edit#gid=0). Kemudian menggunakan library schedule untuk membuat jadwal dan rutinitas tugas yang dikerjakan.

Terdapat 2 file:
1. main4.py: program utama. Jalankan file ini untuk menjalankan program.
2. Google.py: berisi fungsi-fungsi untuk melakukan berbagai aksi yang diperlukan untuk mengerjakan tugas.

Fungsi-fungsi yang tersedia antara lain:
* Membuat service dari Google Workspace API.

Program ini akan mengedit isi dari [Google Sheets](https://docs.google.com/spreadsheets/d/1JSgfzgXzJ3zYwITGuBiHlCh56GZUE0uLV-vGBrVTS4Q/edit#gid=0) dengan mengupdate nilai secara rutin dan terjadwal. 

### Cara menggunakan program
- Sebelum menjalankan file main3.py, siapkan file *credentials.json* yang didapatkan dari Google Cloud Project yang telah mengaktifkan Google Sheets API.
- Simpan file *credentials.json* di folder yang sama dengan file main4.py.
- Siapkan environment dengan *pip install -r requirements.txt*
- Jalankan file main4.py. Running pertama akan diminta beberapa akses ke akun Google Anda.
- Program akan berjalan dengan mengupdate isi dari [Google Sheets](https://docs.google.com/spreadsheets/d/1JSgfzgXzJ3zYwITGuBiHlCh56GZUE0uLV-vGBrVTS4Q/edit#gid=0) secara rutin dan terjadwal.