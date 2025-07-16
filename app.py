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
        st.write(f"Telah dikonversi otomatis: {T_input}°C = {T:.2f} K")
    else:
        T = T_input
    return T

# Fungsi konversi tekanan ke atm

def konversi_tekanan_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], key=satuan_key)
    P_input = st.number_input(f"{label} ({satuan})", min_value=0.0, key=input_key)
    if satuan == "Pa":
        P = P_input / 101325
        st.write(f"Telah dikonversi otomatis: {P_input} Pa = {P:.5f} atm")
    elif satuan == "kPa":
        P = P_input / 101.325
        st.write(f"Telah dikonversi otomatis: {P_input} kPa = {P:.5f} atm")
    elif satuan == "hPa":
        P = P_input / 1013.25
        st.write(f"Telah dikonversi otomatis: {P_input} hPa = {P:.5f} atm")
    elif satuan == "bar":
        P = P_input / 1.01325
        st.write(f"Telah dikonversi otomatis: {P_input} bar = {P:.5f} atm")
    elif satuan == "Torr" or satuan == "mmHg":
        P = P_input / 760
        st.write(f"Telah dikonversi otomatis: {P_input} {satuan} = {P:.5f} atm")
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
            V *= 1000  # konversi ke liter (dm³)
        if st.button("Hitung Tekanan"):
            P = (n * R * T) / V  # hasil dalam atm
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
        V = st.number_input(f"Volume ({satuan_v})", min_value=0.0, key="V_mol")
        if satuan_v == "m³":
            V *= 1000
        T = konversi_suhu_input("Suhu", "satuan_t_mol", "T_input_mol")
        if st.button("Hitung Jumlah Mol"):
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.2f} mol")
