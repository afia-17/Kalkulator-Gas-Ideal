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
# CSS CUSTOM DENGAN WARNA YANG LEBIH SEDERHANA
# ===========================================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(74, 144, 226, 0.3);
        margin-bottom: 20px;
    }
    
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        background: white;
        border: 1px solid #e0e0e0;
    }
    
    .calc-card {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        border: none;
    }
    
    .result-card {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
    }
    
    .gas-card {
        background: linear-gradient(135deg, #6f42c1 0%, #e83e8c 100%);
        color: white;
        border: none;
    }
    
    .safety-card {
        background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
        color: white;
        border: none;
    }
    
    .info-card {
        background: #f8f9fa;
        color: #333;
        border: 1px solid #dee2e6;
    }
    
    .conversion-box {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .property-table th {
        background: #4a90e2;
        color: white;
        padding: 12px;
        font-weight: bold;
        text-align: left;
    }
    
    .property-table td {
        padding: 12px;
        border-bottom: 1px solid #dee2e6;
        background: white;
    }
    
    .property-table tr:hover td {
        background: #f8f9fa;
    }
    
    .input-label {
        font-weight: bold;
        color: #495057;
        margin-bottom: 5px;
    }
    
    /* Button styling yang lebih sederhana */
    .stButton > button {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #357abd 0%, #2c5aa0 100%);
        transform: translateY(-1px);
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: white;
        border: 2px solid #4a90e2;
        border-radius: 8px;
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background: white;
        border: 2px solid #4a90e2;
        border-radius: 8px;
        color: #333;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background: white;
        border: 2px solid #4a90e2;
        border-radius: 8px;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# CSS BACKGROUND YANG PROPORSIONAL
# ===========================================
st.markdown("""
<style>
    /* Background untuk Beranda - Subtle Geometric */
    .beranda-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
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
            radial-gradient(circle at 20% 20%, rgba(255,255,255,0.1) 2px, transparent 2px),
            radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 60px 60px, 40px 40px;
        opacity: 0.3;
    }

    /* Background untuk Kalkulator - Minimal Grid */
    .kalkulator-bg {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.03;
    }
    
    .kalkulator-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px),
            linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }

    /* Background untuk Ensiklopedia - Organic Dots */
    .ensiklopedia-bg {
        background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.04;
    }
    
    .ensiklopedia-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.08) 2px, transparent 2px),
            radial-gradient(circle at 75% 75%, rgba(255,255,255,0.06) 1px, transparent 1px);
        background-size: 50px 50px, 25px 25px;
    }

    /* Background untuk Keselamatan - Subtle Warning */
    .keselamatan-bg {
        background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        opacity: 0.04;
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
                rgba(255,255,255,0.02) 0px,
                rgba(255,255,255,0.02) 2px,
                transparent 2px,
                transparent 20px
            );
    }

    /* Overlay yang lebih ringan */
    .content-overlay {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(5px);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.3);
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
# MENU SIDEBAR YANG LEBIH SEDERHANA
# ===========================================
with st.sidebar:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%); 
                padding: 20px; 
                border-radius: 10px; 
                text-align: center; 
                margin-bottom: 20px;">
        <h1 style="color: white; margin: 0; font-size: 1.8em;">⚗️ ChemGasMaster</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 5px 0 0 0;">Platform Kimia Interaktif</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Menu dengan styling yang lebih sederhana
    menu_options = ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
    menu = st.radio(
        "📋 MENU UTAMA",
        menu_options,
        index=0
    )
    
    st.markdown("---")
    
    # Info box yang lebih sederhana
    st.markdown("""
    <div style="background: #f8f9fa;
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid #4a90e2;
                margin-bottom: 15px;">
        <div style="font-size: 1.2em; margin-bottom: 8px;">🧪</div>
        <small><b>ℹ️ Info Penting</b><br>
        Menggunakan persamaan gas ideal:<br>
        <b>PV = nRT</b><br>
        (R = 0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)
    
    # Fun facts box
    st.markdown("""
    <div style="background: #e8f4fd;
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid #28a745;">
        <div style="font-size: 1.2em; margin-bottom: 8px;">🎯</div>
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
        <h1 style="color: #4a90e2; font-size: 2.5em; margin-bottom: 20px;">
            ⚗️ ChemGasMaster
        </h1>
        <p style="font-size: 1.2em; color: #666; margin-bottom: 30px;">
            Platform Interaktif untuk Eksplorasi Dunia Gas Ideal
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Welcome card
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
                padding: 25px;
                border-radius: 10px;
                color: white;
                text-align: center;
                margin-bottom: 25px;">
        <div style="font-size: 2em; margin-bottom: 15px;">🎉</div>
        <h2 style="margin: 0 0 15px 0;">Selamat Datang di ChemGasMaster!</h2>
        <p style="font-size: 1.1em; margin: 0; opacity: 0.9;">
            Jelajahi dunia gas ideal dengan kalkulator canggih, ensiklopedia lengkap, 
            dan panduan keselamatan yang komprehensif!
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Persamaan Gas Ideal
    st.markdown(wrap_content_with_overlay("""
    <div style="text-align: center; margin: 30px 0;">
        <h3 style="color: #4a90e2; margin-bottom: 20px;">🔬 Persamaan Gas Ideal</h3>
    </div>
    """), unsafe_allow_html=True)
    
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
            <h4 style="color: #4a90e2; margin-bottom: 15px;">📊 Variabel Persamaan:</h4>
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px; border-left: 3px solid #dc3545;">
                    <b style="color: #dc3545;">P</b> = Tekanan (atm)
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px; border-left: 3px solid #28a745;">
                    <b style="color: #28a745;">V</b> = Volume (L)
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px; border-left: 3px solid #007bff;">
                    <b style="color: #007bff;">n</b> = Jumlah mol (mol)
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px; border-left: 3px solid #6f42c1;">
                    <b style="color: #6f42c1;">R</b> = Konstanta gas = 0.0821 L·atm/mol·K
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px; border-left: 3px solid #fd7e14;">
                    <b style="color: #fd7e14;">T</b> = Suhu (K)
                </p>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown(wrap_content_with_overlay("""
        <div style="background: #fff3cd; padding: 20px; border-radius: 8px; border: 1px solid #ffeaa7;">
            <h4 style="color: #856404; margin-bottom: 15px;">🎯 Fakta Menarik:</h4>
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px;">
                    🎚️ <b>Gas Ideal</b> - Hanya model matematis sempurna!
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px;">
                    🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px;">
                    🧪 <b>1 mol gas</b> = 6.022×10²³ molekul
                </p>
                <p style="margin: 0; padding: 8px; background: white; border-radius: 5px;">
                    🚀 <b>STP</b> - 0°C, 1 atm, 22.4 L/mol
                </p>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    # Visualisasi variabel
    st.markdown(wrap_content_with_overlay("<h4 style='text-align: center; color: #4a90e2; margin: 30px 0 20px 0;'>📊 Visualisasi Variabel Gas Ideal</h4>"), unsafe_allow_html=True)
    
    var_cols = st.columns(5)
    variables = [
        ("P", "Tekanan", "Gaya gas pada dinding wadah", "#dc3545"),
        ("V", "Volume", "Ruang yang ditempati gas", "#28a745"),
        ("n", "Jumlah Mol", "Banyaknya partikel gas", "#007bff"),
        ("R", "Konstanta", "Tetapan gas universal", "#6f42c1"),
        ("T", "Suhu", "Energi kinetik rata-rata", "#fd7e14")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background: {color};
                        padding: 20px;
                        border-radius: 8px;
                        height: 150px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        color: white;">
                <h2 style="margin: 5px 0; font-size: 2em;">{var}</h2>
                <p style="margin: 5px 0; font-weight: bold;">{name}</p>
                <p style="margin: 5px 0; font-size: 0.8em; opacity: 0.9;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    add_menu_background("kalkulator")
    
    # Header
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
                 padding: 25px;
                 border-radius: 10px;
                margin-bottom: 25px;
                text-align: center;">
        <h1 style="color: white; margin: 0; font-size: 2em;">
              🧪 Kalkulator Gas Ideal
        </h1>
        <p style="color: rgba(255,255,255,0.9); margin: 10px 0 0 0;">
            Hitung dengan Presisi Tinggi menggunakan Persamaan PV = nRT
        </p>
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
            <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                        padding: 20px;
                        border-radius: 8px;
                        color: white;
                        margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 2.5em;">🧪</div>
                    <div>
                        <h2 style="margin: 0; font-size: 1.5em;">Kalkulator Massa Gas</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 8px 12px; 
                                    border-radius: 5px; 
                                    display: inline-block;
                                    margin-top: 8px;">
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
                <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                            padding: 20px;
                            border-radius: 8px;
                            margin-top: 20px;
                            color: white;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 2em;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 12px; 
                                        border-radius: 5px;">
                                <p style="margin: 0; font-size: 1.2em;">
                                    Massa <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.3em; font-weight: bold;">
                                        {massa:.4f} gram
                                    </span>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan
        with st.container():
            st.markdown(wrap_content_with_overlay("""
            <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
                        padding: 20px;
                        border-radius: 8px;
                        color: white;
                        margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 2.5em;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; font-size: 1.5em;">Kalkulator Tekanan Gas</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 8px 12px; 
                                    border-radius: 5px; 
                                    display: inline-block;
                                    margin-top: 8px;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
        
            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
                            padding: 20px;
                            border-radius: 8px;
                            margin-top: 20px;
                            color: white;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 2em;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 12px; 
                                        border-radius: 5px;">
                                <p style="margin: 0; font-size: 1.2em;">
                                    Tekanan <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.3em; font-weight: bold;">
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
            <div style="background: linear-gradient(135deg, #6f42c1 0%, #e83e8c 100%);
                        padding: 20px;
                        border-radius: 8px;
                        color: white;
                        margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 2.5em;">🫙</div>
                    <div>
                        <h2 style="margin: 0; font-size: 1.5em;">Kalkulator Volume Gas</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 8px 12px; 
                                    border-radius: 5px; 
                                    display: inline-block;
                                    margin-top: 8px;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
        
            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #6f42c1 0%, #e83e8c 100%);
                            padding: 20px;
                            border-radius: 8px;
                            margin-top: 20px;
                            color: white;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 2em;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 12px; 
                                        border-radius: 5px;">
                                <p style="margin: 0; font-size: 1.2em;">
                                    Volume <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.3em; font-weight: bold;">
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
            <div style="background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
                        padding: 20px;
                        border-radius: 8px;
                        color: white;
                        margin-bottom: 20px;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 2.5em;">🧪</div>
                    <div>
                        <h2 style="margin: 0; font-size: 1.5em;">Kalkulator Jumlah Mol</h2>
                        <div style="background: rgba(255,255,255,0.2); 
                                    padding: 8px 12px; 
                                    border-radius: 5px; 
                                    display: inline-block;
                                    margin-top: 8px;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
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
                    <div style="background: #d1ecf1; color: #0c5460; padding: 8px; border-radius: 5px; margin: 8px 0; text-align: center;">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
        
            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
                            padding: 20px;
                            border-radius: 8px;
                            margin-top: 20px;
                            color: white;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 2em;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0;">🎉 Hasil Perhitungan</h3>
                            <div style="background: rgba(255,255,255,0.2); 
                                        padding: 12px; 
                                        border-radius: 5px;">
                                <p style="margin: 0; font-size: 1.2em;">
                                    Jumlah mol <b>{nama if nama else 'gas'}</b> = 
                                    <span style="font-size: 1.3em; font-weight: bold;">
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
    <div style="background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin-top: 30px;
                border-left: 4px solid #4a90e2;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 2em;">💡</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #4a90e2;">🎓 Tips Perhitungan</h3>
                <p style="margin: 0; color: #666; line-height: 1.6;">
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
    <div style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
                padding: 25px;
                border-radius: 10px;
                color: white;
                text-align: center;
                margin-bottom: 25px;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">📚</div>
        <h1 style="margin: 0; font-size: 2em;">Ensiklopedia Gas</h1>
        <p style="margin: 10px 0 0 0; opacity: 0.9;">
            Jelajahi Dunia Gas dengan Informasi Lengkap & Akurat
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Selectbox
    st.markdown(wrap_content_with_overlay("""
    <div style="background: #f8f9fa;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                text-align: center;
                border: 1px solid #dee2e6;">
        <h3 style="margin: 0; color: #495057;">🔍 Pilih Gas untuk Dipelajari</h3>
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
        <div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
                    padding: 20px;
                    border-radius: 8px;
                    color: white;">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="font-size: 2.5em;">{gas['icon']}</div>
                <h2 style="margin: 0; font-size: 1.8em;">{selected_gas}</h2>
            </div>
            <div style="background: rgba(255,255,255,0.2); 
                        padding: 12px; 
                        border-radius: 5px;
                        margin-bottom: 15px;">
                <p style="margin: 0; font-style: italic;">
                    {gas['description']}
                </p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 10px; 
                            border-radius: 5px;">
                    <p style="margin: 0;"><b>📂 Kategori:</b> {gas['category']}</p>
                </div>
                <div style="background: rgba(255,255,255,0.1); 
                            padding: 10px; 
                            border-radius: 5px;">
                    <p style="margin: 0;"><b>🔧 Aplikasi:</b> {gas['aplikasi']}</p>
                </div>
            </div>
        </div>
        """), unsafe_allow_html=True)
    
    with col2:
        st.markdown(wrap_content_with_overlay(f"""
        <div style="background: #f8f9fa;
                    padding: 15px;
                    border-radius: 8px;
                    text-align: center;
                    border: 1px solid #dee2e6;">
            <img src="{gas['image']}" 
                 style="width: 100%; 
                        max-width: 200px; 
                        border-radius: 8px;">
            <p style="color: #495057; margin: 10px 0 0 0; font-weight: bold;">
                🖼️ Struktur Molekul
            </p>
        </div>
        """), unsafe_allow_html=True)
    
    # Tab Informasi dengan tabel yang diperbaiki
    tabs = st.tabs(list(gas["properties"].keys()))
    
    colors = [
        "#4a90e2",
        "#28a745", 
        "#dc3545"
    ]
    
    for i, (tab, (category, props)) in enumerate(zip(tabs, gas["properties"].items())):
        with tab:
            color = colors[i % len(colors)]
            
            # Membuat tabel dengan cara yang aman
            table_content = ""
            for key, value in props.items():
                table_content += f"""
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        {key}
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {value}
                    </td>
                </tr>"""
            
            st.markdown(wrap_content_with_overlay(f"""
            <div style="background: {color};
                        padding: 20px;
                        border-radius: 8px;
                        color: white;
                        margin: 15px 0;">
                <h3 style="margin: 0 0 15px 0; text-align: center;">
                    {category}
                </h3>
                <div style="background: rgba(255,255,255,0.1); 
                            border-radius: 8px;
                            overflow: hidden;">
                    <table style="width: 100%; border-collapse: collapse;">
                        {table_content}
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
    <div style="background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
                padding: 25px;
                border-radius: 10px;
                color: white;
                text-align: center;
                margin-bottom: 25px;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">⚠️</div>
        <h1 style="margin: 0; font-size: 2em;">Panduan Keselamatan Gas</h1>
        <p style="margin: 10px 0 0 0; opacity: 0.9;">
            🛡️ Keselamatan Adalah Prioritas Utama dalam Bekerja dengan Gas
        </p>
    </div>
    """), unsafe_allow_html=True)
    
    # Simbol Bahaya
    st.markdown(wrap_content_with_overlay("""
    <div style="background: #f8f9fa;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 25px;
                border: 1px solid #dee2e6;">
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 2.5em; margin-bottom: 10px;">🚧</div>
            <h2 style="margin: 0; color: #495057;">Simbol Bahaya Umum</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
            <div style="background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 2.5em; margin-bottom: 10px;">🔥</div>
                <h3 style="margin: 0 0 10px 0;">Mudah Terbakar</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 12px; 
                            border-radius: 5px;">
                    <p style="margin: 0 0 8px 0;"><b>Contoh:</b> Hidrogen, Metana</p>
                    <p style="margin: 4px 0;">• Jauhkan dari sumber api</p>
                    <p style="margin: 4px 0;">• Gunakan di area berventilasi</p>
                    <p style="margin: 4px 0;">• Hindari percikan listrik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #6f42c1 0%, #5a32a3 100%);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 2.5em; margin-bottom: 10px;">☠️</div>
                <h3 style="margin: 0 0 10px 0;">Beracun</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 12px; 
                            border-radius: 5px;">
                    <p style="margin: 0 0 8px 0;"><b>Contoh:</b> Klorin, Amonia</p>
                    <p style="margin: 4px 0;">• Gunakan alat pelindung diri</p>
                    <p style="margin: 4px 0;">• Hindari inhalasi langsung</p>
                    <p style="margin: 4px 0;">• Ventilasi yang baik</p>
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;
                        color: white;">
                <div style="font-size: 2.5em; margin-bottom: 10px;">💨</div>
                <h3 style="margin: 0 0 10px 0;">Pengoksidasi</h3>
                <div style="background: rgba(255,255,255,0.2); 
                            padding: 12px; 
                            border-radius: 5px;">
                    <p style="margin: 0 0 8px 0;"><b>Contoh:</b> Oksigen, Fluorin</p>
                    <p style="margin: 4px 0;">• Hindari kontak dengan bahan organik</p>
                    <p style="margin: 4px 0;">• Simpan terpisah dari reduktor</p>
                    <p style="margin: 4px 0;">• Meningkatkan risiko kebakaran</p>
                </div>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    # APD
    st.markdown(wrap_content_with_overlay("""
    <div style="background: linear-gradient(135deg, #28a745 0%, #1e7e34 100%);
                padding: 25px;
                border-radius: 10px;
                color: white;
                margin-bottom: 25px;">
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 2.5em; margin-bottom: 10px;">🛡️</div>
            <h2 style="margin: 0;">Alat Pelindung Diri (APD)</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
            <div style="background: rgba(255,255,255,0.2);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;">
                <div style="font-size: 3em; margin-bottom: 10px;">😷</div>
                <h4 style="margin: 0 0 8px 0;">Masker Gas</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi dari inhalasi gas berbahaya</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;">
                <div style="font-size: 3em; margin-bottom: 10px;">🧤</div>
                <h4 style="margin: 0 0 8px 0;">Sarung Tangan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi tangan dari kontak langsung</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;">
                <div style="font-size: 3em; margin-bottom: 10px;">🥽</div>
                <h4 style="margin: 0 0 8px 0;">Kacamata Keselamatan</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi mata dari percikan</p>
            </div>
            <div style="background: rgba(255,255,255,0.2);
                        padding: 20px;
                        border-radius: 8px;
                        text-align: center;">
                <div style="font-size: 3em; margin-bottom: 10px;">🥼</div>
                <h4 style="margin: 0 0 8px 0;">Jas Laboratorium</h4>
                <p style="margin: 0; opacity: 0.9; font-size: 0.9em;">Melindungi tubuh dari kontaminasi</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

    # Prosedur Darurat
    st.markdown(wrap_content_with_overlay("""
    <div style="background: #fff3cd;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 25px;
                border: 1px solid #ffeaa7;">
        <div style="text-align: center; margin-bottom: 20px;">
            <div style="font-size: 2.5em; margin-bottom: 10px;">🚨</div>
            <h2 style="margin: 0; color: #856404;">Prosedur Darurat</h2>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #dc3545;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">1️⃣</div>
                    <h4 style="margin: 0; color: #495057;">Evakuasi Segera</h4>
                </div>
                <p style="margin: 0; color: #666;">Segera tinggalkan area jika terjadi kebocoran gas berbahaya</p>
            </div>
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #28a745;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">2️⃣</div>
                    <h4 style="margin: 0; color: #495057;">Gunakan APD</h4>
                </div>
                <p style="margin: 0; color: #666;">Selalu gunakan alat pelindung diri yang sesuai sebelum menangani gas</p>
            </div>
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #fd7e14;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">3️⃣</div>
                    <h4 style="margin: 0; color: #495057;">Hindari Api</h4>
                </div>
                <p style="margin: 0; color: #666;">Jauhkan dari sumber api, percikan listrik, dan benda panas</p>
            </div>
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #007bff;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">4️⃣</div>
                    <h4 style="margin: 0; color: #495057;">Ventilasi Area</h4>
                </div>
                <p style="margin: 0; color: #666;">Buka jendela dan pintu untuk sirkulasi udara yang baik</p>
            </div>
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #6f42c1;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">5️⃣</div>
                    <h4 style="margin: 0; color: #495057;">Hubungi Petugas</h4>
                </div>
                <p style="margin: 0; color: #666;">Segera hubungi petugas berwenang atau layanan darurat jika diperlukan</p>
            </div>
            <div style="background: white; 
                        padding: 15px; 
                        border-radius: 8px;
                        border-left: 4px solid #17a2b8;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="font-size: 1.5em;">📞</div>
                    <h4 style="margin: 0; color: #495057;">Nomor Darurat</h4>
                </div>
                <p style="margin: 0; color: #666;"><b>Pemadam Kebakaran:</b> 113<br><b>Ambulans:</b> 118<br><b>Polisi:</b> 110</p>
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            color: white;
            margin-top: 30px;">
    <div style="font-size: 2em; margin-bottom: 10px;">⚗️</div>
    <h3 style="margin: 0 0 8px 0;">ChemGasMaster</h3>
    <p style="margin: 0; opacity: 0.9;">© 2025 Kelompok 7 Kelas 1A | Platform Kimia Interaktif</p>
    <div style="margin-top: 15px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 6px 12px; 
                     border-radius: 15px;">
            🧪 Kalkulator Gas
        </span>
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 6px 12px; 
                     border-radius: 15px;">
            📚 Ensiklopedia
        </span>
        <span style="background: rgba(255,255,255,0.2); 
                     padding: 6px 12px; 
                     border-radius: 15px;">
            ⚠️ Keselamatan
        </span>
    </div>
</div>
""", unsafe_allow_html=True)
