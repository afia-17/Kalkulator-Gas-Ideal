# ===========================================
# APLIKASI KALKULATOR GAS IDEAL + ENSIKLOPEDIA + PANDUAN KESELAMATAN
# ===========================================
import streamlit as st
import base64

# Konfigurasi Halaman
st.set_page_config(
    page_title="GasMaster Pro",
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
# FUNGSI KONVERSI
# ===========================================
def konversi_suhu(label, key_prefix):
    st.markdown(f'<div class="input-row"><div class="input-label">{label}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,1])
    with col1:
        T_input = st.number_input(label, min_value=-273.0, key=f"{key_prefix}_input", label_visibility="collapsed")
    with col2:
        satuan = st.selectbox("Satuan", ["K", "°C"], key=f"{key_prefix}_unit", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if satuan == "°C":
        T = T_input + 273.15
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {T_input}°C = {T:.2f} K
        </div>
        """, unsafe_allow_html=True)
    else:
        T = T_input
    return T

def konversi_tekanan(label, key_prefix):
    st.markdown(f'<div class="input-row"><div class="input-label">{label}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,1])
    with col1:
        P_input = st.number_input(label, min_value=0.0, key=f"{key_prefix}_input", label_visibility="collapsed")
    with col2:
        satuan = st.selectbox("Satuan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], 
                            key=f"{key_prefix}_unit", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if satuan == "Pa":
        P = P_input / 101325
    elif satuan == "kPa":
        P = P_input / 101.325
    elif satuan == "hPa":
        P = P_input / 1013.25
    elif satuan == "bar":
        P = P_input / 1.01325
    elif satuan in ["Torr", "mmHg"]:
        P = P_input / 760
    else:
        P = P_input
    
    if satuan != "atm":
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} {satuan} = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    return P

def konversi_volume(label, key_prefix):
    st.markdown(f'<div class="input-row"><div class="input-label">{label}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,1])
    with col1:
        V_input = st.number_input(label, min_value=0.1, key=f"{key_prefix}_input", label_visibility="collapsed")
    with col2:
        satuan = st.selectbox("Satuan", ["L", "m³", "mL"], key=f"{key_prefix}_unit", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if satuan == "m³":
        V = V_input * 1000
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {V_input} m³ = {V:.2f} L
        </div>
        """, unsafe_allow_html=True)
    elif satuan == "mL":
        V = V_input / 1000
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {V_input} mL = {V:.4f} L
        </div>
        """, unsafe_allow_html=True)
    else:
        V = V_input
    return V

# ===========================================
# DATABASE GAS
# ===========================================
GAS_DATABASE = {
    "Hidrogen (H₂)": {
        "icon": "🚀",
        "category": "Gas Diatomik",
        "description": "Unsur paling ringan di alam semesta dengan sifat unik sebagai bahan bakar masa depan.",
        "image": "https://www.shutterstock.com/video/clip-1068494438-hydrogen-h2-molecule-3d-chemistry-structure-isolated?dd_referrer=https%3A%2F%2Fwww.google.com%2F",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "H₂",
                "Massa Molar": "2.016 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan tunggal"
            },
            "📊 Sifat Fisika": {
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Oxygen_molecule.png/320px-Oxygen_molecule.png",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "O₂",
                "Massa Molar": "32.00 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Diatomik, ikatan rangkap"
            },
            "📊 Sifat Fisika": {
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Nitrogen-3D-vdW.png/320px-Nitrogen-3D-vdW.png",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "N₂",
                "Massa Molar": "28.014 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan rangkap tiga"
            },
            "📊 Sifat Fisika": {
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Carbon-dioxide-3D-vdW.png/320px-Carbon-dioxide-3D-vdW.png",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CO₂",
                "Massa Molar": "44.01 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Linear, ikatan rangkap"
            },
            "📊 Sifat Fisika": {
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
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Oxygen_molecule.png/320px-Oxygen_molecule.png",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ne",
                "Massa Molar": "20.18 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "📊 Sifat Fisika": {
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
    "description": "Gas tidak berwarna dan tidak berbau, sangat ringan. Tidak mudah terbakar dan digunakan secara luas dalam balon, pendinginan MRI, serta sebagai atmosfer inert untuk pengelasan.",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Helium_discharge_tube.jpg/320px-Helium_discharge_tube.jpg",
    "properties": {
      "🧪 Identitas Molekul": {
        "Rumus": "He",
        "Massa Molar": "4.00 g/mol",
        "Penampilan": "Gas tak berwarna",
        "Struktur": "Monoatomik"
      },
      "📊 Sifat Fisika": {
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
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Argon_discharge_tube.jpg/320px-Argon_discharge_tube.jpg",
    "properties": {
      "🧪 Identitas Molekul": {
        "Rumus": "Ar",
        "Massa Molar": "39.95 g/mol",
        "Penampilan": "Gas tak berwarna",
        "Struktur": "Monoatomik"
      },
      "📊 Sifat Fisika": {
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
  "Nitrogen (N₂)": {
    "icon": "🧬",
    "category": "Gas Diatomik",
    "description": "Menyusun sekitar 78% atmosfer bumi. Tidak mudah bereaksi dan digunakan untuk penyimpanan makanan, atmosfer inert, serta produksi amonia.",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Nitrogen-dioxide-3D-vdW.png/320px-Nitrogen-dioxide-3D-vdW.png",
    "properties": {
      "🧪 Identitas Molekul": {
        "Rumus": "N₂",
        "Massa Molar": "28.01 g/mol",
        "Penampilan": "Gas tak berwarna",
        "Struktur": "Diatomik, ikatan rangkap tiga"
      },
      "📊 Sifat Fisika": {
        "Titik Leleh": "-210 °C (63.15 K)",
        "Titik Didih": "-196 °C (77.36 K)",
        "Densitas (STP)": "1.25 g/L",
        "Kalor Jenis": "1.04 J/(g·K)"
      },
      "⚠️ Keselamatan": {
        "Bahaya": "Asfiksia dalam konsentrasi tinggi",
        "Penanganan": "Gunakan ventilasi dan deteksi oksigen di area tertutup"
      }
    },
    "aplikasi": "Penyimpanan makanan, pengelasan, industri pupuk"
  }
}

# ===========================================
# MENU SIDEBAR
# ===========================================
with st.sidebar:
    st.title("GasMaster Pro")
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
    st.markdown("<h1 class='main-header'>GasMaster Pro</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card calc-card">
        <h3>Selamat Datang di Aplikasi GasMaster Pro!</h3>
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
            <p>🎈 <b>Gas Ideal Tidak Nyata</b> - Hanya model matematis yang sempurna</p>
            <p>🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi</p>
            <p>⚛️ <b>1 mol gas</b> = 6.022×10²³ molekul</p>
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
    
    # Tips penggunaan
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
# HALAMAN KALKULATOR GAS (COMPLETE FIXED VERSION)
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
        "🧂 Hitung Massa", 
        "🎈 Hitung Tekanan",
        "🧊 Hitung Volume",
        "⚛️ Hitung Mol"
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
                            <b>Rumus:</b> Massa = n × Mr
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
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.4f", label_visibility="collapsed")
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🚀 Hitung Massa", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #FF9800;
                            animation: fadeIn 0.5s ease-in-out;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🎯</div>
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
                    <div style="font-size: 40px;">🎈</div>
                    <div>
                        <h2 style="margin: 0; color: #F44336;">Kalkulator Tekanan Gas</h2>
                        <div style="background: #FFEBEE; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> P = (n × R × T) / V
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
                    V_input = st.number_input("Volume", min_value=0.1, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.2f} L
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

            if st.button("💥 Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #F44336;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">📊</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #C62828;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #C62828; font-weight: bold; font-size: 1.5em; margin: 0;">{P:.6f} atm</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #4CAF50;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧊</div>
                    <div>
                        <h2 style="margin: 0; color: #4CAF50;">Kalkulator Volume Gas</h2>
                        <div style="background: #E8F5E9; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> V = (n × R × T) / P
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.6f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🧊 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
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
                                <p style="color: #2E7D32; font-weight: bold; font-size: 1.5em; margin: 0;">{V:.4f} L</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #9C27B0;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">⚛️</div>
                    <div>
                        <h2 style="margin: 0; color: #9C27B0;">Kalkulator Jumlah Mol</h2>
                        <div style="background: #F3E5F5; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> n = (P × V) / (R × T)
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.6f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="input-label">Volume</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    V_input = st.number_input("Volume", min_value=0.1, key="mol_vol_input", label_visibility="collapsed")
                with col2b:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="mol_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.2f} L
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

            if st.button("⚗️ Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
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
                                <p style="color: #7B1FA2; font-weight: bold; font-size: 1.5em; margin: 0;">{n:.4f} mol</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

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
# ===========================================
# HALAMAN ENSIKLOPEDIA GAS (ENHANCED VERSION)
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.markdown("""
    <style>
        .gas-header {
            background: linear-gradient(135deg, #0d47a1, #42a5f5);
            color: white;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
        }
        .gas-header::after {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('https://i.imgur.com/JQJQJQJ.png') no-repeat;
            background-size: cover;
            opacity: 0.1;
            z-index: 1;
        }
        .gas-header-content {
            position: relative;
            z-index: 2;
        }
        .molecule-viewer {
            background-color: #f5f5f5;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            text-align: center;
            border: 1px solid #e0e0e0;
        }
        .property-card {
            background: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-left: 4px solid #0d47a1;
        }
        .app-card {
            background: #e3f2fd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .safety-badge {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            margin-right: 8px;
            margin-bottom: 8px;
        }
        .floating-molecule {
            position: absolute;
            opacity: 0.1;
            z-index: 0;
            font-size: 100px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="gas-header">
        <div class="gas-header-content">
            <h1 class='main-header' style='color:white;'>⚗️ Ensiklopedia Gas</h1>
            <p style='font-size:1.1em;margin-bottom:0;'>Database lengkap sifat-sifat gas penting dalam ilmu kimia</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Gas selection with search functionality
    search_term = st.text_input("🔍 Cari Gas", placeholder="Ketik nama gas...")
    
    filtered_gases = [gas for gas in GAS_DATABASE.keys() 
                     if search_term.lower() in gas.lower()] if search_term else list(GAS_DATABASE.keys())
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        filtered_gases,
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}",
        index=0 if not search_term else None
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Main gas information
    st.markdown(f"""
    <div style='position:relative;'>
        <div class='floating-molecule' style='top:-50px;right:50px;'>{gas['icon']}</div>
        <div class='floating-molecule' style='bottom:0;left:50px;'>{gas['icon']}</div>
        
        <div style='display:flex;gap:30px;margin-bottom:30px;'>
            <div style='flex:2;'>
                <h2 style='margin-top:0;display:flex;align-items:center;'>
                    <span style='font-size:1.5em;margin-right:15px;'>{gas['icon']}</span>
                    {selected_gas}
                </h2>
                <p style='font-size:1.1em;color:#555;'>{gas['description']}</p>
                
                <div style='display:flex;gap:15px;margin:20px 0;'>
                    <div style='background:#e3f2fd;padding:10px 15px;border-radius:8px;'>
                        <div style='font-size:0.9em;color:#0d47a1;'>Kategori</div>
                        <div style='font-weight:bold;'>{gas['category']}</div>
                    </div>
                    <div style='background:#e8f5e9;padding:10px 15px;border-radius:8px;'>
                        <div style='font-size:0.9em;color:#2e7d32;'>Massa Molar</div>
                        <div style='font-weight:bold;'>{gas['properties']['🧪 Identitas Molekul']['Massa Molar']}</div>
                    </div>
                </div>
            </div>
            
            <div style='flex:1;'>
                <div style='border-radius:15px;overflow:hidden;box-shadow:0 5px 15px rgba(0,0,0,0.1);'>
                    <img src='{gas["image"]}' style='width:100%;max-height:250px;object-fit:cover;'>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Molecule 3D viewer placeholder
    st.markdown("""
    <div class='molecule-viewer'>
        <h4>🖼️ Tampilan Molekul 3D</h4>
        <div style='height:200px;background:#f0f0f0;display:flex;justify-content:center;align-items:center;border-radius:10px;margin:15px 0;'>
            <p style='color:#888;'>Visualisasi 3D molekul {selected_gas}</p>
        </div>
        <button style='background:#0d47a1;color:white;border:none;padding:8px 15px;border-radius:5px;cursor:pointer;'>
            🔍 Perbesar Molekul
        </button>
    </div>
    """, unsafe_allow_html=True)

    # Tab system for properties
    tab1, tab2, tab3 = st.tabs(["📊 Sifat Fisika & Kimia", "🏭 Aplikasi Industri", "⚠️ Keselamatan"])
    
    with tab1:
        st.markdown(f"""
        <h3 style='margin-top:0;'>Sifat Fisika & Kimia</h3>
        <div style='display:grid;grid-template-columns:repeat(auto-fill, minmax(300px, 1fr));gap:15px;'>
        """, unsafe_allow_html=True)
        
        for category, props in gas['properties'].items():
            if category != "⚠️ Keselamatan":
                st.markdown(f"""
                <div class='property-card'>
                    <h4 style='margin-top:0;color:#0d47a1;'>{category}</h4>
                    <table style='width:100%;border-collapse:collapse;'>
                        {"".join(f"""
                        <tr>
                            <td style='padding:8px 0;border-bottom:1px solid #eee;width:40%;'><b>{key}</b></td>
                            <td style='padding:8px 0;border-bottom:1px solid #eee;'>{value}</td>
                        </tr>
                        """ for key, value in props.items())}
                    </table>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with tab2:
        st.markdown(f"""
        <h3 style='margin-top:0;'>Aplikasi Industri</h3>
        <div class='app-card'>
            <h4 style='margin-top:0;color:#0d47a1;'>Penggunaan Utama</h4>
            <p>{gas['aplikasi']}</p>
            
            <h4 style='margin-top:20px;color:#0d47a1;'>Proses Produksi</h4>
            <p>Metode utama produksi {selected_gas.split(' ')[0]} dalam industri:</p>
            <ul>
                <li>Destilasi fraksional udara cair (untuk gas seperti O₂, N₂, Ar)</li>
                <li>Reaksi kimia khusus (seperti elektrolisis untuk H₂)</li>
                <li>Proses fermentasi atau biologis (untuk gas seperti CH₄)</li>
            </ul>
            
            <h4 style='margin-top:20px;color:#0d47a1;'>Data Ekonomi</h4>
            <div style='display:flex;gap:15px;'>
                <div style='flex:1;background:#e1f5fe;padding:10px;border-radius:8px;'>
                    <div style='font-size:0.9em;color:#0288d1;'>Harga Pasar</div>
                    <div style='font-weight:bold;'>$2.50 - $5.00 per kg</div>
                </div>
                <div style='flex:1;background:#f1f8e9;padding:10px;border-radius:8px;'>
                    <div style='font-size:0.9em;color:#689f38;'>Produksi Global</div>
                    <div style='font-weight:bold;'>70 juta ton/tahun</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        safety = gas['properties']['⚠️ Keselamatan']
        st.markdown(f"""
        <h3 style='margin-top:0;'>Panduan Keselamatan</h3>
        <div style='display:grid;grid-template-columns:repeat(auto-fill, minmax(300px, 1fr));gap:15px;margin-bottom:20px;'>
            <div class='property-card' style='border-left-color:#f44336;'>
                <h4 style='margin-top:0;color:#f44336;'>Potensi Bahaya</h4>
                <p>{safety['Bahaya']}</p>
            </div>
            <div class='property-card' style='border-left-color:#ff9800;'>
                <h4 style='margin-top:0;color:#ff9800;'>Penanganan Aman</h4>
                <p>{safety['Penanganan']}</p>
            </div>
        </div>
        
        <h4 style='margin-top:20px;color:#f44336;'>Simbol Bahaya</h4>
        <div style='display:flex;flex-wrap:wrap;gap:10px;margin:15px 0;'>
            <span class='safety-badge' style='background:#ffebee;color:#c62828;'>🔥 Mudah Terbakar</span>
            <span class='safety-badge' style='background:#fff3e0;color:#e65100;'>☢️ Bertekanan</span>
            <span class='safety-badge' style='background:#e8f5e9;color:#2e7d32;'>💨 Asfiksian</span>
        </div>
        
        <div class='app-card' style='background:#ffebee;'>
            <h4 style='margin-top:0;color:#c62828;'>Prosedur Darurat</h4>
            <ol>
                <li>Segera evakuasi area jika terjadi kebocoran</li>
                <li>Gunakan alat pernapasan jika diperlukan</li>
                <li>Ventilasi area dengan membuka jendela/pintu</li>
                <li>Hindari sumber api atau percikan</li>
                <li>Hubungi petugas berwenang</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    # Related gases
    st.markdown("""
    <h3 style='margin-top:30px;'>🔗 Gas Terkait</h3>
    <div style='display:flex;overflow-x:auto;gap:15px;padding:10px 0;'>
    """, unsafe_allow_html=True)
    
    related_gases = [g for g in GAS_DATABASE.keys() if g != selected_gas][:5]
    for gas_name in related_gases:
        g = GAS_DATABASE[gas_name]
        st.markdown(f"""
        <div style='flex:0 0 200px;background:white;border-radius:10px;padding:15px;box-shadow:0 2px 5px rgba(0,0,0,0.1);'>
            <div style='font-size:2em;text-align:center;'>{g['icon']}</div>
            <h4 style='margin:10px 0;text-align:center;'>{gas_name.split(' ')[0]}</h4>
            <p style='font-size:0.8em;color:#666;text-align:center;margin-bottom:10px;'>{g['category']}</p>
            <button style='width:100%;background:#e3f2fd;border:none;padding:8px;border-radius:5px;cursor:pointer;'
                    onclick='window.location.href="?gas={gas_name.replace(' ', '_')}"'>
                Lihat Detail
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Periodic table reference
    st.markdown("""
    <div style='margin-top:40px;background:#f5f5f5;padding:20px;border-radius:15px;'>
        <h3 style='margin-top:0;'>🧪 Referensi Tabel Periodik</h3>
        <p>Elemen terkait dalam tabel periodik:</p>
        <div style='display:inline-block;background:#0d47a1;color:white;padding:5px 10px;border-radius:5px;margin:5px;'>H</div>
        <div style='display:inline-block;background:#0d47a1;color:white;padding:5px 10px;border-radius:5px;margin:5px;'>O</div>
        <div style='display:inline-block;background:#0d47a1;color:white;padding:5px 10px;border-radius:5px;margin:5px;'>N</div>
        <div style='display:inline-block;background:#0d47a1;color:white;padding:5px 10px;border-radius:5px;margin:5px;'>C</div>
        <p style='margin-top:15px;'><a href='https://www.rsc.org/periodic-table' target='_blank'>🔗 Lihat Tabel Periodik Lengkap</a></p>
    </div>
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
                <p><b>Kacamata Keselamatan</b></p>
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
    <p>© 2025 GasMaster Pro | Kelompok LPK Poltek AKA</p>
</div>
""", unsafe_allow_html=True)
