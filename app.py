# Aplikasi Kalkulator Gas Ideal dengan Streamlit - Ultimate Version

import streamlit as st
import base64
from PIL import Image
import pandas as pd

# ===========================================
# KONFIGURASI HALAMAN
# ===========================================
st.set_page_config(
    page_title="GasGenius Pro",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================
# CSS CUSTOM & BACKGROUND
# ===========================================
def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
            background-opacity: 0.1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# set_background("lab_background.jpg")  # Uncomment if you have background image

custom_css = """
<style>
    .card {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .gas-card {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 5px solid #2196f3;
    }
    .calc-card {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #4caf50;
    }
    .warning-card {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-left: 5px solid #ff9800;
    }
    .header-text {
        color: #0d47a1;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    .formula-box {
        background-color: #f5f5f5;
        border-radius: 10px;
        padding: 15px;
        font-family: monospace;
        border: 1px dashed #9e9e9e;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ===========================================
# FUNGSI KONVERSI
# ===========================================
def konversi_suhu(label, key_prefix):
    col1, col2 = st.columns([3,1])
    with col1:
        T_input = st.number_input(f"{label}", min_value=-273.0, key=f"{key_prefix}_input")
    with col2:
        satuan = st.selectbox("Satuan", ["K", "°C"], key=f"{key_prefix}_unit")
    
    if satuan == "°C":
        T = T_input + 273.15
        st.success(f"🔁 Konversi: {T_input}°C = {T:.2f} K")
    else:
        T = T_input
    return T

def konversi_tekanan(label, key_prefix):
    col1, col2 = st.columns([3,1])
    with col1:
        P_input = st.number_input(f"{label}", min_value=0.0, key=f"{key_prefix}_input")
    with col2:
        satuan = st.selectbox("Satuan", ["atm", "kPa", "mmHg", "bar"], key=f"{key_prefix}_unit")
    
    factors = {"atm": 1, "kPa": 101.325, "mmHg": 760, "bar": 1.01325}
    P = P_input / factors[satuan]
    
    if satuan != "atm":
        st.success(f"🔁 Konversi: {P_input} {satuan} = {P:.4f} atm")
    return P

# ===========================================
# MENU SIDEBAR
# ===========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2693/2693188.png", width=100)
    st.title("GasGenius Pro")
    st.markdown("---")
    
    menu = st.radio(
        "MENU UTAMA",
        ["🏠 Dashboard", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Safety Guide"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("""
    <div class="card warning-card">
        <small>ℹ️ Aplikasi ini menggunakan persamaan gas ideal PV=nRT dengan R = 0.0821 L·atm/mol·K</small>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN DASHBOARD
# ===========================================
if menu == "🏠 Dashboard":
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2693/2693188.png", width=200)
    with col2:
        st.title("Selamat Datang di GasGenius Pro")
        st.markdown("""
        <div class="card gas-card">
            Alat canggih untuk analisis gas ideal dengan fitur lengkap:
            - Kalkulator properti gas
            - Database gas komprehensif
            - Panduan keselamatan bahan kimia
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("📊 Persamaan Gas Ideal")
    st.latex(r'''PV = nRT''')
    
    cols = st.columns(4)
    variables = [
        ("P", "Tekanan (atm)", "#ffcdd2"),
        ("V", "Volume (L)", "#c8e6c9"),
        ("n", "Jumlah Mol (mol)", "#bbdefb"),
        ("T", "Suhu (K)", "#fff9c4")
    ]
    
    for col, (var, desc, color) in zip(cols, variables):
        with col:
            st.markdown(f"""
            <div style="background-color:{color};padding:15px;border-radius:10px;text-align:center;">
                <h3>{var}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("🎯 Fitur Unggulan")
    features = [
        ("🧮", "Kalkulator Canggih", "Hitung massa, tekanan, dan properti gas lainnya dengan presisi tinggi"),
        ("📊", "Database Gas", "Informasi lengkap 50+ jenis gas dengan sifat fisika & kimia"),
        ("⚠️", "Safety Guide", "Panduan keselamatan untuk penanganan bahan kimia"),
        ("🔄", "Konversi Satuan", "Otomatis konversi antara berbagai satuan pengukuran")
    ]
    
    for i in range(0, len(features), 2):
        cols = st.columns(2)
        for j in range(2):
            if i+j < len(features):
                icon, title, desc = features[i+j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="card">
                        <h3>{icon} {title}</h3>
                        <p>{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("""
    <div class="card calc-card">
        Hitung berbagai properti gas ideal menggunakan persamaan <b>PV = nRT</b>.
        Pilih jenis perhitungan yang ingin Anda lakukan:
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📏 Massa Gas", "⚖️ Tekanan Gas"])
    
    with tab1:
        st.markdown("""
        <div class="card">
            <h3>📏 Menghitung Massa Gas</h3>
            <div class="formula-box">
                Massa (g) = n (mol) × Mr (g/mol)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            nama_gas = st.text_input("Nama Gas", value="Oksigen", key="nama_massa")
            mol = st.number_input("Jumlah Mol (n)", min_value=0.0, value=1.0, step=0.1, key="mol_massa")
        with col2:
            mr = st.number_input("Massa Molar (Mr)", min_value=0.0, value=32.0, step=0.1, key="mr_massa")
        
        if st.button("Hitung Massa", key="btn_massa", type="primary"):
            massa = mol * mr
            st.success(f"""
            <div class="card calc-card">
                <h4>Hasil Perhitungan Massa Gas</h4>
                <p>Gas: <b>{nama_gas}</b></p>
                <p>Massa = {mol} mol × {mr} g/mol = <b>{massa:.4f} gram</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="card">
            <h3>⚖️ Menghitung Tekanan Gas</h3>
            <div class="formula-box">
                P (atm) = [n (mol) × R (0.0821 L·atm/mol·K) × T (K)] / V (L)
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            nama_gas = st.text_input("Nama Gas", value="Nitrogen", key="nama_tekanan")
            mol = st.number_input("Jumlah Mol (n)", min_value=0.0, value=1.0, step=0.1, key="mol_tekanan")
            suhu = konversi_suhu("Suhu", "tekanan_suhu")
        with col2:
            volume = st.number_input("Volume (L)", min_value=0.1, value=22.4, step=0.1, key="vol_tekanan")
        
        if st.button("Hitung Tekanan", key="btn_tekanan", type="primary"):
            R = 0.0821
            tekanan = (mol * R * suhu) / volume
            st.success(f"""
            <div class="card calc-card">
                <h4>Hasil Perhitungan Tekanan Gas</h4>
                <p>Gas: <b>{nama_gas}</b></p>
                <p>Tekanan = ({mol} × {R} × {suhu}) / {volume} = <b>{tekanan:.6f} atm</b></p>
                <p>≈ {tekanan*760:.2f} mmHg ≈ {tekanan*101.325:.2f} kPa</p>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.title("📚 Ensiklopedia Gas Ideal")
    st.markdown("""
    <div class="card gas-card">
        Database lengkap berbagai jenis gas ideal dengan informasi sifat fisika, kimia, dan keselamatan.
    </div>
    """, unsafe_allow_html=True)
    
    # Data Gas Lengkap
    gas_data = {
        "Hidrogen (H₂)": {
            "icon": "🚀",
            "color": "#ffebee",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hydrogen-3D-vdW.png/320px-Hydrogen-3D-vdW.png",
            "kategori": "Gas Umum",
            "deskripsi": "Gas paling ringan di alam semesta, sangat mudah terbakar dengan nyala api tak terlihat.",
            "detail": {
                "🧪 Karakteristik": {
                    "Rumus Molekul": "H₂",
                    "Massa Molar": "2.016 g/mol",
                    "Wujud": "Gas tak berwarna, tak berbau",
                    "Kelarutan": "1.6 mg/L (air, 25°C)"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-259.16 °C (13.99 K)",
                    "Titik Didih": "-252.87 °C (20.28 K)",
                    "Densitas": "0.08988 g/L (STP)",
                    "Kalor Jenis": "14.304 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Sangat reaktif",
                    "Energi Ikatan": "436 kJ/mol",
                    "Potensial Reduksi": "0 V (standar)",
                    "Reaksi Khas": "2H₂ + O₂ → 2H₂O (eksotermik)"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Sangat mudah terbakar",
                    "Rentang Mudah Terbakar": "4-75% di udara",
                    "Pertolongan Pertama": "Jauhkan dari sumber api, beri udara segar",
                    "Penyimpanan": "Tabung bertekanan, jauh dari oksidator"
                }
            }
        },
        "Oksigen (O₂)": {
            "icon": "💨",
            "color": "#e3f2fd",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Oxygen_molecule.png/320px-Oxygen_molecule.png",
            "kategori": "Gas Umum",
            "deskripsi": "Gas vital untuk pernapasan dan pembakaran, menyusun 21% atmosfer bumi.",
            "detail": {
                "🧪 Karakteristik": {
                    "Rumus Molekul": "O₂",
                    "Massa Molar": "32.00 g/mol",
                    "Wujud": "Gas tak berwarna, tak berbau",
                    "Kelarutan": "40 mg/L (air, 20°C)"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-218.79 °C (54.36 K)",
                    "Titik Didih": "-182.96 °C (90.19 K)",
                    "Densitas": "1.429 g/L (STP)",
                    "Kalor Jenis": "0.918 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Oksidator kuat",
                    "Energi Ikatan": "498 kJ/mol",
                    "Potensial Reduksi": "+1.23 V",
                    "Reaksi Khas": "Mendukung pembakaran"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Meningkatkan risiko kebakaran",
                    "Konsentrasi Aman": "<23.5% di udara",
                    "Pertolongan Pertama": "Berikan udara normal",
                    "Penyimpanan": "Jauh dari bahan mudah terbakar"
                }
            }
        },
        # [Tambahkan gas lainnya dengan format yang sama]
    }
    
    # Pilih Gas
    selected_gas = st.selectbox(
        "Pilih Gas untuk Melihat Detail", 
        list(gas_data.keys()),
        format_func=lambda x: f"{gas_data[x]['icon']} {x}"
    )
    
    # Tampilkan Detail Gas
    if selected_gas in gas_data:
        gas = gas_data[selected_gas]
        
        # Header Gas
        st.markdown(f"""
        <div style="background:{gas['color']};padding:20px;border-radius:15px;margin-bottom:20px;">
            <div style="display:flex;align-items:center;">
                <h1 style="margin:0;flex-grow:1;">{gas['icon']} {selected_gas}</h1>
                <img src="{gas['image']}" width="120" style="border-radius:10px;">
            </div>
            <p style="font-size:18px;margin-bottom:0;"><i>{gas['deskripsi']}</i></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tab Informasi
        tabs = st.tabs(list(gas["detail"].keys()))
        
        for tab, (category, details) in zip(tabs, gas["detail"].items()):
            with tab:
                st.markdown(f"""
                <div style="background-color:#fafafa;padding:20px;border-radius:10px;">
                    <h3>{category}</h3>
                    <ul style="padding-left:20px;">
                """, unsafe_allow_html=True)
                
                for key, value in details.items():
                    st.markdown(f"<li><b>{key}:</b> {value}</li>", unsafe_allow_html=True)
                
                st.markdown("</ul></div>", unsafe_allow_html=True)

# ===========================================
# HALAMAN SAFETY GUIDE
# ===========================================
elif menu == "⚠️ Safety Guide":
    st.title("⚠️ Panduan Keselamatan Gas")
    st.markdown("""
    <div class="card warning-card">
        Pedoman penting untuk penanganan bahan kimia gas yang aman di laboratorium dan industri.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h3>🚧 Tanda Bahaya Umum</h3>
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
    <div class="card">
        <h3>🛡️ Alat Pelindung Diri (APD)</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3143/3143466.png" width="80">
                <p><b>Masker Gas</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3143/3143455.png" width="80">
                <p><b>Sarung Tangan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3143/3143475.png" width="80">
                <p><b>Kacamata Keselamatan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3143/3143483.png" width="80">
                <p><b>Jas Lab</b></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;padding:20px;">
    <p>© 2025 GasGenius Pro | Kelompok LPK Poltek AKA | Dibangun dengan Streamlit</p>
</div>
""", unsafe_allow_html=True)
