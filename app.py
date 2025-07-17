# Aplikasi Kalkulator Gas Ideal dengan Streamlit

import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

# Fungsi konversi suhu

def konversi_suhu_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key=satuan_key)
    T_input = st.number_input(f"{label} ({satuan})", min_value=-273.0, key=input_key)
    if satuan == "°C":
        T = T_input + 273.15
        st.success(f"Telah dikonversi otomatis: {T_input}°C = {T:.2f} K")
    else:
        T = T_input
    return T

# Fungsi konversi tekanan ke atm

def konversi_tekanan_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], key=satuan_key)
    P_input = st.number_input(f"{label} ({satuan})", min_value=0.0, key=input_key)
    if satuan == "Pa":
        P = P_input / 101325
        st.success(f"Telah dikonversi otomatis: {P_input} Pa = {P:.5f} atm")
    elif satuan == "kPa":
        P = P_input / 101.325
        st.success(f"Telah dikonversi otomatis: {P_input} kPa = {P:.5f} atm")
    elif satuan == "hPa":
        P = P_input / 1013.25
        st.success(f"Telah dikonversi otomatis: {P_input} hPa = {P:.5f} atm")
    elif satuan == "bar":
        P = P_input / 1.01325
        st.success(f"Telah dikonversi otomatis: {P_input} bar = {P:.5f} atm")
    elif satuan in ["Torr", "mmHg"]:
        P = P_input / 760
        st.success(f"Telah dikonversi otomatis: {P_input} {satuan} = {P:.5f} atm")
    else:
        P = P_input
    return P

# Sidebar menu
menu = st.sidebar.selectbox("📂 Menu", ["🏠 Halaman Utama", "🧮 Kalkulator", "📚 Library"], key="menu_select")

# Halaman Utama
if menu == "🏠 Halaman Utama":
    st.title("💨 Kalkulator Gas Ideal")
    st.markdown("""
    Selamat datang di **Kalkulator Gas Ideal**!

    🔹 Aplikasi ini dapat digunakan untuk menghitung massa, tekanan, volume, dan jumlah mol gas ideal menggunakan persamaan PV = nRT.  
    🔹 Anda juga dapat mempelajari informasi kimia, fisika, serta aspek K3L berbagai gas ideal di bagian *Library*.  
    Silakan pilih menu di sidebar untuk melanjutkan. ⬅️
    """)

# Halaman Kalkulator
if menu == "🧮 Kalkulator":
    st.header("🧮 Kalkulator Gas Ideal")
    pilihan = st.radio("Pilih jenis perhitungan:", ["Massa Gas", "Tekanan", "Volume", "Jumlah Mol"])

    R = 0.0821  # konstanta gas ideal dalam L.atm/mol.K

    if pilihan == "Massa Gas":
        nama = st.text_input("Nama Gas", key="nama_massa")
        n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa")
        mr = st.number_input("Massa Molar (g/mol)", min_value=0.0, key="mr_massa")
        if st.button("Hitung Massa"):
            massa = n * mr
            st.success(f"Massa {nama} = {massa:.2f} gram")

    elif pilihan == "Tekanan":
        nama = st.text_input("Nama Gas", key="nama_tekanan")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_tekanan")
        T = konversi_suhu_input("Suhu", "satuan_t_tekanan", "T_input_tekanan")
        V = st.number_input("Volume", min_value=0.1, key="V_tekanan")
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"], key="satuan_v_tekanan")
        if satuan_v == "m³":
            V *= 1000
        if st.button("Hitung Tekanan"):
            P = (n * R * T) / V
            st.success(f"Tekanan {nama} = {P:.4f} atm")

    elif pilihan == "Volume":
        nama = st.text_input("Nama Gas", key="nama_volume")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_volume")
        T = konversi_suhu_input("Suhu", "satuan_t_volume", "T_input_volume")
        P = konversi_tekanan_input("Tekanan", "satuan_p_volume", "P_volume")
        satuan_v = st.selectbox("Satuan Volume Output", ["L", "m³"], key="satuan_v_volume")
        if st.button("Hitung Volume"):
            V = (n * R * T) / P
            if satuan_v == "m³":
                V /= 1000
            st.success(f"Volume {nama} = {V:.4f} {satuan_v}")

    elif pilihan == "Jumlah Mol":
        nama = st.text_input("Nama Gas", key="nama_mol")
        P = konversi_tekanan_input("Tekanan", "satuan_p_mol", "P_mol")
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"], key="satuan_v_mol")
        V = st.number_input(f"Volume ({satuan_v})", min_value=0.1, key="V_mol")
        if satuan_v == "m³":
            V *= 1000
        T = konversi_suhu_input("Suhu", "satuan_t_mol", "T_input_mol")
        if st.button("Hitung Jumlah Mol"):
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.2f} mol")

# Halaman Library
if menu == "📚 Library":
    st.header("📚 Informasi Gas Ideal")
    st.markdown("""
    Di bawah ini adalah daftar gas ideal dengan informasi terkait:
    - Rumus molekul
    - Sifat fisika
    - Sifat kimia
    - Pengetahuan Bahan Kimia (PBK)
    - Kesehatan dan Keselamatan Kerja dan Lingkungan (K3L)
    """)

    gas_ideal = {
        "Hidrogen (H₂)": {
            "Rumus Molekul": "Hidrogen adalah unsur paling ringan, berbentuk H₂ dalam kondisi standar.",
            "Sifat Fisika": "Tidak berwarna, tidak berbau, sangat ringan, mudah menguap dan terbakar.",
            "Sifat Kimia": "Sangat reaktif dan mudah membentuk senyawa dengan banyak unsur lain.",
            "PBK": "Disimpan dalam tabung bertekanan tinggi, jauhkan dari sumber api dan panas.",
            "K3L": "Gunakan ventilasi baik dan alat pelindung diri saat menangani hidrogen."
        },
        "Oksigen (O₂)": {
            "Rumus Molekul": "Oksigen adalah gas diatomik yang menunjang pembakaran, rumusnya O₂.",
            "Sifat Fisika": "Gas tidak berbau dan tidak berwarna, sangat penting untuk respirasi.",
            "Sifat Kimia": "Bersifat oksidator kuat dan mudah membentuk senyawa oksida.",
            "PBK": "Simpan dalam tabung khusus dan jauhkan dari bahan yang mudah terbakar.",
            "K3L": "Gunakan di ruang berventilasi, hindari kontak dengan bahan mudah terbakar."
        },
        "Nitrogen (N₂)": {
            "Rumus Molekul": "Nitrogen hadir secara alami sebagai gas diatomik N₂.",
            "Sifat Fisika": "Gas inert, tak berwarna dan tak berbau, titik didih -196 °C.",
            "Sifat Kimia": "Reaktivitas rendah, digunakan sebagai pelindung dari oksidasi.",
            "PBK": "Disimpan dalam tabung bertekanan, digunakan dalam kondisi aman.",
            "K3L": "Cegah asfiksia, gunakan dalam ruangan dengan ventilasi baik."
        },
        "Karbon Dioksida (CO₂)": {
            "Rumus Molekul": "Karbon dioksida adalah gas hasil respirasi dan pembakaran, CO₂.",
            "Sifat Fisika": "Gas berat, larut dalam air, tidak berbau dan tidak berwarna.",
            "Sifat Kimia": "Reaktif dengan air membentuk asam karbonat, sifat asam lemah.",
            "PBK": "Simpan dalam ruang sejuk dan silinder berlabel.",
            "K3L": "Ventilasi diperlukan untuk mencegah akumulasi dan sesak napas."
        }
    }

    warna_kategori = {
        "Rumus Molekul": "#e0f7fa",
        "Sifat Fisika": "#e8f5e9",
        "Sifat Kimia": "#fff3e0",
        "PBK": "#fce4ec",
        "K3L": "#f5f5f5"
    }

    ikon_kategori = {
        "Rumus Molekul": "🧪 Rumus Molekul",
        "Sifat Fisika": "💨 Sifat Fisika",
        "Sifat Kimia": "⚗️ Sifat Kimia",
        "PBK": "📦 Pengetahuan dan Penanganan Bahan Kimia (PBK)",
        "K3L": "🛡️ Kesehatan dan Keselamatan Kerja dan Lingkungan (K3L)"
    }

    pilih = st.selectbox("Pilih Gas Ideal", list(gas_ideal.keys()))
    data = gas_ideal[pilih]
    for k, v in data.items():
        warna = warna_kategori.get(k, "#ffffff")
        judul = ikon_kategori.get(k, k)
        st.markdown(f"""
        <div style='background-color:{warna}; padding:15px; border-radius:10px; margin-bottom:10px;'>
            <h4>{judul}</h4>
            <p style='text-align: justify;'>{v}</p>
        </div>
        """, unsafe_allow_html=True)
