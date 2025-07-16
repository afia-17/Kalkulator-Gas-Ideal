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
        nama = st.text_input("Nama Gas")
        n = st.number_input("Jumlah Mol (n)", min_value=0.0)
        mr = st.number_input("Massa Molar (g/mol)", min_value=0.0)
        if st.button("Hitung Massa"):
            massa = n * mr
            st.success(f"Massa {nama} = {massa:.2f} gram")

    elif pilihan == "Tekanan":
        nama = st.text_input("Nama Gas")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0)
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"])
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0)
        if satuan_t == "°C":
            st.write(f"Telah dikonversi otomatis: {T_input}°C = {T_input + 273.15:.2f} K")
            T = T_input + 273.15
else:
    T = T_input

    # Perbaiki indentasi blok di bawah ini
    V = st.number_input("Volume", min_value=0.1)
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"])
        if satuan_v == "m³":
            V *= 1000  # konversi ke liter (dm³)
        satuan_p = st.selectbox("Satuan Tekanan Output", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"])
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
            P = (n * R * T) / V
            st.success(f"Tekanan {nama} = {P:.2f} atm")

    elif pilihan == "Volume":
        nama = st.text_input("Nama Gas")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0)
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"])
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0)
        T = T_input + 273.15 if satuan_t == "°C" else T_input
        P = st.number_input("Tekanan (atm)", min_value=0.1)
        if st.button("Hitung Volume"):
            V = (n * R * T) / P
            st.success(f"Volume {nama} = {V:.2f} L (dm³)")
            V = (n * R * T) / P
            if satuan_v == "m³":
                V /= 1000
            st.success(f"Volume {nama} = {V:.4f} {satuan_v}")
            V = (n * R * T) / P
            st.success(f"Volume {nama} = {V:.2f} L")

    elif pilihan == "Jumlah Mol":
        nama = st.text_input("Nama Gas")
        satuan_p = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"])
        P = st.number_input(f"Tekanan ({satuan_p})", min_value=0.1)
        satuan_v = st.selectbox("Satuan Volume", ["L", "m³"])
        V = st.number_input(f"Volume ({satuan_v})", min_value=0.1)
        satuan_t = st.selectbox("Satuan Suhu", ["K", "°C"])
        T_input = st.number_input(f"Suhu ({satuan_t})", min_value=-273.0)
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
        elif satuan_p == "L.atm":
            P = P  # sudah dalam atm

        # Konversi volume ke liter (dm³)
        if satuan_v == "m³":
            V *= 1000

        if st.button("Hitung Jumlah Mol"):
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.2f} mol")
            n = (P * V) / (R * T)
            st.success(f"Jumlah mol {nama} = {n:.2f} mol")

# Halaman Library
elif menu == "📚 Library":
    st.header("📚 Library: Gas Ideal")
    st.markdown("""
Gas ideal adalah model teoretis yang menggambarkan perilaku gas yang tidak memiliki volume partikel dan tidak mengalami gaya antar molekul. Model ini mengikuti hukum Boyle, Charles, dan Avogadro, serta dinyatakan dalam persamaan **PV = nRT**. Meskipun ideal, banyak gas nyata berperilaku mendekati gas ideal dalam suhu tinggi dan tekanan rendah.

Berikut adalah informasi lengkap tentang berbagai jenis gas ideal, termasuk rumus molekul, sifat fisika dan kimia, penggunaan industri (PBK), serta aspek K3L.
""")

    daftar_gas = {
        "Hidrogen (H₂)": {
            "🔬 Rumus Molekul": "H₂ adalah molekul diatomik yang sangat ringan dan terdiri dari dua atom hidrogen dengan ikatan kovalen tunggal. Molekul ini paling sederhana dan paling banyak di alam semesta.",
            "🌡️ Sifat Fisika": "Gas ini tidak berwarna, tidak berbau, memiliki densitas sangat rendah dan titik didih -252,9°C. Sangat mudah terbakar dan digunakan dalam balon serta roket.",
            "⚗️ Sifat Kimia": "Hidrogen mudah bereaksi membentuk senyawa, sangat reaktif, dan dapat menjadi agen reduktor. Reaksi dengan oksigen menghasilkan air.",
            "🏭 Pengetahuan dan Penanganan Bahan Kimia (PBK)": "Digunakan untuk hidrogenasi minyak, pembuatan amonia, dan sel bahan bakar. Juga dipakai dalam proses metalurgi dan industri petrokimia.",
            "🛡️ Keselamatan, Kesehatan Kerja dan Lingkungan (K3L)": "Bersifat sangat mudah meledak jika bercampur udara. Penyimpanan harus pada tangki khusus dan jauh dari sumber panas."
        },
        "Oksigen (O₂)": {
            "🔬 Rumus Molekul": "O₂ adalah molekul diatomik dengan dua atom oksigen yang sangat penting untuk respirasi dan pembakaran. Berperan penting dalam kehidupan dan industri.",
            "🌡️ Sifat Fisika": "Tidak berwarna dan tidak berbau, dengan titik didih -183°C. Dalam bentuk cair berwarna biru pucat dan memiliki sifat paramagnetik.",
            "⚗️ Sifat Kimia": "Zat pengoksidasi kuat yang bereaksi dengan hampir semua unsur. Membentuk senyawa oksida seperti CO₂ dan H₂O.",
            "🏭 Pengetahuan dan Penanganan Bahan Kimia (PBK)": "Digunakan dalam respirasi medis, pengelasan logam, pembangkit energi, dan pemurnian logam. Juga berperan dalam bioteknologi.",
            "🛡️ Keselamatan, Kesehatan Kerja dan Lingkungan (K3L)": "Meningkatkan risiko kebakaran. Harus disimpan dalam silinder bertekanan dan jauh dari bahan mudah terbakar."
        },
        "Nitrogen (N₂)": {
            "🔬 Rumus Molekul": "N₂ adalah molekul diatomik yang stabil dengan ikatan rangkap tiga antara dua atom nitrogen. Menyusun 78% atmosfer bumi.",
            "🌡️ Sifat Fisika": "Tidak berwarna dan tidak berbau, dengan titik didih -195,8°C. Tidak mendukung pembakaran dan bersifat inert.",
            "⚗️ Sifat Kimia": "Kurang reaktif pada suhu kamar, tapi membentuk amonia, asam nitrat, dan senyawa organik dalam kondisi tertentu.",
            "🏭 Pengetahuan Bahan Kimia (PBK)": "Digunakan sebagai atmosfer inert untuk mencegah oksidasi. Penting dalam industri makanan, farmasi, dan elektronik.",
            "🛡️ Kesehatan dan Keselamatan Kerja Lingkungan (K3L)": "Gas inert yang bisa menyebabkan asfiksia. Harus digunakan di ruang berventilasi baik dan disimpan dengan aman."
        },
        "Karbondioksida (CO₂)": {
            "🔬 Rumus Molekul": "CO₂ terdiri dari satu atom karbon dan dua atom oksigen yang terikat linier. Dihasilkan dari respirasi dan pembakaran.",
            "🌡️ Sifat Fisika": "Tidak berwarna dan tidak berbau. Dapat berbentuk padat (dry ice) pada -78,5°C dan lebih berat dari udara.",
            "⚗️ Sifat Kimia": "Bersifat asam dan larut dalam air membentuk asam karbonat. Tidak mendukung pembakaran dan bisa menggantikan oksigen.",
            "🏭 Pengetahuan Bahan Kimia (PBK)": "Digunakan dalam minuman bersoda, pemadam kebakaran, inkubasi kultur sel, dan industri makanan.",
            "🛡️ Kesehatan dan Keselamatan Kerja Lingkungan (K3L)": "Dapat menyebabkan sesak napas di ruang tertutup. Harus ditangani dengan ventilasi baik dan APD bila perlu."
        },
        "Metana (CH₄)": {
            "🔬 Rumus Molekul": "CH₄ adalah molekul satu atom karbon dan empat atom hidrogen. Merupakan hidrokarbon sederhana dan komponen utama gas alam.",
            "🌡️ Sifat Fisika": "Gas tak berwarna dan tak berbau (diberi odorant). Titik didih -161,5°C. Lebih ringan dari udara dan mudah terbakar.",
            "⚗️ Sifat Kimia": "Sangat mudah terbakar, menghasilkan CO₂ dan H₂O saat terbakar. Tidak reaktif pada suhu kamar, tapi reaktif dalam pembakaran.",
            "🏭 Pengetahuan Bahan Kimia (PBK)": "Digunakan sebagai bahan bakar, bahan baku industri kimia (metanol, amonia), dan sumber energi domestik dan industri.",
            "🛡️ Kesehatan dan Keselamatan Kerja Lingkungan (K3L)": "Dapat menyebabkan ledakan bila terakumulasi. Harus disimpan dan digunakan dengan deteksi kebocoran dan ventilasi cukup."
        },
        "Helium (He)": {
            "🔬 Rumus Molekul": "He adalah gas monoatomik dengan satu atom helium. Bersifat inert dan termasuk gas mulia.",
            "🌡️ Sifat Fisika": "Gas tak berwarna, tak berbau, dan sangat ringan. Titik didih -268,9°C. Tidak terbakar dan tidak reaktif.",
            "⚗️ Sifat Kimia": "Tidak bereaksi dengan unsur lain. Tidak membentuk senyawa secara normal dan sangat stabil.",
            "🏭 Pengetahuan Bahan Kimia (PBK)": "Digunakan dalam balon, pendinginan MRI, deteksi kebocoran, dan atmosfer inert dalam reaksi sensitif.",
            "🛡️ Kesehatan dan Keselamatan Kerja Lingkungan (K3L)": "Tidak beracun tapi dapat menggantikan oksigen. Harus digunakan dalam ruang berventilasi dan dihindari untuk dihirup langsung."
        },
        "Neon (Ne)": {
            "🔬 Rumus Molekul": "Ne adalah gas mulia monoatomik yang sangat stabil. Bersifat non-reaktif dan ditemukan dalam jumlah kecil di atmosfer.",
            "🌡️ Sifat Fisika": "Tidak berwarna dan tidak berbau. Titik didih -246°C. Digunakan untuk lampu dan aplikasi kriogenik.",
            "⚗️ Sifat Kimia": "Sangat inert dan tidak bereaksi dengan unsur lain. Tidak membentuk senyawa dalam kondisi normal.",
            "🏭 Pengetahuan Bahan Kimia (PBK)": "Dipakai dalam lampu neon, indikator listrik, serta aplikasi vakum dan laser.",
            "🛡️ Kesehatan dan Keselamatan Kerja Lingkungan (K3L)": "Tidak berbahaya, namun dapat menggantikan oksigen. Gunakan di ruang dengan ventilasi yang memadai."
        }
    }

    pilih = st.selectbox("Pilih Gas Ideal", ["-- Pilih --"] + list(daftar_gas.keys()))
    if pilih != "-- Pilih --":
        st.subheader(f"🔬 {pilih}")
        warna_kategori = {
            "🔬 Rumus Molekul": "#FFEB3B",
            "🌡️ Sifat Fisika": "#B3E5FC",
            "⚗️ Sifat Kimia": "#FF8A80",
            "🏭 Pengetahuan dan Penanganan Bahan Kimia (PBK)": "#E1BEE7",
            "🛡️ Keselamatan, Kesehatan Kerja dan Lingkungan (K3L)": "#C8E6C9"
        }

        for k, v in daftar_gas[pilih].items():
            warna = warna_kategori.get(k, "#f5faff")
            st.markdown(f"""
            <div style='border: 2px solid {warna}; padding: 15px; border-radius: 10px; background-color: #ffffff; margin-bottom: 10px;'>
                <h5 style='color: {warna}; margin-bottom: 5px;'>{k}</h5>
                <p style='margin: 0;'>{v}</p>
            </div>
            """, unsafe_allow_html=True)

# File requirements.txt (letakkan di root folder proyek)
# ---
# streamlit==1.35.0
