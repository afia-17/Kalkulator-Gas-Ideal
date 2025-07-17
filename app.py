# Aplikasi Master Gas - Kalkulator & Ensiklopedia Gas Ideal
import streamlit as st
import base64

# ========== KONFIGURASI HALAMAN ==========
st.set_page_config(
    page_title="Master Gas",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CSS KUSTOM ==========
st.markdown("""
<style>
    .judul {
        color: #0d47a1;
        border-bottom: 2px solid #0d47a1;
        padding-bottom: 10px;
    }
    .kartu {
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .kartu-kalkulator {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        border-left: 5px solid #2196f3;
    }
    .kartu-hasil {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        border-left: 5px solid #4caf50;
    }
    .kartu-gas {
        background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
        border-left: 5px solid #ff9800;
    }
    .kotak-konversi {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px dashed #9e9e9e;
    }
    .tabel-properti {
        width: 100%;
        border-collapse: collapse;
    }
    .tabel-properti th {
        background-color: #0d47a1;
        color: white;
        padding: 8px;
    }
    .tabel-properti td {
        padding: 8px;
        border-bottom: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# ========== FUNGSI KONVERSI ==========
def konversi_suhu(label, key_prefix):
    col1, col2 = st.columns([3,1])
    with col1:
        suhu = st.number_input(label, min_value=-273.0, key=f"{key_prefix}_input")
    with col2:
        satuan = st.selectbox("Satuan", ["K", "°C"], key=f"{key_prefix}_unit")
    
    if satuan == "°C":
        kelvin = suhu + 273.15
        st.markdown(f"""
        <div class="kotak-konversi">
            🔄 Terkonversi: {suhu}°C = {kelvin:.2f} K
        </div>
        """, unsafe_allow_html=True)
        return kelvin
    return suhu

def konversi_tekanan(label, key_prefix):
    satuan = ["atm", "Pa", "kPa", "bar", "mmHg", "Torr"]
    col1, col2 = st.columns([3,1])
    with col1:
        tekanan = st.number_input(label, min_value=0.0, key=f"{key_prefix}_input")
    with col2:
        unit = st.selectbox("Satuan", satuan, key=f"{key_prefix}_unit")
    
    konversi = {
        "atm": 1,
        "Pa": 101325,
        "kPa": 101.325,
        "bar": 1.01325,
        "mmHg": 760,
        "Torr": 760
    }
    atm = tekanan / konversi[unit]
    
    if unit != "atm":
        st.markdown(f"""
        <div class="kotak-konversi">
            🔄 Terkonversi: {tekanan} {unit} = {atm:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    return atm

def konversi_volume(label, key_prefix):
    satuan = ["L", "m³", "mL"]
    col1, col2 = st.columns([3,1])
    with col1:
        volume = st.number_input(label, min_value=0.1, key=f"{key_prefix}_input")
    with col2:
        unit = st.selectbox("Satuan", satuan, key=f"{key_prefix}_unit")
    
    if unit == "m³":
        liter = volume * 1000
        st.markdown(f"""
        <div class="kotak-konversi">
            🔄 Terkonversi: {volume} m³ = {liter:.2f} L
        </div>
        """, unsafe_allow_html=True)
    elif unit == "mL":
        liter = volume / 1000
        st.markdown(f"""
        <div class="kotak-konversi">
            🔄 Terkonversi: {volume} mL = {liter:.4f} L
        </div>
        """, unsafe_allow_html=True)
    else:
        liter = volume
    return liter

# ========== DATABASE GAS ==========
DATABASE_GAS = {
    "Hidrogen (H₂)": {
        "ikon": "🚀",
        "kategori": "Gas Diatomik",
        "deskripsi": "Unsur paling ringan di alam semesta dengan sifat unik sebagai bahan bakar masa depan.",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hydrogen-3D-vdW.png/320px-Hydrogen-3D-vdW.png",
        "properti": {
            "🧪 Identitas Molekul": {
                "Rumus": "H₂",
                "Massa Molar": "2.016 g/mol",
                "Penampilan": "Gas tidak berwarna, tidak berbau",
                "Struktur": "Diatomik, ikatan kovalen tunggal"
            },
            "📊 Sifat Fisika": {
                "Titik Leleh": "-259.16 °C (13.99 K)",
                "Titik Didih": "-252.87 °C (20.28 K)",
                "Massa Jenis (STP)": "0.08988 g/L",
                "Kalor Jenis": "14.304 J/(g·K)"
            },
            "⚗️ Sifat Kimia": {
                "Reaktivitas": "Sangat mudah terbakar",
                "Energi Ikatan": "436 kJ/mol",
                "Reaksi Umum": "2H₂ + O₂ → 2H₂O (eksoterm)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (4-75% di udara)",
                "Perlindungan": "Gunakan di area berventilasi, hindari percikan api",
                "Penyimpanan": "Tabung bertekanan tinggi jauh dari oksidator"
            }
        },
        "aplikasi": "Bahan bakar roket, produksi amonia, hidrogenasi minyak"
    },
    "Oksigen (O₂)": {
        "ikon": "💨",
        "kategori": "Gas Diatomik",
        "deskripsi": "Gas vital untuk kehidupan dan proses pembakaran, menyusun 21% atmosfer Bumi.",
        "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Oxygen_molecule.png/320px-Oxygen_molecule.png",
        "properti": {
            "🧪 Identitas Molekul": {
                "Rumus": "O₂",
                "Massa Molar": "32.00 g/mol",
                "Penampilan": "Gas tidak berwarna",
                "Struktur": "Diatomik, ikatan rangkap"
            },
            "📊 Sifat Fisika": {
                "Titik Leleh": "-218.79 °C (54.36 K)",
                "Titik Didih": "-182.96 °C (90.19 K)",
                "Massa Jenis (STP)": "1.429 g/L",
                "Kalor Jenis": "0.918 J/(g·K)"
            },
            "⚗️ Sifat Kimia": {
                "Reaktivitas": "Oksidator kuat",
                "Energi Ikatan": "498 kJ/mol",
                "Reaksi Umum": "Mendukung pembakaran"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Meningkatkan risiko kebakaran",
                "Perlindungan": "Hindari kontak dengan bahan organik",
                "Penyimpanan": "Pisahkan dari zat mudah terbakar"
            }
        },
        "aplikasi": "Penggunaan medis, pengolahan logam, pengolahan air"
    }
}

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("Master Gas")
    st.markdown("---")
    menu = st.radio(
        "Navigasi",
        ["🏠 Beranda", "🧮 Kalkulator", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    <div class="kartu kartu-gas">
        <small>ℹ️ Menggunakan persamaan gas ideal: PV=nRT (R=0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)

# ========== HALAMAN UTAMA ==========
if menu == "🏠 Beranda":
    st.markdown("<h1 class='judul'>Master Gas</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="kartu kartu-kalkulator">
        Alat lengkap untuk perhitungan gas ideal dan informasi kimia dengan panduan keselamatan.
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r'''PV = nRT''')
    cols = st.columns(4)
    variabel = [
        ("P", "Tekanan (atm)", "#ffcdd2"),
        ("V", "Volume (L)", "#c8e6c9"), 
        ("n", "Mol (mol)", "#bbdefb"),
        ("T", "Suhu (K)", "#fff9c4")
    ]
    for col, (var, desc, warna) in zip(cols, variabel):
        with col:
            st.markdown(f"""
            <div style="background:{warna};padding:15px;border-radius:10px;text-align:center;">
                <h3>{var}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "🧮 Kalkulator":
    st.markdown("<h1 class='judul'>Kalkulator Gas</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📏 Massa", 
        "⚖️ Tekanan",
        "📦 Volume",
        "🧪 Mol"
    ])
    
    R = 0.0821  # Konstanta gas
    
    with tab1:
        st.markdown("""
        <div class="kartu kartu-kalkulator">
            <h3>Hitung Massa Gas</h3>
            <p><b>Rumus:</b> Massa (g) = Mol × Massa Molar</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="massa_nama")
        mol = st.number_input("Mol (n)", min_value=0.0, key="massa_mol")
        massa_molar = st.number_input("Massa Molar (g/mol)", min_value=0.0, key="massa_mm")
        
        if st.button("Hitung Massa", key="btn_massa"):
            massa = mol * massa_molar
            st.markdown(f"""
            <div class="kartu kartu-hasil">
                <h4>Hasil</h4>
                <p>Massa {nama} = <b>{massa:.4f} g</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="kartu kartu-kalkulator">
            <h3>Hitung Tekanan</h3>
            <p><b>Rumus:</b> P = nRT/V</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="tekanan_nama")
        mol = st.number_input("Mol (n)", min_value=0.0, key="tekanan_mol")
        suhu = konversi_suhu("Suhu", "tekanan_suhu")
        vol = konversi_volume("Volume", "tekanan_vol")
        
        if st.button("Hitung Tekanan", key="btn_tekanan"):
            tekanan = (mol * R * suhu) / vol
            st.markdown(f"""
            <div class="kartu kartu-hasil">
                <h4>Hasil</h4>
                <p>Tekanan {nama} = <b>{tekanan:.6f} atm</b></p>
                <p>≈ {tekanan*760:.2f} mmHg ≈ {tekanan*101.325:.2f} kPa</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="kartu kartu-kalkulator">
            <h3>Hitung Volume</h3>
            <p><b>Rumus:</b> V = nRT/P</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="vol_nama")
        mol = st.number_input("Mol (n)", min_value=0.0, key="vol_mol")
        suhu = konversi_suhu("Suhu", "vol_suhu")
        tekanan = konversi_tekanan("Tekanan", "vol_tekanan")
        
        if st.button("Hitung Volume", key="btn_vol"):
            volume = (mol * R * suhu) / tekanan
            st.markdown(f"""
            <div class="kartu kartu-hasil">
                <h4>Hasil</h4>
                <p>Volume {nama} = <b>{volume:.4f} L</b></p>
                <p>≈ {volume/1000:.6f} m³ ≈ {volume*1000:.2f} mL</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="kartu kartu-kalkulator">
            <h3>Hitung Mol</h3>
            <p><b>Rumus:</b> n = PV/RT</p>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input("Nama Gas", key="mol_nama")
        tekanan = konversi_tekanan("Tekanan", "mol_tekanan")
        vol = konversi_volume("Volume", "mol_vol")
        suhu = konversi_suhu("Suhu", "mol_suhu")
        
        if st.button("Hitung Mol", key="btn_mol"):
            mol = (tekanan * vol) / (R * suhu)
            st.markdown(f"""
            <div class="kartu kartu-hasil">
                <h4>Hasil</h4>
                <p>Mol {nama} = <b>{mol:.4f} mol</b></p>
                <p>≈ {mol*6.022e23:.2e} molekul</p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "📚 Ensiklopedia Gas":
    st.markdown("<h1 class='judul'>Ensiklopedia Gas</h1>", unsafe_allow_html=True)
    
    gas_terpilih = st.selectbox(
        "Pilih Gas", 
        list(DATABASE_GAS.keys()),
        format_func=lambda x: f"{DATABASE_GAS[x]['ikon']} {x}"
    )
    
    gas = DATABASE_GAS[gas_terpilih]
    
    # Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <h2>{gas['ikon']} {gas_terpilih}</h2>
        <p><i>{gas['deskripsi']}</i></p>
        <p><b>Kategori:</b> {gas['kategori']}</p>
        <p><b>Aplikasi:</b> {gas['aplikasi']}</p>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["gambar"], width=200)
    
    # Tab Properti
    tab_properti = st.tabs(list(gas["properti"].keys()))
    for tab, (kategori, props) in zip(tab_properti, gas["properti"].items()):
        with tab:
            st.markdown(f"""
            <div style="padding: 15px; background: white; border-radius: 10px;">
                <h3>{kategori}</h3>
                <table class="tabel-properti">
                    {"".join(f"<tr><td><b>{k}</b></td><td>{v}</td></tr>" for k,v in props.items())}
                </table>
            </div>
            """, unsafe_allow_html=True)

elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("<h1 class='judul'>Panduan Keselamatan Gas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="kartu kartu-gas">
        <h3>Simbol Bahaya Umum</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px;">
            <div style="background: #ffebee; padding: 15px; border-radius: 10px;">
                <h4>🔥 Mudah Terbakar</h4>
                <p>Contoh: H₂, CH₄</p>
                <p>• Jauhkan dari sumber api</p>
                <p>• Gunakan di area berventilasi</p>
            </div>
            <div style="background: #fff8e1; padding: 15px; border-radius: 10px;">
                <h4>☠️ Beracun</h4>
                <p>Contoh: Cl₂, NH₃</p>
                <p>• Gunakan APD lengkap</p>
                <p>• Hindari inhalasi</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>© 2025 Master Gas | Kelompok LPK Poltek AKA</p>
</div>
""", unsafe_allow_html=True)
