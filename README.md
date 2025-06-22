# 🗂️ File Organizer GUI (Python + Tkinter)

Aplikasi desktop sederhana berbasis Python + Tkinter untuk mengatur file secara otomatis ke dalam folder berdasarkan ekstensi — lengkap dengan fitur **Undo**, **Kategori Kustom**, dan **Log File**.

---

## 🚀 Fitur Utama

✅ GUI berbasis Tkinter  
✅ Kategori otomatis berdasarkan ekstensi file  
✅ Fitur **Undo** untuk mengembalikan file ke lokasi semula  
✅ **Kategori Kustom**: Tambah/edit jenis file dan kategorinya langsung dari GUI  
✅ Log otomatis (file `organize_log.json`) untuk pelacakan dan pemulihan  
✅ Responsif, ringan, dan mudah digunakan

---

## 📦 Struktur Proyek

📁 FileOrganizer/
├── file_organizer_gui_custom.py
├── kategori.json # Dibuat otomatis jika belum ada
├── organize_log.json # Dibuat saat file dipindahkan

---

## 💡 Cara Menggunakan

1. **Jalankan aplikasi:**
   ```bash
   python file_organizer_gui_custom.py
Klik Pilih Folder & Organize → pilih folder yang ingin ditata.
Klik Atur Kategori jika ingin menambah/mengubah kategori dan ekstensi.
Gunakan tombol Undo Organize untuk mengembalikan semua file ke posisi semula (selama file organize_log.json belum dihapus).

---

## 🛠️ Fitur Tambah Kategori atau Ekstensi
- Klik tombol Atur Kategori di GUI
- Tambah kategori baru (misal: Archive)
- Tambah ekstensi ke kategori tersebut (misal: .zip, .7z)
- Kategori dan ekstensi disimpan di file kategori.json agar tetap tersimpan saat aplikasi ditutup.

---

## 🔧 Dependensi
Python 3.x
Modul built-in: os, shutil, json, tkinter
Tidak butuh instalasi library eksternal.

---

## 📸 Tampilan GUI
GUI dengan tiga tombol utama:
- Pilih Folder & Organize
- Undo Organize
- Atur Kategori

---

## 🧠 Catatan
File yang sudah dipindahkan disimpan dalam organize_log.json agar bisa di-undo
Tidak disarankan menghapus file log jika ingin bisa melakukan Undo
Aplikasi tidak menghapus file, hanya memindahkan

---

## 📄 Lisensi
MIT License © 2025 — Dibuat oleh Raihan Anmar Widyasmoro.
