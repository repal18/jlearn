# J-Learn SMKN 1 Lahat — Interactive Learning Platform

Platform belajar Bahasa Jepang untuk siswa SMKN 1 Lahat. Frontend-first, akses terbuka, akun tidak wajib.

## Teknologi
- **Python + Flask**: routing dan backend web.
- **Jinja2 + HTML**: template halaman.
- **CSS**: desain Japanese Minimalist responsif.
- **JavaScript**: logika kuis, game, penyimpanan lokal, Web Speech API.
- **Alpine.js**: state reaktif untuk filter, flashcard, dan kuis kosakata.
- **HTMX**: mengambil study tip dari Flask dan memperbarui satu bagian halaman tanpa reload.
- **Chart.js**: grafik aktivitas belajar.
- **Browser LocalStorage**: progres lokal tanpa akun.

## Halaman
- `/` Beranda
- `/belajar` Learning Center
- `/kana` Kana Learning Lab: 46 Hiragana + 46 Katakana, pencarian, audio, kuis
- `/kosakata` Vocabulary Lab: 28 kosakata, filter kategori, pencarian, flashcard flip, audio, kuis 10 soal
- `/dojo` J-Dojo: memory-match game dan daily mission
- `/progress` Learning Passport: XP, level, statistik, grafik Chart.js, achievement, ekspor JSON
- `/latihan` Latihan
- `/budaya` Budaya Jepang
- `/tentang` Tentang
- `/htmx/tip` HTML fragment untuk demonstrasi HTMX
- `/api/ping` API health check JSON

## Jalankan di Windows / VS Code
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
py app.py
```
Buka `http://127.0.0.1:5000`.

## Catatan teknis
- Alpine.js, HTMX, dan Chart.js dimuat dari CDN; koneksi internet dibutuhkan untuk library tersebut.
- Data progres disimpan pada browser/perangkat yang dipakai, tidak disinkronkan antar perangkat.
- Browser Speech Synthesis menyediakan pelafalan; ketersediaan suara Jepang bergantung pada sistem operasi dan browser.
- Konten kosakata merupakan bahan demonstrasi awal. Minta guru/pembina Bahasa Jepang memeriksa romaji, contoh kalimat, dan tingkat kesulitannya sebelum publikasi.
- Belum ada akun, leaderboard publik, atau panel admin. Fitur tersebut perlu desain privasi dan persetujuan sekolah terlebih dahulu.


## J-Learn 2.0 visual upgrade

Versi ini menambahkan desain beranda baru, navigasi responsif, maskot Kitsune, bubble tips interaktif, animasi reveal saat scroll, dan styling global yang konsisten. Aset maskot berada di `static/images/kitsune-mascot.png`.

Jalankan dengan: `pip install -r requirements.txt` lalu `python app.py`.
