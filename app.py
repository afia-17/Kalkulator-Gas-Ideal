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
# CSS CUSTOM + BACKGROUND DRAMATIS UNTUK SETIAP MENU
# ===========================================
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* Animasi Kompleks */
    @keyframes matrix-rain {
        0% { transform: translateY(-100vh); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    
    @keyframes neon-pulse {
        0%, 100% { 
            text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 15px #00ff00, 0 0 20px #00ff00;
            box-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 15px #00ff00;
        }
        50% { 
            text-shadow: 0 0 2px #00ff00, 0 0 5px #00ff00, 0 0 8px #00ff00, 0 0 12px #00ff00;
            box-shadow: 0 0 2px #00ff00, 0 0 5px #00ff00, 0 0 8px #00ff00;
        }
    }
    
    @keyframes fire-flicker {
        0%, 100% { 
            background: radial-gradient(circle, #ff4500 0%, #ff6347 30%, #ff0000 60%, #8b0000 100%);
            transform: scale(1) rotate(0deg);
        }
        25% { 
            background: radial-gradient(circle, #ff6347 0%, #ff4500 30%, #dc143c 60%, #8b0000 100%);
            transform: scale(1.05) rotate(1deg);
        }
        50% { 
            background: radial-gradient(circle, #ff0000 0%, #ff4500 30%, #b22222 60%, #8b0000 100%);
            transform: scale(0.95) rotate(-1deg);
        }
        75% { 
            background: radial-gradient(circle, #ff4500 0%, #dc143c 30%, #ff0000 60%, #8b0000 100%);
            transform: scale(1.02) rotate(0.5deg);
        }
    }
    
    @keyframes electric-spark {
        0% { opacity: 0; transform: scale(0) rotate(0deg); }
        50% { opacity: 1; transform: scale(1) rotate(180deg); }
        100% { opacity: 0; transform: scale(0) rotate(360deg); }
    }
    
    @keyframes cosmic-drift {
        0% { transform: translateX(-100vw) translateY(50vh) rotate(0deg); }
        100% { transform: translateX(100vw) translateY(-50vh) rotate(360deg); }
    }
    
    @keyframes toxic-bubble {
        0% { 
            transform: translateY(100vh) scale(0.1);
            background: radial-gradient(circle, #32cd32 0%, #228b22 50%, #006400 100%);
        }
        50% { 
            background: radial-gradient(circle, #7fff00 0%, #32cd32 50%, #228b22 100%);
        }
        100% { 
            transform: translateY(-100vh) scale(1.5);
            background: radial-gradient(circle, #adff2f 0%, #7fff00 50%, #32cd32 100%);
        }
    }

    /* BACKGROUND BERANDA - TEMA CYBER MATRIX */
    .beranda-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, #000000, #001100, #002200, #000000);
        z-index: -1;
        overflow: hidden;
    }
    
    .beranda-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            repeating-linear-gradient(0deg, transparent, transparent 2px, #00ff00 2px, #00ff00 4px),
            repeating-linear-gradient(90deg, transparent, transparent 2px, #00ff00 2px, #00ff00 4px);
        opacity: 0.1;
        animation: neon-pulse 3s infinite;
    }
    
    .matrix-code {
        position: absolute;
        color: #00ff00;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        animation: matrix-rain 8s linear infinite;
        text-shadow: 0 0 10px #00ff00;
    }

    /* BACKGROUND KALKULATOR - TEMA LABORATORIUM FUTURISTIK */
    .kalkulator-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 20%, #0066cc 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, #004499 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, #0088ff 0%, transparent 50%),
            linear-gradient(135deg, #001122, #003366, #001144);
        z-index: -1;
        overflow: hidden;
    }
    
    .electric-grid {
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0,150,255,0.3) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,150,255,0.3) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: electric-spark 2s infinite;
    }
    
    .floating-formula {
        position: absolute;
        color: #00aaff;
        font-family: 'Orbitron', monospace;
        font-size: 18px;
        text-shadow: 0 0 15px #00aaff;
        animation: cosmic-drift 15s linear infinite;
    }

    /* BACKGROUND ENSIKLOPEDIA - TEMA HUTAN KIMIA MISTIS */
    .ensiklopedia-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(ellipse at top, #2d5016 0%, #1a3009 50%, #0d1804 100%),
            radial-gradient(ellipse at bottom, #4a7c59 0%, #2d5016 50%, #1a3009 100%);
        z-index: -1;
        overflow: hidden;
    }
    
    .toxic-particles {
        position: absolute;
        width: 100%;
        height: 100%;
    }
    
    .toxic-bubble {
        position: absolute;
        border-radius: 50%;
        animation: toxic-bubble 12s infinite linear;
        box-shadow: 0 0 20px rgba(50, 205, 50, 0.5);
    }
    
    .mystical-symbols {
        position: absolute;
        color: #32cd32;
        font-size: 24px;
        text-shadow: 0 0 20px #32cd32;
        animation: cosmic-drift 20s linear infinite;
        opacity: 0.7;
    }

    /* BACKGROUND KESELAMATAN - TEMA APOCALYPSE FIRE */
    .keselamatan-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 30% 70%, #ff4500 0%, transparent 50%),
            radial-gradient(circle at 70% 30%, #dc143c 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, #8b0000 0%, transparent 70%),
            linear-gradient(45deg, #2f1b14, #8b0000, #2f1b14);
        z-index: -1;
        overflow: hidden;
        animation: fire-flicker 4s infinite;
    }
    
    .danger-warnings {
        position: absolute;
        width: 100%;
        height: 100%;
    }
    
    .warning-symbol {
        position: absolute;
        color: #ff4500;
        font-size: 30px;
        text-shadow: 0 0 25px #ff4500;
        animation: electric-spark 3s infinite;
    }
    
    .fire-particles {
        position: absolute;
        width: 4px;
        height: 4px;
        background: radial-gradient(circle, #ff4500, #ff0000);
        border-radius: 50%;
        animation: toxic-bubble 8s infinite linear;
        box-shadow: 0 0 15px #ff4500;
    }

    /* Efek Khusus untuk Setiap Menu */
    .cyber-text {
        font-family: 'Orbitron', monospace !important;
        color: #00ff00 !important;
        text-shadow: 0 0 10px #00ff00 !important;
        background: rgba(0, 0, 0, 0.8) !important;
        border: 2px solid #00ff00 !important;
        border-radius: 10px !important;
        animation: neon-pulse 2s infinite !important;
    }
    
    .lab-text {
        font-family: 'Orbitron', monospace !important;
        color: #00aaff !important;
        text-shadow: 0 0 15px #00aaff !important;
        background: rgba(0, 20, 40, 0.9) !important;
        border: 2px solid #00aaff !important;
        border-radius: 15px !important;
        box-shadow: 0 0 20px rgba(0, 170, 255, 0.3) !important;
    }
    
    .nature-text {
        font-family: 'Orbitron', monospace !important;
        color: #32cd32 !important;
        text-shadow: 0 0 20px #32cd32 !important;
        background: rgba(20, 40, 20, 0.9) !important;
        border: 2px solid #32cd32 !important;
        border-radius: 15px !important;
        box-shadow: 0 0 25px rgba(50, 205, 50, 0.4) !important;
    }
    
    .danger-text {
        font-family: 'Orbitron', monospace !important;
        color: #ff4500 !important;
        text-shadow: 0 0 25px #ff4500 !important;
        background: rgba(40, 20, 10, 0.9) !important;
        border: 2px solid #ff4500 !important;
        border-radius: 15px !important;
        box-shadow: 0 0 30px rgba(255, 69, 0, 0.5) !important;
        animation: fire-flicker 3s infinite !important;
    }

    /* CSS yang sudah ada sebelumnya dengan modifikasi */
    .main-header {
        color: #ffffff;
        border-bottom: 3px solid currentColor;
        padding: 20px;
        text-shadow: 0 0 20px currentColor;
        border-radius: 15px;
        margin-bottom: 30px;
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        backdrop-filter: blur(10px);
    }
    
    .card {
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .calc-card {
        background: rgba(0, 50, 100, 0.8) !important;
        border: 2px solid #00aaff !important;
        box-shadow: 0 0 30px rgba(0, 170, 255, 0.3) !important;
    }
    
    .result-card {
        background: rgba(20, 60, 20, 0.8) !important;
        border: 2px solid #32cd32 !important;
        box-shadow: 0 0 30px rgba(50, 205, 50, 0.3) !important;
    }
    
    .gas-card {
        background: rgba(30, 60, 30, 0.8) !important;
        border: 2px solid #32cd32 !important;
        box-shadow: 0 0 30px rgba(50, 205, 50, 0.3) !important;
    }
    
    .safety-card {
        background: rgba(60, 30, 20, 0.8) !important;
        border: 2px solid #ff4500 !important;
        box-shadow: 0 0 30px rgba(255, 69, 0, 0.3) !important;
    }
    
    /* Sidebar dengan efek futuristik */
    .css-1d391kg {
        background: rgba(0, 0, 0, 0.8) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 2px solid #00ff00 !important;
    }
    
    /* Tombol dengan efek dramatis */
    .stButton > button {
        background: linear-gradient(45deg, #ff4500, #ff6347) !important;
        border: 2px solid #ff4500 !important;
        border-radius: 25px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 20px rgba(255, 69, 0, 0.5) !important;
        color: white !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 0 40px rgba(255, 69, 0, 0.8) !important;
        animation: neon-pulse 1s infinite !important;
    }
</style>
""", unsafe_allow_html=True)

# Tambahkan floating particles
# st.markdown("""
# <div class="floating-particles">
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
#     <div class="particle"></div>
# </div>
# """, unsafe_allow_html=True)

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

# Fungsi untuk menerapkan background dan efek khusus berdasarkan menu
def apply_background_and_effects(menu_name):
    if menu_name == "🏠 Beranda":
        # Matrix Cyber Background
        st.markdown("""
        <div class="beranda-bg">
            <div class="matrix-code" style="left: 10%; animation-delay: 0s;">01001000 01100101 01101100 01101100 01101111</div>
            <div class="matrix-code" style="left: 30%; animation-delay: 1s;">PV = nRT</div>
            <div class="matrix-code" style="left: 50%; animation-delay: 2s;">11000011 10101010 01010101</div>
            <div class="matrix-code" style="left: 70%; animation-delay: 3s;">CHEMISTRY.EXE</div>
            <div class="matrix-code" style="left: 90%; animation-delay: 4s;">10110010 11001100</div>
        </div>
        """, unsafe_allow_html=True)
        return "cyber-text"
        
    elif menu_name == "🧮 Kalkulator Gas":
        # Futuristic Lab Background
        st.markdown("""
        <div class="kalkulator-bg">
            <div class="electric-grid"></div>
            <div class="floating-formula" style="top: 20%; left: 10%; animation-delay: 0s;">P = nRT/V</div>
            <div class="floating-formula" style="top: 40%; left: 80%; animation-delay: 3s;">V = nRT/P</div>
            <div class="floating-formula" style="top: 60%; left: 20%; animation-delay: 6s;">n = PV/RT</div>
            <div class="floating-formula" style="top: 80%; left: 70%; animation-delay: 9s;">T = PV/nR</div>
        </div>
        """, unsafe_allow_html=True)
        return "lab-text"
        
    elif menu_name == "📚 Ensiklopedia Gas":
        # Mystical Forest Background
        st.markdown("""
        <div class="ensiklopedia-bg">
            <div class="toxic-particles">
                <div class="toxic-bubble" style="left: 10%; width: 20px; height: 20px; animation-delay: 0s;"></div>
                <div class="toxic-bubble" style="left: 30%; width: 15px; height: 15px; animation-delay: 2s;"></div>
                <div class="toxic-bubble" style="left: 50%; width: 25px; height: 25px; animation-delay: 4s;"></div>
                <div class="toxic-bubble" style="left: 70%; width: 18px; height: 18px; animation-delay: 6s;"></div>
                <div class="toxic-bubble" style="left: 90%; width: 22px; height: 22px; animation-delay: 8s;"></div>
            </div>
            <div class="mystical-symbols" style="top: 20%; left: 15%; animation-delay: 0s;">⚛️</div>
            <div class="mystical-symbols" style="top: 40%; left: 75%; animation-delay: 5s;">🧬</div>
            <div class="mystical-symbols" style="top: 60%; left: 25%; animation-delay: 10s;">🔬</div>
            <div class="mystical-symbols" style="top: 80%; left: 85%; animation-delay: 15s;">⚗️</div>
        </div>
        """, unsafe_allow_html=True)
        return "nature-text"
        
    elif menu_name == "⚠️ Panduan Keselamatan":
        # Apocalypse Fire Background
        st.markdown("""
        <div class="keselamatan-bg">
            <div class="danger-warnings">
                <div class="warning-symbol" style="top: 15%; left: 20%; animation-delay: 0s;">⚠️</div>
                <div class="warning-symbol" style="top: 35%; left: 70%; animation-delay: 1s;">☠️</div>
                <div class="warning-symbol" style="top: 55%; left: 30%; animation-delay: 2s;">🔥</div>
                <div class="warning-symbol" style="top: 75%; left: 80%; animation-delay: 3s;">💀</div>
                <div class="fire-particles" style="left: 10%; animation-delay: 0s;"></div>
                <div class="fire-particles" style="left: 25%; animation-delay: 1s;"></div>
                <div class="fire-particles" style="left: 40%; animation-delay: 2s;"></div>
                <div class="fire-particles" style="left: 55%; animation-delay: 3s;"></div>
                <div class="fire-particles" style="left: 70%; animation-delay: 4s;"></div>
                <div class="fire-particles" style="left: 85%; animation-delay: 5s;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        return "danger-text"

# Terapkan background dan dapatkan kelas CSS yang sesuai
text_class = apply_background_and_effects(menu)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    st.markdown(f"<h1 class='main-header {text_class}'>⚗️ CHEMGASMASTER SYSTEM v2.0 ⚗️</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card {text_class}">
        <h3>🔋 SISTEM ANALISIS GAS TERINTEGRASI</h3>
        <p>Platform cyber untuk komputasi molekular dan database kimia digital.</p>
        <p><strong>STATUS:</strong> <span style="color: #00ff00;">ONLINE</span> | <strong>VERSION:</strong> 2.0.1</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan styling cyber
    st.markdown(f"""
    <div class="card {text_class}" style="text-align: center;">
        <h2 style="color: #00ff00; font-family: 'Orbitron', monospace;">PERSAMAAN INTI SISTEM</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown(f"""
        <div class="card {text_class}">
            <h4>📊 PARAMETER SISTEM:</h4>
            <p><b>P</b> = Tekanan Molekular (atm)</p>
            <p><b>V</b> = Volume Kontainer (L)</p>
            <p><b>n</b> = Kuantitas Mol (mol)</p>
            <p><b>R</b> = Konstanta Universal = 0.0821 L·atm/mol·K</p>
            <p><b>T</b> = Temperatur Absolut (K)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(f"""
        <div class="card {text_class}">
            <h4>🧠 DATA INTELIJEN:</h4>
            <p>🔬 <b>Gas Ideal</b> - Model teoretis sempurna</p>
            <p>🌡️ <b>Kondisi Optimal</b> - P rendah & T tinggi</p>
            <p>⚛️ <b>1 mol</b> = 6.022×10²³ entitas</p>
            <p>🚀 <b>Aplikasi</b> - Teknologi masa depan</p>
        </div>
        """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    st.markdown(f"""
    <div class="card {text_class}" style="text-align: center; margin-bottom: 30px;">
        <h1 style="font-family: 'Orbitron', monospace; font-weight: 900;">
            ⚡ QUANTUM GAS CALCULATOR ⚡
        </h1>
        <p style="font-size: 1.2em;">Sistem Komputasi Molekular Tingkat Lanjut</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "⚖️ MASSA ANALYZER", 
        "🎚️ PRESSURE SCANNER",
        "🫙 VOLUME DETECTOR",
        "🧪 MOL COUNTER"
    ])
    
    R = 0.0821  # Konstanta gas ideal

    with tab1:
        st.markdown(f"""
        <div class="card {text_class}">
            <h2>⚖️ SISTEM ANALISIS MASSA MOLEKULAR</h2>
            <p><strong>FORMULA:</strong> Massa = n (mol) × Mr (g/mol)</p>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)
        with cols[0]:
            nama = st.text_input("🏷️ Identifikasi Gas", key="nama_massa", placeholder="Contoh: Oksigen")
        with cols[1]:
            n = st.number_input("🧪 Kuantitas Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f")
        with cols[2]:
            mr = st.number_input("⚛️ Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f")

        if st.button("⚖️ EXECUTE MASS CALCULATION", key="btn_massa", use_container_width=True, type="primary"):
            massa = n * mr
            st.markdown(f"""
            <div class="card {text_class}" style="border: 3px solid #00aaff; animation: neon-pulse 2s infinite;">
                <h3>📊 HASIL KOMPUTASI MASSA</h3>
                <p style="font-size: 1.5em;"><strong>Massa {nama if nama else 'gas'} = {massa:.4f} gram</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

    with tab2:
        st.markdown(f"""
        <div class="card {text_class}">
            <h2>🎚️ SISTEM SCANNER TEKANAN</h2>
            <p><strong>FORMULA:</strong> P = [n × R × T] / V</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("🏷️ Identifikasi Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen")
            n = st.number_input("🧪 Kuantitas Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f")
            
        with col2:
            col2a, col2b = st.columns([3,1])
            with col2a:
                T_input = st.number_input("🌡️ Temperatur", min_value=-273.0, key="tekanan_suhu_input")
            with col2b:
                satuan = st.selectbox("Unit", ["K", "°C"], key="tekanan_suhu_unit")
            
            if satuan == "°C":
                T = T_input + 273.15
                st.info(f"🔄 Konversi: {T_input}°C = {T:.2f} K")
            else:
                T = T_input
            
            col2c, col2d = st.columns([3,1])
            with col2c:
                V_input = st.number_input("📦 Volume", min_value=0.0, key="tekanan_vol_input")
            with col2d:
                satuan_vol = st.selectbox("Unit", ["L", "m³", "mL"], key="tekanan_vol_unit")
            
            if satuan_vol == "m³":
                V = V_input * 1000
                st.info(f"🔄 Konversi: {V_input} m³ = {V:.4f} L")
            elif satuan_vol == "mL":
                V = V_input / 1000
                st.info(f"🔄 Konversi: {V_input} mL = {V:.4f} L")
            else:
                V = V_input

        if st.button("🎚️ EXECUTE PRESSURE SCAN", key="btn_tekanan", use_container_width=True, type="primary"):
            P = (n * R * T) / V
            st.markdown(f"""
            <div class="card {text_class}" style="border: 3px solid #00aaff; animation: neon-pulse 2s infinite;">
                <h3>📊 HASIL SCANNER TEKANAN</h3>
                <p style="font-size: 1.5em;"><strong>Tekanan {nama if nama else 'gas'} = {P:.2f} atm</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

    with tab3:
        st.markdown(f"""
        <div class="card {text_class}">
            <h2>🫙 SISTEM DETEKSI VOLUME</h2>
            <p><strong>FORMULA:</strong> V = [n × R × T] / P</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("🏷️ Identifikasi Gas", key="nama_volume", placeholder="Contoh: Hidrogen")
            n = st.number_input("🧪 Kuantitas Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f")
            
        with col2:
            col2a, col2b = st.columns([3,1])
            with col2a:
                T_input = st.number_input("🌡️ Temperatur", min_value=-273.0, key="volume_suhu_input")
            with col2b:
                satuan = st.selectbox("Unit", ["K", "°C"], key="volume_suhu_unit")
            
            if satuan == "°C":
                T = T_input + 273.15
                st.info(f"🔄 Konversi: {T_input}°C = {T:.2f} K")
            else:
                T = T_input
            
            col2c, col2d = st.columns([3,1])
            with col2c:
                P_input = st.number_input("🎚️ Tekanan", min_value=0.0, key="volume_tekanan_input")
            with col2d:
                satuan_tekanan = st.selectbox("Unit", ["atm", "Pa", "kPa", "bar"], key="volume_tekanan_unit")
            
            if satuan_tekanan == "Pa":
                P = P_input / 101325
            elif satuan_tekanan == "kPa":
                P = P_input / 101.325
            elif satuan_tekanan == "bar":
                P = P_input / 1.01325
            else:
                P = P_input
            
            if satuan_tekanan != "atm":
                st.info(f"🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm")

        if st.button("🫙 EXECUTE VOLUME DETECTION", key="btn_volume", use_container_width=True, type="primary"):
            V = (n * R * T) / P
            st.markdown(f"""
            <div class="card {text_class}" style="border: 3px solid #00aaff; animation: neon-pulse 2s infinite;">
                <h3>📊 HASIL DETEKSI VOLUME</h3>
                <p style="font-size: 1.5em;"><strong>Volume {nama if nama else 'gas'} = {V:.2f} L</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

    with tab4:
        st.markdown(f"""
        <div class="card {text_class}">
            <h2>🧪 SISTEM PENGHITUNG MOL</h2>
            <p><strong>FORMULA:</strong> n = [P × V] / [R × T]</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("🏷️ Identifikasi Gas", key="nama_mol", placeholder="Contoh: CO₂")
            col1a, col1b = st.columns([3,1])
            with col1a:
                P_input = st.number_input("🎚️ Tekanan", min_value=0.0, key="mol_tekanan_input")
            with col1b:
                satuan_tekanan = st.selectbox("Unit", ["atm", "Pa", "kPa"], key="mol_tekanan_unit")
            
            if satuan_tekanan == "Pa":
                P = P_input / 101325
            elif satuan_tekanan == "kPa":
                P = P_input / 101.325
            else:
                P = P_input
            
            if satuan_tekanan != "atm":
                st.info(f"🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm")
                
        with col2:
            col2a, col2b = st.columns([3,1])
            with col2a:
                V_input = st.number_input("📦 Volume", min_value=0.0, key="mol_vol_input")
            with col2b:
                satuan_vol = st.selectbox("Unit", ["L", "m³", "mL"], key="mol_vol_unit")
            
            if satuan_vol == "m³":
                V = V_input * 1000
                st.info(f"🔄 Konversi: {V_input} m³ = {V:.4f} L")
            elif satuan_vol == "mL":
                V = V_input / 1000
                st.info(f"🔄 Konversi: {V_input} mL = {V:.4f} L")
            else:
                V = V_input
            
            col2c, col2d = st.columns([3,1])
            with col2c:
                T_input = st.number_input("🌡️ Temperatur", min_value=-273.0, key="mol_suhu_input")
            with col2d:
                satuan = st.selectbox("Unit", ["K", "°C"], key="mol_suhu_unit")
            
            if satuan == "°C":
                T = T_input + 273.15
                st.info(f"🔄 Konversi: {T_input}°C = {T:.2f} K")
            else:
                T = T_input

        if st.button("🧪 EXECUTE MOL COUNTING", key="btn_mol", use_container_width=True, type="primary"):
            n = (P * V) / (R * T)
            st.markdown(f"""
            <div class="card {text_class}" style="border: 3px solid #00aaff; animation: neon-pulse 2s infinite;">
                <h3>📊 HASIL PENGHITUNGAN MOL</h3>
                <p style="font-size: 1.5em;"><strong>Jumlah mol {nama if nama else 'gas'} = {n:.2f} mol</strong></p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.markdown(f"<h1 class='main-header {text_class}'>🌿 MYSTICAL GAS CODEX 🌿</h1>", unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "🔮 Pilih Entitas Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas dengan styling mystical
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <div class="card {text_class}">
            <h2>{gas['icon']} {selected_gas}</h2>
            <p style="font-style: italic; color: #32cd32;">{gas['description']}</p>
            <p><b>🏷️ Kategori:</b> {gas['category']}</p>
            <p><b>🔬 Aplikasi:</b> {gas['aplikasi']}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["image"], width=200)
    
    # Tab Informasi dengan styling mystical
    tabs = st.tabs(list(gas["properties"].keys()))
    
    for tab, (category, props) in zip(tabs, gas["properties"].items()):
        with tab:
            st.markdown(f"""
            <div class="card {text_class}">
                <table style="width: 100%; border-collapse: collapse;">
                    {"".join(f"<tr><td style='padding: 10px; border-bottom: 1px solid #32cd32; font-weight: bold; color: #32cd32;'>{key}</td><td style='padding: 10px; border-bottom: 1px solid #32cd32;'>{value}</td></tr>" for key, value in props.items())}
                </table>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    st.markdown(f"<h1 class='main-header {text_class}'>🔥 APOCALYPSE SAFETY PROTOCOL 🔥</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card {text_class}">
        <h3>💀 SIMBOL BAHAYA KEMATIAN</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:200px;background:rgba(60,20,10,0.9);padding:15px;border-radius:10px;border:2px solid #ff4500;">
                <h4>🔥 FLAMMABLE DEATH</h4>
                <p>Contoh: Hidrogen, Metana</p>
                <p>• Jauhkan dari api neraka</p>
                <p>• Gunakan di area terbuka</p>
            </div>
            <div style="flex:1;min-width:200px;background:rgba(60,20,10,0.9);padding:15px;border-radius:10px;border:2px solid #ff4500;">
                <h4>☠️ TOXIC POISON</h4>
                <p>Contoh: Klorin, Amonia</p>
                <p>• Gunakan APD lengkap</p>
                <p>• Hindari inhalasi mematikan</p>
            </div>
            <div style="flex:1;min-width:200px;background:rgba(60,20,10,0.9);padding:15px;border-radius:10px;border:2px solid #ff4500;">
                <h4>💨 OXIDIZER EXPLOSION</h4>
                <p>Contoh: Oksigen, Fluorin</p>
                <p>• Hindari kontak organik</p>
                <p>• Simpan terpisah total</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="card {text_class}">
        <h3>🛡️ SURVIVAL EQUIPMENT</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(60,20,10,0.8);padding:15px;border-radius:10px;">
                <div style="font-size: 50px;">😷</div>
                <p><b>GAS MASK</b></p>
                <p style="color: #ff4500;">SURVIVAL ESSENTIAL</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(60,20,10,0.8);padding:15px;border-radius:10px;">
                <div style="font-size: 50px;">🧤</div>
                <p><b>PROTECTION GLOVES</b></p>
                <p style="color: #ff4500;">CHEMICAL RESISTANT</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(60,20,10,0.8);padding:15px;border-radius:10px;">
                <div style="font-size: 50px;">🥽</div>
                <p><b>SAFETY GOGGLES</b></p>
                <p style="color: #ff4500;">EYE PROTECTION</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;background:rgba(60,20,10,0.8);padding:15px;border-radius:10px;">
                <div style="font-size: 50px;">🥼</div>
                <p><b>LAB COAT</b></p>
                <p style="color: #ff4500;">BODY ARMOR</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card {text_class}">
        <h3>🚨 EMERGENCY SURVIVAL PROTOCOL</h3>
        <ol style="font-size: 1.1em; line-height: 1.8;">
            <li><strong>IMMEDIATE EVACUATION</strong> - Tinggalkan area kontaminasi</li>
            <li><strong>ACTIVATE PROTECTION</strong> - Gunakan APD survival gear</li>
            <li><strong>ELIMINATE IGNITION</strong> - Matikan semua sumber api</li>
            <li><strong>MAXIMUM VENTILATION</strong> - Buka semua akses udara</li>
            <li><strong>CALL EMERGENCY</strong> - Hubungi tim penyelamat</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown(f"""
<div class="card {text_class}" style="text-align:center;">
    <p style="font-family: 'Orbitron', monospace;">
        © 2025 CHEMGASMASTER SYSTEM | KELOMPOK 7 KELAS 1A | VERSION 2.0.1
    </p>
    <p style="color: #00ff00; font-size: 0.9em;">
        POWERED BY QUANTUM CHEMISTRY ENGINE
    </p>
</div>
""", unsafe_allow_html=True)
