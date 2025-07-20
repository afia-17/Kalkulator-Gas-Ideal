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
# CSS CUSTOM
# ===========================================
st.markdown("""
<style>
    .main-header {
        color: #0d47a1;
        border-bottom: 2px solid #0d47a1;
        padding-bottom: 10px;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .calc-card {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 5px solid #2196f3;
    }
    .result-card {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #4caf50;
    }
    .gas-card {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-left: 5px solid #ff9800;
    }
    .safety-card {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-left: 5px solid #f44336;
    }
    .conversion-box {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px dashed #9e9e9e;
    }
    .property-table {
        width: 100%;
        border-collapse: collapse;
    }
    .property-table th {
        background-color: #0d47a1;
        color: white;
        padding: 8px;
    }
    .property-table td {
        padding: 8px;
        border-bottom: 1px solid #ddd;
    }
    .input-row {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .input-label {
        min-width: 120px;
    }
    .input-field {
        flex-grow: 1;
    }
    .input-unit {
        min-width: 100px;
    }
    .gas-icon {
        font-size: 24px;
        margin-right: 10px;
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
        "description": "Gas tidak berwarna, dapat memancarkan warna oranye kemerahan jika berada pada medan listrik bertegangan tinggi. Dapat digunakan sebagai pengisi lampu neon, penangkal petir, pengisi tabung televisi, dan dalam wujud cair neon dapat digunakan sebagai zat pendingir.",
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
    "icon": "🎚️",
    "category": "Gas Monoatomik",
    "description": "Gas tidak berwarna dan tidak berbau, sangat ringan. Tidak mudah terbakar dan digunakan secara luas dalam balon, pendinginan MRI, serta sebagai atmosfer inert untuk pengelasan.",
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
    "icon": "🔏",
    "category": "Gas Monoatomik",
    "description": "Gas inert, tidak reaktif secara kimia. Digunakan dalam pengelasan, bola lampu pijar, dan sebagai atmosfer pelindung dalam pembuatan semikonduktor.",
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
            <p>🎚️ <b>Gas Ideal Tidak Nyata</b> - Hanya model matematis yang sempurna</p>
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
                <h3 style="margin:5px 0;">{var}</h3>
                <p style="margin:5px 0;font-weight:bold;">{name}</p>
                <p style="margin:5px 0;font-size:0.8em;">{desc}</p>
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
    # Header dengan animasi partikel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0d47a1, #2196F3); 
                padding: 25px; 
                border-radius: 15px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <h1 style="color: white; text-align: center; margin: 0; z-index: 2; position: relative;">
              🧪✨ Kalkulator Gas Ideal ✨⚗️
        </h1>
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1;">
            <div class="particle" style="--size: 3px; --duration: 15s; --delay: 0s; --x: 20%; --y: 30%"></div>
            <div class="particle" style="--size: 5px; --duration: 20s; --delay: 2s; --x: 70%; --y: 10%"></div>
            <div class="particle" style="--size: 4px; --duration: 18s; --delay: 4s; --x: 40%; --y: 60%"></div>
        </div>
    </div>
    <style>
        @keyframes float {
            0% { transform: translate(0, 0) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translate(var(--x-end), var(--y-end)) rotate(360deg); opacity: 0; }
        }
        .particle {
            position: absolute;
            width: var(--size);
            height: var(--size);
            background: rgba(255,255,255,0.5);
            border-radius: 50%;
            animation: float var(--duration) var(--delay) infinite linear;
            --x-end: calc(var(--x) - 50%);
            --y-end: calc(var(--y) - 50%);
        }
        .tab-container {
            padding: 20px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-top: 15px;
        }
        .input-label {
            font-weight: bold;
            margin-bottom: 8px;
            display: block;
        }
        .conversion-box {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
            border: 1px dashed #9e9e9e;
            font-size: 0.9em;
        }
    </style>
    """, unsafe_allow_html=True)

    # Style untuk tabs
    tab_style = """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
            background: #f0f2f6 !important;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #2196F3, #0d47a1) !important;
            color: white !important;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(33, 150, 243, 0.3);
        }
    </style>
    """
    st.markdown(tab_style, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "⚖️ Hitung Massa", 
        "🎚️ Hitung Tekanan",
        "🫙 Hitung Volume",
        "🧪 Hitung Mol"
    ])
    
    R = 0.0821  # Konstanta gas ideal

    with tab1:
        # Kalkulator Massa
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #FF9800;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #FF9800;">Kalkulator Massa Gas</h2>
                        <div style="background: #FFF3E0; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> Massa = n (mol) × Mr (g/mol)
                        </div>
                    </div>
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
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("⚖️ Hitung Massa", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr 
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #FF9800;
                            animation: fadeIn 0.5s ease-in-out;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #E65100;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Massa <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #E65100; font-weight: bold; font-size: 1.5em; margin: 0;">{massa:.4f} gram</p>
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes fadeIn {{
                        from {{ opacity: 0; transform: translateY(10px); }}
                        to {{ opacity: 1; transform: translateY(0); }}
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #F44336;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; color: #F44336;">Kalkulator Tekanan Gas</h2>
                        <div style="background: #FFEBEE; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> P = [n (mol) × R × T (K)] / V (L)
                        </div>
                    </div>
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
                    <div class="conversion-box">
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
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #F44336;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #C62828;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #C62828; font-weight: bold; font-size: 1.5em; margin: 0;">{P:.2f} atm</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #4CAF50;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🫙</div>
                    <div>
                        <h2 style="margin: 0; color: #4CAF50;">Kalkulator Volume Gas</h2>
                        <div style="background: #E8F5E9; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> V = [n (mol) × R × T (K)] / P (atm)
                        </div>
                    </div>
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
                    <div class="conversion-box">
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
                    <div class="conversion-box">
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #4CAF50;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #2E7D32;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Volume <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #2E7D32; font-weight: bold; font-size: 1.5em; margin: 0;">{V:.2f} L</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #9C27B0;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪 </div>
                    <div>
                        <h2 style="margin: 0; color: #9C27B0;">Kalkulator Jumlah Mol</h2>
                        <div style="background: #F3E5F5; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> n = [P (atm) × V (L) / (R × T (K)]
                        </div>
                    </div>
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
                    <div class="conversion-box">
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
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
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
                    <div class="conversion-box">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #9C27B0;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #7B1FA2;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Jumlah mol <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #7B1FA2; font-weight: bold; font-size: 1.5em; margin: 0;">{n:.2f} mol</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
                padding: 20px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 5px solid #2196F3;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 30px;">💡</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #0D47A1;">Tips Ahli Kimia</h3>
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
    st.markdown("<h1 class='main-header'>📚 Ensiklopedia Gas</h1>", unsafe_allow_html=True)
    
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
    st.markdown("<h1 class='main-header'>⚠️ Panduan Keselamatan Gas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🚧 Simbol Bahaya Umum</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:200px;background:#ffebee;padding:15px;border-radius:10px;">
                <h4>🔥 Mudah Terbakar</h4>
                <p>Contoh: Hidrogen, Metana</p>
                <p>• Jauhkan dari sumber api</p>
                <p>• Gunakan di area berventilasi</p>
            </div>
            <div style="flex:1;min-width:200px;background:#fff8e1;padding:15px;border-radius:10px;">
                <h4>☠️ Beracun</h4>
                <p>Contoh: Klorin, Amonia</p>
                <p>• Gunakan alat pelindung diri</p>
                <p>• Hindari inhalasi langsung</p>
            </div>
            <div style="flex:1;min-width:200px;background:#e8f5e9;padding:15px;border-radius:10px;">
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
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2090/2090004.png" width="80">
                <p><b>Masker Gas</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2797/2797688.png" width="80">
                <p><b>Sarung Tangan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/10984/10984307.png" width="80">
                <p><b>Kaca Mata Keselamatan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3000/3000504.png" width="80">
                <p><b>Jas Lab</b></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card safety-card">
        <h3>🚨 Prosedur Darurat</h3>
        <ol>
            <li>Segera evakuasi area jika terjadi kebocoran gas</li>
            <li>Gunakan APD yang sesuai sebelum menangani gas</li>
            <li>Hindari sumber api atau percikan listrik</li>
            <li>Ventilasi area dengan membuka jendela/pintu</li>
            <li>Hubungi petugas berwenang jika diperlukan</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;padding:20px;">
    <p>© 2025 ChemGasMaster | Kelompok 7 Kelas 1A</p>
</div>
""", unsafe_allow_html=True)
