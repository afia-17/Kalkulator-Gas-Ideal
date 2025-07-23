# ===========================================
# APLIKASI KALKULATOR GAS IDEAL + ENSIKLOPEDIA + PANDUAN KESELAMATAN
# ===========================================
import streamlit as st
import base64

# Konfigurasi Halaman
st.set_page_config(
    page_title="ChemGasMaster",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================
# CSS CUSTOM & BACKGROUNDS
# ===========================================
<style>
    /* Base Styles */
    .main {
        background-color: #f5f7fa;
        color: #333333;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
    }
    
    p, li, td {
        color: #34495e;
    }
    
    /* Card Styles */
    .card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        background: white;
        border: 1px solid #e0e0e0;
    }
    
    .calc-card {
        border-left: 5px solid #3498db;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9f5ff 100%);
    }
    
    .result-card {
        border-left: 5px solid #2ecc71;
        background: linear-gradient(135deg, #f0fff4 0%, #e6ffed 100%);
    }
    
    .gas-card {
        border-left: 5px solid #f39c12;
        background: linear-gradient(135deg, #fff8f0 0%, #ffeedd 100%);
    }
    
    .safety-card {
        border-left: 5px solid #e74c3c;
        background: linear-gradient(135deg, #fff0f0 0%, #ffe6e6 100%);
    }
    
    /* Input Styles */
    .input-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 15px;
    }
    
    .input-label {
        min-width: 120px;
        color: #2980b9;
        font-weight: bold;
    }
    
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        background-color: white !important;
        color: #333333 !important;
        border: 1px solid #ced4da !important;
    }
    
    /* Button Styles */
    .stButton>button {
        background-color: #2980b9;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #3498db;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
    }
    
    /* Table Styles */
    .property-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .property-table th {
        background-color: #2980b9;
        color: white;
        padding: 12px;
        text-align: left;
    }
    
    .property-table td {
        padding: 12px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    /* Tab Styles */
    .stTabs [aria-selected="true"] {
        background-color: #e9f5ff !important;
        color: #2980b9 !important;
        font-weight: bold;
        border-bottom: 2px solid #2980b9;
    }
    
    /* Background Overrides */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
        background-attachment: fixed;
    }
    
    /* Animation Styles */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# DATABASE GAS
# ===========================================
GAS_DATABASE = {
    "Hidrogen (H₂)": {
        "icon": "🚀",
        "category": "Gas Diatomik",
        "description": "Unsur paling ringan di alam semesta dengan sifat unik sebagai bahan bakar masa depan.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/H2.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "H₂",
                "Massa Molar": "2.016 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan tunggal"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-259.16 °C (13.99 K)",
                "Titik Didih": "-252.87 °C (20.28 K)",
                "Densitas (STP)": "0.08988 g/L",
                "Kalor Jenis": "14.304 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (4-75% di udara)",
                "Penanganan": "Gunakan di area berventilasi, hindari percikan api"
            }
        },
        "aplikasi": "Bahan bakar roket, produksi amonia, hidrogenasi minyak"
    },
    "Oksigen (O₂)": {
        "icon": "💨",
        "category": "Gas Diatomik",
        "description": "Gas vital untuk kehidupan dan pembakaran, menyusun 21% atmosfer Bumi.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/O2_-.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "O₂",
                "Massa Molar": "32.00 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Diatomik, ikatan rangkap"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-218.79 °C (54.36 K)",
                "Titik Didih": "-182.96 °C (90.19 K)",
                "Densitas (STP)": "1.429 g/L",
                "Kalor Jenis": "0.918 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Meningkatkan risiko kebakaran",
                "Penanganan": "Hindari kontak dengan bahan organik"
            }
        },
        "aplikasi": "Penggunaan medis, industri baja, pengolahan air"
    },
    "Nitrogen (N₂)": {
        "icon": "🌬️",
        "category": "Gas Diatomik",
        "description": "Gas inert yang menyusun 78% atmosfer Bumi, penting untuk berbagai aplikasi industri.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/N2.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "N₂",
                "Massa Molar": "28.014 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan rangkap tiga"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-210.00 °C (63.15 K)",
                "Titik Didih": "-195.79 °C (77.36 K)",
                "Densitas (STP)": "1.2506 g/L",
                "Kalor Jenis": "1.040 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Dapat menyebabkan asfiksia",
                "Penanganan": "Gunakan di area berventilasi baik"
            }
        },
        "aplikasi": "Pembuatan amonia, pendingin, atmosfer inert"
    },
    "Karbon Dioksida (CO₂)": {
        "icon": "🌫️",
        "category": "Gas Poliatomik",
        "description": "Gas rumah kaca yang penting untuk fotosintesis tanaman.",
        "image": "https://www.chemtube3d.com/images/gallery/JPGfiles%20structures/I606ST04.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CO₂",
                "Massa Molar": "44.01 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Linear, ikatan rangkap"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-78.5 °C (194.65 K)",
                "Titik Didih": "-56.6 °C (216.55 K)",
                "Densitas (STP)": "1.977 g/L",
                "Kalor Jenis": "0.839 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Dapat menyebabkan sesak napas",
                "Penanganan": "Hindari area tertutup tanpa ventilasi"
            }
        },
        "aplikasi": "Minuman berkarbonasi, pemadam kebakaran"
    },
    "Neon (Ne)": {
        "icon": "💡",
        "category": "Gas Monoatomik",
        "description": "Gas tidak berwarna, dapat memancarkan warna oranye kemerahan jika berada pada medan listrik bertegangan tinggi.",
        "image": "https://png.pngtree.com/thumb_back/fh260/background/20220426/pngtree-mendeleevs-periodic-table-luminescent-noble-gases-chemical-symbol-chemical-science-photo-image_30134580.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ne",
                "Massa Molar": "20.18 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-248.59 °C (24.56 K)",
                "Titik Didih": "-246.046 °C (27.104 K)",
                "Densitas (STP)": "0.89 g/L",
                "Kalor Jenis": "0.904 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Tekanan tinggi, asfiksia dalam ruang tertutup",
                "Penanganan": "Gunakan ventilasi baik dan simpan dalam tabung bertekanan sesuai standar"
            }
        },
        "aplikasi": "Lampu neon, pendingin kriogenik, alat elektronik"
    },
    "Helium (He)": {
        "icon": "🎈",
        "category": "Gas Monoatomik",
        "description": "Gas tidak berwarna dan tidak berbau, sangat ringan. Tidak mudah terbakar dan digunakan secara luas dalam balon.",
        "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/186450350-56a132cb5f9b58b7d0bcf751.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "He",
                "Massa Molar": "4.00 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-272.2 °C (0.95 K)",
                "Titik Didih": "-268.93 °C (4.22 K)",
                "Densitas (STP)": "0.18 g/L",
                "Kalor Jenis": "5.19 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia jika menggantikan oksigen",
                "Penanganan": "Gunakan dalam ruang berventilasi"
            }
        },
        "aplikasi": "Balon, pendingin MRI, pengelasan, pengujian kebocoran"
    },
    "Argon (Ar)": {
        "icon": "🛡️",
        "category": "Gas Monoatomik",
        "description": "Gas inert, tidak reaktif secara kimia. Digunakan dalam pengelasan, bola lampu pijar, dan sebagai atmosfer pelindung.",
        "image": "https://www.vallalandco.com/Air-Products-Theni/1723628095.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ar",
                "Massa Molar": "39.95 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-189.35 °C (83.8 K)",
                "Titik Didih": "-185.85 °C (87.3 K)",
                "Densitas (STP)": "1.78 g/L",
                "Kalor Jenis": "0.52 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Tidak beracun namun dapat menyebabkan asfiksia",
                "Penanganan": "Ventilasi baik saat digunakan dalam ruang tertutup"
            }
        },
        "aplikasi": "Pengelasan, bola lampu, atmosfer inert industri"
    },
}

# ===========================================
# MENU SIDEBAR
# ===========================================
with st.sidebar:
    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #0a192f;
            border-right: 1px solid #1e2a3a;
        }
        
        .stRadio>div>label>div {
            padding: 10px;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        
        .stRadio>div>label>div:hover {
            background-color: #112240;
        }
        
        [data-testid="stSidebarNav"] {
            color: #64ffda;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("ChemGasMaster")
    st.markdown("---")
    menu = st.radio(
        "MENU UTAMA",
        ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    <div class="card gas-card">
        <small>ℹ️ Menggunakan persamaan gas ideal: PV=nRT (R=0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>ChemGasMaster</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card calc-card">
        <h3>Selamat Datang di Aplikasi ChemGasMaster!</h3>
        <p>Platform lengkap untuk analisis gas ideal dan informasi kimia.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan penjelasan
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown("""
        <div style="margin-top:20px;">
            <h4>Persamaan Gas Ideal:</h4>
            <p><b>P</b> = Tekanan (atm)</p>
            <p><b>V</b> = Volume (L)</p>
            <p><b>n</b> = Jumlah mol (mol)</p>
            <p><b>R</b> = Konstanta gas = 0.0821 L·atm/mol·K</p>
            <p><b>T</b> = Suhu (K)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div style="margin-top:20px;">
            <h4>Fakta Menarik:</h4>
            <p>🎈 <b>Helium</b> - Gas paling ringan kedua setelah hidrogen</p>
            <p>🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi</p>
            <p>🧪 <b>1 mol gas</b> = 6.022×10²³ molekul</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualisasi variabel
    st.markdown("<h4 style='margin-top:30px;'>Variabel Utama:</h4>", unsafe_allow_html=True)
    var_cols = st.columns(4)
    variables = [
        ("P", "Tekanan", "Mengukur gaya gas<br>pada wadah", "#ffcdd2"),
        ("V", "Volume", "Ruang yang<br>ditempati gas", "#c8e6c9"),
        ("n", "Jumlah Mol", "Banyaknya<br>partikel gas", "#bbdefb"),
        ("T", "Suhu", "Ukuran energi<br>kinetik partikel", "#fff9c4")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background:{color};padding:15px;border-radius:10px;height:150px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
                <h3 style="margin:5px 0;color:#0a192f;">{var}</h3>
                <p style="margin:5px 0;font-weight:bold;color:#0a192f;">{name}</p>
                <p style="margin:5px 0;font-size:0.8em;color:#0a192f;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contoh aplikasi
    st.markdown("""
    <div class="card" style="margin-top:30px;">
        <h4>💡 Contoh Aplikasi Persamaan Gas Ideal:</h4>
        <ul>
            <li>Menghitung volume gas yang dihasilkan dalam reaksi kimia</li>
            <li>Memahami perilaku gas dalam sistem tertutup</li>
            <li>Memprediksi pengaruh perubahan suhu terhadap tekanan gas</li>
            <li>Mendesain sistem pneumatik dan hidrolik</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips Penggunaan
    st.markdown("""
    <div class="card gas-card" style="margin-top:20px;">
        <h4>🔧 Tips Menggunakan Aplikasi:</h4>
        <ol>
            <li>Pilih menu <b>Kalkulator Gas</b> untuk perhitungan</li>
            <li>Gunakan <b>Ensiklopedia Gas</b> untuk informasi detail</li>
            <li>Pelajari <b>Panduan Keselamatan</b> sebelum bekerja dengan gas</li>
            <li>Pastikan satuan yang digunakan konsisten</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    st.markdown("""
    <style>
        .calc-header {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
    </style>
    
    <div class="calc-header">
        <h1 style="color: white; text-align: center; margin: 0;">
            🧮 Kalkulator Gas Ideal
        </h1>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "⚖️ Hitung Massa", 
        "🎚️ Hitung Tekanan",
        "🫙 Hitung Volume",
        "🧪 Hitung Mol"
    ])
    
    R = 0.0821  # Konstanta gas ideal

    with tab1:
        with st.container():
            st.markdown("""
            <div style="border-left: 5px solid #FF9800; padding-left: 15px; margin-bottom: 20px;">
                <h2>🧪 Kalkulator Massa Gas</h2>
                <p style="color: #a8b2d1;"><b>Rumus:</b> Massa = n (mol) × Mr (g/mol)</p>
            </div>
            """, unsafe_allow_html=True)

            cols = st.columns(3)
            with cols[0]:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Contoh: Oksigen", label_visibility="collapsed")
            with cols[1]:
                st.markdown('<div class="input-label">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f", label_visibility="collapsed")
            with cols[2]:
                st.markdown('<div class="input-label">Massa Molar (Mr)</div>', unsafe_allow_html=True)
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f", label_visibility="collapsed")
            
            if st.button("⚖️ Hitung Massa", key="btn_massa", use_container_width=True):
                massa = n * mr 
                
                st.markdown(f"""
                <div style="background: rgba(255, 152, 0, 0.1);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #FF9800;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #FF9800;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Massa <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #FF9800; font-weight: bold; font-size: 1.5em; margin: 0;">{massa:.4f} gram</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        with st.container():
            st.markdown("""
            <div style="border-left: 5px solid #F44336; padding-left: 15px; margin-bottom: 20px;">
                <h2>🎚️ Kalkulator Tekanan Gas</h2>
                <p style="color: #a8b2d1;"><b>Rumus:</b> P = [n (mol) × R × T (K)] / V (L)</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="input-label">Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="tekanan_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="tekanan_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div style="background: rgba(244, 67, 54, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Volume</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    V_input = st.number_input("Volume", min_value=0.0, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div style="background: rgba(244, 67, 54, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: rgba(244, 67, 54, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
            
            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: rgba(244, 67, 54, 0.1);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #F44336;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #F44336;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #F44336; font-weight: bold; font-size: 1.5em; margin: 0;">{P:.2f} atm</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        with st.container():
            st.markdown("""
            <div style="border-left: 5px solid #4CAF50; padding-left: 15px; margin-bottom: 20px;">
                <h2>🫙 Kalkulator Volume Gas</h2>
                <p style="color: #a8b2d1;"><b>Rumus:</b> V = [n (mol) × R × T (K)] / P (atm)</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_volume", placeholder="Contoh: Hidrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="input-label">Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="volume_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="volume_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div style="background: rgba(76, 175, 80, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Tekanan</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    P_input = st.number_input("Tekanan", min_value=0.0, key="volume_tekanan_input", label_visibility="collapsed")
                with col2d:
                    satuan_tekanan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key="volume_tekanan_unit", label_visibility="collapsed")
                
                if satuan_tekanan == "Pa":
                    P = P_input / 101325
                elif satuan_tekanan == "kPa":
                    P = P_input / 101.325
                elif satuan_tekanan == "hPa":
                    P = P_input / 1013.25
                elif satuan_tekanan == "bar":
                    P = P_input / 1.01325
                elif satuan_tekanan in ["Torr", "mmHg"]:
                    P = P_input / 760
                else:
                    P = P_input
                
                if satuan_tekanan != "atm":
                    st.markdown(f"""
                    <div style="background: rgba(76, 175, 80, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: rgba(76, 175, 80, 0.1);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #4CAF50;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #4CAF50;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Volume <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #4CAF50; font-weight: bold; font-size: 1.5em; margin: 0;">{V:.2f} L</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab4:
        with st.container():
            st.markdown("""
            <div style="border-left: 5px solid #9C27B0; padding-left: 15px; margin-bottom: 20px;">
                <h2>🧪 Kalkulator Jumlah Mol</h2>
                <p style="color: #a8b2d1;"><b>Rumus:</b> n = [P (atm) × V (L)] / (R × T (K))</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_mol", placeholder="Contoh: Karbon Dioksida", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Tekanan</div>', unsafe_allow_html=True)
                col1a, col1b = st.columns([3,1])
                with col1a:
                    P_input = st.number_input("Tekanan", min_value=0.0, key="mol_tekanan_input", label_visibility="collapsed")
                with col1b:
                    satuan_tekanan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key="mol_tekanan_unit", label_visibility="collapsed")
                
                if satuan_tekanan == "Pa":
                    P = P_input / 101325
                elif satuan_tekanan == "kPa":
                    P = P_input / 101.325
                elif satuan_tekanan == "hPa":
                    P = P_input / 1013.25
                elif satuan_tekanan == "bar":
                    P = P_input / 1.01325
                elif satuan_tekanan in ["Torr", "mmHg"]:
                    P = P_input / 760
                else:
                    P = P_input
                
                if satuan_tekanan != "atm":
                    st.markdown(f"""
                    <div style="background: rgba(156, 39, 176, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="input-label">Volume</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    V_input = st.number_input("Volume", min_value=0.0, key="mol_vol_input", label_visibility="collapsed")
                with col2b:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="mol_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div style="background: rgba(156, 39, 176, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: rgba(156, 39, 176, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Suhu</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="mol_suhu_input", label_visibility="collapsed")
                with col2d:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="mol_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div style="background: rgba(156, 39, 176, 0.1); padding: 8px; border-radius: 5px; margin: 5px 0;">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
            
            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: rgba(156, 39, 176, 0.1);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #9C27B0;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #9C27B0;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Jumlah mol <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #9C27B0; font-weight: bold; font-size: 1.5em; margin: 0;">{n:.2f} mol</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Catatan edukasi
    st.markdown("""
    <div style="background: rgba(100, 255, 218, 0.1);
                padding: 20px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 5px solid #64ffda;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 30px;">💡</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #64ffda;">Tips Ahli Kimia</h3>
                <p style="margin: 0;">
                    Untuk hasil terbaik, pastikan semua satuan konsisten dengan konstanta gas R 
                    (0.0821 L·atm/mol·K). Gunakan suhu dalam Kelvin dan tekanan dalam atm.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.markdown("""
    <style>
        .encyclo-header {
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
    </style>
    
    <div class="encyclo-header">
        <h1 style="color: white; text-align: center; margin: 0;">
            📚 Ensiklopedia Gas
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <h2>{gas['icon']} {selected_gas}</h2>
        <p><i>{gas['description']}</i></p>
        <p><b>Kategori:</b> {gas['category']}</p>
        <p><b>Aplikasi:</b> {gas['aplikasi']}</p>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["image"], width=200)
    
    # Tab Informasi
    tabs = st.tabs(list(gas["properties"].keys()))
    
    for tab, (category, props) in zip(tabs, gas["properties"].items()):
        with tab:
            st.markdown(f"""
            <table class="property-table">
                {"".join(f"<tr><td><b>{key}</b></td><td>{value}</td></tr>" for key, value in props.items())}
            </table>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("""
    <style>
        .safety-header {
            background: linear-gradient(135deg, #200122, #2a0845, #4b1248);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }
    </style>
    
    <div class="safety-header">
        <h1 style="color: white; text-align: center; margin: 0;">
            ⚠️ Panduan Keselamatan Gas
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🚧 Simbol Bahaya Umum</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:200px;background:rgba(244, 67, 54, 0.1);padding:15px;border-radius:10px;border-left:3px solid #f44336;">
                <h4>🔥 Mudah Terbakar</h4>
                <p>Contoh: Hidrogen, Metana</p>
                <p>• Jauhkan dari sumber api</p>
                <p>• Gunakan di area berventilasi</p>
            </div>
            <div style="flex:1;min-width:200px;background:rgba(255, 152, 0, 0.1);padding:15px;border-radius:10px;border-left:3px solid #ff9800;">
                <h4>☠️ Beracun</h4>
                <p>Contoh: Klorin, Amonia</p>
                <p>• Gunakan alat pelindung diri</p>
                <p>• Hindari inhalasi langsung</p>
            </div>
            <div style="flex:1;min-width:200px;background:rgba(76, 175, 80, 0.1);padding:15px;border-radius:10px;border-left:3px solid #4caf50;">
                <h4>💨 Pengoksidasi</h4>
                <p>Contoh: Oksigen, Fluorin</p>
                <p>• Hindari kontak dengan bahan organik</p>
                <p>• Simpan terpisah dari bahan reduktor</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🛡️ Alat Pelindung Diri (APD)</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(33, 150, 243, 0.1);padding:15px;border-radius:10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/2090/2090004.png" width="80">
                <p><b>Masker Gas</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(156, 39, 176, 0.1);padding:15px;border-radius:10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/2797/2797688.png" width="80">
                <p><b>Sarung Tangan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(255, 87, 34, 0.1);padding:15px;border-radius:10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/10984/10984307.png" width="80">
                <p><b>Kaca Mata Keselamatan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(0, 150, 136, 0.1);padding:15px;border-radius:10px;">
                <img src="https://cdn-icons-png.flaticon.com/512/3000/3000504.png" width="80">
                <p><b>Jas Laboratorium</b></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🚨 Prosedur Darurat</h3>
        <ol style="padding-left:20px;">
            <li style="margin-bottom:10px;">Segera evakuasi area jika terjadi kebocoran gas</li>
            <li style="margin-bottom:10px;">Gunakan APD yang sesuai sebelum menangani gas</li>
            <li style="margin-bottom:10px;">Hindari sumber api atau percikan listrik</li>
            <li style="margin-bottom:10px;">Ventilasi area dengan membuka jendela atau pintu</li>
            <li>Hubungi petugas berwenang jika diperlukan</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("""
<div style="text-align:center;color:#a8b2d1;padding:20px;margin-top:50px;border-top:1px solid #1e2a3a;">
    <p>© 2025 ChemGasMaster | Kelompok 7 Kelas 1A</p>
</div>
""", unsafe_allow_html=True)
