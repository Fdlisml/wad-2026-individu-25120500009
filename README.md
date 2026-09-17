# WAD 2026 - Individu (Topik 3: Pengiriman)

Repository ini berisi implementasi endpoint API untuk layanan **Pengiriman** menggunakan **FastAPI**. Tugas ini dibuat untuk memenuhi Definition of Done (DoD) tugas individu mata kuliah Pemrograman Web dan Aplikasi (WAD).

## Informasi Mahasiswa
* **Nama:** Fadli Ismail
* **NIM:** 25120500009
* **Topik:** 3 (Pengiriman)

## Prasyarat
Pastikan Python versi 3.10 ke atas sudah terinstal di komputermu.

## Cara Menjalankan Project Lokal

1. **Aktifkan Virtual Environment**
   Windows:
   ```bash
   .venv\Scripts\activate
   ```
   Mac/Linux:
   ```bash
   source .venv/bin/activate
   ```

2. **Install Dependencies**
   Pastikan library yang dibutuhkan sudah terinstal:
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```

3. **Jalankan Server FastAPI**
   Jalankan server menggunakan CLI FastAPI:
   ```bash
   fastapi dev app/main.py
   ```
   Server akan berjalan secara lokal di: `http://127.0.0.1:8000`

## Dokumentasi API (Swagger UI)
FastAPI secara otomatis menyediakan dokumentasi interaktif. Setelah server berjalan, kamu bisa mengaksesnya dan mencoba endpoint secara langsung melalui:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## Spesifikasi Endpoint API
Sesuai dengan panduan tugas, berikut adalah endpoint yang tersedia:

1. **`POST /api/pengiriman`**
   * **Deskripsi:** Membuat data resi pengiriman baru.
   * **Validasi:** `no_resi` wajib berawalan JKT diikuti 7 digit angka (misal: `JKT1234567`). `berat_kg` maksimal 50kg.
   * **Respons Sukses:** `201 Created` disertai header `Location`.
   * **Respons Gagal:** `422 Unprocessable Entity` jika input tidak valid.

2. **`GET /api/pengiriman`**
   * **Deskripsi:** Mengambil daftar pengiriman yang sudah dibuat.
   * **Query Params:** Mendukung `?skip`, `?limit`, dan pencarian no_resi dengan `?search`.
   * **Respons Sukses:** `200 OK`.

3. **`GET /api/pengiriman/{id}`**
   * **Deskripsi:** Mengambil detail pengiriman spesifik berdasarkan ID (ID di-generate oleh server).
   * **Respons Gagal:** `404 Not Found` jika ID tidak ditemukan.

## Testing/Verifikasi (Sesuai DoD)
Untuk memastikan kode sudah lulus standar pengecekan dosen, jalankan perintah tester dari root repository:
```bash
python verify.py --individu
```
Pastikan hasilnya berstatus **hijau (PASS)**.
