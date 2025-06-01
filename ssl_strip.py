import time

def tampilkan_koneksi(judul, url, protokol, status):
    print(f"\n🔍 {judul}")
    print("=" * 40)
    print(f"URL      : {url}")
    print(f"Protokol : {protokol}")
    print(f"Status   : {status}")
    print("=" * 40)

def simulasi_ssl_stripping():
    url = "www.bank-ku.com"
    protokol_asli = "HTTPS"
    protokol_strip = "HTTP"

    print("""
╔════════════════════════════════════════════╗
║         🔓 SSL Strip - Simulasi Edukasi    ║
║       HTTPS ➜ HTTP (Tanpa Enkripsi)       ║
╚════════════════════════════════════════════╝
""")

    time.sleep(1)
    tampilkan_koneksi("Koneksi Aman (Normal)", url, protokol_asli, "🔒 Enkripsi Aktif")
    time.sleep(2)
    tampilkan_koneksi("Koneksi Setelah SSL Stripping", url, protokol_strip, "⚠️ TIDAK TERENKRIPSI")

    print("""
🚨 Hati-Hati:
- Jika HTTPS berubah jadi HTTP, data bisa disadap
- Jangan masukkan password di situs tanpa ikon gembok

✅ Edukasi selesai - Jaga privasi & keamanan data Anda!
""")

if __name__ == "__main__":
    input("Tekan Enter untuk mulai simulasi SSL stripping...")
    simulasi_ssl_stripping()
