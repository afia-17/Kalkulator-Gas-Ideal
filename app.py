# Library Konversi dan Konstanta Gas Ideal

# Konversi suhu dari Celsius ke Kelvin
def konversi_suhu(suhu_c):
    """
    Fungsi untuk mengonversi suhu dari Celsius ke Kelvin.
    Rumus: K = °C + 273.15
    Suhu dalam Kelvin merupakan satuan standar dalam perhitungan gas ideal.
    """
    return suhu_c + 273.15

# Konversi tekanan dari berbagai satuan ke atm
def konversi_tekanan(nilai, satuan):
    """
    Fungsi untuk mengonversi tekanan dari berbagai satuan ke satuan atm.
    Didukung: Pa, kPa, hPa, bar, torr, mmHg, atm, L.atm
    Konversi ini penting karena perhitungan menggunakan konstanta R (L.atm/mol.K).
    Rumus konversi tekanan tergantung pada satuan input, contoh:
    - Pa ke atm: bagi dengan 101325
    - kPa ke atm: bagi dengan 101.325
    - mmHg atau Torr ke atm: bagi dengan 760
    - bar ke atm: bagi dengan 1.01325
    """
    satuan = satuan.lower()
    if satuan == 'pa':
        return nilai / 101325
    elif satuan == 'kpa':
        return nilai / 101.325
    elif satuan == 'hpa':
        return nilai / 1013.25
    elif satuan == 'bar':
        return nilai / 1.01325
    elif satuan == 'torr' or satuan == 'mmhg':
        return nilai / 760
    elif satuan == 'l.atm':
        return nilai
    elif satuan == 'atm':
        return nilai
    else:
        raise ValueError("Satuan tekanan tidak dikenali")

# Konversi volume ke liter
def konversi_volume(nilai, satuan):
    """
    Fungsi untuk mengonversi volume ke satuan liter.
    Didukung: mL, cm^3, m^3, L
    Volume dalam liter digunakan dalam rumus gas ideal PV = nRT.
    Rumus umum:
    - m^3 ke L: dikali 1000
    - mL atau cm^3 ke L: dibagi 1000
    """
    satuan = satuan.lower()
    if satuan == 'ml' or satuan == 'cm^3':
        return nilai / 1000
    elif satuan == 'm^3':
        return nilai * 1000
    elif satuan == 'l':
        return nilai
    else:
        raise ValueError("Satuan volume tidak dikenali")

# Pilihan jenis gas ideal yang dapat digunakan dalam perhitungan
# Setiap gas dilengkapi dengan informasi lengkap

# Keterangan kategori:
# 🧪 Rumus Molekul: Struktur kimia dasar dari gas.
# 💨 Sifat Fisika: Warna, bau, massa jenis, titik didih, kelarutan, dll.
# ⚗️ Sifat Kimia: Reaktivitas, stabilitas, interaksi dengan unsur lain.
# 📦 PBK: Pengetahuan dan Penanganan Bahan Kimia — cara penyimpanan, transportasi, dampak kesehatan.
# 🛡️ K3L: Kesehatan, Keselamatan Kerja dan Lingkungan — risiko dan mitigasi saat menggunakan gas.

gas_ideal_info = {
    "Oksigen (O₂)": {
        "🧪 Rumus Molekul": "Gas diatomik dengan rumus O₂, menopang respirasi dan pembakaran.",
        "💨 Sifat Fisika": "Tidak berwarna, tidak berbau, titik didih −183 °C, sedikit larut dalam air.",
        "⚗️ Sifat Kimia": "Oksidator kuat, mudah bereaksi dengan hampir semua unsur membentuk oksida.",
        "📦 PBK": "Disimpan dalam tabung logam bertekanan tinggi, jauh dari minyak dan pelumas.",
        "🛡️ K3L": "Dapat menyebabkan kebakaran hebat, gunakan pelindung dan ventilasi yang memadai."
    },
    "Hidrogen (H₂)": {
        "🧪 Rumus Molekul": "Gas diatomik H₂, unsur paling ringan di alam.",
        "💨 Sifat Fisika": "Tidak berwarna, tidak berbau, sangat ringan, titik didih −253 °C.",
        "⚗️ Sifat Kimia": "Sangat mudah terbakar, membentuk senyawa seperti HCl, H₂O.",
        "📦 PBK": "Dikompresi dalam tabung, sangat mudah terbakar dan meledak dalam udara.",
        "🛡️ K3L": "Jauhkan dari sumber api, gunakan sensor kebocoran dan ruang berventilasi."
    },
    "Karbon dioksida (CO₂)": {
        "🧪 Rumus Molekul": "CO₂, gas hasil dari respirasi, pembakaran sempurna, dan fermentasi.",
        "💨 Sifat Fisika": "Gas berat, larut dalam air membentuk asam lemah, tidak mudah terbakar.",
        "⚗️ Sifat Kimia": "Bereaksi dengan air membentuk H₂CO₃, bersifat asam lemah.",
        "📦 PBK": "Disimpan dalam bentuk cair terkompresi dalam silinder baja.",
        "🛡️ K3L": "Bisa menyebabkan asfiksia, hindari paparan tertutup tanpa ventilasi."
    },
    "Nitrogen (N₂)": {
        "🧪 Rumus Molekul": "N₂ adalah gas diatomik inert yang membentuk 78% atmosfer bumi.",
        "💨 Sifat Fisika": "Tidak berwarna, tidak berbau, inert, titik didih −196 °C.",
        "⚗️ Sifat Kimia": "Sangat stabil dan tidak mudah bereaksi kecuali pada suhu tinggi.",
        "📦 PBK": "Digunakan untuk atmosfer inert, simpan dalam silinder bertekanan.",
        "🛡️ K3L": "Gas inert bisa menyebabkan asfiksia, gunakan monitor O₂."
    },
    "Helium (He)": {
        "🧪 Rumus Molekul": "Unsur gas mulia monoatomik, simbol He.",
        "💨 Sifat Fisika": "Ringan, tak berwarna, tak berbau, titik didih −269 °C.",
        "⚗️ Sifat Kimia": "Tidak reaktif, tidak membentuk senyawa kimia biasa.",
        "📦 PBK": "Simpan dalam silinder logam, tidak mudah terbakar.",
        "🛡️ K3L": "Asfiksia dalam ruang tertutup, tetapi tidak beracun atau mudah terbakar."
    },
    "Argon (Ar)": {
        "🧪 Rumus Molekul": "Gas mulia monoatomik Ar, terdapat dalam udara.",
        "💨 Sifat Fisika": "Tak berwarna, tak berbau, inert, titik didih −186 °C.",
        "⚗️ Sifat Kimia": "Inert secara kimia, tidak bereaksi dalam kondisi normal.",
        "📦 PBK": "Digunakan dalam pengelasan dan laboratorium, disimpan dalam silinder.",
        "🛡️ K3L": "Gunakan ventilasi, karena bisa menggantikan O₂ dan sebabkan asfiksia."
    },
    "Metana (CH₄)": {
        "🧪 Rumus Molekul": "CH₄ adalah gas hidrokarbon sederhana, komponen utama gas alam.",
        "💨 Sifat Fisika": "Tidak berwarna, tidak berbau (ditambahkan bau buatan), mudah terbakar.",
        "⚗️ Sifat Kimia": "Reaktif dalam pembakaran, menghasilkan CO₂ dan H₂O.",
        "📦 PBK": "Simpan di ruang aman, hindari kebocoran karena risiko ledakan.",
        "🛡️ K3L": "Risiko kebakaran dan ledakan tinggi, gunakan detektor gas dan ventilasi cukup."
    }
}

# Konstanta Gas Ideal
R = 0.0821  # L.atm/mol.K
