import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(
    page_title="ChemGasMaster",
    page_icon="⚗️",
    layout="wide"
)

# Fungsi untuk menerapkan background
def apply_background(menu_type):
    if menu_type == "beranda":
        st.markdown("""
        <style>
        .stApp > div:first-child {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
            overflow: hidden;
        }
        
        .stApp > div:first-child::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 20%, rgba(255,255,255,0.1) 2px, transparent 2px),
                radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 2px, transparent 2px),
                radial-gradient(circle at 40% 60%, rgba(255,255,255,0.1) 1px, transparent 1px);
            animation: float 20s ease-in-out infinite;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
        .content-overlay {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            position: relative;
            z-index: 1;
            backdrop-filter: blur(5px);
        }
        </style>
        """, unsafe_allow_html=True)
    
    elif menu_type == "kalkulator":
        st.markdown("""
        <style>
        .stApp > div:first-child {
            background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
            position: relative;
            overflow: hidden;
        }
        
        .stApp > div:first-child::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                polygon(50% 0%, 0% 100%, 100% 100%),
                polygon(50% 0%, 0% 100%, 100% 100%);
            background-size: 30px 30px, 60px 60px;
            background-position: 0 0, 30px 30px;
            opacity: 0.1;
            animation: slide 15s linear infinite;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes slide {
            0% { transform: translateX(-30px); }
            100% { transform: translateX(30px); }
        }
        
        .content-overlay {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            position: relative;
            z-index: 1;
            backdrop-filter: blur(5px);
        }
        </style>
        """, unsafe_allow_html=True)
    
    elif menu_type == "ensiklopedia":
        st.markdown("""
        <style>
        .stApp > div:first-child {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            position: relative;
            overflow: hidden;
        }
        
        .stApp > div:first-child::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(2px 2px at 20px 30px, #fff, transparent),
                radial-gradient(2px 2px at 40px 70px, #fff, transparent),
                radial-gradient(1px 1px at 90px 40px, #fff, transparent),
                radial-gradient(1px 1px at 130px 80px, #fff, transparent),
                radial-gradient(2px 2px at 160px 30px, #fff, transparent);
            background-repeat: repeat;
            background-size: 200px 100px;
            animation: twinkle 3s ease-in-out infinite alternate;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes twinkle {
            0% { opacity: 0.3; }
            100% { opacity: 0.8; }
        }
        
        .content-overlay {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            position: relative;
            z-index: 1;
            backdrop-filter: blur(5px);
        }
        </style>
        """, unsafe_allow_html=True)
    
    elif menu_type == "keselamatan":
        st.markdown("""
        <style>
        .stApp > div:first-child {
            background: linear-gradient(135deg, #ff6b6b 0%, #ffa500 100%);
            position: relative;
            overflow: hidden;
        }
        
        .stApp > div:first-child::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: repeating-linear-gradient(
                45deg,
                transparent,
                transparent 10px,
                rgba(255,255,255,0.1) 10px,
                rgba(255,255,255,0.1) 20px
            );
            animation: warning 2s linear infinite;
            pointer-events: none;
            z-index: 0;
        }
        
        @keyframes warning {
            0% { transform: translateX(0); }
            100% { transform: translateX(20px); }
        }
        
        .content-overlay {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
            position: relative;
            z-index: 1;
            backdrop-filter: blur(5px);
        }
        </style>
        """, unsafe_allow_html=True)

# Data gas
gas_data = {
    "Hidrogen (H₂)": {
        "rumus": "H₂",
        "massa_molar": 2.016,
        "densitas": 0.08988,
        "titik_didih": -252.9,
        "sifat": "Gas tidak berwarna, tidak berbau, sangat mudah terbakar",
        "kegunaan": "Bahan bakar roket, produksi amonia, hidrogenasi minyak"
    },
    "Oksigen (O₂)": {
        "rumus": "O₂", 
        "massa_molar": 31.998,
        "densitas": 1.429,
        "titik_didih": -183.0,
        "sifat": "Gas tidak berwarna, tidak berbau, mendukung pembakaran",
        "kegunaan": "Respirasi, pembakaran, pengelasan, medis"
    },
    "Nitrogen (N₂)": {
        "rumus": "N₂",
        "massa_molar": 28.014,
        "densitas": 1.2506,
        "titik_didih": -195.8,
        "sifat": "Gas tidak berwarna, tidak berbau, inert",
        "kegunaan": "Atmosfer inert, produksi amonia, pembekuan makanan"
    },
    "Karbon Dioksida (CO₂)": {
        "rumus": "CO₂",
        "massa_molar": 44.01,
        "densitas": 1.977,
        "titik_didih": -78.5,
        "sifat": "Gas tidak berwarna, sedikit asam, larut dalam air",
        "kegunaan": "Minuman berkarbonasi, pemadam kebakaran, es kering"
    },
    "Metana (CH₄)": {
        "rumus": "CH₄",
        "massa_molar": 16.04,
        "densitas": 0.717,
        "titik_didih": -161.5,
        "sifat": "Gas tidak berwarna, tidak berbau, mudah terbakar",
        "kegunaan": "Gas alam, bahan bakar, produksi hidrogen"
    },
    "Amonia (NH₃)": {
        "rumus": "NH₃",
        "massa_molar": 17.031,
        "densitas": 0.7681,
        "titik_didih": -33.3,
        "sifat": "Gas tidak berwarna, bau menyengat, basa kuat",
        "kegunaan": "Pupuk, pembersih, refrigeran, produksi plastik"
    }
}

# Sidebar
st.sidebar.title("🧪 ChemGasMaster")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "Pilih Menu:",
    ["Beranda", "Kalkulator Gas", "Ensiklopedia Gas", "Panduan Keselamatan"]
)

# Menu: Beranda
if menu == "Beranda":
    apply_background("beranda")
    
    st.markdown('<div class="content-overlay">', unsafe_allow_html=True)
    
    st.title("🧪 Selamat Datang di ChemGasMaster")
    
    st.markdown("""
    **ChemGasMaster** adalah aplikasi komprehensif untuk mempelajari dan menghitung properti gas ideal.
    
    ## 🎯 Fitur Utama:
    
    ### 1. 🧮 Kalkulator Gas Ideal
    - Menghitung tekanan, volume, suhu, dan jumlah mol
    - Berdasarkan persamaan gas ideal: PV = nRT
    - Interface yang mudah digunakan
    
    ### 2. 📚 Ensiklopedia Gas  
    - Database lengkap berbagai jenis gas
    - Informasi massa molar, densitas, titik didih
    - Sifat fisik dan kimia gas
    - Kegunaan dalam industri
    
    ### 3. ⚠️ Panduan Keselamatan
    - Prosedur keselamatan laboratorium
    - Penanganan gas berbahaya
    - Tanda bahaya dan simbolnya
    - Tips keselamatan praktis
    
    ## 🚀 Cara Menggunakan:
    1. Pilih menu di sidebar kiri
    2. Ikuti petunjuk pada setiap halaman
    3. Masukkan nilai yang diperlukan
    4. Dapatkan hasil perhitungan atau informasi
    
    ---
    *Dikembangkan untuk membantu pembelajaran kimia gas* ⚗️
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Menu: Kalkulator Gas
elif menu == "Kalkulator Gas":
    apply_background("kalkulator")
    
    st.markdown('<div class="content-overlay">', unsafe_allow_html=True)
    
    st.title("🧮 Kalkulator Gas Ideal")
    
    st.markdown("""
    Gunakan kalkulator ini untuk menghitung properti gas ideal berdasarkan persamaan:
    
    **PV = nRT**
    
    Dimana:
    - P = Tekanan (atm)
    - V = Volume (L) 
    - n = Jumlah mol (mol)
    - R = Konstanta gas ideal (0.0821 L·atm/mol·K)
    - T = Suhu (K)
    """)
    
    st.markdown("---")
    
    # Input parameter
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Parameter yang Diketahui")
        
        # Pilih parameter yang ingin dihitung
        hitung = st.selectbox(
            "Pilih parameter yang ingin dihitung:",
            ["Tekanan (P)", "Volume (V)", "Jumlah Mol (n)", "Suhu (T)"]
        )
        
        if hitung == "Tekanan (P)":
            V = st.number_input("Volume (L):", min_value=0.001, value=1.0, step=0.1)
            n = st.number_input("Jumlah mol (mol):", min_value=0.001, value=1.0, step=0.1)
            T = st.number_input("Suhu (K):", min_value=0.1, value=273.15, step=1.0)
            
        elif hitung == "Volume (V)":
            P = st.number_input("Tekanan (atm):", min_value=0.001, value=1.0, step=0.1)
            n = st.number_input("Jumlah mol (mol):", min_value=0.001, value=1.0, step=0.1)
            T = st.number_input("Suhu (K):", min_value=0.1, value=273.15, step=1.0)
            
        elif hitung == "Jumlah Mol (n)":
            P = st.number_input("Tekanan (atm):", min_value=0.001, value=1.0, step=0.1)
            V = st.number_input("Volume (L):", min_value=0.001, value=1.0, step=0.1)
            T = st.number_input("Suhu (K):", min_value=0.1, value=273.15, step=1.0)
            
        elif hitung == "Suhu (T)":
            P = st.number_input("Tekanan (atm):", min_value=0.001, value=1.0, step=0.1)
            V = st.number_input("Volume (L):", min_value=0.001, value=1.0, step=0.1)
            n = st.number_input("Jumlah mol (mol):", min_value=0.001, value=1.0, step=0.1)
    
    with col2:
        st.subheader("📊 Hasil Perhitungan")
        
        # Konstanta gas ideal
        R = 0.0821  # L·atm/mol·K
        
        if st.button("🔄 Hitung", use_container_width=True):
            try:
                if hitung == "Tekanan (P)":
                    hasil = (n * R * T) / V
                    st.success(f"**Tekanan (P) = {hasil:.4f} atm**")
                    
                elif hitung == "Volume (V)":
                    hasil = (n * R * T) / P
                    st.success(f"**Volume (V) = {hasil:.4f} L**")
                    
                elif hitung == "Jumlah Mol (n)":
                    hasil = (P * V) / (R * T)
                    st.success(f"**Jumlah Mol (n) = {hasil:.4f} mol**")
                    
                elif hitung == "Suhu (T)":
                    hasil = (P * V) / (n * R)
                    st.success(f"**Suhu (T) = {hasil:.4f} K**")
                    st.info(f"Suhu dalam Celsius = {hasil - 273.15:.2f} °C")
                
                # Tampilkan ringkasan
                st.markdown("---")
                st.markdown("### 📋 Ringkasan Perhitungan")
                st.markdown(f"Menggunakan persamaan: **PV = nRT**")
                st.markdown(f"Konstanta R = {R} L·atm/mol·K")
                
            except ZeroDivisionError:
                st.error("❌ Error: Tidak dapat membagi dengan nol!")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Informasi tambahan
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips Penggunaan:
    - Pastikan suhu dalam satuan Kelvin (K)
    - Untuk konversi: K = °C + 273.15
    - Tekanan dalam atmosfer (atm)
    - Volume dalam liter (L)
    - Jumlah mol dalam mol
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Menu: Ensiklopedia Gas
elif menu == "Ensiklopedia Gas":
    apply_background("ensiklopedia")
    
    st.markdown('<div class="content-overlay">', unsafe_allow_html=True)
    
    st.title("📚 Ensiklopedia Gas")
    
    st.markdown("Pilih gas untuk melihat informasi detail tentang properti fisik dan kimia:")
    
    # Pilih gas
    gas_pilihan = st.selectbox("🔍 Pilih Gas:", list(gas_data.keys()))
    
    if gas_pilihan:
        data = gas_data[gas_pilihan]
        
        st.markdown("---")
        st.subheader(f"🧪 {gas_pilihan}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Properti Fisik")
            st.markdown(f"**Rumus Kimia:** {data['rumus']}")
            st.markdown(f"**Massa Molar:** {data['massa_molar']} g/mol")
            st.markdown(f"**Densitas:** {data['densitas']} g/L (STP)")
            st.markdown(f"**Titik Didih:** {data['titik_didih']} °C")
            
        with col2:
            st.markdown("### 🔬 Sifat & Kegunaan")
            st.markdown(f"**Sifat:** {data['sifat']}")
            st.markdown(f"**Kegunaan:** {data['kegunaan']}")
        
        # Tampilkan informasi tambahan
        st.markdown("---")
        st.markdown("### 📈 Informasi Tambahan")
        
        # Hitung jumlah molekul dalam 1 mol
        avogadro = 6.022e23
        st.info(f"Dalam 1 mol {gas_pilihan} terdapat {avogadro:.2e} molekul")
        
        # Hitung volume molar pada STP
        volume_molar_stp = 22.4  # L/mol pada STP
        st.info(f"Volume molar pada STP: {volume_molar_stp} L/mol")
        
        # Hitung densitas relatif terhadap udara
        massa_molar_udara = 28.97  # g/mol
        densitas_relatif = data['massa_molar'] / massa_molar_udara
        
        if densitas_relatif > 1:
            keterangan = "lebih berat dari udara"
        else:
            keterangan = "lebih ringan dari udara"
            
        st.info(f"Densitas relatif terhadap udara: {densitas_relatif:.2f} ({keterangan})")
    
    # Tabel perbandingan semua gas
    st.markdown("---")
    st.subheader("📋 Tabel Perbandingan Gas")
    
    import pandas as pd
    
    # Buat dataframe dari data gas
    df_data = []
    for nama, info in gas_data.items():
        df_data.append({
            'Gas': nama,
            'Rumus': info['rumus'],
            'Massa Molar (g/mol)': info['massa_molar'],
            'Densitas (g/L)': info['densitas'],
            'Titik Didih (°C)': info['titik_didih']
        })
    
    df = pd.DataFrame(df_data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Menu: Panduan Keselamatan
elif menu == "Panduan Keselamatan":
    apply_background("keselamatan")
    
    st.markdown('<div class="content-overlay">', unsafe_allow_html=True)
    
    st.title("⚠️ Panduan Keselamatan Laboratorium")
    
    st.markdown("""
    Keselamatan adalah prioritas utama dalam bekerja dengan gas di laboratorium.
    Berikut adalah panduan penting yang harus diikuti:
    """)
    
    # Tab untuk berbagai kategori keselamatan
    tab1, tab2, tab3, tab4 = st.tabs(["🏥 Umum", "⚠️ Gas Berbahaya", "🛡️ APD", "🚨 Darurat"])
    
    with tab1:
        st.subheader("🏥 Keselamatan Umum")
        st.markdown("""
        ### ✅ Yang Harus Dilakukan:
        - Selalu baca MSDS (Material Safety Data Sheet) sebelum menggunakan gas
        - Pastikan ventilasi laboratorium berfungsi dengan baik
        - Gunakan alat pelindung diri (APD) yang sesuai
        - Periksa kondisi tabung gas sebelum digunakan
        - Simpan tabung gas dalam posisi tegak dan terikat dengan aman
        - Tutup katup tabung setelah selesai digunakan
        
        ### ❌ Yang Tidak Boleh Dilakukan:
        - Jangan merokok atau menyalakan api di dekat gas mudah terbakar
        - Jangan menggunakan gas tanpa pengawasan
        - Jangan menyimpan tabung gas di tempat yang panas
        - Jangan memaksa membuka katup yang macet
        - Jangan mencampur gas tanpa pengetahuan yang cukup
        """)
        
    with tab2:
        st.subheader("⚠️ Penanganan Gas Berbahaya")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🔥 Gas Mudah Terbakar
            **Contoh:** H₂, CH₄, C₂H₄
            
            **Bahaya:**
            - Dapat meledak jika tercampur udara
            - Mudah terbakar dengan sumber panas
            
            **Pencegahan:**
            - Jauhkan dari sumber api
            - Gunakan dalam ruang berventilasi
            - Pasang detektor gas
            """)
            
        with col2:
            st.markdown("""
            ### ☠️ Gas Beracun
            **Contoh:** CO, H₂S, NO₂
            
            **Bahaya:**
            - Dapat menyebabkan keracunan
            - Efek akut dan kronis pada kesehatan
            
            **Pencegahan:**
            - Gunakan dalam lemari asam
            - Pantau konsentrasi di udara
            - Gunakan respirator jika perlu
            """)
        
        st.markdown("""
        ### 🧊 Gas Kriogenik
        **Contoh:** N₂ cair, O₂ cair
        
        **Bahaya:**
        - Dapat menyebabkan luka bakar dingin
        - Dapat menyebabkan kekurangan oksigen
        
        **Pencegahan:**
        - Gunakan sarung tangan kriogenik
        - Hindari kontak langsung dengan kulit
        - Pastikan sirkulasi udara yang baik
        """)
        
    with tab3:
        st.subheader("🛡️ Alat Pelindung Diri (APD)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 👓 Pelindung Mata
            - **Safety goggles** untuk gas berbahaya
            - **Face shield** untuk gas korosif
            - Pastikan fit dengan wajah
            """)
            
        with col2:
            st.markdown("""
            ### 🧤 Pelindung Tangan
            - **Sarung tangan nitrile** untuk gas umum
            - **Sarung tangan kriogenik** untuk gas dingin
            - **Sarung tangan tahan kimia** untuk gas korosif
            """)
            
        with col3:
            st.markdown("""
            ### 👕 Pelindung Tubuh
            - **Jas laboratorium** tahan api
            - **Sepatu safety** tertutup
            - **Respirator** jika diperlukan
            """)
        
    with tab4:
        st.subheader("🚨 Prosedur Darurat")
        
        st.markdown("""
        ### 🔥 Kebocoran Gas Mudah Terbakar
        1. **JANGAN** menyalakan saklar listrik
        2. Matikan sumber gas jika aman
        3. Buka jendela untuk ventilasi
        4. Evakuasi area jika perlu
        5. Hubungi petugas keselamatan
        
        ### ☠️ Kebocoran Gas Beracun
        1. **Segera** tinggalkan area
        2. Bernapas dengan mulut tertutup
        3. Cari udara segar
        4. Hubungi bantuan medis jika ada gejala
        5. Laporkan ke petugas keselamatan
        
        ### 🧊 Kontak dengan Gas Kriogenik
        1. **Jangan** gosok area yang terkena
        2. Siram dengan air hangat (bukan panas)
        3. Lepaskan pakaian yang terkena
        4. Cari bantuan medis segera
        5. Jangan pecahkan gelembung jika ada
        
        ### 📞 Nomor Penting
        - **Pemadam Kebakaran:** 113
        - **Ambulans:** 118/119
        - **Polisi:** 110
        - **Keselamatan Lab:** (sesuai institusi)
        """)
        
    st.markdown("---")
    st.warning("""
    ⚠️ **INGAT:** Keselamatan adalah tanggung jawab bersama. 
    Jika ragu tentang prosedur keselamatan, tanyakan kepada supervisor atau petugas keselamatan.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Bantuan")
st.sidebar.info("Jika mengalami kesulitan, hubungi administrator lab.")

st.sidebar.markdown("---")
st.sidebar.markdown("*© 2024 ChemGasMaster - Aplikasi Pembelajaran Kimia Gas*")
