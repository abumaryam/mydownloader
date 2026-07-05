#!/usr/bin/env python3
"""
Script untuk mendownload video YouTube dari daftar link di file download.txt
kemudian mengkonversinya ke format MP3.

Requirement:
    pip install yt-dlp
    ffmpeg harus terinstall di sistem (untuk konversi audio)
    - Windows: download dari https://ffmpeg.org/download.html lalu tambahkan ke PATH
    - Linux (Debian/Ubuntu): sudo apt install ffmpeg
    - macOS: brew install ffmpeg

Cara pakai:
    1. Buat file bernama download.txt di folder yang sama dengan script ini.
    2. Isi download.txt dengan link video YouTube, satu link per baris. Contoh:
        https://www.youtube.com/watch?v=xxxxxxxxxxx
        https://www.youtube.com/watch?v=yyyyyyyyyyy
    3. Jalankan: python download_youtube_mp3.py
    4. Hasil MP3 akan tersimpan di folder "hasil_mp3".
"""

import os
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Package 'yt-dlp' belum terinstall.")
    print("Install dulu dengan perintah: pip install yt-dlp")
    sys.exit(1)


INPUT_FILE = "download.txt"
OUTPUT_DIR = "hasil_mp3"


def baca_daftar_link(file_path: str) -> list[str]:
    """Membaca daftar link dari file text, mengabaikan baris kosong dan komentar (#)."""
    if not os.path.exists(file_path):
        print(f"File '{file_path}' tidak ditemukan.")
        print(f"Silakan buat file '{file_path}' berisi daftar link YouTube (satu link per baris).")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    links = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            links.append(line)

    return links


def progress_hook(d):
    if d["status"] == "downloading":
        persen = d.get("_percent_str", "").strip()
        judul = d.get("info_dict", {}).get("title", "video")
        print(f"\rDownload '{judul}': {persen}", end="", flush=True)
    elif d["status"] == "finished":
        print("\nDownload selesai, sedang konversi ke MP3...")


def download_dan_konversi(links: list[str], output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "progress_hooks": [progress_hook],
        "noplaylist": True,
        "ignoreerrors": True,  # lanjut ke link berikutnya jika satu link gagal
        "quiet": False,
    }

    berhasil, gagal = 0, 0

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i, link in enumerate(links, start=1):
            print(f"\n[{i}/{len(links)}] Memproses: {link}")
            try:
                ydl.download([link])
                berhasil += 1
            except Exception as e:
                print(f"Gagal memproses {link}: {e}")
                gagal += 1

    print("\n" + "=" * 50)
    print(f"Selesai! Berhasil: {berhasil}, Gagal: {gagal}")
    print(f"File MP3 tersimpan di folder: {os.path.abspath(output_dir)}")


def main():
    print("=== YouTube to MP3 Downloader ===\n")
    links = baca_daftar_link(INPUT_FILE)

    if not links:
        print(f"Tidak ada link yang ditemukan di '{INPUT_FILE}'.")
        sys.exit(1)

    print(f"Ditemukan {len(links)} link di '{INPUT_FILE}'.\n")
    download_dan_konversi(links, OUTPUT_DIR)


if __name__ == "__main__":
    main()