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
# CSS CUSTOM DENGAN WARNA LEBIH MENARIK
# ===========================================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        margin-bottom: 20px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3); }
        to { box-shadow: 0 12px 40px rgba(102, 126, 234, 0.5); }
    }
    
    .card {
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57);
        background-size: 300% 100%;
        animation: rainbow 3s ease infinite;
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .calc-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    .result-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
    }
    
    .gas-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        color: white;
        border: none;
    }
    
    .safety-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white;
        border: none;
    }
    
    .info-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        color: #333;
        border: none;
    }
    
    .success-card {
        background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
        color: #333;
        border: none;
    }
    
    .warning-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        color: #333;
        border: none;
    }
    
    .conversion-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 15px 0;
        border: 2px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .property-table th {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        font-weight: bold;
        text-align: left;
    }
    
    .property-table td {
        padding: 12px 15px;
        border-bottom: 1px solid #eee;
        background: white;
        transition: background 0.3s ease;
    }
    
    .property-table tr:hover td {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f4fd 100%);
    }
    
    .input-row {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    
    .input-label {
        min-width: 140px;
        font-weight: bold;
        color: #333;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .input-field {
        flex-grow: 1;
    }
    
    .input-unit {
        min-width: 120px;
    }
    
    .gas-icon {
        font-size: 28px;
        margin-right: 15px;
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
    }
    
    /* Animasi untuk sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Button styling yang lebih menarik */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f4fd 100%);
        border: 2px solid #667eea;
        border-radius: 15px;
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f4fd 100%);
        border: 2px solid #667eea;
        border-radius: 15px;
        color: #333;
        font-weight: bold;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f4fd 100%);
        border: 2px solid #667eea;
        border-radius: 15px;
        color: #333;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# CSS BACKGROUND ANIMASI YANG LEBIH BERWARNA
# ===========================================
st.markdown("""
<style>
    /* Background Super Colorful untuk Beranda */
    .beranda-bg {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4, #feca57, #ff9ff3, #54a0ff);
        background-size: 400% 400%;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.15;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .beranda-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(255, 107, 107, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(78, 205, 196, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(69, 183, 209, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 60% 80%, rgba(150, 206, 180, 0.4) 0%, transparent 50%),
            radial-gradient(circle at 90% 60%, rgba(254, 202, 87, 0.4) 0%, transparent 50%);
        animation: float-molecules 15s ease-in-out infinite;
    }
    
    @keyframes float-molecules {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.4; }
        25% { transform: translateY(-30px) rotate(90deg); opacity: 0.7; }
        50% { transform: translateY(-10px) rotate(180deg); opacity: 0.5; }
        75% { transform: translateY(-20px) rotate(270deg); opacity: 0.8; }
    }

    /* Background Rainbow untuk Kalkulator Gas */
    .kalkulator-bg {
        background: linear-gradient(45deg, #ff9a9e, #fecfef, #fecfef, #a8edea, #fed6e3, #d299c2, #fef9d7);
        background-size: 400% 400%;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.12;
        animation: rainbowShift 10s ease infinite;
    }
    
    @keyframes rainbowShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .kalkulator-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            repeating-linear-gradient(45deg, 
                rgba(255,107,107,0.1) 0px, 
                rgba(255,107,107,0.1) 20px, 
                rgba(78,205,196,0.1) 20px, 
                rgba(78,205,196,0.1) 40px,
                rgba(69,183,209,0.1) 40px,
                rgba(69,183,209,0.1) 60px,
                rgba(150,206,180,0.1) 60px,
                rgba(150,206,180,0.1) 80px),
            repeating-linear-gradient(-45deg, 
                rgba(254,202,87,0.1) 0px, 
                rgba(254,202,87,0.1) 25px, 
                rgba(255,159,243,0.1) 25px, 
                rgba(255,159,243,0.1) 50px);
        animation: slide-rainbow 25s linear infinite;
    }
    
    @keyframes slide-rainbow {
        0% { transform: translateX(0) translateY(0); }
        100% { transform: translateX(80px) translateY(80px); }
    }

    /* Background Galaxy untuk Ensiklopedia */
    .ensiklopedia-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        background-size: 300% 300%;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.1;
        animation: galaxyMove 12s ease infinite;
    }
    
    @keyframes galaxyMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .ensiklopedia-bg::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.3) 2px, transparent 2px),
            radial-gradient(circle at 75% 75%, rgba(255,107,107,0.2) 1px, transparent 1px),
            radial-gradient(circle at 50% 50%, rgba(78,205,196,0.2) 3px, transparent 3px),
            radial-gradient(circle at 10% 90%, rgba(69,183,209,0.3) 2px, transparent 2px),
            radial-gradient(circle at 90% 10%, rgba(254,202,87,0.2) 1px, transparent 1px);
        background-size: 80px 80px, 120px 120px, 160px 160px, 100px 100px, 140px 140px;
        animation: twinkle-rainbow 10s ease-in-out infinite;
    }
    
    @keyframes twinkle-rainbow {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        25% { opacity: 0.8; transform: scale(1.1); }
        50% { opacity: 0.5; transform: scale(0.9); }
        75% { opacity: 0.9; transform: scale(1.05); }
    }

    /* Background Fire untuk Panduan Keselamatan */
    .keselamatan-bg {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 25%, #ff9ff3 50%, #54a0ff 75%, #5f27cd 100%);
        background-size: 400% 400%;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.08;
        animation: fireMove 6s ease infinite;
    }
    
    @keyframes fireMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .keselamatan-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            linear-gradient(45deg, rgba(255,107,107,0.15) 25%, transparent 25%),
            linear-gradient(-45deg, rgba(254,202,87,0.15) 25%, transparent 25%),
            linear-gradient(45deg, transparent 75%, rgba(255,159,243,0.15) 75%),
            linear-gradient(-45deg, transparent 75%, rgba(84,160,255,0.15) 75%),
            repeating-linear-gradient(90deg, 
                rgba(95,39,205,0.1) 0px, 
                rgba(95,39,205,0.1) 10px, 
                transparent 10px, 
                transparent 20px);
        background-size: 40px 40px, 40px 40px, 40px 40px, 40px 40px, 80px 80px;
        background-position: 0 0, 0 20px, 20px -20px, -20px 0px, 0 0;
        animation: warning-rainbow 5s linear infinite;
    }
    
    @keyframes warning-rainbow {
        0% { 
            background-position: 0 0, 0 20px, 20px -20px, -20px 0px, 0 0;
            filter: hue-rotate(0deg);
        }
        50% { 
            background-position: 40px 40px, 40px 60px, 60px 20px, 20px 40px, 80px 80px;
            filter: hue-rotate(180deg);
        }
        100% { 
            background-position: 0 0, 0 20px, 20px -20px, -20px 0px, 0 0;
            filter: hue-rotate(360deg);
        }
    }

    /* Overlay dengan efek glass morphism */
    .content-overlay {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .content-overlay:hover {
        background: rgba(255, 255, 255, 0.35);
        transform: translateY(-2px);
        box-shadow: 
            0 12px 40px rgba(0, 0, 0, 0.15),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }

    /* Partikel rainbow mengambang */
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle-element {
        position: absolute;
        width: 6px;
        height: 6px;
        border-radius: 50%;
        animation: float-up-rainbow 20s infinite linear;
    }
    
    .particle-element:nth-child(1) { background: #ff6b6b; }
    .particle-element:nth-child(2) { background: #4ecdc4; }
    .particle-element:nth-child(3) { background: #45b7d1; }
    .particle-element:nth-child(4) { background: #96ceb4; }
    .particle-element:nth-child(5) { background: #feca57; }
    .particle-element:nth-child(6) { background: #ff9ff3; }
    .particle-element:nth-child(7) { background: #54a0ff; }
    .particle-element:nth-child(8) { background: #5f27cd; }
    .particle-element:nth-child(9) { background: #00d2d3; }
    .particle-element:nth-child(10) { background: #ff9f43; }
    
    @keyframes float-up-rainbow {
        0% {
            transform: translateY(100vh) rotate(0deg) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
            transform: translateY(90vh) rotate(36deg) scale(1);
        }
        90% {
            opacity: 1;
            transform: translateY(-10vh) rotate(324deg) scale(1);
        }
        100% {
            transform: translateY(-20vh) rotate(360deg) scale(0);
            opacity: 0;
        }
    }

    /* Efek hover yang lebih colorful */
    .stSelectbox:hover > div > div,
    .stNumberInput:hover > div > div > input,
    .stTextInput:hover > div > div > input {
        border-color: #ff6b6b;
        box-shadow: 0 0 20px rgba(255, 107, 107, 0.3);
        transform: scale(1.02);
    }

    /* Responsif untuk mobile dengan warna yang tetap menarik */
    @media (max-width: 768px) {
        .beranda-bg, .kalkulator-bg, .ensiklopedia-bg, .keselamatan-bg {
            opacity: 0.05;
        }
        .content-overlay {
            background: rgba(255, 255, 255, 0.9);
            margin: 8px 0;
            padding: 20px;
        }
        .card {
            padding: 20px;
            margin-bottom: 20px;
        }
    }
    
    /* Animasi loading yang colorful */
    @keyframes colorfulSpin {
        0% { 
            transform: rotate(0deg);
            filter: hue-rotate(0deg);
        }
        100% { 
            transform: rotate(360deg);
            filter: hue-rotate(360deg);
        }
    }
    
    .loading-spinner {
        animation: colorfulSpin 2s linear infinite;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi untuk menambahkan background sesuai menu
def add_menu_background(menu_type):
    if menu_type == "beranda":
        st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
        # Tambahkan partikel rainbow mengambang
        particles_html = """
        <div class="floating-particles">
            <div class="particle-element" style="left: 10%; animation-delay: 0s;"></div>
            <div class="particle-element" style="left: 15%; animation-delay: 1s;"></div>
            <div class="particle-element" style="left: 25%; animation-delay: 2s;"></div>
            <div class="particle-element" style="left: 35%; animation-delay: 3s;"></div>
            <div class="particle-element" style="left: 45%; animation-delay: 4s;"></div>
            <div class="particle-element" style="left: 55%; animation-delay: 5s;"></div>
            <div class="particle-element" style="left: 65%; animation-delay: 6s;"></div>
            <div class="particle-element" style="left: 75%; animation-delay: 7s;"></div>
            <div class="particle-element" style="left: 85%; animation-delay: 8s;"></div>
            <div class="particle-element" style="left: 95%; animation-delay: 9s;"></div>
        </div>
        """
        st.markdown(particles_html, unsafe_allow_html=True)
        
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
# MENU SIDEBAR DENGAN WARNA MENARIK
# ===========================================
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; 
                border-radius: 15px; 
                text-align: center; 
                margin-bottom: 20px;
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);">
        <h1 style="color: white; margin: 0; font-size: 2em;">⚗️ ChemGasMaster ✨</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 5px 0 0 0;">Platform Kimia Interaktif</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu dengan styling yang lebih colorful
    menu_options = ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
    menu = st.radio(
        "🌈 MENU UTAMA",
        menu_options,
        index=0
    )
    
    st.markdown("---")
    
    # Info box yang lebih colorful
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                padding: 20px;
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 8px 25px rgba(250, 112, 154, 0.3);
                margin-bottom: 20px;">
        <div style="font-size: 2em; margin-bottom: 10px;">🧪</div>
        <small><b>ℹ️ Info Penting</b><br>
        Menggunakan persamaan gas ideal:<br>
        <b>PV = nRT</b><br>
        (R = 0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun facts box
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                padding: 15px;
                border-radius: 15px;
                color: white;
                text-align: center;
                box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);">
        <div style="font-size: 1.5em; margin-bottom: 8px;">🎯</div>
        <small><b>Fakta Menarik!</b><br>
        1 mol gas = 6.022×10²³ molekul<br>
        Gas ideal hanya ada dalam teori! 🤓</small>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    add_menu_background("beranda")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; padding: 30px;">
        <h1 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;
                   background-clip: text;
                   font-size: 3.5em;
                   margin-bottom: 20px;
                   animation: glow 2s ease-in-out infinite alternate;">
            ⚗️ ChemGasMaster ✨
        </h1>
        <p style="font-size: 1.3em; color: #666; margin-bottom: 30px;">
            🌈 Platform Interaktif untuk Eksplorasi Dunia Gas Ideal! 🚀
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Welcome card dengan gradient rainbow
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
                margin-bottom: 30px;">
        <div style="font-size: 3em; margin-bottom: 15px;">🎉</div>
        <h2 style="margin: 0 0 15px 0;">Selamat Datang di ChemGasMaster!</h2>
        <p style="font-size: 1.1em; margin: 0; opacity: 0.9;">
            Jelajahi dunia gas ideal dengan kalkulator canggih, ensiklopedia lengkap, 
            dan panduan keselamatan yang komprehensif! 🧪✨
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan styling menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; margin: 30px 0;">
        <h3 style="color: #667eea; margin-bottom: 20px;">🔬 Persamaan Gas Ideal</h3>
    </div>
    """), unsafe_allow_html=True)
    
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                    padding: 25px;
                    border-radius: 15px;
                    color: #333;">
            <h4 style="color: #667eea; margin-bottom: 20px;">📊 Variabel Persamaan:</h4>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    <b style="color: #ff6b6b;">P</b> = Tekanan (atm) 🎚️
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    <b style="color: #4ecdc4;">V</b> = Volume (L) 📦
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    <b style="color: #45b7d1;">n</b> = Jumlah mol (mol) 🧪
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    <b style="color: #96ceb4;">R</b> = Konstanta gas = 0.0821 L·atm/mol·K ⚖️
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    <b style="color: #feca57;">T</b> = Suhu (K) 🌡️
                </p>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                    padding: 25px;
                    border-radius: 15px;
                    color: #333;">
            <h4 style="color: #ff6b6b; margin-bottom: 20px;">🎯 Fakta Menarik:</h4>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    🎚️ <b>Gas Ideal</b> - Hanya model matematis sempurna!
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    🧪 <b>1 mol gas</b> = 6.022×10²³ molekul
                </p>
                <p style="margin: 0; padding: 8px; background: rgba(255,255,255,0.7); border-radius: 8px;">
                    🚀 <b>STP</b> - 0°C, 1 atm, 22.4 L/mol
                </p>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    # Visualisasi variabel dengan warna rainbow
    st.markdown(wrap_content_with_overlay("<h4 style='text-align: center; color: #667eea; margin: 40px 0 30px 0;'>🌈 Visualisasi Variabel Gas Ideal</h4>"), unsafe_allow_html=True)
    
    var_cols = st.columns(5)
    variables = [
        ("P", "Tekanan", "Gaya gas pada<br>dinding wadah", "linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%)"),
        ("V", "Volume", "Ruang yang<br>ditempati gas", "linear-gradient(135deg, #4ecdc4 0%, #7ed6cc 100%)"),
        ("n", "Jumlah Mol", "Banyaknya<br>partikel gas", "linear-gradient(135deg, #45b7d1 0%, #73c5da 100%)"),
        ("R", "Konstanta", "Tetapan gas<br>universal", "linear-gradient(135deg, #96ceb4 0%, #aad6c4 100%)"),
        ("T", "Suhu", "Energi kinetik<br>rata-rata", "linear-gradient(135deg, #feca57 0%, #fed976 100%)")
    ]
    
    for col, (var, name, desc, gradient) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background: {gradient};
                        padding: 20px;
                        border-radius: 15px;
                        height: 180px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        color: white;
                        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                        transition: transform 0.3s ease;
                        cursor: pointer;">
                <h2 style="margin: 8px 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{var}</h2>
                <p style="margin: 5px 0; font-weight: bold; font-size: 1.1em;">{name}</p>
                <p style="margin: 5px 0; font-size: 0.85em; opacity: 0.9;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Aplikasi dengan card berwarna
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-top: 40px;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 10px;">💡</div>
            <h3 style="margin: 0;">Aplikasi Persamaan Gas Ideal</h3>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <div style="font-size: 2em; margin-bottom: 10px;">🧪</div>
                <h4 style="margin: 0 0 10px 0;">Reaksi Kimia</h4>
                <p style="margin: 0; opacity: 0.9;">Menghitung volume gas yang dihasilkan dalam reaksi</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <div style="font-size: 2em; margin-bottom: 10px;">🌡️</div>
                <h4 style="margin: 0 0 10px 0;">Sistem Tertutup</h4>
                <p style="margin: 0; opacity: 0.9;">Memahami perilaku gas dalam wadah tertutup</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <div style="font-size: 2em; margin-bottom: 10px;">📊</div>
                <h4 style="margin: 0 0 10px 0;">Prediksi Tekanan</h4>
                <p style="margin: 0; opacity: 0.9;">Memprediksi pengaruh suhu terhadap tekanan</p>
            </div>
            <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);">
                <div style="font-size: 2em; margin-bottom: 10px;">⚙️</div>
                <h4 style="margin: 0 0 10px 0;">Sistem Pneumatik</h4>
                <p style="margin: 0; opacity: 0.9;">Mendesain sistem pneumatik dan hidrolik</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # Tips penggunaan dengan warna menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-top: 30px;
                box-shadow: 0 15px 35px rgba(250, 112, 154, 0.4);">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 10px;">🔧</div>
            <h3 style="margin: 0;">Tips Menggunakan ChemGasMaster</h3>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.8em; margin-bottom: 8px;">🧮</div>
                <p style="margin: 0; font-weight: bold;">Kalkulator Gas</p>
                <small style="opacity: 0.9;">Untuk perhitungan cepat</small>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.8em; margin-bottom: 8px;">📚</div>
                <p style="margin: 0; font-weight: bold;">Ensiklopedia</p>
                <small style="opacity: 0.9;">Informasi detail gas</small>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.8em; margin-bottom: 8px;">⚠️</div>
                <p style="margin: 0; font-weight: bold;">Keselamatan</p>
                <small style="opacity: 0.9;">Panduan penting</small>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.8em; margin-bottom: 8px;">⚖️</div>
                <p style="margin: 0; font-weight: bold;">Satuan Konsisten</p>
                <small style="opacity: 0.9;">Pastikan satuan sesuai</small>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    add_menu_background("kalkulator")
    
    # Header dengan animasi rainbow
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                 padding: 30px;
                 border-radius: 20px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);">
        <h1 style="color: white; text-align: center; margin: 0; z-index: 2; position: relative; font-size: 2.5em;">
              🧪✨ Kalkulator Gas Ideal Super Canggih ✨⚗️
        </h1>
        <p style="color: rgba(255,255,255,0.9); text-align: center; margin: 10px 0 0 0; font-size: 1.2em;">
            🌈 Hitung dengan Presisi Tinggi & Tampilan Menarik! 🚀
        </p>
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1;">
            <div class="particle" style="--size: 4px; --duration: 12s; --delay: 0s; --x: 15%; --y: 25%"></div>
            <div class="particle" style="--size: 6px; --duration: 15s; --delay: 1s; --x: 75%; --y: 15%"></div>
            <div class="particle" style="--size: 5px; --duration: 18s; --delay: 2s; --x: 45%; --y: 65%"></div>
            <div class="particle" style="--size: 3px; --duration: 20s; --delay: 3s; --x: 85%; --y: 75%"></div>
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
            background: rgba(255,255,255,0.7);
            border-radius: 50%;
            animation: float var(--duration) var(--delay) infinite linear;
            --x-end: calc(var(--x) - 50%);
            --y-end: calc(var(--y) - 50%);
        }
    </style>
    """), unsafe_allow_html=True)

    # Style untuk tabs yang lebih colorful
    tab_style = """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 15px;
            background: linear-gradient(135deg, #f8f9ff 0%, #e8f4fd 100%);
            padding: 10px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .stTabs [data-baseweb="tab"] {
            height: 60px;
            padding: 0 25px;
            border-radius: 15px;
            transition: all 0.3s ease;
            background: linear-gradient(135deg, #ffffff 0%, #f0f2f6 100%) !important;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%) !important;
            color: white !important;
            font-weight: bold;
            box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
            transform: translateY(-2px);
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
        # Kalkulator Massa dengan warna menarik
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.3);">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3.5em;">🧪</div>
                    <div>
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Massa Gas</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 12px 18px; 
                                    border-radius: 12px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    backdrop-filter: blur(10px);">
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
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            box-shadow: 0 10px 30px rgba(79, 172, 254, 0.4);
                            animation: fadeIn 0.5s ease-in-out;">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 15px; 
                                        border-radius: 12px;
                                        backdrop-filter: blur(10px);">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Massa <b style="color: #feca57;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #feca57;">
                                        {massa:.4f} gram
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes fadeIn {{
                        from {{ opacity: 0; transform: translateY(20px); }}
                        to {{ opacity: 1; transform: translateY(0); }}
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan dengan warna menarik
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3.5em;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Tekanan Gas</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 12px 18px; 
                                    border-radius: 12px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    backdrop-filter: blur(10px);">
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
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">🧪 Jumlah Mol (n)</div>', unsafe_allow_html=True)
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
                    <div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">📦 Volume</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    V_input = st.number_input("Volume", min_value=0.0, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(78, 205, 196, 0.3);">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
        
            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            box-shadow: 0 10px 30px rgba(250, 112, 154, 0.4);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 15px; 
                                        border-radius: 12px;
                                        backdrop-filter: blur(10px);">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Tekanan <b style="color: #feca57;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #feca57;">
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
        # Kalkulator Volume dengan warna menarik
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: #333;
                        margin-bottom: 25px;
                        box-shadow: 0 10px 30px rgba(168, 237, 234, 0.4);">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3.5em;">🫙</div>
                    <div>
                        <h2 style="margin: 0; font-size: 2em; color: #667eea;">Kalkulator Volume Gas</h2>
                        <div style="background: rgba(102, 126, 234, 0.1); 
                                    padding: 12px 18px; 
                                    border-radius: 12px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    border: 2px solid rgba(102, 126, 234, 0.3);">
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
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">🧪 Jumlah Mol (n)</div>', unsafe_allow_html=True)
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
                    <div style="background: linear-gradient(135deg, #96ceb4 0%, #ffeaa7 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(150, 206, 180, 0.3);">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
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
                    <div style="background: linear-gradient(135deg, #96ceb4 0%, #ffeaa7 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(150, 206, 180, 0.3);">
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
        
            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 15px; 
                                        border-radius: 12px;
                                        backdrop-filter: blur(10px);">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Volume <b style="color: #feca57;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #feca57;">
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
        # Kalkulator Mol dengan warna menarik
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #ff9ff3 0%, #54a0ff 100%);
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin-bottom: 25px;
                        box-shadow: 0 10px 30px rgba(255, 159, 243, 0.4);">
                <div style="display: flex; align-items: center; gap: 20px;">
                    <div style="font-size: 3.5em;">🧪</div>
                    <div>
                        <h2 style="margin: 0; font-size: 2em;">Kalkulator Jumlah Mol</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 12px 18px; 
                                    border-radius: 12px; 
                                    display: inline-block;
                                    margin-top: 10px;
                                    backdrop-filter: blur(10px);">
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
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
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
                    <div style="background: linear-gradient(135deg, #5f27cd 0%, #00d2d3 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(95, 39, 205, 0.3);">
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
                    <div style="background: linear-gradient(135deg, #5f27cd 0%, #00d2d3 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(95, 39, 205, 0.3);">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #5f27cd 0%, #00d2d3 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(95, 39, 205, 0.3);">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
                st.markdown('<div class="input-label" style="margin-top: 20px;">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="mol_suhu_input", label_visibility="collapsed")
                with col2d:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="mol_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #5f27cd 0%, #00d2d3 100%);
                                color: white;
                                padding: 12px;
                                border-radius: 10px;
                                margin: 10px 0;
                                text-align: center;
                                box-shadow: 0 4px 15px rgba(95, 39, 205, 0.3);">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
        
            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #ff9f43 0%, #ee5a24 100%);
                            padding: 25px;
                            border-radius: 20px;
                            margin-top: 25px;
                            color: white;
                            box-shadow: 0 10px 30px rgba(255, 159, 67, 0.4);">
                    <div style="display: flex; align-items: center; gap: 20px;">
                        <div style="font-size: 3em;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 15px; 
                                        border-radius: 12px;
                                        backdrop-filter: blur(10px);">
                                <p style="margin: 0; font-size: 1.3em;">
                                    Jumlah mol <b style="color: #feca57;">{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.5em; font-weight: bold; color: #feca57;">
                                        {n:.2f} mol
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah dengan warna menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 20px;
                margin-top: 40px;
                color: white;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="font-size: 3em;">💡</div>
            <div>
                <h3 style="margin: 0 0 15px 0; font-size: 1.8em;">🎓 Tips Ahli Kimia</h3>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 15px;
                            backdrop-filter: blur(10px);">
                    <p style="margin: 0; font-size: 1.1em; line-height: 1.6;">
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
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    add_menu_background("ensiklopedia")
    
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
                margin-bottom: 30px;">
        <div style="font-size: 3.5em; margin-bottom: 15px;">📚</div>
        <h1 style="margin: 0; font-size: 2.5em;">Ensiklopedia Gas Interaktif</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.2em; opacity: 0.9;">
            🌟 Jelajahi Dunia Gas dengan Informasi Lengkap & Menarik! 🚀
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Selectbox dengan styling menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 25px;
                text-align: center;">
        <h3 style="margin: 0 0 15px 0; color: #333; font-size: 1.5em;">🔍 Pilih Gas untuk Dipelajari</h3>
    </div>
    """), unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}",
        label_visibility="collapsed"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas dengan design menarik
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
                    padding: 25px;
                    border-radius: 20px;
                    color: white;
                    box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4);">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div style="font-size: 3em;">{gas['icon']}</div>
                <h2 style="margin: 0; font-size: 2.2em;">{selected_gas}</h2>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 15px; 
                        border-radius: 12px;
                        backdrop-filter: blur(10px);
                        margin-bottom: 15px;">
                <p style="margin: 0; font-size: 1.1em; font-style: italic;">
                    {gas['description']}
                </p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 12px; 
                            border-radius: 10px;
                            backdrop-filter: blur(5px);">
                    <p style="margin: 0;"><b>📂 Kategori:</b> {gas['category']}</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 12px; 
                            border-radius: 10px;
                            backdrop-filter: blur(5px);">
                    <p style="margin: 0;"><b>🔧 Aplikasi:</b> {gas['aplikasi']}</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with col2:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                    padding: 20px;
                    border-radius: 20px;
                    text-align: center;
                    box-shadow: 0 10px 30px rgba(79, 172, 254, 0.4);">
            <img src="{gas['image']}" 
                 style="width: 100%; 
                        max-width: 200px; 
                        border-radius: 15px; 
                        box-shadow: 0 8px 25px rgba(0,0,0,0.2);">
            <p style="color: white; margin: 15px 0 0 0; font-weight: bold;">
                🖼️ Struktur Molekul
            </p>
        </div>
        """), unsafe_allow_html=True)
    
    # Tab Informasi dengan styling colorful
    st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 15px;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        }
        .stTabs [data-baseweb="tab"] {
            height: 55px;
            padding: 0 25px;
            border-radius: 15px;
            transition: all 0.3s ease;
            background: rgba(255,255,255,0.2) !important;
            color: white !important;
            font-weight: bold;
            backdrop-filter: blur(10px);
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-2px);
            background: rgba(255,255,255,0.3) !important;
            box-shadow: 0 5px 15px rgba(255,255,255,0.2);
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%) !important;
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 107, 107, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(list(gas["properties"].keys()))
    
    colors = [
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
    ]
    
    for i, (tab, (category, props)) in enumerate(zip(tabs, gas["properties"].items())):
        with tab:
            color = colors[i % len(colors)]
            
            # Membuat tabel HTML dengan cara yang lebih aman
            table_rows = ""
            for key, value in props.items():
                table_rows += f"""
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.2);">
                    <td style="padding: 15px; font-weight: bold; background: rgba(255,255,255,0.1); width: 40%;">
                        {key}
                    </td>
                    <td style="padding: 15px; background: rgba(255,255,255,0.05);">
                        {value}
                    </td>
                </tr>
                """
            
            st.markdown(wrap_content_with_overlay(f"""
            <div style="background: {color};
                        padding: 25px;
                        border-radius: 20px;
                        color: white;
                        margin: 20px 0;
                        box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                <h3 style="margin: 0 0 20px 0; text-align: center; font-size: 1.8em;">
                    {category}
                </h3>
                <div style="background: rgba(255,255,255,0.1); 
                            border-radius: 15px; 
                            overflow: hidden;
                            backdrop-filter: blur(10px);">
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
    <div style="background: linear-gradient(135deg, #ff6b6b 0%, #feca57 50%, #ff9ff3 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                text-align: center;
                box-shadow: 0 15px 35px rgba(255, 107, 107, 0.4);
                margin-bottom: 30px;">
        <div style="font-size: 3.5em; margin-bottom: 15px;">⚠️</div>
        <h1 style="margin: 0; font-size: 2.5em;">Panduan Keselamatan Gas</h1>
        <p style="margin: 10px 0 0 0; font-size: 1.2em; opacity: 0.9;">
            🛡️ Keselamatan Adalah Prioritas Utama dalam Bekerja dengan Gas! 🚨
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Simbol Bahaya dengan design menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-bottom: 30px;
                box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 10px;">🚧</div>
            <h2 style="margin: 0; font-size: 2em;">Simbol Bahaya Umum</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.3);">
                <div style="font-size: 3em; margin-bottom: 15px;">🔥</div>
                <h3 style="margin: 0 0 15px 0;">Mudah Terbakar</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 15px; 
                            border-radius: 10px;
                            backdrop-filter: blur(10px);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Hidrogen, Metana</p>
                    <p style="margin: 5px 0;">• Jauhkan dari sumber api</p>
                    <p style="margin: 5px 0;">• Gunakan di area berventilasi</p>
                    <p style="margin: 5px 0;">• Hindari percikan listrik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #5f27cd 0%, #341f97 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        box-shadow: 0 8px 25px rgba(95, 39, 205, 0.3);">
                <div style="font-size: 3em; margin-bottom: 15px;">☠️</div>
                <h3 style="margin: 0 0 15px 0;">Beracun</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 15px; 
                            border-radius: 10px;
                            backdrop-filter: blur(10px);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Klorin, Amonia</p>
                    <p style="margin: 5px 0;">• Gunakan alat pelindung diri</p>
                    <p style="margin: 5px 0;">• Hindari inhalasi langsung</p>
                    <p style="margin: 5px 0;">• Ventilasi yang baik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #00d2d3 0%, #54a0ff 100%);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        box-shadow: 0 8px 25px rgba(0, 210, 211, 0.3);">
                <div style="font-size: 3em; margin-bottom: 15px;">💨</div>
                <h3 style="margin: 0 0 15px 0;">Pengoksidasi</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 15px; 
                            border-radius: 10px;
                            backdrop-filter: blur(10px);">
                    <p style="margin: 0 0 10px 0;"><b>Contoh:</b> Oksigen, Fluorin</p>
                    <p style="margin: 5px 0;">• Hindari kontak dengan bahan organik</p>
                    <p style="margin: 5px 0;">• Simpan terpisah dari reduktor</p>
                    <p style="margin: 5px 0;">• Meningkatkan risiko kebakaran</p>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # APD dengan design menarik
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-bottom: 30px;
                box-shadow: 0 15px 35px rgba(79, 172, 254, 0.4);">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 10px;">🛡️</div>
            <h2 style="margin: 0; font-size: 2em;">Alat Pelindung Diri (APD)</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
            <div style="background: rgba(255,255,255,0.2);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        backdrop-filter: blur(10px);
                        transition: transform 0.3s ease;">
                <div style="font-size: 4em; margin-bottom: 15px;">😷</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Masker Gas</h4>
                <p style="margin: 0; opacity: 0.9;">Melindungi dari inhalasi gas berbahaya</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        backdrop-filter: blur(10px);
                        transition: transform 0.3s ease;">
                <div style="font-size: 4em; margin-bottom: 15px;">🧤</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Sarung Tangan</h4>
                <p style="margin: 0; opacity: 0.9;">Melindungi tangan dari kontak langsung</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        backdrop-filter: blur(10px);
                        transition: transform 0.3s ease;">
                <div style="font-size: 4em; margin-bottom: 15px;">🥽</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Kacamata Keselamatan</h4>
                <p style="margin: 0; opacity: 0.9;">Melindungi mata dari percikan</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 25px;
                        border-radius: 15px;
                        text-align: center;
                        backdrop-filter: blur(10px);
                        transition: transform 0.3s ease;">
                <div style="font-size: 4em; margin-bottom: 15px;">🥼</div>
                <h4 style="margin: 0 0 10px 0; font-size: 1.3em;">Jas Laboratorium</h4>
                <p style="margin: 0; opacity: 0.9;">Melindungi tubuh dari kontaminasi</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

    # Prosedur Darurat
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                padding: 30px;
                border-radius: 20px;
                color: white;
                margin-bottom: 30px;
                box-shadow: 0 15px 35px rgba(250, 112, 154, 0.4);">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 3em; margin-bottom: 10px;">🚨</div>
            <h2 style="margin: 0; font-size: 2em;">Prosedur Darurat</h2>
        </div>
        <div style="background: rgba(255,255,255,0.2); 
                    padding: 25px; 
                    border-radius: 15px;
                    backdrop-filter: blur(10px);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">1️⃣</div>
                        <h4 style="margin: 0;">Evakuasi Segera</h4>
                    </div>
                    <p style="margin: 0;">Segera tinggalkan area jika terjadi kebocoran gas berbahaya</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">2️⃣</div>
                        <h4 style="margin: 0;">Gunakan APD</h4>
                    </div>
                    <p style="margin: 0;">Selalu gunakan alat pelindung diri yang sesuai sebelum menangani gas</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">3️⃣</div>
                        <h4 style="margin: 0;">Hindari Api</h4>
                    </div>
                    <p style="margin: 0;">Jauhkan dari sumber api, percikan listrik, dan benda panas</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">4️⃣</div>
                        <h4 style="margin: 0;">Ventilasi Area</h4>
                    </div>
                    <p style="margin: 0;">Buka jendela dan pintu untuk sirkulasi udara yang baik</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">5️⃣</div>
                        <h4 style="margin: 0;">Hubungi Petugas</h4>
                    </div>
                    <p style="margin: 0;">Segera hubungi petugas berwenang atau layanan darurat jika diperlukan</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 20px; 
                            border-radius: 12px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                        <div style="font-size: 2em;">📞</div>
                        <h4 style="margin: 0;">Nomor Darurat</h4>
                    </div>
                    <p style="margin: 0;"><b>Pemadam Kebakaran:</b> 113<br><b>Ambulans:</b> 118<br><b>Polisi:</b> 110</p>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# FOOTER DENGAN WARNA MENARIK
# ===========================================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-top: 40px;
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);">
    <div style="font-size: 2.5em; margin-bottom: 15px;">⚗️</div>
    <h3 style="margin: 0 0 10px 0;">ChemGasMaster</h3>
    <p style="margin: 0; opacity: 0.9;">© 2025 Kelompok 7 Kelas 1A | Platform Kimia Interaktif</p>
    <div style="margin-top: 15px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 8px 15px; 
                     border-radius: 20px;
                     backdrop-filter: blur(10px);">
            🧪 Kalkulator Gas
        </span>
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 8px 15px; 
                     border-radius: 20px;
                     backdrop-filter: blur(10px);">
            📚 Ensiklopedia
        </span>
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 8px 15px; 
                     border-radius: 20px;
                     backdrop-filter: blur(10px);">
            ⚠️ Keselamatan
        </span>
    </div>
</div>
""", unsafe_allow_html=True)
