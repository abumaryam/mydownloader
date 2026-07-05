#!/usr/bin/env python3
"""
Script untuk mendownload seluruh file (termasuk isi subfolder) dari sebuah
folder Google Drive yang dishare secara PUBLIK (bisa diakses tanpa login).

Requirement:
    pip install gdown

Cara pakai:
    1. Copy link folder Google Drive publik tersebut.
       Contoh format link:
         https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOpQrStUvWxYz
    2. Jalankan script ini:
         python download_gdrive_folder.py
       lalu tempel (paste) link folder saat diminta.
       Atau langsung lewat argumen:
         python download_gdrive_folder.py "https://drive.google.com/drive/folders/xxxxx"
    3. Semua file & subfolder akan otomatis didownload ke folder "hasil_download"
       dengan struktur folder yang sama seperti aslinya.

Catatan:
    - Script ini HANYA bekerja untuk folder yang sharing-nya diset
      "Anyone with the link" (publik), karena tidak melakukan login akun Google.
    - Untuk folder yang sangat besar, Google kadang membatasi (rate limit).
      Jika terjadi error karena limit, coba jalankan ulang beberapa saat kemudian.
"""

import sys
import re

try:
    import gdown
except ImportError:
    print("Package 'gdown' belum terinstall.")
    print("Install dulu dengan perintah: pip install gdown")
    sys.exit(1)


OUTPUT_DIR = "hasil_download"


def ekstrak_folder_id(link: str) -> str:
    """Mengambil folder ID dari berbagai kemungkinan format link Google Drive."""
    link = link.strip()

    # Format: https://drive.google.com/drive/folders/<ID>
    match = re.search(r"/folders/([a-zA-Z0-9_-]+)", link)
    if match:
        return match.group(1)

    # Format: https://drive.google.com/drive/u/0/folders/<ID>
    match = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", link)
    if match:
        return match.group(1)

    # Kalau yang dimasukkan sudah berupa ID langsung
    if re.fullmatch(r"[a-zA-Z0-9_-]+", link):
        return link

    return ""


def main():
    print("=== Google Drive Public Folder Downloader ===\n")

    if len(sys.argv) > 1:
        link = sys.argv[1]
    else:
        link = input("Masukkan link folder Google Drive publik: ").strip()

    folder_id = ekstrak_folder_id(link)

    if not folder_id:
        print("Link/ID folder tidak dikenali. Pastikan formatnya seperti:")
        print("  https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOpQrStUvWxYz")
        sys.exit(1)

    folder_url = f"https://drive.google.com/drive/folders/{folder_id}"
    print(f"\nFolder ID terdeteksi: {folder_id}")
    print(f"Mulai mendownload ke folder: {OUTPUT_DIR}\n")

    # Beberapa versi gdown belum mendukung parameter 'remaining_ok',
    # jadi coba dulu dengan parameter itu, kalau error karena versi lama,
    # otomatis fallback tanpa parameter tersebut.
    base_kwargs = dict(
        url=folder_url,
        output=OUTPUT_DIR,
        quiet=False,
        use_cookies=False,   # tidak butuh login karena folder publik
    )

    try:
        try:
            gdown.download_folder(remaining_ok=True, **base_kwargs)
        except TypeError:
            # Versi gdown lama tidak mengenal parameter 'remaining_ok'
            gdown.download_folder(**base_kwargs)
    except Exception as e:
        print(f"\nTerjadi kesalahan saat mendownload: {e}")
        print("Kemungkinan penyebab:")
        print("- Folder tidak benar-benar publik (butuh login/izin akses)")
        print("- Terkena rate limit Google, coba lagi beberapa saat lagi")
        sys.exit(1)

    print("\n" + "=" * 50)
    print(f"Selesai! Semua file tersimpan di folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()