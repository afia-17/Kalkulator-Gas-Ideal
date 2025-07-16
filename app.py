# Aplikasi Kalkulator Gas Ideal dengan Streamlit

import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

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
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"], key="satuan_t_tekanan")
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0, key="T_input_tekanan")
        if satuan_t == "°C":
            T = T_input + 273.15
            st.write(f"Telah dikonversi otomatis: {T_input}°C = {T:.2f} K")
        else:
            T = T_input

        V = st.number_input("Volume", min_value=0.1, key="V_tekanan")
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"], key="satuan_v_tekanan")
        if satuan_v == "m³":
            V *= 1000  # konversi ke liter (dm³)

        satuan_p = st.selectbox("Satuan Tekanan Output", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], key="satuan_p_tekanan")

        if st.button("Hitung Tekanan"):
            P = (n * R * T) / V  # hasil dalam atm
            hasil = P
            if satuan_p == "Pa":
                hasil = P * 101325
            elif satuan_p == "kPa":
                hasil = P * 101.325
            elif satuan_p == "hPa":
                hasil = P * 1013.25
            elif satuan_p == "bar":
                hasil = P * 1.01325
            elif satuan_p == "Torr" or satuan_p == "mmHg":
                hasil = P * 760
            elif satuan_p == "L.atm":
                hasil = P
            st.success(f"Tekanan {nama} = {hasil:.2f} {satuan_p}")

    elif pilihan == "Volume":
        nama = st.text_input("Nama Gas", key="nama_volume")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_volume")
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"], key="satuan_t_volume")
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0, key="T_input_volume")
        T = T_input + 273.15 if satuan_t == "°C" else T_input
        P = st.number_input("Tekanan (atm)", min_value=0.1, key="P_volume")
        satuan_v = st.selectbox("Satuan Volume Output", ["L", "m³"], key="satuan_v_volume")
        if st.button("Hitung Volume"):
            V = (n * R * T) / P
            if satuan_v == "m³":
                V /= 1000
            st.success(f"Volume {nama} = {V:.4f} {satuan_v}")

    elif pilihan == "Jumlah Mol":
        nama = st.text_input("Nama Gas", key="nama_mol")
        satuan_p = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], key="satuan_p_mol")
        P = st.number_input(f"Tekanan ({satuan_p})", min_value=0.1, key="P_mol")
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"], key="satuan_v_mol")
        V = st.number_input(f"Volume ({satuan_v})", min_value=0.1, key="V_mol")
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"], key="satuan_t_mol")
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0, key="T_input_mol")
        T = T_input + 273.15 if satuan_t == "°C" else T_input

        # Konversi tekanan ke atm
        if satuan_p == "Pa":
            P /= 101325
        elif satuan_p == "kPa":
            P /= 101.325
        elif satuan_p == "hPa":
            P /= 1013.25
        elif satuan_p == "bar":
            P /= 1.01325
        elif satuan_p == "Torr" or satuan_p == "mmHg":
            P /= 760

        # Konversi volume ke liter (dm³)
        if satuan_v == "m³":
            V *= 1000

        if st.button("Hitung Jumlah Mol"):
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.2f} mol")
