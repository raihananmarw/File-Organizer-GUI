import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

LOG_FILE = "organize_log.json"
KATEGORI_FILE = "kategori.json"

# Load kategori dari file atau buat default
def load_kategori():
    if not os.path.exists(KATEGORI_FILE):
        default = {
            'Gambar': ['.jpg', '.jpeg', '.png'],
            'Dokumen': ['.pdf', '.docx', '.txt'],
            'Musik': ['.mp3'],
            'Video': ['.mp4'],
            'Python': ['.py']
        }
        with open(KATEGORI_FILE, 'w') as f:
            json.dump(default, f)
        return default
    with open(KATEGORI_FILE, 'r') as f:
        return json.load(f)

def save_kategori(kategori):
    with open(KATEGORI_FILE, 'w') as f:
        json.dump(kategori, f, indent=2)

kategori = load_kategori()

def dapatkan_kategori(ekstensi):
    for nama, ekstensi_list in kategori.items():
        if ekstensi.lower() in ekstensi_list:
            return nama
    return 'Lainnya'

def organize_folder(folder_path):
    log_data = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path):
            ekstensi = os.path.splitext(file)[1]
            folder_tujuan = os.path.join(folder_path, dapatkan_kategori(ekstensi))
            os.makedirs(folder_tujuan, exist_ok=True)
            new_path = os.path.join(folder_tujuan, file)
            shutil.move(full_path, new_path)
            log_data.append({
                "asal": new_path,
                "tujuan": full_path
            })

    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f)

def undo_organize():
    if not os.path.exists(LOG_FILE):
        messagebox.showinfo("Info", "Tidak ada log untuk undo.")
        return
    with open(LOG_FILE, "r") as f:
        log_data = json.load(f)
        for item in log_data:
            if os.path.exists(item["asal"]):
                shutil.move(item["asal"], item["tujuan"])
    os.remove(LOG_FILE)
    messagebox.showinfo("Sukses", "Undo selesai.")

def atur_kategori():
    kategori_baru = load_kategori()
    top = tk.Toplevel()
    top.title("Atur Kategori")
    top.geometry("400x300")

    tk.Label(top, text="Edit atau Tambah Kategori dan Ekstensi", font=("Arial", 10)).pack(pady=5)

    listbox = tk.Listbox(top)
    listbox.pack(fill=tk.BOTH, expand=True, padx=10)

    def refresh_list():
        listbox.delete(0, tk.END)
        for nama, exts in kategori_baru.items():
            listbox.insert(tk.END, f"{nama}: {', '.join(exts)}")

    def tambah_kategori():
        nama = simpledialog.askstring("Tambah Kategori", "Masukkan nama kategori:")
        if nama and nama not in kategori_baru:
            kategori_baru[nama] = []
            refresh_list()

    def tambah_ekstensi():
        nama = simpledialog.askstring("Kategori", "Kategori tujuan:")
        if nama and nama in kategori_baru:
            ext = simpledialog.askstring("Tambah Ekstensi", "Masukkan ekstensi (misal: .zip):")
            if ext and ext not in kategori_baru[nama]:
                kategori_baru[nama].append(ext)
                refresh_list()

    def simpan():
        save_kategori(kategori_baru)
        global kategori
        kategori = kategori_baru
        top.destroy()
        messagebox.showinfo("Sukses", "Kategori berhasil diperbarui!")

    tk.Button(top, text="Tambah Kategori", command=tambah_kategori).pack(pady=2)
    tk.Button(top, text="Tambah Ekstensi", command=tambah_ekstensi).pack(pady=2)
    tk.Button(top, text="Simpan Perubahan", command=simpan).pack(pady=5)

    refresh_list()

# GUI Utama
root = tk.Tk()
root.title("File Organizer - Kategori Kustom")
root.geometry("420x220")
root.resizable(False, False)

tk.Label(root, text="Organisasi File Otomatis", font=("Arial", 13, "bold"), pady=10).pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

def pilih_folder():
    folder = filedialog.askdirectory()
    if folder:
        try:
            organize_folder(folder)
            status_label.config(text="✅ Berhasil mengorganisir file!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

tk.Button(root, text="Pilih Folder & Organize", command=pilih_folder, bg="#4caf50", fg="white", padx=10, pady=5).pack(pady=5)
tk.Button(root, text="Undo Organize", command=undo_organize, bg="#f44336", fg="white", padx=10, pady=5).pack(pady=5)
tk.Button(root, text="Atur Kategori", command=atur_kategori, bg="#2196f3", fg="white", padx=10, pady=5).pack(pady=5)

root.mainloop()