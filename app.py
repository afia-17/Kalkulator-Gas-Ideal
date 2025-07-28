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
# CSS CUSTOM DENGAN BACKGROUND KREATIF
# ===========================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;500;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Roboto', sans-serif;
    }
    
    /* Background Animations */
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.1); }
    }
    
    @keyframes drift {
        0% { transform: translateX(-100px) translateY(0px); }
        50% { transform: translateX(100px) translateY(-50px); }
        100% { transform: translateX(-100px) translateY(0px); }
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    
    /* Background untuk Beranda - Molecular Structure */
    .beranda-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        opacity: 0.05;
    }
    
    .beranda-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(255,255,255,0.1) 3px, transparent 3px),
            radial-gradient(circle at 80% 20%, rgba(255,255,255,0.08) 2px, transparent 2px),
            radial-gradient(circle at 40% 70%, rgba(255,255,255,0.12) 4px, transparent 4px),
            radial-gradient(circle at 90% 80%, rgba(255,255,255,0.06) 1px, transparent 1px);
        background-size: 100px 100px, 150px 150px, 80px 80px, 200px 200px;
        animation: drift 20s infinite linear;
    }
    
    .beranda-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(45deg, transparent 40%, rgba(255,255,255,0.02) 50%, transparent 60%),
            linear-gradient(-45deg, transparent 40%, rgba(255,255,255,0.02) 50%, transparent 60%);
        background-size: 60px 60px;
        animation: float 15s infinite ease-in-out;
    }

    /* Background untuk Kalkulator - Laboratory Grid */
    .kalkulator-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        opacity: 0.04;
    }
    
    .kalkulator-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px),
            linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px),
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.1) 2px, transparent 2px);
        background-size: 40px 40px, 40px 40px, 80px 80px;
        animation: pulse 8s infinite ease-in-out;
    }
    
    .kalkulator-bg::after {
        content: '⚗️';
        position: absolute;
        top: 10%;
        left: 10%;
        font-size: 20px;
        opacity: 0.1;
        animation: sparkle 6s infinite ease-in-out;
    }

    /* Background untuk Ensiklopedia - Organic Hexagons */
    .ensiklopedia-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
        opacity: 0.05;
    }
    
    .ensiklopedia-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 30% 40%, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.1) 2px, transparent 2px),
            radial-gradient(circle at 70% 20%, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.08) 3px, transparent 3px),
            radial-gradient(circle at 20% 80%, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.06) 1px, transparent 1px);
        background-size: 60px 60px, 90px 90px, 120px 120px;
        animation: float 12s infinite ease-in-out;
    }
    
    .ensiklopedia-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
        background-size: 100px 100px;
        opacity: 0.03;
        animation: drift 25s infinite linear;
    }

    /* Background untuk Keselamatan - Warning Pattern */
    .keselamatan-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
        opacity: 0.05;
    }
    
    .keselamatan-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            repeating-linear-gradient(
                45deg,
                rgba(255,255,255,0.05) 0px,
                rgba(255,255,255,0.05) 3px,
                transparent 3px,
                transparent 15px
            ),
            repeating-linear-gradient(
                -45deg,
                rgba(255,255,255,0.03) 0px,
                rgba(255,255,255,0.03) 2px,
                transparent 2px,
                transparent 20px
            );
        animation: pulse 10s infinite ease-in-out;
    }
    
    .keselamatan-bg::after {
        content: '⚠️';
        position: absolute;
        top: 15%;
        right: 15%;
        font-size: 25px;
        opacity: 0.08;
        animation: sparkle 8s infinite ease-in-out;
    }

    /* Content Overlay dengan Glass Effect */
    .content-overlay {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .content-overlay::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            transparent,
            rgba(255, 255, 255, 0.2),
            transparent
        );
        transition: left 0.5s ease;
    }
    
    .content-overlay:hover::before {
        left: 100%;
    }

    /* Enhanced Card Styles */
    .main-header {
        color: #0d47a1;
        border-bottom: 3px solid #0d47a1;
        padding-bottom: 15px;
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .card {
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 25px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .calc-card {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 6px solid #2196f3;
        border-top: 1px solid rgba(33, 150, 243, 0.3);
    }
    
    .result-card {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 6px solid #4caf50;
        border-top: 1px solid rgba(76, 175, 80, 0.3);
    }
    
    .gas-card {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-left: 6px solid #ff9800;
        border-top: 1px solid rgba(255, 152, 0, 0.3);
    }
    
    .safety-card {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-left: 6px solid #f44336;
        border-top: 1px solid rgba(244, 67, 54, 0.3);
    }
    
    /* Enhanced Input Styles */
    .conversion-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 12px 16px;
        border-radius: 12px;
        margin: 12px 0;
        border: 2px dashed #6c757d;
        font-size: 0.9em;
        position: relative;
        overflow: hidden;
    }
    
    .conversion-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(108, 117, 125, 0.1), transparent);
        transition: left 0.5s ease;
    }
    
    .conversion-box:hover::before {
        left: 100%;
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .property-table th {
        background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
        color: white;
        padding: 15px;
        font-weight: 600;
        text-align: left;
        font-family: 'Orbitron', monospace;
    }
    
    .property-table td {
        padding: 15px;
        border-bottom: 1px solid #e0e0e0;
        background: white;
        transition: background-color 0.3s ease;
    }
    
    .property-table tr:hover td {
        background: #f8f9fa;
    }
    
    .property-table tr:last-child td {
        border-bottom: none;
    }
    
    /* Enhanced Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #2196f3 0%, #0d47a1 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 25px;
        font-weight: 600;
        font-family: 'Orbitron', monospace;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(33, 150, 243, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.4);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Enhanced Input Field Styles */
    .stSelectbox > div > div {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #2196f3;
        box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.1);
    }
    
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 12px;
        padding: 12px 16px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stTextInput > div > div > input:focus {
        border-color: #2196f3;
        box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.1);
    }
    
    /* Tab Enhancements */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        padding: 0 25px;
        border-radius: 12px;
        transition: all 0.3s ease;
        background: rgba(255, 255, 255, 0.8) !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 500;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2196f3, #0d47a1) !important;
        color: white !important;
        font-weight: 700;
        box-shadow: 0 6px 20px rgba(33, 150, 243, 0.4);
        font-family: 'Orbitron', monospace;
    }
    
    /* Sidebar Enhancements */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Input Labels */
    .input-label {
        font-weight: 600;
        margin-bottom: 8px;
        display: block;
        color: #495057;
        font-family: 'Roboto', sans-serif;
    }
    
    /* Floating Elements */
    .floating-element {
        position: absolute;
        pointer-events: none;
        opacity: 0.1;
        animation: float 6s infinite ease-in-out;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .content-overlay {
            padding: 15px;
            margin: 10px 0;
        }
        
        .card {
            padding: 15px;
        }
        
        .property-table th,
        .property-table td {
            padding: 10px;
            font-size: 0.9em;
        }
    }
</style>
""", unsafe_allow_html=True)

# Fungsi untuk menambahkan background sesuai menu
def add_menu_background(menu_type):
    if menu_type == "beranda":
        st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
    elif menu_type == "kalkulator":
        st.markdown('<div class="kalkulator-bg"></div>', unsafe_allow_html=True)
    elif menu_type == "ensiklopedia":
        st.markdown('<div class="ensiklopedia-bg"></div>', unsafe_allow_html=True)
    elif menu_type == "keselamatan":
        st.markdown('<div class="keselamatan-bg"></div>', unsafe_allow_html=True)

# Fungsi untuk wrap konten dengan overlay
def wrap_content_with_overlay(content_html):
    return f'<div class="content-overlay">{content_html}</div>'

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
        "icon": "🎚️",
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
        "icon": "🔏",
        "category": "Gas Monoatomik",
        "description": "Gas inert, tidak reaktif secara kimia. Digunakan dalam pengelasan dan sebagai atmosfer pelindung.",
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
# MENU SIDEBAR DENGAN DESAIN FUTURISTIK
# ===========================================
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 25px; 
                border-radius: 20px; 
                text-align: center; 
                margin-bottom: 25px;
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 20px; opacity: 0.3;">⚗️</div>
        <div style="position: absolute; bottom: 10px; left: 10px; font-size: 15px; opacity: 0.2;">🧪</div>
        <h1 style="color: white; margin: 0; font-size: 2em; font-family: 'Orbitron', monospace; font-weight: 900;">
            ChemGasMaster
        </h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-weight: 300;">
            🚀 Platform Kimia Futuristik
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu dengan styling futuristik
    menu_options = ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
    menu = st.radio(
        "🎯 MENU NAVIGASI",
        menu_options,
        index=0
    )
    
    st.markdown("---")
    
    # Info box futuristik
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                padding: 20px;
                border-radius: 15px;
                border-left: 5px solid #2196f3;
                margin-bottom: 20px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 5px; right: 5px; font-size: 25px; opacity: 0.2;">🔬</div>
        <div style="font-size: 1.3em; margin-bottom: 10px;">⚛️</div>
        <small><b>💡 Persamaan Gas Ideal</b><br>
        <code style="background: rgba(33, 150, 243, 0.1); padding: 2px 6px; border-radius: 4px;">PV = nRT</code><br>
        <span style="color: #1976d2;">R = 0.0821 L·atm/mol·K</span></small>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun facts box dengan animasi
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
                padding: 20px;
                border-radius: 15px;
                border-left: 5px solid #4caf50;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 5px; right: 5px; font-size: 20px; opacity: 0.2; animation: sparkle 3s infinite;">✨</div>
        <div style="font-size: 1.3em; margin-bottom: 10px;">🎯</div>
        <small><b>🧬 Fakta Molekuler!</b><br>
        • 1 mol = 6.022×10²³ partikel<br>
        • Gas ideal = Model teoretis<br>
        • STP = 0°C, 1 atm, 22.4 L/mol</small>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    add_menu_background("beranda")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; padding: 40px; position: relative;">
        <div style="position: absolute; top: 20px; left: 20px; font-size: 30px; opacity: 0.1; animation: float 8s infinite;">⚗️</div>
        <div style="position: absolute; top: 50px; right: 30px; font-size: 25px; opacity: 0.1; animation: float 6s infinite 2s;">🧪</div>
        <div style="position: absolute; bottom: 30px; left: 50px; font-size: 20px; opacity: 0.1; animation: float 10s infinite 4s;">🔬</div>
        
        <h1 style="color: #0d47a1; font-size: 3.5em; margin-bottom: 20px; font-family: 'Orbitron', monospace; font-weight: 900; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">
            ⚗️ ChemGasMaster
        </h1>
        <p style="font-size: 1.4em; color: #666; margin-bottom: 30px; font-weight: 300;">
            🚀 Platform Interaktif untuk Eksplorasi Dunia Gas Ideal
        </p>
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 3px; 
                    border-radius: 50px; 
                    display: inline-block;">
            <div style="background: white; 
                        padding: 15px 30px; 
                        border-radius: 50px; 
                        color: #667eea; 
                        font-weight: 600;">
                ✨ Teknologi Kimia Masa Depan ✨
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # Welcome card dengan efek futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
        <div style="position: absolute; top: -50px; right: -50px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 6s infinite 2s;"></div>
        
        <div style="font-size: 3em; margin-bottom: 20px; animation: sparkle 4s infinite;">🎉</div>
        <h2 style="margin: 0 0 20px 0; font-family: 'Orbitron', monospace; font-weight: 700;">
            Selamat Datang di Era Baru Kimia!
        </h2>
        <p style="font-size: 1.2em; margin: 0; opacity: 0.95; line-height: 1.6;">
            Jelajahi dunia gas ideal dengan teknologi canggih, kalkulator presisi tinggi, 
            ensiklopedia komprehensif, dan panduan keselamatan yang revolusioner!
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan visualisasi futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; margin: 40px 0;">
        <h3 style="color: #0d47a1; margin-bottom: 25px; font-family: 'Orbitron', monospace; font-weight: 700;">
            🔬 Persamaan Gas Ideal Futuristik
        </h3>
    </div>
    """), unsafe_allow_html=True)
    
    # LaTeX equation dengan styling
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px; margin: 20px 0;">
    """, unsafe_allow_html=True)
    st.latex(r'''PV = nRT''')
    st.markdown("</div>", unsafe_allow_html=True)
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    border-left: 5px solid #2196f3;">
            <h4 style="color: #0d47a1; margin-bottom: 20px; font-family: 'Orbitron', monospace;">
                📊 Variabel Persamaan Futuristik:
            </h4>
            <div style="display: flex; flex-direction: column; gap: 15px;">
                <div style="background: white; padding: 15px; border-radius: 10px; border-left: 4px solid #f44336; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <b style="color: #f44336; font-size: 1.2em;">P</b> = Tekanan (atm)
                    <div style="font-size: 0.9em; color: #666; margin-top: 5px;">Gaya molekul pada dinding wadah</div>
                </div>
                <div style="background: white; padding: 15px; border-radius: 10px; border-left: 4px solid #4caf50; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <b style="color: #4caf50; font-size: 1.2em;">V</b> = Volume (L)
                    <div style="font-size: 0.9em; color: #666; margin-top: 5px;">Ruang tiga dimensi gas</div>
                </div>
                <div style="background: white; padding: 15px; border-radius: 10px; border-left: 4px solid #2196f3; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <b style="color: #2196f3; font-size: 1.2em;">n</b> = Jumlah mol (mol)
                    <div style="font-size: 0.9em; color: #666; margin-top: 5px;">Kuantitas materi gas</div>
                </div>
                <div style="background: white; padding: 15px; border-radius: 10px; border-left: 4px solid #9c27b0; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <b style="color: #9c27b0; font-size: 1.2em;">R</b> = Konstanta gas = 0.0821 L·atm/mol·K
                    <div style="font-size: 0.9em; color: #666; margin-top: 5px;">Konstanta universal</div>
                </div>
                <div style="background: white; padding: 15px; border-radius: 10px; border-left: 4px solid #ff9800; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateX(5px)'" onmouseout="this.style.transform='translateX(0)'">
                    <b style="color: #ff9800; font-size: 1.2em;">T</b> = Suhu (K)
                    <div style="font-size: 0.9em; color: #666; margin-top: 5px;">Energi kinetik rata-rata</div>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); 
                    padding: 25px; 
                    border-radius: 15px; 
                    border-left: 5px solid #ff9800;">
            <h4 style="color: #e65100; margin-bottom: 20px; font-family: 'Orbitron', monospace;">
                🎯 Fakta Futuristik:
            </h4>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: white; padding: 12px; border-radius: 8px; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                    🎚️ <b>Gas Ideal</b> - Model matematis sempurna!
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                    🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                    🧪 <b>1 mol gas</b> = 6.022×10²³ molekul
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                    🚀 <b>STP</b> - 0°C, 1 atm, 22.4 L/mol
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'" onmouseout="this.style.boxShadow='none'">
                    ⚛️ <b>Molekul</b> - Bergerak acak dengan kecepatan tinggi
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    # Visualisasi variabel dengan efek hover
    st.markdown(wrap_content_with_overlay("<h4 style='text-align: center; color: #0d47a1; margin: 40px 0 25px 0; font-family: \"Orbitron\", monospace;'>📊 Visualisasi Variabel Gas Ideal Futuristik</h4>"), unsafe_allow_html=True)
    
    var_cols = st.columns(5)
    variables = [
        ("P", "Tekanan", "Gaya gas pada dinding wadah", "#f44336"),
        ("V", "Volume", "Ruang yang ditempati gas", "#4caf50"),
        ("n", "Jumlah Mol", "Banyaknya partikel gas", "#2196f3"),
        ("R", "Konstanta", "Tetapan gas universal", "#9c27b0"),
        ("T", "Suhu", "Energi kinetik rata-rata", "#ff9800")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                        padding: 25px;
                        border-radius: 15px;
                        height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        color: white;
                        transition: all 0.3s ease;
                        cursor: pointer;
                        position: relative;
                        overflow: hidden;"
                 onmouseover="this.style.transform='translateY(-10px) scale(1.05)'; this.style.boxShadow='0 15px 30px rgba(0,0,0,0.2)'"
                 onmouseout="this.style.transform='translateY(0) scale(1)'; this.style.boxShadow='0 4px 15px rgba(0,0,0,0.1)'">
                <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 3s infinite;"></div>
                <h2 style="margin: 8px 0; font-size: 2.5em; font-family: 'Orbitron', monospace; font-weight: 900;">{var}</h2>
                <p style="margin: 8px 0; font-weight: 700; font-size: 1.1em;">{name}</p>
                <p style="margin: 8px 0; font-size: 0.85em; opacity: 0.9; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    add_menu_background("kalkulator")
    
    # Header dengan animasi partikel yang diperbaiki
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #0d47a1, #2196F3);
                padding: 30px;
                border-radius: 20px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(33, 150, 243, 0.3);">
        <h1 style="color: white; text-align: center; margin: 0; z-index: 2; position: relative; font-family: 'Orbitron', monospace; font-weight: 900; font-size: 2.5em;">
              🧪✨ Kalkulator Gas Ideal Futuristik ✨⚗️
        </h1>
        <p style="color: rgba(255,255,255,0.9); text-align: center; margin: 15px 0 0 0; z-index: 2; position: relative; font-size: 1.1em;">
            🚀 Teknologi Perhitungan Presisi Tinggi
        </p>
        
        <!-- Floating particles -->
        <div style="position: absolute; top: 20%; left: 15%; width: 6px; height: 6px; background: rgba(255,255,255,0.6); border-radius: 50%; animation: float 8s infinite ease-in-out;"></div>
        <div style="position: absolute; top: 60%; right: 20%; width: 4px; height: 4px; background: rgba(255,255,255,0.4); border-radius: 50%; animation: float 12s infinite ease-in-out 2s;"></div>
        <div style="position: absolute; bottom: 30%; left: 70%; width: 5px; height: 5px; background: rgba(255,255,255,0.5); border-radius: 50%; animation: float 10s infinite ease-in-out 4s;"></div>
    </div>
    """), unsafe_allow_html=True)

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
            st.markdown(wrap_content_with_overlay("""
            <div style="border-left: 6px solid #FF9800; padding: 25px; background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); border-radius: 15px;">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
                    <div style="font-size: 50px; animation: pulse 3s infinite;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #E65100; font-family: 'Orbitron', monospace; font-weight: 700;">
                            Kalkulator Massa Gas Futuristik
                        </h2>
                        <div style="background: rgba(230, 81, 0, 0.1); 
                                    padding: 10px 15px; 
                                    border-radius: 10px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    border: 1px solid rgba(230, 81, 0, 0.2);">
                            <b>🔬 Rumus:</b> <code>Massa = n (mol) × Mr (g/mol)</code>
                        </div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

            cols = st.columns(3)
            with cols[0]:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Contoh: Oksigen", label_visibility="collapsed")
            with cols[1]:
                st.markdown('<div class="input-label">🧪 Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f", label_visibility="collapsed")
            with cols[2]:
                st.markdown('<div class="input-label">⚖️ Massa Molar (Mr)</div>', unsafe_allow_html=True)
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f", label_visibility="collapsed")
                
            if st.button("⚖️ Hitung Massa", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr
                
                st.markdown(wrap_content_with_overlay(f"""
                <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
                            padding: 25px;
                            border-radius: 15px;
                            margin-top: 25px;
                            border-left: 6px solid #4CAF50;
                            position: relative;
                            overflow: hidden;">
                    <div style="position: absolute; top: -30px; right: -30px; width: 60px; height: 60px; background: rgba(76, 175, 80, 0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; animation: sparkle 2s infinite;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #2E7D32; font-family: 'Orbitron', monospace;">
                                🎉 Hasil Perhitungan Futuristik
                            </h3>
                            <div style="background: rgba(46, 125, 50, 0.1); 
                                        padding: 15px; 
                                        border-radius: 10px;
                                        border: 1px solid rgba(46, 125, 50, 0.2);">
                                <p style="margin: 0; font-size: 1.3em; display: flex; align-items: baseline; gap: 10px;">
                                    Massa <b style="color: #2E7D32;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: 900; color: #2E7D32; font-family: 'Orbitron', monospace;">
                                        {massa:.4f} gram
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """), unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="border-left: 6px solid #F44336; padding: 25px; background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%); border-radius: 15px;">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
                    <div style="font-size: 50px; animation: pulse 3s infinite;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; color: #C62828; font-family: 'Orbitron', monospace; font-weight: 700;">
                            Kalkulator Tekanan Gas Futuristik
                        </h2>
                        <div style="background: rgba(198, 40, 40, 0.1); 
                                    padding: 10px 15px; 
                                    border-radius: 10px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    border: 1px solid rgba(198, 40, 40, 0.2);">
                            <b>🔬 Rumus:</b> <code>P = [n (mol) × R × T (K)] / V (L)</code>
                        </div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🧪 Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f", label_visibility="collapsed")
        
            with col2:
                st.markdown('<div class="input-label">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="tekanan_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="tekanan_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">📦 Volume</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    V_input = st.number_input("Volume", min_value=0.0, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
        
            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(wrap_content_with_overlay(f"""
                <div style="background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
                            padding: 25px;
                            border-radius: 15px;
                            margin-top: 25px;
                            border-left: 6px solid #F44336;
                            position: relative;
                            overflow: hidden;">
                    <div style="position: absolute; top: -30px; right: -30px; width: 60px; height: 60px; background: rgba(244, 67, 54, 0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; animation: sparkle 2s infinite;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #C62828; font-family: 'Orbitron', monospace;">
                                🎉 Hasil Perhitungan Futuristik
                            </h3>
                            <div style="background: rgba(198, 40, 40, 0.1); 
                                        padding: 15px; 
                                        border-radius: 10px;
                                        border: 1px solid rgba(198, 40, 40, 0.2);">
                                <p style="margin: 0; font-size: 1.3em; display: flex; align-items: baseline; gap: 10px;">
                                    Tekanan <b style="color: #C62828;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: 900; color: #C62828; font-family: 'Orbitron', monospace;">
                                        {P:.2f} atm
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """), unsafe_allow_html=True)
                st.balloons()

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="border-left: 6px solid #4CAF50; padding: 25px; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); border-radius: 15px;">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
                    <div style="font-size: 50px; animation: pulse 3s infinite;">🫙</div>
                    <div>
                        <h2 style="margin: 0; color: #2E7D32; font-family: 'Orbitron', monospace; font-weight: 700;">
                            Kalkulator Volume Gas Futuristik
                        </h2>
                        <div style="background: rgba(46, 125, 50, 0.1); 
                                    padding: 10px 15px; 
                                    border-radius: 10px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    border: 1px solid rgba(46, 125, 50, 0.2);">
                            <b>🔬 Rumus:</b> <code>V = [n (mol) × R × T (K)] / P (atm)</code>
                        </div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_volume", placeholder="Contoh: Hidrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🧪 Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f", label_visibility="collapsed")
        
            with col2:
                st.markdown('<div class="input-label">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="volume_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="volume_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
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
                        🔄 Konversi Futuristik: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
        
            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(wrap_content_with_overlay(f"""
                <div style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
                            padding: 25px;
                            border-radius: 15px;
                            margin-top: 25px;
                            border-left: 6px solid #4CAF50;
                            position: relative;
                            overflow: hidden;">
                    <div style="position: absolute; top: -30px; right: -30px; width: 60px; height: 60px; background: rgba(76, 175, 80, 0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; animation: sparkle 2s infinite;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #2E7D32; font-family: 'Orbitron', monospace;">
                                🎉 Hasil Perhitungan Futuristik
                            </h3>
                            <div style="background: rgba(46, 125, 50, 0.1); 
                                        padding: 15px; 
                                        border-radius: 10px;
                                        border: 1px solid rgba(46, 125, 50, 0.2);">
                                <p style="margin: 0; font-size: 1.3em; display: flex; align-items: baseline; gap: 10px;">
                                    Volume <b style="color: #2E7D32;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: 900; color: #2E7D32; font-family: 'Orbitron', monospace;">
                                        {V:.2f} L
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """), unsafe_allow_html=True)
                st.balloons()

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="border-left: 6px solid #9C27B0; padding: 25px; background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); border-radius: 15px;">
                <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 25px;">
                    <div style="font-size: 50px; animation: pulse 3s infinite;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #7B1FA2; font-family: 'Orbitron', monospace; font-weight: 700;">
                            Kalkulator Jumlah Mol Futuristik
                        </h2>
                        <div style="background: rgba(123, 31, 162, 0.1); 
                                    padding: 10px 15px; 
                                    border-radius: 10px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    border: 1px solid rgba(123, 31, 162, 0.2);">
                            <b>🔬 Rumus:</b> <code>n = [P (atm) × V (L)] / [R × T (K)]</code>
                        </div>
                    </div>
                </div>
            </div>
            """), unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_mol", placeholder="Contoh: Karbon Dioksida", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
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
                        🔄 Konversi Futuristik: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
        
            with col2:
                st.markdown('<div class="input-label">📦 Volume</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    V_input = st.number_input("Volume", min_value=0.0, key="mol_vol_input", label_visibility="collapsed")
                with col2b:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="mol_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="mol_suhu_input", label_visibility="collapsed")
                with col2d:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="mol_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Futuristik: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
        
            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(wrap_content_with_overlay(f"""
                <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
                            padding: 25px;
                            border-radius: 15px;
                            margin-top: 25px;
                            border-left: 6px solid #9C27B0;
                            position: relative;
                            overflow: hidden;">
                    <div style="position: absolute; top: -30px; right: -30px; width: 60px; height: 60px; background: rgba(156, 39, 176, 0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; animation: sparkle 2s infinite;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #7B1FA2; font-family: 'Orbitron', monospace;">
                                🎉 Hasil Perhitungan Futuristik
                            </h3>
                            <div style="background: rgba(123, 31, 162, 0.1); 
                                        padding: 15px; 
                                        border-radius: 10px;
                                        border: 1px solid rgba(123, 31, 162, 0.2);">
                                <p style="margin: 0; font-size: 1.3em; display: flex; align-items: baseline; gap: 10px;">
                                    Jumlah mol <b style="color: #7B1FA2;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: 900; color: #7B1FA2; font-family: 'Orbitron', monospace;">
                                        {n:.2f} mol
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """), unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
                padding: 25px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 6px solid #2196F3;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(33, 150, 243, 0.1); border-radius: 50%; animation: pulse 5s infinite;"></div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 40px; animation: sparkle 4s infinite;">💡</div>
            <div>
                <h3 style="margin: 0 0 15px 0; color: #0D47A1; font-family: 'Orbitron', monospace;">
                    🎓 Tips Ahli Kimia Futuristik
                </h3>
                <p style="margin: 0; line-height: 1.6; font-size: 1.1em;">
                    ✨ Untuk hasil terbaik, pastikan semua satuan konsisten dengan konstanta gas R 
                    (0.0821 L·atm/mol·K). Gunakan suhu dalam Kelvin dan tekanan dalam atm.
                    <br><br>
                    🌡️ <b>Konversi Suhu:</b> K = °C + 273.15
                    <br>
                    🎚️ <b>Konversi Tekanan:</b> 1 atm = 101.325 kPa = 760 mmHg
                    <br>
                    📦 <b>Konversi Volume:</b> 1 m³ = 1000 L = 1,000,000 mL
                </p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    add_menu_background("ensiklopedia")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(0, 184, 148, 0.3);">
        <div style="position: absolute; top: -50px; right: -50px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 6s infinite;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 8s infinite 2s;"></div>
        
        <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 5s infinite;">📚</div>
        <h1 style="margin: 0; font-size: 2.5em; font-family: 'Orbitron', monospace; font-weight: 900;">
            Ensiklopedia Gas Futuristik
        </h1>
        <p style="margin: 15px 0 0 0; opacity: 0.95; font-size: 1.2em;">
            🚀 Jelajahi Dunia Gas dengan Database Molekuler Canggih
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Selectbox dengan styling futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 25px;
                text-align: center;
                border: 2px solid #00b894;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 20px; opacity: 0.2;">🔍</div>
        <h3 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">
            🔬 Pilih Gas untuk Analisis Molekuler
        </h3>
    </div>
    """), unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}",
        label_visibility="collapsed"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas dengan desain futuristik
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
                    padding: 25px;
                    border-radius: 15px;
                    color: white;
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 4s infinite;"></div>
            
            <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                <div style="font-size: 3em; animation: float 6s infinite;">{gas['icon']}</div>
                <h2 style="margin: 0; font-size: 2em; font-family: 'Orbitron', monospace; font-weight: 700;">
                    {selected_gas}
                </h2>
            </div>
            <div style="background: rgba(255,255,255,0.15); 
                        padding: 15px; 
                        border-radius: 10px;
                        margin-bottom: 20px;
                        border: 1px solid rgba(255,255,255,0.2);">
                <p style="margin: 0; font-style: italic; line-height: 1.5;">
                    {gas['description']}
                </p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 12px; 
                            border-radius: 8px;
                            border: 1px solid rgba(255,255,255,0.2);">
                    <p style="margin: 0;"><b>📂 Kategori:</b> {gas['category']}</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 12px; 
                            border-radius: 8px;
                            border: 1px solid rgba(255,255,255,0.2);">
                    <p style="margin: 0;"><b>🔧 Aplikasi:</b> {gas['aplikasi']}</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with col2:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    border: 2px solid #00b894;
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: 5px; right: 5px; font-size: 15px; opacity: 0.3;">🔬</div>
            <img src="{gas['image']}" 
                 style="width: 100%; 
                        max-width: 200px; 
                        border-radius: 10px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <p style="color: #495057; margin: 15px 0 0 0; font-weight: 600; font-family: 'Orbitron', monospace;">
                🖼️ Struktur Molekul 3D
            </p>
        </div>
        """), unsafe_allow_html=True)
    
    # Tab Informasi dengan tabel yang diperbaiki dan styling futuristik
    tabs = st.tabs(list(gas["properties"].keys()))
    
    colors = [
        ("#00b894", "rgba(0, 184, 148, 0.1)"),
        ("#6c5ce7", "rgba(108, 92, 231, 0.1)"), 
        ("#fd79a8", "rgba(253, 121, 168, 0.1)")
    ]
    
    for i, (tab, (category, props)) in enumerate(zip(tabs, gas["properties"].items())):
        with tab:
            color, bg_color = colors[i % len(colors)]
            
            # Membuat tabel dengan cara yang aman dan styling futuristik
            table_rows = ""
            for key, value in props.items():
                table_rows += f"""
                <tr style="transition: all 0.3s ease;" onmouseover="this.style.backgroundColor='rgba(0,0,0,0.05)'" onmouseout="this.style.backgroundColor='white'">
                    <td style="padding: 15px; font-weight: 600; background: {bg_color}; width: 40%; border-bottom: 1px solid #dee2e6; font-family: 'Orbitron', monospace;">
                        {key}
                    </td>
                    <td style="padding: 15px; background: white; border-bottom: 1px solid #dee2e6;">
                        {value}
                    </td>
                </tr>"""
            
            st.markdown(wrap_content_with_overlay(f"""
            <div style="background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
                        padding: 25px;
                        border-radius: 15px;
                        color: white;
                        margin: 20px 0;
                        position: relative;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(0,0,0,0.15);">
                <div style="position: absolute; top: -30px; right: -30px; width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 5s infinite;"></div>
                
                <h3 style="margin: 0 0 20px 0; text-align: center; font-family: 'Orbitron', monospace; font-weight: 700;">
                    {category}
                </h3>
                <div style="background: rgba(255,255,255,0.95); 
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                    <table style="width: 100%; border-collapse: collapse;">
                        {table_rows}
                    </table>
                </div>
            </div>
            """), unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    add_menu_background("keselamatan")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(253, 121, 168, 0.3);">
        <div style="position: absolute; top: -50px; right: -50px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 6s infinite;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 8s infinite 2s;"></div>
        
        <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 4s infinite;">⚠️</div>
        <h1 style="margin: 0; font-size: 2.5em; font-family: 'Orbitron', monospace; font-weight: 900;">
            Panduan Keselamatan Gas Futuristik
        </h1>
        <p style="margin: 15px 0 0 0; opacity: 0.95; font-size: 1.2em;">
            🛡️ Keselamatan Adalah Prioritas Utama dalam Era Teknologi Kimia
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Simbol Bahaya dengan desain futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                padding: 30px;
                border-radius: 20px;
                margin-bottom: 30px;
                border: 2px solid #fd79a8;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 25px; opacity: 0.1;">🚧</div>
        
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px; animation: pulse 4s infinite;">🚧</div>
            <h2 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace; font-weight: 700;">
                Simbol Bahaya Molekuler
            </h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
            <div style="background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-5px)'"
                 onmouseout="this.style.transform='translateY(0)'">
                <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 5s infinite;"></div>
                <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 3s infinite;">🔥</div>
                <h3 style="margin: 0 0 15px 0; font-family: 'Orbitron', monospace;">Mudah Terbakar</h3>
                <div style="background: rgba(255,255,255,0.15); 
                            padding: 15px; 
                            border-radius: 10px;
                            border: 1px solid rgba(255,255,255,0.2);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Hidrogen, Metana</p>
                    <p style="margin: 5px 0;">• Jauhkan dari sumber api</p>
                    <p style="margin: 5px 0;">• Gunakan di area berventilasi</p>
                    <p style="margin: 5px 0;">• Hindari percikan listrik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #6f42c1 0%, #5a32a3 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-5px)'"
                 onmouseout="this.style.transform='translateY(0)'">
                <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 5s infinite 1s;"></div>
                <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 4s infinite;">☠️</div>
                <h3 style="margin: 0 0 15px 0; font-family: 'Orbitron', monospace;">Beracun</h3>
                <div style="background: rgba(255,255,255,0.15); 
                            padding: 15px; 
                            border-radius: 10px;
                            border: 1px solid rgba(255,255,255,0.2);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Klorin, Amonia</p>
                    <p style="margin: 5px 0;">• Gunakan alat pelindung diri</p>
                    <p style="margin: 5px 0;">• Hindari inhalasi langsung</p>
                    <p style="margin: 5px 0;">• Ventilasi yang baik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='translateY(-5px)'"
                 onmouseout="this.style.transform='translateY(0)'">
                <div style="position: absolute; top: -20px; right: -20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 5s infinite 2s;"></div>
                <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 5s infinite;">💨</div>
                <h3 style="margin: 0 0 15px 0; font-family: 'Orbitron', monospace;">Pengoksidasi</h3>
                <div style="background: rgba(255,255,255,0.15); 
                            padding: 15px; 
                            border-radius: 10px;
                            border: 1px solid rgba(255,255,255,0.2);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Oksigen, Fluorin</p>
                    <p style="margin: 5px 0;">• Hindari kontak dengan bahan organik</p>
                    <p style="margin: 5px 0;">• Simpan terpisah dari reduktor</p>
                    <p style="margin: 5px 0;">• Meningkatkan risiko kebakaran</p>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # APD dengan desain futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);">
        <div style="position: absolute; top: -50px; right: -50px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 7s infinite;"></div>
        
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px; animation: sparkle 6s infinite;">🛡️</div>
            <h2 style="margin: 0; font-family: 'Orbitron', monospace; font-weight: 700;">
                Alat Pelindung Diri Futuristik (APD)
            </h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.15);
                        padding: 25px;
                        border-radius: 12px;
                        text-align: center;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'">
                <div style="font-size: 3.5em; margin-bottom: 15px; animation: float 8s infinite;">😷</div>
                <h4 style="margin: 0 0 10px 0; font-family: 'Orbitron', monospace;">Masker Gas</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi dari inhalasi gas berbahaya</p>
            </div>
            <div style="background: rgba(255,255,255,0.15);
                        padding: 25px;
                        border-radius: 12px;
                        text-align: center;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'">
                <div style="font-size: 3.5em; margin-bottom: 15px; animation: float 8s infinite 1s;">🧤</div>
                <h4 style="margin: 0 0 10px 0; font-family: 'Orbitron', monospace;">Sarung Tangan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi tangan dari kontak langsung</p>
            </div>
            <div style="background: rgba(255,255,255,0.15);
                        padding: 25px;
                        border-radius: 12px;
                        text-align: center;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'">
                <div style="font-size: 3.5em; margin-bottom: 15px; animation: float 8s infinite 2s;">🥽</div>
                <h4 style="margin: 0 0 10px 0; font-family: 'Orbitron', monospace;">Kacamata Keselamatan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi mata dari percikan</p>
            </div>
            <div style="background: rgba(255,255,255,0.15);
                        padding: 25px;
                        border-radius: 12px;
                        text-align: center;
                        border: 1px solid rgba(255,255,255,0.2);
                        transition: transform 0.3s ease;"
                 onmouseover="this.style.transform='scale(1.05)'"
                 onmouseout="this.style.transform='scale(1)'">
                <div style="font-size: 3.5em; margin-bottom: 15px; animation: float 8s infinite 3s;">🥼</div>
                <h4 style="margin: 0 0 10px 0; font-family: 'Orbitron', monospace;">Jas Laboratorium</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi tubuh dari kontaminasi</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

    # Prosedur Darurat dengan desain futuristik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
                padding: 30px;
                border-radius: 20px;
                margin-bottom: 30px;
                border: 2px solid #ffc107;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 30px; opacity: 0.1;">🚨</div>
        
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px; animation: pulse 3s infinite;">🚨</div>
            <h2 style="margin: 0; color: #856404; font-family: 'Orbitron', monospace; font-weight: 700;">
                Prosedur Darurat Futuristik
            </h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #dc3545;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite;">1️⃣</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Evakuasi Segera</h4>
                </div>
                <p style="margin: 0; color: #666;">Segera tinggalkan area jika terjadi kebocoran gas berbahaya</p>
            </div>
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #28a745;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite 1s;">2️⃣</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Gunakan APD</h4>
                </div>
                <p style="margin: 0; color: #666;">Selalu gunakan alat pelindung diri yang sesuai sebelum menangani gas</p>
            </div>
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #fd7e14;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite 2s;">3️⃣</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Hindari Api</h4>
                </div>
                <p style="margin: 0; color: #666;">Jauhkan dari sumber api, percikan listrik, dan benda panas</p>
            </div>
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #007bff;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite 3s;">4️⃣</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Ventilasi Area</h4>
                </div>
                <p style="margin: 0; color: #666;">Buka jendela dan pintu untuk sirkulasi udara yang baik</p>
            </div>
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #6f42c1;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite 4s;">5️⃣</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Hubungi Petugas</h4>
                </div>
                <p style="margin: 0; color: #666;">Segera hubungi petugas berwenang atau layanan darurat jika diperlukan</p>
            </div>
            <div style="background: white; 
                        padding: 20px; 
                        border-radius: 12px;
                        border-left: 5px solid #17a2b8;
                        transition: transform 0.3s ease;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);"
                 onmouseover="this.style.transform='translateX(5px)'"
                 onmouseout="this.style.transform='translateX(0)'">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 12px;">
                    <div style="font-size: 2em; animation: sparkle 4s infinite 5s;">📞</div>
                    <h4 style="margin: 0; color: #495057; font-family: 'Orbitron', monospace;">Nomor Darurat</h4>
                </div>
                <p style="margin: 0; color: #666;"><b>Pemadam Kebakaran:</b> 113<br><b>Ambulans:</b> 118<br><b>Polisi:</b> 110</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# FOOTER FUTURISTIK
# ===========================================
st.markdown("---")
st.markdown(wrap_content_with_overlay("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-top: 40px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);">
    <div style="position: absolute; top: -50px; right: -50px; width: 100px; height: 100px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 8s infinite;"></div>
    <div style="position: absolute; bottom: -30px; left: -30px; width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; animation: pulse 10s infinite 2s;"></div>
    
    <div style="font-size: 2.5em; margin-bottom: 15px; animation: sparkle 6s infinite;">⚗️</div>
    <h3 style="margin: 0 0 10px 0; font-family: 'Orbitron', monospace; font-weight: 900; font-size: 1.8em;">
        ChemGasMaster Futuristik
    </h3>
    <p style="margin: 0; opacity: 0.9; font-size: 1.1em;">
        © 2025 Kelompok 7 Kelas 1A | Platform Kimia Teknologi Masa Depan
    </p>
    <div style="margin-top: 20px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <span style="background: rgba(255,255,255,0.15); 
                     padding: 8px 16px; 
                     border-radius: 20px;
                     border: 1px solid rgba(255,255,255,0.2);
                     transition: transform 0.3s ease;"
              onmouseover="this.style.transform='scale(1.05)'"
              onmouseout="this.style.transform='scale(1)'">
            🧪 Kalkulator Gas Futuristik
        </span>
        <span style="background: rgba(255,255,255,0.15); 
                     padding: 8px 16px; 
                     border-radius: 20px;
                     border: 1px solid rgba(255,255,255,0.2);
                     transition: transform 0.3s ease;"
              onmouseover="this.style.transform='scale(1.05)'"
              onmouseout="this.style.transform='scale(1)'">
            📚 Ensiklopedia Molekuler
        </span>
        <span style="background: rgba(255,255,255,0.15); 
                     padding: 8px 16px; 
                     border-radius: 20px;
                     border: 1px solid rgba(255,255,255,0.2);
                     transition: transform 0.3s ease;"
              onmouseover="this.style.transform='scale(1.05)'"
              onmouseout="this.style.transform='scale(1)'">
            ⚠️ Keselamatan Canggih
        </span>
    </div>
</div>
"""), unsafe_allow_html=True)
