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
        "description": "Gas tidak berwarna, dapat memancarkan warna oranye kemerahan jika berada pada medan listrik bertegangan tinggi. Dapat digunakan sebagai pengisi lampu neon, penangkal petir, pengisi tabung televisi, dan dalam wujud cair neon dapat digunakan sebagai zat pendingin.",
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
# HALAMAN KALKULATOR GAS
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    st.markdown("<h1 class='main-header'>🧮 Kalkulator Gas Ideal</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📏 Massa Gas", 
        "⚖️ Tekanan",
        "📦 Volume",
        "🧪 Jumlah Mol"
    ])
    
    R = 0.0821  # L.atm/mol.K

    with tab1:
        st.markdown("""
        <div class="card calc-card">
            <h3>📏 Menghitung Massa Gas</h3>
            <p><b>Rumus:</b> Massa = n × Mr</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="nama_massa")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_massa")
        mr = st.number_input("Massa Molar (Mr) [g/mol]", min_value=0.0, key="mr_massa")
        
        if st.button("Hitung Massa", key="btn_massa"):
            massa = n * mr
            st.markdown(f"""
            <div class="result-card">
                <h4>Hasil Perhitungan:</h4>
                <p>Massa {nama} = <b>{massa:.4f} gram</b></p>
                <p>Detail: {n} mol × {mr} g/mol = {massa:.4f} gram</p>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="card calc-card">
            <h3>⚖️ Menghitung Tekanan Gas</h3>
            <p><b>Rumus:</b> P = (n × R × T) / V</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="nama_tekanan")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_tekanan")
        T = konversi_suhu("Suhu", "tekanan_suhu")
        V = konversi_volume("Volume", "tekanan_vol")
        
        if st.button("Hitung Tekanan", key="btn_tekanan"):
            P = (n * R * T) / V
            st.markdown(f"""
            <div class="result-card">
                <h4>Hasil Perhitungan:</h4>
                <p>Tekanan {nama} = <b>{P:.6f} atm</b></p>
                <p>≈ {P*760:.2f} mmHg ≈ {P*101.325:.2f} kPa</p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class="card calc-card">
            <h3>📦 Menghitung Volume Gas</h3>
            <p><b>Rumus:</b> V = (n × R × T) / P</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="nama_volume")
        n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_volume")
        T = konversi_suhu("Suhu", "volume_suhu")
        P = konversi_tekanan("Tekanan", "volume_tekanan")
        
        if st.button("Hitung Volume", key="btn_volume"):
            V = (n * R * T) / P
            st.markdown(f"""
            <div class="result-card">
                <h4>Hasil Perhitungan:</h4>
                <p>Volume {nama} = <b>{V:.4f} L</b></p>
                <p>≈ {V/1000:.6f} m³ ≈ {V*1000:.2f} mL</p>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div class="card calc-card">
            <h3>🧪 Menghitung Jumlah Mol</h3>
            <p><b>Rumus:</b> n = (P × V) / (R × T)</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="nama_mol")
        P = konversi_tekanan("Tekanan", "mol_tekanan")
        V = konversi_volume("Volume", "mol_vol")
        T = konversi_suhu("Suhu", "mol_suhu")
        
        if st.button("Hitung Jumlah Mol", key="btn_mol"):
            n = (P * V) / (R * T)
            st.markdown(f"""
            <div class="result-card">
                <h4>Hasil Perhitungan:</h4>
                <p>Jumlah mol {nama} = <b>{n:.4f} mol</b></p>
                <p>≈ {n*6.022e23:.2e} molekul</p>
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
