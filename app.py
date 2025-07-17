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
    satuan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key=satuan_key)
    P_input = st.number_input(f"{label} ({satuan})", min_value=0.0, key=input_key)
    
    konversi = {
        "Pa": 101325,
        "kPa": 101.325,
        "hPa": 1013.25,
        "bar": 1.01325,
        "Torr": 760,
        "mmHg": 760
    }
    
    if satuan in konversi:
        P = P_input / konversi[satuan]
        st.success(f"Telah dikonversi otomatis: {P_input} {satuan} = {P:.5f} atm")
    else:
        P = P_input
    return P

# Fungsi konversi volume
def konversi_volume_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key=satuan_key)
    V_input = st.number_input(f"{label} ({satuan})", min_value=0.1, key=input_key)
    
    if satuan == "m³":
        V = V_input * 1000
        st.success(f"Telah dikonversi otomatis: {V_input} m³ = {V:.2f} L")
    elif satuan == "mL":
        V = V_input / 1000
        st.success(f"Telah dikonversi otomatis: {V_input} mL = {V:.4f} L")
    else:
        V = V_input
    return V

# Sidebar menu
menu = st.sidebar.selectbox("📂 Menu", ["🏠 Halaman Utama", "🧮 Kalkulator", "📚 Library"])

# Halaman Utama
if menu == "🏠 Halaman Utama":
    st.title("💨 Kalkulator Gas Ideal")
    st.markdown("""
    Selamat datang di **Kalkulator Gas Ideal**!
    
    🔹 Aplikasi ini dapat digunakan untuk menghitung massa, tekanan, volume, dan jumlah mol gas ideal menggunakan persamaan gas ideal:
    """)
    
    st.latex(r'''PV = nRT''')
    
    st.markdown("""
    Dimana:
    - P = Tekanan (atm)
    - V = Volume (L)
    - n = Jumlah mol (mol)
    - R = Konstanta gas ideal (0.0821 L·atm/mol·K)
    - T = Suhu (K)
    
    🔹 Anda juga dapat mempelajari informasi kimia, fisika, serta aspek K3L berbagai gas ideal di bagian *Library*.  
    Silakan pilih menu di sidebar untuk melanjutkan. ⬅️
    """)

# Halaman Kalkulator
if menu == "🧮 Kalkulator":
    st.header("🧮 Kalkulator Gas Ideal")
    pilihan = st.radio("Pilih jenis perhitungan:", ["Massa Gas", "Tekanan", "Volume", "Jumlah Mol"])

    R = 0.0821  # konstanta gas ideal dalam L.atm/mol.K

    if pilihan == "Massa Gas":
        st.markdown("**Rumus:** Massa = n × Mr")
        nama = st.text_input("Nama Gas", key="nama_massa")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_massa")
        mr = st.number_input("Massa Molar (Mr) [g/mol]", min_value=0.0, key="mr_massa")
        if st.button("Hitung Massa"):
            massa = n * mr
            st.success(f"Massa {nama} = {massa:.2f} gram")

    elif pilihan == "Tekanan":
        st.markdown("**Rumus:** P = (n × R × T) / V")
        nama = st.text_input("Nama Gas", key="nama_tekanan")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_tekanan")
        T = konversi_suhu_input("Suhu", "satuan_t_tekanan", "T_input_tekanan")
        V = konversi_volume_input("Volume", "satuan_v_tekanan", "V_tekanan")
        if st.button("Hitung Tekanan"):
            P = (n * R * T) / V
            st.success(f"Tekanan {nama} = {P:.4f} atm")

    elif pilihan == "Volume":
        st.markdown("**Rumus:** V = (n × R × T) / P")
        nama = st.text_input("Nama Gas", key="nama_volume")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_volume")
        T = konversi_suhu_input("Suhu", "satuan_t_volume", "T_input_volume")
        P = konversi_tekanan_input("Tekanan", "satuan_p_volume", "P_volume")
        if st.button("Hitung Volume"):
            V = (n * R * T) / P
            st.success(f"Volume {nama} = {V:.4f} L")

    elif pilihan == "Jumlah Mol":
        st.markdown("**Rumus:** n = (P × V) / (R × T)")
        nama = st.text_input("Nama Gas", key="nama_mol")
        P = konversi_tekanan_input("Tekanan", "satuan_p_mol", "P_mol")
        V = konversi_volume_input("Volume", "satuan_v_mol", "V_mol")
        T = konversi_suhu_input("Suhu", "satuan_t_mol", "T_input_mol")
        if st.button("Hitung Jumlah Mol"):
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.4f} mol")

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
            "🧪 Rumus Molekul": "Hidrogen adalah unsur kimia dengan simbol H dan nomor atom 1. Pada kondisi standar, hidrogen adalah gas diatomik (H₂) yang tidak berwarna, tidak berbau, sangat mudah terbakar, dan merupakan unsur paling ringan di alam semesta.",
            "💨 Sifat Fisika": """
            - Massa molar: 2.016 g/mol
            - Titik leleh: -259.16 °C (13.99 K)
            - Titik didih: -252.87 °C (20.28 K)
            - Densitas: 0.08988 g/L (STP)
            - Fase pada suhu kamar: Gas
            - Tidak berwarna dan tidak berbau
            """,
            "⚗️ Sifat Kimia": """
            - Sangat mudah terbakar
            - Bereaksi dengan oksigen membentuk air (2H₂ + O₂ → 2H₂O)
            - Dapat bereaksi dengan logam alkali dan alkali tanah membentuk hidrida
            - Bersifat reduktor kuat
            - Memiliki energi ikatan yang tinggi (436 kJ/mol)
            """,
            "📦 Pengetahuan dan Penanganan Bahan Kimia (PBK)": """
            - Harus disimpan dalam tabung bertekanan tinggi
            - Jauhkan dari sumber api, panas, dan oksidator
            - Ruang penyimpanan harus memiliki ventilasi yang baik
            - Gunakan material yang kompatibel seperti baja nirkarat atau aluminium
            """,
            "🛡️ Kesehatan dan Keselamatan Kerja dan Lingkungan (K3L)": """
            - Dapat menyebabkan asfiksia pada konsentrasi tinggi
            - Sangat mudah terbakar (rentang mudah terbakar 4-75% di udara)
            - Tidak beracun tetapi dapat menggantikan oksigen di udara
            - Gunakan alat pelindung diri (APD) yang sesuai saat menangani
            - Detektor kebocoran hidrogen diperlukan di area kerja
            """
        },
        "Oksigen (O₂)": {
            "🧪 Rumus Molekul": "Oksigen adalah unsur kimia dengan simbol O dan nomor atom 8. Pada kondisi standar, oksigen adalah gas diatomik (O₂) yang tidak berwarna, tidak berbau, dan sangat penting untuk proses respirasi dan pembakaran.",
            "💨 Sifat Fisika": """
            - Massa molar: 32.00 g/mol
            - Titik leleh: -218.79 °C (54.36 K)
            - Titik didih: -182.96 °C (90.19 K)
            - Densitas: 1.429 g/L (STP)
            - Fase pada suhu kamar: Gas
            - Paramagnetik (tertarik oleh medan magnet)
            """,
            "⚗️ Sifat Kimia": """
            - Oksidator kuat
            - Mendukung pembakaran
            - Bereaksi dengan kebanyakan unsur membentuk oksida
            - Membentuk ozon (O₃) dengan adanya pelepasan listrik
            - Esensial untuk respirasi seluler
            """,
            "📦 Pengetahuan dan Penanganan Bahan Kimia (PBK)": """
            - Simpan dalam tabung bertekanan khusus
            - Jauhkan dari minyak dan bahan mudah terbakar
            - Gunakan regulator tekanan yang tepat
            - Periksa kebocoran secara rutin
            - Hindari kontaminasi dengan bahan organik
            """,
            "🛡️ Kesehatan dan Keselamatan Kerja dan Lingkungan (K3L)": """
            - Pada konsentrasi tinggi dapat menyebabkan keracunan oksigen
            - Meningkatkan risiko kebakaran secara signifikan
            - Gunakan di ruangan berventilasi baik
            - Hindari kontak dengan kulit cairan oksigen (sangat dingin)
            - APD yang diperlukan: kacamata keselamatan, sarung tangan
            """
        },
        # [Tambahkan gas lainnya dengan format yang sama...]
    }

    # Pilih gas
    selected_gas = st.selectbox("Pilih Gas Ideal", list(gas_ideal.keys()))
    
    # Tampilkan informasi gas
    gas_info = gas_ideal[selected_gas]
    
    for category, info in gas_info.items():
        with st.expander(category):
            st.markdown(info)
