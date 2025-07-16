import streamlit as st
import math

# --- Halaman Awal ---
st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

st.title("💨 Kalkulator Gas Ideal")
st.markdown("""
Selamat datang di **Kalkulator Gas Ideal**!

🔹 Gunakan aplikasi ini untuk menghitung: massa gas, tekanan, volume, dan jumlah mol berdasarkan persamaan **PV = nRT**.  
🔹 Pelajari juga teori dan sifat berbagai **gas ideal** di bagian *Library*.  

Pilih menu di sidebar untuk memulai ⬅️
""")

# --- Sidebar Menu ---
menu = st.sidebar.selectbox("📂 Menu", ["Halaman Utama", "Kalkulator", "Library"])

# --- Menu Kalkulator ---
if menu == "Kalkulator":
    st.header("🧮 Kalkulator Gas Ideal")
    tab = st.radio("Pilih jenis perhitungan:", ["Massa Gas", "Tekanan", "Volume", "Jumlah Mol"])

    R = 0.0821  # konstanta gas dalam L.atm/mol.K

    if tab == "Massa Gas":
        st.subheader("📦 Menghitung Massa Gas")
        nama = st.text_input("Nama gas")
        mol = st.number_input("Jumlah mol (n)", min_value=0.0, format="%.4f")
        mr = st.number_input("Massa molar (g/mol)", min_value=0.0, format="%.4f")
        if st.button("Hitung Massa"):
            massa = mol * mr
            st.success(f"Massa {nama}: {massa:.4f} gram")

    elif tab == "Tekanan":
        st.subheader("🧯 Menghitung Tekanan Gas")
        nama = st.text_input("Nama gas")
        mol = st.number_input("Jumlah mol (n)", min_value=0.0, format="%.4f")
        T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
        V = st.number_input("Volume (L)", min_value=0.0, format="%.2f")
        if st.button("Hitung Tekanan"):
            P = (mol * R * T) / V if V != 0 else 0
            st.success(f"Tekanan {nama}: {P:.4f} atm")

    elif tab == "Volume":
        st.subheader("🔲 Menghitung Volume Gas")
        nama = st.text_input("Nama gas")
        mol = st.number_input("Jumlah mol (n)", min_value=0.0, format="%.4f")
        T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
        P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f")
        if st.button("Hitung Volume"):
            V = (mol * R * T) / P if P != 0 else 0
            st.success(f"Volume {nama}: {V:.4f} L")

    elif tab == "Jumlah Mol":
        st.subheader("🌡️ Menghitung Jumlah Mol Gas")
        nama = st.text_input("Nama gas")
        P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f")
        V = st.number_input("Volume (L)", min_value=0.0, format="%.2f")
        T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
        if st.button("Hitung Mol"):
            n = (P * V) / (R * T) if T != 0 else 0
            st.success(f"Jumlah mol {nama}: {n:.4f} mol")

# --- Menu Library ---
elif menu == "Library":
    st.title("📚 Library: Gas Ideal dan Contohnya")

    st.subheader("📖 Apa Itu Gas Ideal?")
    st.markdown("""
Gas ideal adalah model teoritis dalam ilmu kimia yang menggambarkan perilaku gas di mana partikel gas:
- ⚪ Tidak memiliki volume sendiri
- 🧲 Tidak saling berinteraksi
- 🔁 Bergerak acak secara terus menerus
- 💥 Mengalami tumbukan elastis sempurna

#### Rumus Gas Ideal:
""")
    st.latex("PV = nRT")
    st.markdown("""
- **P** = Tekanan (atm)
- **V** = Volume (L)
- **n** = Mol gas
- **R** = Konstanta gas (0.0821)
- **T** = Suhu (K)

ℹ️ Gas nyata dapat berperilaku mendekati gas ideal pada suhu tinggi dan tekanan rendah.
---
""")

    st.subheader("🔍 Pilih Gas Ideal untuk Detail")
    gas_list = [
        "Pilih gas ideal...",
        "Hidrogen (H₂)", "Oksigen (O₂)", "Nitrogen (N₂)",
        "Karbon Dioksida (CO₂)", "Metana (CH₄)",
        "Helium (He)", "Neon (Ne)"
    ]
    pilihan = st.selectbox("🧬 Gas Ideal:", gas_list)

    gas_data = {
        "Hidrogen (H₂)": {
            "rumus": "H₂",
            "fisika": "🌀 Gas sangat ringan, tidak berwarna, titik didih -252.9°C",
            "kimia": "🔥 Reaktif, mudah terbakar, membentuk H₂O",
            "pbk": "⚙️ Digunakan sebagai bahan bakar alternatif",
            "k3l": "🚨 Hindari api terbuka, gunakan detektor kebocoran"
        },
        "Oksigen (O₂)": {
            "rumus": "O₂",
            "fisika": "💨 Tak berwarna, mendukung pembakaran",
            "kimia": "🔥 Bereaksi membentuk oksida",
            "pbk": "🏥 Digunakan di rumah sakit, industri logam",
            "k3l": "⚠️ Hindari kontak dengan bahan mudah terbakar"
        },
        "Nitrogen (N₂)": {
            "rumus": "N₂",
            "fisika": "🌫️ Gas inert, tidak berbau",
            "kimia": "🧪 Tidak reaktif pada suhu normal",
            "pbk": "❄️ Digunakan sebagai pendingin",
            "k3l": "🚷 Dapat menyebabkan asfiksia di ruang tertutup"
        },
        "Karbon Dioksida (CO₂)": {
            "rumus": "CO₂",
            "fisika": "⚫ Gas berat, larut dalam air",
            "kimia": "🍋 Bersifat asam, membentuk H₂CO₃",
            "pbk": "🥤 Digunakan di minuman karbonasi",
            "k3l": "🛑 Hindari paparan berlebih di ruang tertutup"
        },
        "Metana (CH₄)": {
            "rumus": "CH₄",
            "fisika": "🔋 Gas mudah terbakar",
            "kimia": "🔥 Bereaksi dengan O₂ membentuk CO₂ dan H₂O",
            "pbk": "💡 Digunakan sebagai gas alam",
            "k3l": "⚠️ Risiko ledakan tinggi, perlu ventilasi baik"
        },
        "Helium (He)": {
            "rumus": "He",
            "fisika": "🎈 Gas sangat ringan dan inert",
            "kimia": "🧊 Tidak reaktif",
            "pbk": "🔬 Digunakan dalam MRI dan balon",
            "k3l": "⚠️ Jangan dihirup langsung, bisa sebabkan asfiksia"
        },
        "Neon (Ne)": {
            "rumus": "Ne",
            "fisika": "💡 Digunakan dalam lampu neon",
            "kimia": "🧪 Sangat stabil, tidak reaktif",
            "pbk": "🌈 Dipakai dalam industri pencahayaan",
            "k3l": "📦 Simpan sesuai prosedur tekanan"
        }
    }

    if pilihan != "Pilih gas ideal...":
        data = gas_data[pilihan]
        st.markdown(f"### 🧪 Rumus Molekul: `{data['rumus']}`")
        st.markdown(f"**🧊 Sifat Fisika:** {data['fisika']}")
        st.markdown(f"**🧪 Sifat Kimia:** {data['kimia']}")
        st.markdown(f"**📘 PBK:** {data['pbk']}")
        st.markdown(f"**🦺 K3L:** {data['k3l']}")

    st.markdown("---")
    st.subheader("🔗 Referensi")
    st.markdown("""
- [Studiobelajar – Gas Ideal](https://www.studiobelajar.com/gas-mulia/)
- [Kumparan – Elektron Gas Mulia](https://kumparan.com/kabar-harian/konfigurasi-elektron-gas-mulia-sebagai-penyebab-kestabilan-unsur-gas-mulia-1xHrcUepikN/full)
- [Aku Pintar – Sifat Gas](https://akupintar.id/belajar/-/online/materi/modul/12-mia/kimia/kimia-unsur/sifat-sifat-unsur/461443)
- [Pijar Belajar – Gas Ideal](https://www.pijarbelajar.id/blog/gas-mulia)
""")
