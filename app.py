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
# CSS CUSTOM + BACKGROUND SPEKTAKULER UNTUK SETIAP MENU
# ===========================================
st.markdown("""
<style>
    /* ========== ANIMASI UMUM ========== */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-30px) rotate(120deg); }
        66% { transform: translateY(15px) rotate(240deg); }
        100% { transform: translateY(0px) rotate(360deg); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
    }
    
    @keyframes wave {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100vw); }
    }
    
    @keyframes spiral {
        0% { transform: rotate(0deg) translateX(50px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(50px) rotate(-360deg); }
    }
    
    @keyframes aurora {
        0% { background-position: 0% 0%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 50% 100%; }
        75% { background-position: 0% 50%; }
        100% { background-position: 0% 0%; }
    }

    /* ========== BERANDA - TEMA MOLEKUL 3D & AURORA ========== */
    .beranda-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: 
            radial-gradient(circle at 20% 20%, rgba(120, 119, 241, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 90%, rgba(120, 241, 199, 0.3) 0%, transparent 50%),
            linear-gradient(45deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        animation: aurora 20s ease-in-out infinite;
        overflow: hidden;
    }
    
    .beranda-bg::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 100px 50px, rgba(255,255,255,0.8), transparent),
            radial-gradient(2px 2px at 200px 100px, rgba(0,255,255,0.6), transparent),
            radial-gradient(1px 1px at 300px 150px, rgba(255,0,255,0.7), transparent),
            radial-gradient(2px 2px at 150px 200px, rgba(255,255,0,0.5), transparent),
            radial-gradient(3px 3px at 250px 250px, rgba(255,100,100,0.8), transparent);
        background-size: 400px 400px;
        animation: float 15s ease-in-out infinite;
    }
    
    .molecule {
        position: absolute;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,0.9) 20%, rgba(100,200,255,0.6) 80%);
        box-shadow: 0 0 30px rgba(100,200,255,0.8);
        animation: spiral 25s linear infinite;
    }
    
    .molecule:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
    .molecule:nth-child(2) { top: 30%; left: 70%; animation-delay: 5s; }
    .molecule:nth-child(3) { top: 60%; left: 20%; animation-delay: 10s; }
    .molecule:nth-child(4) { top: 80%; left: 80%; animation-delay: 15s; }

    /* ========== KALKULATOR - TEMA LABORATORY BUBBLES ========== */
    .kalkulator-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: aurora 30s ease infinite;
        overflow: hidden;
    }
    
    .lab-bubble {
        position: absolute;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.8), rgba(100,200,255,0.3));
        box-shadow: inset 0 0 20px rgba(255,255,255,0.3), 0 0 20px rgba(100,200,255,0.4);
        animation: float 20s ease-in-out infinite;
    }
    
    .lab-bubble:nth-child(1) { width: 80px; height: 80px; top: 20%; left: 15%; animation-delay: 0s; }
    .lab-bubble:nth-child(2) { width: 120px; height: 120px; top: 60%; left: 75%; animation-delay: 4s; }
    .lab-bubble:nth-child(3) { width: 60px; height: 60px; top: 10%; left: 60%; animation-delay: 8s; }
    .lab-bubble:nth-child(4) { width: 100px; height: 100px; top: 70%; left: 30%; animation-delay: 12s; }
    .lab-bubble:nth-child(5) { width: 40px; height: 40px; top: 40%; left: 85%; animation-delay: 16s; }
    
    .formula-text {
        position: absolute;
        color: rgba(255,255,255,0.3);
        font-size: 2rem;
        font-weight: bold;
        animation: wave 15s linear infinite;
        white-space: nowrap;
    }
    
    .formula-text:nth-child(7) { top: 15%; content: 'PV=nRT'; animation-delay: 0s; }
    .formula-text:nth-child(8) { top: 45%; content: 'P₁V₁=P₂V₂'; animation-delay: 5s; }
    .formula-text:nth-child(9) { top: 75%; content: 'n=m/Mr'; animation-delay: 10s; }

    /* ========== ENSIKLOPEDIA - TEMA MAGICAL LIBRARY ========== */
    .ensiklopedia-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: 
            radial-gradient(circle at 0% 50%, rgba(255, 175, 189, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 100% 50%, rgba(255, 195, 113, 0.4) 0%, transparent 50%),
            linear-gradient(180deg, #2c1810 0%, #8b4513 50%, #daa520 100%);
        overflow: hidden;
    }
    
    .flying-book {
        position: absolute;
        width: 40px;
        height: 30px;
        background: linear-gradient(45deg, #8B4513, #DAA520);
        border-radius: 3px;
        box-shadow: 0 0 15px rgba(218, 165, 32, 0.6);
        animation: float 18s ease-in-out infinite;
    }
    
    .flying-book::before {
        content: '';
        position: absolute;
        top: 5px;
        left: 5px;
        right: 5px;
        bottom: 5px;
        background: linear-gradient(45deg, #F4A460, #FFE4B5);
        border-radius: 2px;
    }
    
    .flying-book:nth-child(1) { top: 20%; left: 10%; animation-delay: 0s; transform: rotate(15deg); }
    .flying-book:nth-child(2) { top: 50%; left: 70%; animation-delay: 6s; transform: rotate(-20deg); }
    .flying-book:nth-child(3) { top: 30%; left: 50%; animation-delay: 12s; transform: rotate(25deg); }
    .flying-book:nth-child(4) { top: 70%; left: 20%; animation-delay: 18s; transform: rotate(-15deg); }
    
    .magic-particle {
        position: absolute;
        width: 6px;
        height: 6px;
        background: gold;
        border-radius: 50%;
        box-shadow: 0 0 10px gold;
        animation: spiral 12s linear infinite;
    }
    
    .magic-particle:nth-child(6) { top: 25%; left: 30%; animation-delay: 0s; }
    .magic-particle:nth-child(7) { top: 55%; left: 60%; animation-delay: 4s; }
    .magic-particle:nth-child(8) { top: 75%; left: 80%; animation-delay: 8s; }

    /* ========== KESELAMATAN - TEMA DANGER ZONE ========== */
    .keselamatan-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: 
            linear-gradient(45deg, #ff0000 0%, #ff4500 25%, #ff6b00 50%, #ff8c00 75%, #ffa500 100%);
        background-size: 400% 400%;
        animation: aurora 25s ease infinite;
        overflow: hidden;
    }
    
    .danger-stripe {
        position: absolute;
        width: 100%;
        height: 20px;
        background: repeating-linear-gradient(
            45deg,
            rgba(255,255,0,0.8) 0px,
            rgba(255,255,0,0.8) 20px,
            rgba(255,0,0,0.8) 20px,
            rgba(255,0,0,0.8) 40px
        );
        animation: wave 8s linear infinite;
    }
    
    .danger-stripe:nth-child(1) { top: 15%; animation-delay: 0s; }
    .danger-stripe:nth-child(2) { top: 35%; animation-delay: 2s; }
    .danger-stripe:nth-child(3) { top: 55%; animation-delay: 4s; }
    .danger-stripe:nth-child(4) { top: 75%; animation-delay: 6s; }
    
    .warning-icon {
        position: absolute;
        font-size: 4rem;
        color: rgba(255,255,255,0.7);
        text-shadow: 0 0 20px rgba(255,255,0,0.8);
        animation: pulse 3s ease-in-out infinite;
    }
    
    .warning-icon:nth-child(6) { top: 20%; left: 20%; content: '⚠️'; animation-delay: 0s; }
    .warning-icon:nth-child(7) { top: 60%; left: 70%; content: '☢️'; animation-delay: 1s; }
    .warning-icon:nth-child(8) { top: 40%; left: 50%; content: '⚡'; animation-delay: 2s; }

    /* ========== EFEK TAMBAHAN ========== */
    .glowing-orb {
        position: absolute;
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        box-shadow: 0 0 100px rgba(255,255,255,0.2);
        animation: float 20s ease-in-out infinite;
        pointer-events: none;
    }
    
    .glowing-orb:nth-child(10) { top: 10%; left: 80%; animation-delay: 0s; }
    .glowing-orb:nth-child(11) { top: 70%; left: 10%; animation-delay: 10s; }

    /* ========== CSS YANG SUDAH ADA SEBELUMNYA (IMPROVED) ========== */
    .main-header {
        color: #0d47a1;
        border-bottom: 2px solid #0d47a1;
        padding-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        background: rgba(255,255,255,0.95);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .calc-card {
        background: linear-gradient(135deg, rgba(227, 242, 253, 0.95) 0%, rgba(187, 222, 251, 0.95) 100%) !important;
        border-left: 5px solid #2196f3;
        box-shadow: 0 8px 32px rgba(33, 150, 243, 0.2);
    }
    
    .result-card {
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.95) 0%, rgba(200, 230, 201, 0.95) 100%) !important;
        border-left: 5px solid #4caf50;
        box-shadow: 0 8px 32px rgba(76, 175, 80, 0.2);
    }
    
    .gas-card {
        background: linear-gradient(135deg, rgba(255, 243, 224, 0.95) 0%, rgba(255, 224, 178, 0.95) 100%) !important;
        border-left: 5px solid #ff9800;
        box-shadow: 0 8px 32px rgba(255, 152, 0, 0.2);
    }
    
    .safety-card {
        background: linear-gradient(135deg, rgba(255, 235, 238, 0.95) 0%, rgba(255, 205, 210, 0.95) 100%) !important;
        border-left: 5px solid #f44336;
        box-shadow: 0 8px 32px rgba(244, 67, 54, 0.2);
    }
    
    .conversion-box {
        background: linear-gradient(135deg, rgba(245, 245, 245, 0.9) 0%, rgba(230, 230, 230, 0.9) 100%);
        padding: 12px;
        border-radius: 10px;
        margin: 10px 0;
        border: 2px dashed #9e9e9e;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        background: rgba(255,255,255,0.95);
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .property-table th {
        background: linear-gradient(135deg, rgba(13, 71, 161, 0.9) 0%, rgba(25, 118, 210, 0.9) 100%);
        color: white;
        padding: 12px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    .property-table td {
        padding: 10px;
        border-bottom: 1px solid #e0e0e0;
        background: rgba(255,255,255,0.9);
    }
    
    /* ========== ENHANCED UI ELEMENTS ========== */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2) !important;
        border: none !important;
        border-radius: 25px !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 12px 40px rgba(0,0,0,0.25) !important;
        background: linear-gradient(45deg, #764ba2, #f093fb) !important;
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.9) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1) !important;
    }
    
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.9) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 10px !important;
        border: 2px solid rgba(0,0,0,0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #2196f3 !important;
        box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.2) !important;
    }
    
    /* ========== TAB STYLING ========== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background: rgba(255,255,255,0.1);
        padding: 10px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 25px;
        border-radius: 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        background: rgba(240, 242, 246, 0.8) !important;
        backdrop-filter: blur(10px);
        border: 2px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        background: rgba(255,255,255,0.9) !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2196F3, #21CBF3) !important;
        color: white !important;
        font-weight: bold;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.4);
        border-color: rgba(255,255,255,0.3);
    }
    
    /* ========== SIDEBAR ENHANCEMENT ========== */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255,255,255,0.2) !important;
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

# Fungsi untuk menerapkan background berdasarkan menu
def apply_background(menu_name):
    if menu_name == "🏠 Beranda":
        st.markdown("""
        <div class="beranda-bg">
            <div class="molecule"></div>
            <div class="molecule"></div>
            <div class="molecule"></div>
            <div class="molecule"></div>
            <div class="glowing-orb"></div>
            <div class="glowing-orb"></div>
        </div>
        """, unsafe_allow_html=True)
    elif menu_name == "🧮 Kalkulator Gas":
        st.markdown("""
        <div class="kalkulator-bg">
            <div class="lab-bubble"></div>
            <div class="lab-bubble"></div>
            <div class="lab-bubble"></div>
            <div class="lab-bubble"></div>
            <div class="lab-bubble"></div>
            <div class="formula-text" style="top: 15%;">PV=nRT</div>
            <div class="formula-text" style="top: 45%;">P₁V₁=P₂V₂</div>
            <div class="formula-text" style="top: 75%;">n=m/Mr</div>
        </div>
        """, unsafe_allow_html=True)
    elif menu_name == "📚 Ensiklopedia Gas":
        st.markdown("""
        <div class="ensiklopedia-bg">
            <div class="flying-book"></div>
            <div class="flying-book"></div>
            <div class="flying-book"></div>
            <div class="flying-book"></div>
            <div class="magic-particle"></div>
            <div class="magic-particle"></div>
            <div class="magic-particle"></div>
        </div>
        """, unsafe_allow_html=True)
    elif menu_name == "⚠️ Panduan Keselamatan":
        st.markdown("""
        <div class="keselamatan-bg">
            <div class="danger-stripe"></div>
            <div class="danger-stripe"></div>
            <div class="danger-stripe"></div>
            <div class="danger-stripe"></div>
            <div class="warning-icon" style="top: 20%; left: 20%;">⚠️</div>
            <div class="warning-icon" style="top: 60%; left: 70%;">☢️</div>
            <div class="warning-icon" style="top: 40%; left: 50%;">⚡</div>
        </div>
        """, unsafe_allow_html=True)

# Terapkan background sesuai menu yang dipilih
apply_background(menu)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>🌌 ChemGasMaster - Portal Molekul</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card calc-card">
        <h3>🎭 Selamat Datang di Dunia Molekul!</h3>
        <p>Jelajahi keajaiban gas ideal dalam dimensi yang spektakuler.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan penjelasan
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown("""
        <div style="margin-top:20px;">
            <h4>⚛️ Persamaan Gas Ideal:</h4>
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
            <h4>🌟 Fakta Menakjubkan:</h4>
            <p>🚀 <b>Gas Ideal</b> - Model matematis yang sempurna</p>
            <p>🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi</p>
            <p>🧪 <b>1 mol gas</b> = 6.022×10²³ molekul</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualisasi variabel dengan efek khusus
    st.markdown("<h4 style='margin-top:30px;'>🎨 Variabel Utama:</h4>", unsafe_allow_html=True)
    var_cols = st.columns(4)
    variables = [
        ("P", "Tekanan", "Gaya molekul<br>pada dinding", "linear-gradient(45deg, #ff6b6b, #ee5a24)"),
        ("V", "Volume", "Ruang yang<br>ditempati", "linear-gradient(45deg, #4ecdc4, #44bd87)"),
        ("n", "Jumlah Mol", "Banyaknya<br>partikel", "linear-gradient(45deg, #45b7d1, #96ceb4)"),
        ("T", "Suhu", "Energi kinetik<br>molekul", "linear-gradient(45deg, #feca57, #ff9ff3)")
    ]
    
    for col, (var, name, desc, gradient) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background:{gradient};
                       padding:20px;
                       border-radius:15px;
                       height:160px;
                       display:flex;
                       flex-direction:column;
                       justify-content:center;
                       align-items:center;
                       text-align:center;
                       color:white;
                       box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                       transform: perspective(1000px) rotateX(10deg);
                       transition: all 0.3s ease;">
                <h2 style="margin:5px 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{var}</h2>
                <p style="margin:5px 0;font-weight:bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{name}</p>
                <p style="margin:5px 0;font-size:0.85em; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "🧮 Kalkulator Gas":
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(13, 71, 161, 0.9), rgba(33, 150, 243, 0.9));
                 padding: 30px;
                 border-radius: 20px;
                 margin-bottom: 30px;
                 text-align: center;
                 box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
        <h1 style="color: white; margin: 0; font-size: 2.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            🧪 Laboratory Calculator 🔬
        </h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 1.1rem;">
            Advanced Gas Computation Engine
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Enhanced Tab System
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
            <div class="card" style="border-left: 5px solid #FF9800; box-shadow: 0 10px 30px rgba(255, 152, 0, 0.2);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 50px;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #FF9800; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Kalkulator Massa Gas</h2>
                        <div style="background: linear-gradient(45deg, #FFF3E0, #FFE0B2); 
                                   padding: 10px 15px; 
                                   border-radius: 10px; 
                                   display: inline-block;
                                   box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <b>Rumus:</b> Massa = n (mol) × Mr (g/mol)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            cols = st.columns(3)
            with cols[0]:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #FF9800;">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Contoh: Oksigen", label_visibility="collapsed")

            with cols[1]:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #FF9800;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f", label_visibility="collapsed")

            with cols[2]:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #FF9800;">Massa Molar (Mr)</div>', unsafe_allow_html=True)
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f", label_visibility="collapsed")
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("⚖️ Hitung Massa", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 20px;
                            border-left: 8px solid #FF9800;
                            box-shadow: 0 15px 35px rgba(255, 152, 0, 0.3);
                            animation: slideIn 0.6s ease-out;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #E65100; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 15px; flex-wrap: wrap;">
                                <p style="margin: 0; font-size: 1.3em; color: #333;">Massa <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #E65100; font-weight: bold; font-size: 2em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">{massa:.4f} gram</p>
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes slideIn {{
                        from {{ opacity: 0; transform: translateY(30px) scale(0.95); }}
                        to {{ opacity: 1; transform: translateY(0) scale(1); }}
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan dengan desain enhanced
        with st.container():
            st.markdown("""
            <div class="card" style="border-left: 5px solid #F44336; box-shadow: 0 10px 30px rgba(244, 67, 54, 0.2);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 50px;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; color: #F44336; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Kalkulator Tekanan Gas</h2>
                        <div style="background: linear-gradient(45deg, #FFEBEE, #FFCDD2); 
                                   padding: 10px 15px; 
                                   border-radius: 10px; 
                                   display: inline-block;
                                   box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <b>Rumus:</b> P = [n (mol) × R × T (K)] / V (L)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #F44336;">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen", label_visibility="collapsed")
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #F44336;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f", label_visibility="collapsed")
                
            with col2:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #F44336;">Suhu</div>', unsafe_allow_html=True)
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
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #F44336;">Volume</div>', unsafe_allow_html=True)
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
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 20px;
                            border-left: 8px solid #F44336;
                            box-shadow: 0 15px 35px rgba(244, 67, 54, 0.3);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #C62828; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 15px; flex-wrap: wrap;">
                                <p style="margin: 0; font-size: 1.3em; color: #333;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #C62828; font-weight: bold; font-size: 2em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">{P:.2f} atm</p>
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
            <div class="card" style="border-left: 5px solid #4CAF50; box-shadow: 0 10px 30px rgba(76, 175, 80, 0.2);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 50px;">🫙</div>
                    <div>
                        <h2 style="margin: 0; color: #4CAF50; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Kalkulator Volume Gas</h2>
                        <div style="background: linear-gradient(45deg, #E8F5E9, #C8E6C9); 
                                   padding: 10px 15px; 
                                   border-radius: 10px; 
                                   display: inline-block;
                                   box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <b>Rumus:</b> V = [n (mol) × R × T (K)] / P (atm)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #4CAF50;">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_volume", placeholder="Contoh: Hidrogen", label_visibility="collapsed")
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #4CAF50;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f", label_visibility="collapsed")
                
            with col2:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #4CAF50;">Suhu</div>', unsafe_allow_html=True)
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
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #4CAF50;">Tekanan</div>', unsafe_allow_html=True)
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
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 20px;
                            border-left: 8px solid #4CAF50;
                            box-shadow: 0 15px 35px rgba(76, 175, 80, 0.3);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">📦</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #2E7D32; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 15px; flex-wrap: wrap;">
                                <p style="margin: 0; font-size: 1.3em; color: #333;">Volume <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #2E7D32; font-weight: bold; font-size: 2em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">{V:.2f} L</p>
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
            <div class="card" style="border-left: 5px solid #9C27B0; box-shadow: 0 10px 30px rgba(156, 39, 176, 0.2);">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 50px;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #9C27B0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Kalkulator Jumlah Mol</h2>
                        <div style="background: linear-gradient(45deg, #F3E5F5, #E1BEE7); 
                                   padding: 10px 15px; 
                                   border
                                   padding: 10px 15px;
                                   border-radius: 10px;
                                   display: inline-block;
                                   box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                            <b>Rumus:</b> n = [P (atm) × V (L)] / [R × T (K)]
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #9C27B0;">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_mol", placeholder="Contoh: Karbon Dioksida", label_visibility="collapsed")
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #9C27B0;">Tekanan</div>', unsafe_allow_html=True)
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
                st.markdown('<div style="font-weight: bold; margin-bottom: 8px; color: #9C27B0;">Volume</div>', unsafe_allow_html=True)
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
                
                st.markdown('<div style="font-weight: bold; margin-top: 15px; margin-bottom: 8px; color: #9C27B0;">Suhu</div>', unsafe_allow_html=True)
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
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 20px;
                            border-left: 8px solid #9C27B0;
                            box-shadow: 0 15px 35px rgba(156, 39, 176, 0.3);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 40px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; color: #7B1FA2; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 15px; flex-wrap: wrap;">
                                <p style="margin: 0; font-size: 1.3em; color: #333;">Jumlah mol <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #7B1FA2; font-weight: bold; font-size: 2em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">{n:.2f} mol</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Enhanced footer untuk kalkulator
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(227, 242, 253, 0.95), rgba(187, 222, 251, 0.95));
                padding: 25px;
                border-radius: 20px;
                margin-top: 40px;
                border-left: 8px solid #2196F3;
                box-shadow: 0 15px 35px rgba(33, 150, 243, 0.2);">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 40px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">🧠</div>
            <div>
                <h3 style="margin: 0 0 15px 0; color: #0D47A1; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">Tips Ahli Kimia</h3>
                <p style="margin: 0; font-size: 1.1em; color: #333; line-height: 1.6;">
                    Untuk hasil terbaik, pastikan semua satuan konsisten dengan konstanta gas R 
                    (0.0821 L·atm/mol·K). Gunakan suhu dalam Kelvin dan tekanan dalam atm untuk akurasi maksimal.
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
    <div style="background: linear-gradient(135deg, rgba(139, 69, 19, 0.9), rgba(218, 165, 32, 0.9));
                 padding: 30px;
                 border-radius: 20px;
                 margin-bottom: 30px;
                 text-align: center;
                 box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
        <h1 style="color: white; margin: 0; font-size: 2.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            📚 Perpustakaan Molekul Ajaib ✨
        </h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 1.1rem;">
            Portal Pengetahuan Gas & Molekul
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "🔍 Pilih Gas untuk Dipelajari", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Enhanced Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <div class="card" style="border-left: 8px solid #DAA520; box-shadow: 0 15px 35px rgba(218, 165, 32, 0.2);">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="font-size: 50px; filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));">{gas['icon']}</div>
                <h2 style="margin: 0; color: #B8860B; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{selected_gas}</h2>
            </div>
            <p style="font-style: italic; font-size: 1.1em; color: #333; line-height: 1.6; margin-bottom: 15px;">{gas['description']}</p>
            <div style="display: flex; gap: 30px; flex-wrap: wrap;">
                <p style="margin: 5px 0;"><b style="color: #B8860B;">Kategori:</b> <span style="background: #FFF8DC; padding: 4px 8px; border-radius: 5px;">{gas['category']}</span></p>
                <p style="margin: 5px 0;"><b style="color: #B8860B;">Aplikasi:</b> {gas['aplikasi']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["image"], width=220, caption=f"Struktur {selected_gas}")
    
    # Enhanced Tab Informasi
    tabs = st.tabs(list(gas["properties"].keys()))
    
    for tab, (category, props) in zip(tabs, gas["properties"].items()):
        with tab:
            st.markdown(f"""
            <div class="card" style="border-left: 8px solid #DAA520; box-shadow: 0 15px 35px rgba(218, 165, 32, 0.1);">
                <h3 style="color: #B8860B; margin-bottom: 20px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{category}</h3>
                <table class="property-table" style="border-radius: 15px; overflow: hidden;">
                    {"".join(f'<tr><td style="background: linear-gradient(45deg, #FFF8DC, #F5F5DC); font-weight: bold; color: #8B4513; border-right: 2px solid #DAA520;"><b>{key}</b></td><td style="background: rgba(255,255,255,0.95); color: #333;">{value}</td></tr>' for key, value in props.items())}
                </table>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(255, 0, 0, 0.9), rgba(255, 140, 0, 0.9));
                 padding: 30px;
                 border-radius: 20px;
                 margin-bottom: 30px;
                 text-align: center;
                 box-shadow: 0 15px 35px rgba(255, 0, 0, 0.3);
                 border: 3px solid rgba(255, 255, 0, 0.8);">
        <h1 style="color: white; margin: 0; font-size: 2.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
            ⚠️ ZONA KESELAMATAN MAKSIMUM 🚨
        </h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            Protokol Keamanan Laboratorium
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card" style="border-left: 8px solid #FF0000; box-shadow: 0 15px 35px rgba(255, 0, 0, 0.2);">
        <h3 style="color: #CC0000; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); margin-bottom: 20px;">🚧 Simbol Bahaya Kritikal</h3>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap:20px; margin-top:20px;">
            <div style="background: linear-gradient(45deg, #ffebee, #ffcdd2); 
                       padding:20px; 
                       border-radius:15px; 
                       border-left: 5px solid #f44336;
                       box-shadow: 0 8px 25px rgba(244, 67, 54, 0.2);">
                <h4 style="color: #d32f2f; margin-bottom: 10px;">🔥 Mudah Terbakar</h4>
                <p><b>Contoh:</b> Hidrogen, Metana</p>
                <p>• Jauhkan dari sumber api</p>
                <p>• Gunakan di area berventilasi</p>
                <p>• Simpan dalam wadah anti-statis</p>
            </div>
            <div style="background: linear-gradient(45deg, #fff8e1, #ffecb3); 
                       padding:20px; 
                       border-radius:15px; 
                       border-left: 5px solid #ff9800;
                       box-shadow: 0 8px 25px rgba(255, 152, 0, 0.2);">
                <h4 style="color: #f57c00; margin-bottom: 10px;">☠️ Beracun</h4>
                <p><b>Contoh:</b> Klorin, Amonia</p>
                <p>• Gunakan alat pelindung diri</p>
                <p>• Hindari inhalasi langsung</p>
                <p>• Ventilasi wajib aktif</p>
            </div>
            <div style="background: linear-gradient(45deg, #e8f5e9, #c8e6c9); 
                       padding:20px; 
                       border-radius:15px; 
                       border-left: 5px solid #4caf50;
                       box-shadow: 0 8px 25px rgba(76, 175, 80, 0.2);">
                <h4 style="color: #388e3c; margin-bottom: 10px;">💨 Pengoksidasi</h4>
                <p><b>Contoh:</b> Oksigen, Fluorin</p>
                <p>• Hindari kontak dengan organik</p>
                <p>• Simpan terpisah dari reduktor</p>
                <p>• Monitor suhu penyimpanan</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card" style="border-left: 8px solid #FF4500; box-shadow: 0 15px 35px rgba(255, 69, 0, 0.2);">
        <h3 style="color: #CC0000; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); margin-bottom: 20px;">🛡️ Arsenal Pelindung Diri (APD)</h3>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:20px; margin-top:20px;">
            <div style="text-align:center; 
                       background: linear-gradient(45deg, #f3e5f5, #e1bee7); 
                       padding:25px; 
                       border-radius:15px;
                       box-shadow: 0 8px 25px rgba(156, 39, 176, 0.2);
                       transition: transform 0.3s ease;">
                <img src="https://cdn-icons-png.flaticon.com/512/2090/2090004.png" width="80" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
                <p style="font-weight: bold; margin-top: 15px; color: #7b1fa2;">Masker Gas</p>
                <p style="font-size: 0.9em; color: #666;">Proteksi Respiratori</p>
            </div>
            <div style="text-align:center; 
                       background: linear-gradient(45deg, #e3f2fd, #bbdefb); 
                       padding:25px; 
                       border-radius:15px;
                       box-shadow: 0 8px 25px rgba(33, 150, 243, 0.2);
                       transition: transform 0.3s ease;">
                <img src="https://cdn-icons-png.flaticon.com/512/2797/2797688.png" width="80" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
                <p style="font-weight: bold; margin-top: 15px; color: #1976d2;">Sarung Tangan</p>
                <p style="font-size: 0.9em; color: #666;">Proteksi Tangan</p>
            </div>
            <div style="text-align:center; 
                       background: linear-gradient(45deg, #e8f5e9, #c8e6c9); 
                       padding:25px; 
                       border-radius:15px;
                       box-shadow: 0 8px 25px rgba(76, 175, 80, 0.2);
                       transition: transform 0.3s ease;">
                <img src="https://cdn-icons-png.flaticon.com/512/10984/10984307.png" width="80" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
                <p style="font-weight: bold; margin-top: 15px; color: #388e3c;">Kacamata Safety</p>
                <p style="font-size: 0.9em; color: #666;">Proteksi Mata</p>
            </div>
            <div style="text-align:center; 
                       background: linear-gradient(45deg, #fff3e0, #ffe0b2); 
                       padding:25px; 
                       border-radius:15px;
                       box-shadow: 0 8px 25px rgba(255, 152, 0, 0.2);
                       transition: transform 0.3s ease;">
                <img src="https://cdn-icons-png.flaticon.com/512/3000/3000504.png" width="80" style="filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));">
                <p style="font-weight: bold; margin-top: 15px; color: #f57c00;">Jas Lab</p>
                <p style="font-size: 0.9em; color: #666;">Proteksi Tubuh</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card safety-card" style="border-left: 8px solid #DC143C; box-shadow: 0 15px 35px rgba(220, 20, 60, 0.2);">
        <h3 style="color: #CC0000; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); margin-bottom: 20px;">🚨 Protokol Darurat Maksimum</h3>
        <div style="background: linear-gradient(45deg, #ffebee, #ffcdd2); 
                   padding: 20px; 
                   border-radius: 15px; 
                   border: 3px dashed #f44336;
                   margin-top: 15px;">
            <ol style="font-size: 1.1em; line-height: 2; color: #333;">
                <li><b style="color: #d32f2f;">EVAKUASI SEGERA</b> - Tinggalkan area jika terjadi kebocoran gas</li>
                <li><b style="color: #d32f2f;">APD WAJIB</b> - Gunakan perlengkapan pelindung sebelum menangani</li>
                <li><b style="color: #d32f2f;">NO SPARK ZONE</b> - Hindari sumber api atau percikan listrik</li>
                <li><b style="color: #d32f2f;">VENTILASI AKTIF</b> - Buka semua jalur udara dan pintu darurat</li>
                <li><b style="color: #d32f2f;">KONTAK EMERGENCY</b> - Hubungi petugas berwenang SEGERA</li>
                <li><b style="color: #d32f2f;">DEKONTAMINASI</b> - Bersihkan area dengan prosedur standar</li>
            </ol>
        </div>
        
        <div style="background: linear-gradient(45deg, #fff8e1, #ffecb3); 
                   padding: 15px; 
                   border-radius: 10px; 
                   margin-top: 20px;
                   border-left: 5px solid #ff9800;">
            <p style="margin: 0; font-weight: bold; color: #e65100; text-align: center;">
                ⚠️ INGAT: Keselamatan adalah prioritas utama dalam setiap eksperimen kimia! ⚠️
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER ENHANCED
# ===========================================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(50, 50, 50, 0.9), rgba(80, 80, 80, 0.9));
           color: white;
           text-align: center;
           padding: 30px;
           border-radius: 15px;
           margin-top: 40px;
           box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
    <div style="display: flex; align-items: center; justify-content: center; gap: 15px; margin-bottom: 15px;">
        <div style="font-size: 30px;">⚗️</div>
        <h3 style="margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">ChemGasMaster</h3>
        <div style="font-size: 30px;">🧪</div>
    </div>
    <p style="margin: 0; font-size: 1.1em; opacity: 0.9;">
        © 2025 ChemGasMaster - Advanced Gas Analysis Platform
    </p>
    <p style="margin: 5px 0 0 0; opacity: 0.7;">
        Kelompok 7 Kelas 1A | Powered by Streamlit & Science
    </p>
</div>
""", unsafe_allow_html=True)
