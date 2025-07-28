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
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .card {
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        background: white;
        border: 1px solid #e0e0e0;
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .calc-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    .result-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        border: none;
    }
    
    .gas-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        border: none;
    }
    
    .safety-card {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        color: #333;
        border: none;
    }
    
    .info-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #333;
        border: 1px solid #dee2e6;
    }
    
    .conversion-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 15px;
        margin: 15px 0;
        border: 1px solid rgba(255,255,255,0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(102, 126, 234, 0); }
        100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .property-table th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        font-weight: bold;
        text-align: left;
    }
    
    .property-table td {
        padding: 15px;
        border-bottom: 1px solid #dee2e6;
        background: white;
        transition: background 0.3s ease;
    }
    
    .property-table tr:hover td {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    .input-label {
        font-weight: bold;
        color: #495057;
        margin-bottom: 8px;
        font-size: 16px;
    }
    
    /* Animated background particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .particle {
        position: absolute;
        border-radius: 50%;
        animation: float 6s ease-in-out infinite;
        opacity: 0.6;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.6; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
    }
    
    /* Button styling yang lebih menarik */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: white;
        border: 2px solid #667eea;
        border-radius: 15px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background: white;
        border: 2px solid #667eea;
        border-radius: 15px;
        color: #333;
        transition: all 0.3s ease;
        padding: 10px 15px;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background: white;
        border: 2px solid #667eea;
        border-radius: 15px;
        color: #333;
        transition: all 0.3s ease;
        padding: 10px 15px;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# BACKGROUND KREATIF DAN MENARIK
# ===========================================
st.markdown("""
<style>
    /* Background Beranda - Animated Gradient dengan Geometric Shapes */
    .beranda-bg {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #f5576c);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.1;
    }
    
    .beranda-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.3) 2px, transparent 2px),
            radial-gradient(circle at 75% 75%, rgba(255,255,255,0.2) 1px, transparent 1px),
            linear-gradient(45deg, transparent 45%, rgba(255,255,255,0.1) 50%, transparent 55%);
        background-size: 50px 50px, 30px 30px, 100px 100px;
        animation: patternMove 15s linear infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes patternMove {
        0% { transform: translateX(0) translateY(0); }
        100% { transform: translateX(50px) translateY(50px); }
    }

    /* Background Kalkulator - Animated Circuit Pattern */
    .kalkulator-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.08;
    }
    
    .kalkulator-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px),
            linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
            radial-gradient(circle at 30% 70%, rgba(255,255,255,0.2) 3px, transparent 3px);
        background-size: 40px 40px, 40px 40px, 80px 80px;
        animation: circuitFlow 20s linear infinite;
    }
    
    @keyframes circuitFlow {
        0% { transform: translateX(0) translateY(0); opacity: 0.5; }
        50% { transform: translateX(20px) translateY(20px); opacity: 1; }
        100% { transform: translateX(40px) translateY(40px); opacity: 0.5; }
    }

    /* Background Ensiklopedia - Molecular Structure Pattern */
    .ensiklopedia-bg {
        background: linear-gradient(120deg, #a8edea 0%, #fed6e3 50%, #d299c2 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.1;
    }
    
    .ensiklopedia-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 20%, rgba(255,255,255,0.3) 4px, transparent 4px),
            radial-gradient(circle at 60% 80%, rgba(255,255,255,0.2) 2px, transparent 2px),
            radial-gradient(circle at 80% 40%, rgba(255,255,255,0.25) 3px, transparent 3px);
        background-size: 60px 60px, 40px 40px, 80px 80px;
        animation: molecularDance 12s ease-in-out infinite;
    }
    
    @keyframes molecularDance {
        0%, 100% { transform: translateX(0) translateY(0) rotate(0deg); }
        33% { transform: translateX(10px) translateY(-10px) rotate(120deg); }
        66% { transform: translateX(-10px) translateY(10px) rotate(240deg); }
    }

    /* Background Keselamatan - Warning Pattern */
    .keselamatan-bg {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.08;
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
                rgba(255,255,255,0.1) 0px,
                rgba(255,255,255,0.1) 10px,
                transparent 10px,
                transparent 20px
            ),
            repeating-linear-gradient(
                -45deg,
                rgba(255,255,255,0.05) 0px,
                rgba(255,255,255,0.05) 15px,
                transparent 15px,
                transparent 30px
            );
        animation: warningPulse 3s ease-in-out infinite;
    }
    
    @keyframes warningPulse {
        0%, 100% { opacity: 0.8; }
        50% { opacity: 1; }
    }

    /* Content overlay yang lebih modern */
    .content-overlay {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .content-overlay:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
    }

    /* Floating particles animation */
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        pointer-events: none;
    }
    
    .particle-element {
        position: absolute;
        border-radius: 50%;
        background: rgba(102, 126, 234, 0.3);
        animation: floatUp 15s infinite linear;
    }
    
    @keyframes floatUp {
        0% {
            transform: translateY(100vh) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-10vh) scale(1);
            opacity: 0;
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

# Fungsi untuk menambahkan partikel mengambang
def add_floating_particles():
    st.markdown("""
    <div class="floating-particles">
        <div class="particle-element" style="left: 10%; width: 4px; height: 4px; animation-delay: 0s;"></div>
        <div class="particle-element" style="left: 20%; width: 6px; height: 6px; animation-delay: 2s;"></div>
        <div class="particle-element" style="left: 30%; width: 3px; height: 3px; animation-delay: 4s;"></div>
        <div class="particle-element" style="left: 40%; width: 5px; height: 5px; animation-delay: 6s;"></div>
        <div class="particle-element" style="left: 50%; width: 4px; height: 4px; animation-delay: 8s;"></div>
        <div class="particle-element" style="left: 60%; width: 7px; height: 7px; animation-delay: 10s;"></div>
        <div class="particle-element" style="left: 70%; width: 3px; height: 3px; animation-delay: 12s;"></div>
        <div class="particle-element" style="left: 80%; width: 5px; height: 5px; animation-delay: 14s;"></div>
        <div class="particle-element" style="left: 90%; width: 4px; height: 4px; animation-delay: 16s;"></div>
    </div>
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
        "icon": "🔒",
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
# MENU SIDEBAR YANG LEBIH MENARIK
# ===========================================
with st.sidebar:
    st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            padding: 25px; 
            border-radius: 20px; 
            text-align: center; 
            margin-bottom: 25px;
            position: relative;
            overflow: hidden;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; 
                background-image: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.1) 2px, transparent 2px),
                                  radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 1px, transparent 1px),
                                  radial-gradient(circle at 40% 60%, rgba(255,255,255,0.1) 1.5px, transparent 1.5px);
                background-size: 60px 60px, 40px 40px, 80px 80px;
                opacity: 0.3;">
    </div>
    <h1 style="color: white; margin: 0; font-size: 2em; position: relative; z-index: 2;">⚗️ ChemGasMaster</h1>
    <p style="color: rgba(255,255,255,0.9); margin: 8px 0 0 0; position: relative; z-index: 2; font-size: 1.1em;">Platform Kimia Interaktif</p>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu dengan styling yang lebih menarik
    menu_options = ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
    menu = st.radio(
        "📋 MENU UTAMA",
        menu_options,
        index=0
    )
    
    st.markdown("---")
    
    # Info box yang lebih menarik
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 20px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🧪</div>
        <div style="font-size: 1.5em; margin-bottom: 10px;">💡</div>
        <small style="color: #333;"><b>ℹ️ Info Penting</b><br>
        Menggunakan persamaan gas ideal:<br>
        <b style="color: #667eea;">PV = nRT</b><br>
        (R = 0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun facts box
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                padding: 20px;
                border-radius: 15px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🎯</div>
        <div style="font-size: 1.5em; margin-bottom: 10px;">🚀</div>
        <small style="color: #333;"><b>Fakta Menarik!</b><br>
        1 mol gas = 6.022×10²³ molekul<br>
        Gas ideal hanya ada dalam teori! 🤓<br>
    </div>
    """, unsafe_allow_html=True)

# Menambahkan partikel mengambang
add_floating_particles()

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    add_menu_background("beranda")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; padding: 40px; position: relative;">
        <div style="font-size: 4em; margin-bottom: 20px; animation: bounce 2s infinite;">⚗️</div>
        <h1 style="color: #667eea; font-size: 3em; margin-bottom: 20px; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            ChemGasMaster
        </h1>
        <p style="font-size: 1.3em; color: #666; margin-bottom: 30px;">
            Platform Interaktif untuk Eksplorasi Dunia Gas Ideal ✨
        </p>
    </div>
    <style>
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
    </style>
    """), unsafe_allow_html=True)
    
    # Welcome card
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -50px; right: -50px; font-size: 10em; opacity: 0.1;">🎉</div>
        <div style="font-size: 3em; margin-bottom: 15px;">🌟</div>
        <h2 style="margin: 0 0 15px 0; font-size: 2em;">Selamat Datang di ChemGasMaster!</h2>
        <p style="font-size: 1.2em; margin: 0; opacity: 0.95; line-height: 1.6;">
            Jelajahi dunia gas ideal dengan kalkulator canggih, ensiklopedia lengkap, 
            dan panduan keselamatan yang komprehensif! 🚀✨
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Persamaan Gas Ideal
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; margin: 40px 0;">
        <h3 style="color: #667eea; margin-bottom: 25px; font-size: 2em;">🔬 Persamaan Gas Ideal</h3>
    </div>
    """), unsafe_allow_html=True)
    
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                    padding: 25px; 
                    border-radius: 20px; 
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">📊</div>
            <h4 style="color: #333; margin-bottom: 20px; font-size: 1.5em;">📊 Variabel Persamaan:</h4>
            <div style="display: flex; flex-direction: column; gap: 15px;">
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px; border-left: 4px solid #ff6b6b;">
                    <b style="color: #ff6b6b; font-size: 1.2em;">P</b> = Tekanan (atm)
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px; border-left: 4px solid #4ecdc4;">
                    <b style="color: #4ecdc4; font-size: 1.2em;">V</b> = Volume (L)
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px; border-left: 4px solid #45b7d1;">
                    <b style="color: #45b7d1; font-size: 1.2em;">n</b> = Jumlah mol (mol)
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px; border-left: 4px solid #9b59b6;">
                    <b style="color: #9b59b6; font-size: 1.2em;">R</b> = Konstanta gas = 0.0821 L·atm/mol·K
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px; border-left: 4px solid #f39c12;">
                    <b style="color: #f39c12; font-size: 1.2em;">T</b> = Suhu (K)
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); 
                    padding: 25px; 
                    border-radius: 20px;
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">🎯</div>
            <h4 style="color: #333; margin-bottom: 20px; font-size: 1.5em;">🎯 Fakta Menarik:</h4>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px;">
                    🎈 <b>Gas Ideal</b> - Hanya model matematis sempurna!
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px;">
                    🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px;">
                    🧪 <b>1 mol gas</b> = 6.022×10²³ molekul
                </div>
                <div style="background: rgba(255,255,255,0.8); padding: 12px; border-radius: 15px;">
                    🚀 <b>STP</b> - 0°C, 1 atm, 22.4 L/mol
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    # Visualisasi variabel
    st.markdown(wrap_content_with_overlay("<h4 style='text-align: center; color: #667eea; margin: 40px 0 25px 0; font-size: 2em;'>📊 Visualisasi Variabel Gas Ideal</h4>"), unsafe_allow_html=True)
    
    var_cols = st.columns(5)
    variables = [
        ("P", "Tekanan", "Gaya gas pada dinding wadah", "#ff6b6b"),
        ("V", "Volume", "Ruang yang ditempati gas", "#4ecdc4"),
        ("n", "Jumlah Mol", "Banyaknya partikel gas", "#45b7d1"),
        ("R", "Konstanta", "Tetapan gas universal", "#9b59b6"),
        ("T", "Suhu", "Energi kinetik rata-rata", "#f39c12")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}, {color}dd);
                        padding: 25px;
                        border-radius: 20px;
                        height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                        transition: transform 0.3s ease;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 3em; opacity: 0.2;">{var}</div>
                <h2 style="margin: 5px 0; font-size: 2.5em; z-index: 2;">{var}</h2>
                <p style="margin: 5px 0; font-weight: bold; z-index: 2; font-size: 1.1em;">{name}</p>
                <p style="margin: 5px 0; font-size: 0.85em; opacity: 0.9; z-index: 2; line-height: 1.3;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    add_menu_background("kalkulator")
    
    # Header dengan animasi yang lebih menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 35px;
                border-radius: 25px;
                margin-bottom: 35px;
                text-align: center;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -20px; left: -20px; width: 100px; height: 100px; 
                    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
                    border-radius: 50%;
                    animation: float 6s ease-in-out infinite;"></div>
        <div style="position: absolute; bottom: -30px; right: -30px; width: 150px; height: 150px; 
                    background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 70%);
                    border-radius: 50%;
                    animation: float 8s ease-in-out infinite reverse;"></div>
        <h1 style="color: white; margin: 0; font-size: 2.5em; position: relative; z-index: 2;">
            🧪✨ Kalkulator Gas Ideal ✨⚗️
        </h1>
        <p style="color: rgba(255,255,255,0.95); margin: 15px 0 0 0; font-size: 1.2em; position: relative; z-index: 2;">
            Hitung dengan Presisi Tinggi menggunakan Persamaan PV = nRT
        </p>
    </div>
    <style>
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
    </style>
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
            <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🧪</div>
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3em;">🧪</div>
                    <div style="z-index: 2;">
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Massa Gas</h2>
                        <div style="background: rgba(255,255,255,0.25); 
                                    padding: 10px 15px; 
                                    border-radius: 15px; 
                                    display: inline-block;
                                    margin-top: 10px;">
                            <b>Rumus:</b> Massa = n (mol) × Mr (g/mol)
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
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            position: relative;
                            overflow: hidden;
                            animation: slideIn 0.5s ease-out;">
                    <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">⚖️</div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🎉</div>
                        <div style="z-index: 2;">
                            <h3 style="margin: 0 0 10px 0; font-size: 1.8em;">Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.25); 
                                        padding: 15px; 
                                        border-radius: 15px;">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Massa <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #fff3cd;">
                                        {massa:.4f} gram
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes slideIn {{
                        from {{ opacity: 0; transform: translateY(20px); }}
                        to {{ opacity: 1; transform: translateY(0); }}
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🎚️</div>
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3em;">🎚️</div>
                    <div style="z-index: 2;">
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Tekanan Gas</h2>
                        <div style="background: rgba(255,255,255,0.25); 
                                    padding: 10px 15px; 
                                    border-radius: 15px; 
                                    display: inline-block;
                                    margin-top: 10px;">
                            <b>Rumus:</b> P = [n (mol) × R × T (K)] / V (L)
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
                        🔄 Konversi: {T_input}°C = {T:.2f} K
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
        
            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            position: relative;
                            overflow: hidden;
                            animation: slideIn 0.5s ease-out;">
                    <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">🎚️</div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🎉</div>
                        <div style="z-index: 2;">
                            <h3 style="margin: 0 0 10px 0; font-size: 1.8em;">Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.25); 
                                        padding: 15px; 
                                        border-radius: 15px;">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Tekanan <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #fff3cd;">
                                        {P:.2f} atm
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🫙</div>
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3em;">🫙</div>
                    <div style="z-index: 2;">
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Volume Gas</h2>
                        <div style="background: rgba(255,255,255,0.25); 
                                    padding: 10px 15px; 
                                    border-radius: 15px; 
                                    display: inline-block;
                                    margin-top: 10px;">
                            <b>Rumus:</b> V = [n (mol) × R × T (K)] / P (atm)
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
                        🔄 Konversi: {T_input}°C = {T:.2f} K
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
        
            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            position: relative;
                            overflow: hidden;
                            animation: slideIn 0.5s ease-out;">
                    <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">📦</div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🎉</div>
                        <div style="z-index: 2;">
                            <h3 style="margin: 0 0 10px 0; font-size: 1.8em;">Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.25); 
                                        padding: 15px; 
                                        border-radius: 15px;">
                                <p style="margin: 0; font-size: 1px; 
                                        border-radius: 15px;">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Volume <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #fff3cd;">
                                        {V:.2f} L
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: #333;
                        margin-bottom: 25px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🧪</div>
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3em;">🧪</div>
                    <div style="z-index: 2;">
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Jumlah Mol</h2>
                        <div style="background: rgba(255,255,255,0.4); 
                                    padding: 10px 15px; 
                                    border-radius: 15px; 
                                    display: inline-block;
                                    margin-top: 10px;">
                            <b>Rumus:</b> n = [P (atm) × V (L)] / [R × T (K)]
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
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
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
        
            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: #333;
                            position: relative;
                            overflow: hidden;
                            animation: slideIn 0.5s ease-out;">
                    <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">🔬</div>
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🎉</div>
                        <div style="z-index: 2;">
                            <h3 style="margin: 0 0 10px 0; font-size: 1.8em; color: #333;">Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.4); 
                                        padding: 15px; 
                                        border-radius: 15px;">
                                <p style="margin: 0; font-size: 1.3em; color: #333;">
                                    Jumlah mol <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #d63384;">
                                        {n:.2f} mol
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                padding: 25px;
                border-radius: 20px;
                margin-top: 35px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">💡</div>
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 3em;">💡</div>
            <div style="z-index: 2;">
                <h3 style="margin: 0 0 15px 0; color: #333; font-size: 1.8em;">🎓 Tips Perhitungan</h3>
                <p style="margin: 0; color: #555; line-height: 1.8; font-size: 1.1em;">
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
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                padding: 30px;
                border-radius: 25px;
                color: #333;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -20px; right: -20px; font-size: 8em; opacity: 0.1;">📚</div>
        <div style="font-size: 3em; margin-bottom: 15px;">📚</div>
        <h1 style="margin: 0; font-size: 2.5em; color: #333;">Ensiklopedia Gas</h1>
        <p style="margin: 15px 0 0 0; opacity: 0.8; font-size: 1.2em;">
            🔬 Jelajahi Dunia Gas dengan Informasi Lengkap & Akurat
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Selectbox
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                padding: 20px;
                border-radius: 20px;
                margin-bottom: 25px;
                text-align: center;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 5px; right: 5px; font-size: 3em; opacity: 0.2;">🔍</div>
        <h3 style="margin: 0; color: #333; font-size: 1.5em;">🔍 Pilih Gas untuk Dipelajari</h3>
    </div>
    """), unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}",
        label_visibility="collapsed"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 25px;
                    border-radius: 20px;
                    color: white;
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">{gas['icon']}</div>
            <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                <div style="font-size: 3em;">{gas['icon']}</div>
                <h2 style="margin: 0; font-size: 2.2em; z-index: 2;">{selected_gas}</h2>
            </div>
            <div style="background: rgba(255,255,255,0.25); 
                        padding: 15px; 
                        border-radius: 15px;
                        margin-bottom: 20px;
                        z-index: 2;
                        position: relative;">
                <p style="margin: 0; font-style: italic; font-size: 1.1em; line-height: 1.6;">
                    {gas['description']}
                </p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; z-index: 2; position: relative;">
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 15px; 
                            border-radius: 15px;">
                    <p style="margin: 0; font-size: 1.1em;"><b>📂 Kategori:</b> {gas['category']}</p>
                </div>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 15px; 
                            border-radius: 15px;">
                    <p style="margin: 0; font-size: 1.1em;"><b>🔧 Aplikasi:</b> {gas['aplikasi']}</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with col2:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                    padding: 20px;
                    border-radius: 20px;
                    text-align: center;
                    position: relative;
                    overflow: hidden;">
            <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🖼️</div>
            <img src="{gas['image']}" 
                 style="width: 100%; 
                        max-width: 250px; 
                        border-radius: 15px;
                        box-shadow: 0 8px 25px rgba(0,0,0,0.2);">
            <p style="color: #333; margin: 15px 0 0 0; font-weight: bold; font-size: 1.1em;">
                🖼️ Struktur Molekul
            </p>
        </div>
        """), unsafe_allow_html=True)
    
    # Tab Informasi dengan tabel yang diperbaiki
    tabs = st.tabs(list(gas["properties"].keys()))
    
    colors = [
        "#667eea",
        "#11998e", 
        "#ff9a9e"
    ]
    
    for i, (tab, (category, props)) in enumerate(zip(tabs, gas["properties"].items())):
        with tab:
            color = colors[i % len(colors)]
            
            st.markdown(wrap_content_with_overlay(f"""
            <div style="background: linear-gradient(135deg, {color}, {color}dd);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin: 20px 0;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 10px; right: 10px; font-size: 3em; opacity: 0.2;">📊</div>
                <h3 style="margin: 0 0 20px 0; text-align: center; font-size: 1.8em; z-index: 2; position: relative;">
                    {category}
                </h3>
                <div style="background: rgba(255,255,255,0.1); 
                            border-radius: 15px;
                            overflow: hidden;
                            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                            z-index: 2;
                            position: relative;">
            """), unsafe_allow_html=True)
            
            # Membuat tabel dengan cara yang lebih sederhana
            for key, value in props.items():
                st.markdown(f"""
                <div style="display: flex; margin-bottom: 2px; background: rgba(255,255,255,0.9); border-radius: 8px; overflow: hidden;">
                    <div style="flex: 1; padding: 15px; font-weight: bold; background: rgba(255,255,255,0.95); color: #333; border-right: 2px solid rgba(255,255,255,0.5);">
                        {key}
                    </div>
                    <div style="flex: 2; padding: 15px; background: rgba(255,255,255,0.8); color: #333;">
                        {value}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(wrap_content_with_overlay("""
                </div>
            </div>
            """), unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    add_menu_background("keselamatan")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
                padding: 30px;
                border-radius: 25px;
                color: #333;
                text-align: center;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -20px; right: -20px; font-size: 8em; opacity: 0.1;">⚠️</div>
        <div style="font-size: 3em; margin-bottom: 15px;">⚠️</div>
        <h1 style="margin: 0; font-size: 2.5em; color: #333;">Panduan Keselamatan Gas</h1>
        <p style="margin: 15px 0 0 0; opacity: 0.8; font-size: 1.2em;">
            🛡️ Keselamatan Adalah Prioritas Utama dalam Bekerja dengan Gas
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Simbol Bahaya
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                padding: 30px;
                border-radius: 25px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🚧</div>
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px;">🚧</div>
            <h2 style="margin: 0; color: #333; font-size: 2em;">Simbol Bahaya Umum</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px;">
            <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 3em; opacity: 0.2;">🔥</div>
                <div style="font-size: 3em; margin-bottom: 15px;">🔥</div>
                <h3 style="margin: 0 0 15px 0; font-size: 1.5em;">Mudah Terbakar</h3>
                <div style="background: rgba(255,255,255,0.25); 
                            padding: 15px; 
                            border-radius: 15px;">
                    <p style="margin: 0 0 10px 0; font-weight: bold;"><b>Contoh:</b> Hidrogen, Metana</p>
                    <p style="margin: 5px 0;">• Jauhkan dari sumber api</p>
                    <p style="margin: 5px 0;">• Gunakan di area berventilasi</p>
                    <p style="margin: 5px 0;">• Hindari percikan listrik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #9b59b6 0%, #8e44ad 100%);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(155, 89, 182, 0.3);">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 3em; opacity: 0.2;">☠️</div>
                <div style="font-size: 3em; margin-bottom: 15px;">☠️</div>
                <h3 style="margin: 0 0 15px 0; font-size: 1.5em;">Beracun</h3>
                <div style="background: rgba(255,255,255,0.25); 
                            padding: 15px; 
                            border-radius: 15px;">
                    <p style="margin: 0 0 10px 0; font-weight: bold;"><b>Contoh:</b> Klorin, Amonia</p>
                    <p style="margin: 5px 0;">• Gunakan alat pelindung diri</p>
                    <p style="margin: 5px 0;">• Hindari inhalasi langsung</p>
                    <p style="margin: 5px 0;">• Ventilasi yang baik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        color: white;
                        position: relative;
                        overflow: hidden;
                        box-shadow: 0 8px 25px rgba(52, 152, 219, 0.3);">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 3em; opacity: 0.2;">💨</div>
                <div style="font-size: 3em; margin-bottom: 15px;">💨</div>
                <h3 style="margin: 0 0 15px 0; font-size: 1.5em;">Pengoksidasi</h3>
                <div style="background: rgba(255,255,255,0.25); 
                            padding: 15px; 
                            border-radius: 15px;">
                    <p style="margin: 0 0 10px 0; font-weight: bold;"><b>Contoh:</b> Oksigen, Fluorin</p>
                    <p style="margin: 5px 0;">• Hindari kontak dengan bahan organik</p>
                    <p style="margin: 5px 0;">• Simpan terpisah dari reduktor</p>
                    <p style="margin: 5px 0;">• Meningkatkan risiko kebakaran</p>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # APD
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                padding: 30px;
                border-radius: 25px;
                color: white;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🛡️</div>
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px;">🛡️</div>
            <h2 style="margin: 0; font-size: 2em;">Alat Pelindung Diri (APD)</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.25);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        transition: transform 0.3s ease;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">😷</div>
                <div style="font-size: 4em; margin-bottom: 15px;">😷</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Masker Gas</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 1em;">Melindungi dari inhalasi gas berbahaya</p>
            </div>
            <div style="background: rgba(255,255,255,0.25);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        transition: transform 0.3s ease;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🧤</div>
                <div style="font-size: 4em; margin-bottom: 15px;">🧤</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Sarung Tangan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 1em;">Melindungi tangan dari kontak langsung</p>
            </div>
            <div style="background: rgba(255,255,255,0.25);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        transition: transform 0.3s ease;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🥽</div>
                <div style="font-size: 4em; margin-bottom: 15px;">🥽</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Kacamata Keselamatan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 1em;">Melindungi mata dari percikan</p>
            </div>
            <div style="background: rgba(255,255,255,0.25);
                        padding: 25px;
                        border-radius: 20px;
                        text-align: center;
                        transition: transform 0.3s ease;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">🥼</div>
                <div style="font-size: 4em; margin-bottom: 15px;">🥼</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Jas Laboratorium</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 1em;">Melindungi tubuh dari kontaminasi</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

    # Prosedur Darurat
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
                padding: 30px;
                border-radius: 25px;
                margin-bottom: 30px;
                color: white;
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: 10px; right: 10px; font-size: 4em; opacity: 0.2;">🚨</div>
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 15px;">🚨</div>
            <h2 style="margin: 0; font-size: 2em;">Prosedur Darurat</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">1️⃣</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">1️⃣</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Evakuasi Segera</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;">Segera tinggalkan area jika terjadi kebocoran gas berbahaya</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">2️⃣</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">2️⃣</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Gunakan APD</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;">Selalu gunakan alat pelindung diri yang sesuai sebelum menangani gas</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">3️⃣</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">3️⃣</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Hindari Api</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;">Jauhkan dari sumber api, percikan listrik, dan benda panas</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">4️⃣</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">4️⃣</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Ventilasi Area</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;">Buka jendela dan pintu untuk sirkulasi udara yang baik</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">5️⃣</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">5️⃣</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Hubungi Petugas</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;">Segera hubungi petugas berwenang atau layanan darurat jika diperlukan</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 20px; 
                        border-radius: 20px;
                        position: relative;
                        overflow: hidden;">
                <div style="position: absolute; top: 5px; right: 5px; font-size: 2em; opacity: 0.2;">📞</div>
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                    <div style="font-size: 2em;">📞</div>
                    <h4 style="margin: 0; font-size: 1.3em;">Nomor Darurat</h4>
                </div>
                <p style="margin: 0; font-size: 1.1em;"><b>Pemadam Kebakaran:</b> 113<br><b>Ambulans:</b> 118<br><b>Polisi:</b> 110</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 25px;
            text-align: center;
            color: white;
            margin-top: 40px;
            position: relative;
            overflow: hidden;">
    <div style="position: absolute; top: -20px; right: -20px; font-size: 8em; opacity: 0.1;">⚗️</div>
    <div style="font-size: 3em; margin-bottom: 15px;">⚗️</div>
    <h3 style="margin: 0 0 10px 0; font-size: 2em;">ChemGasMaster</h3>
    <p style="margin: 0; opacity: 0.95; font-size: 1.1em;">© 2025 Kelompok 7 Kelas 1A | Platform Kimia Interaktif</p>
    <div style="margin-top: 20px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <span style="background: rgba(255,255,255,0.25); 
                     padding: 8px 16px; 
                     border-radius: 25px;
                     font-size: 1.1em;">
            🧪 Kalkulator Gas
        </span>
        <span style="background: rgba(255,255,255,0.25); 
                     padding: 8px 16px; 
                     border-radius: 25px;
                     font-size: 1.1em;">
            📚 Ensiklopedia
        </span>
        <span style="background: rgba(255,255,255,0.25); 
                     padding: 8px 16px; 
                     border-radius: 25px;
                     font-size: 1.1em;">
            ⚠️ Keselamatan
        </span>
    </div>
</div>
""", unsafe_allow_html=True)
