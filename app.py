# Aplikasi Kalkulator Gas Ideal dengan Streamlit - Enhanced Version

import streamlit as st
from PIL import Image
import base64

# Konfigurasi halaman utama
st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered", page_icon="💨")

# Fungsi untuk menambahkan background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string.decode()});
            background-size: cover;
            background-opacity: 0.1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#add_bg_from_local('background.jpg')  # Uncomment if you have a background image

# CSS Custom
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("style.css")  # Uncomment if you have custom CSS

# Fungsi konversi
def konversi_suhu_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key=satuan_key)
    T_input = st.number_input(f"{label} ({satuan})", min_value=-273.0, key=input_key)
    if satuan == "°C":
        T = T_input + 273.15
        st.success(f"🔁 Telah dikonversi: {T_input}°C = {T:.2f} K")
    else:
        T = T_input
    return T

def konversi_tekanan_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key=satuan_key)
    P_input = st.number_input(f"{label} ({satuan})", min_value=0.0, key=input_key)
    
    konversi = {
        "Pa": 101325,
        "kPa": 101.325,
        "hPa": 1013.25,
        "bar": 1.01325,
        "Torr": 760,
        "mmHg": 760
    }
    
    if satuan in konversi:
        P = P_input / konversi[satuan]
        st.success(f"🔁 Telah dikonversi: {P_input} {satuan} = {P:.5f} atm")
    else:
        P = P_input
    return P

def konversi_volume_input(label, satuan_key, input_key):
    satuan = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key=satuan_key)
    V_input = st.number_input(f"{label} ({satuan})", min_value=0.1, key=input_key)
    
    if satuan == "m³":
        V = V_input * 1000
        st.success(f"🔁 Telah dikonversi: {V_input} m³ = {V:.2f} L")
    elif satuan == "mL":
        V = V_input / 1000
        st.success(f"🔁 Telah dikonversi: {V_input} mL = {V:.4f} L")
    else:
        V = V_input
    return V

# Sidebar menu
with st.sidebar:
    st.title("🧪 Menu Aplikasi")
    menu = st.radio(
        "Pilih Modul:",
        ["🏠 Halaman Utama", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### Tentang Aplikasi")
    st.info("""
    Aplikasi Kalkulator Gas Ideal ini dikembangkan untuk membantu perhitungan 
    sifat-sifat gas ideal berdasarkan persamaan PV=nRT.
    """)

# Halaman Utama
if menu == "🏠 Halaman Utama":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2693/2693188.png", width=150)
    with col2:
        st.title("Kalkulator Gas Ideal")
        st.markdown("**Alat canggih untuk menghitung sifat-sifat gas ideal**")
    
    st.markdown("---")
    
    st.markdown("""
    <div style="background-color:#e3f2fd;padding:20px;border-radius:10px;">
        <h3 style="color:#0d47a1;">✨ Tentang Aplikasi</h3>
        <p>Aplikasi ini menyediakan:</p>
        <ul>
            <li>Kalkulator properti gas ideal (massa, tekanan, volume, jumlah mol)</li>
            <li>Konversi satuan otomatis</li>
            <li>Ensiklopedia lengkap berbagai jenis gas</li>
            <li>Informasi keselamatan bahan kimia (K3L)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📝 Persamaan Gas Ideal")
    st.latex(r'''PV = nRT''')
    
    cols = st.columns(4)
    with cols[0]:
        st.markdown("""
        <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
            <p><b>P</b> = Tekanan (atm)</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[1]:
        st.markdown("""
        <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
            <p><b>V</b> = Volume (L)</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[2]:
        st.markdown("""
        <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
            <p><b>n</b> = Jumlah mol (mol)</p>
        </div>
        """, unsafe_allow_html=True)
    with cols[3]:
        st.markdown("""
        <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
            <p><b>T</b> = Suhu (K)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("ℹ️ Pilih modul yang ingin Anda gunakan dari menu sidebar di sebelah kiri.")

# Halaman Kalkulator
elif menu == "🧮 Kalkulator Gas":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("""
    <div style="background-color:#fff3e0;padding:20px;border-radius:10px;margin-bottom:20px;">
        Hitung berbagai properti gas ideal menggunakan persamaan <b>PV = nRT</b>.
        Pilih jenis perhitungan yang ingin Anda lakukan:
    </div>
    """, unsafe_allow_html=True)
    
    pilihan = st.radio(
        "Jenis Perhitungan:",
        ["Massa Gas", "Tekanan", "Volume", "Jumlah Mol"],
        horizontal=True
    )
    
    R = 0.0821  # konstanta gas ideal dalam L.atm/mol.K

    with st.container():
        if pilihan == "Massa Gas":
            st.markdown("""
            <div style="background-color:#e1f5fe;padding:15px;border-radius:10px;">
                <h3>🔹 Massa Gas</h3>
                <p>Menghitung massa gas dari jumlah mol dan massa molar</p>
                <p><b>Rumus:</b> Massa = n × Mr</p>
            </div>
            """, unsafe_allow_html=True)
            
            nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Misal: Oksigen")
            n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_massa")
            mr = st.number_input("Massa Molar (Mr) [g/mol]", min_value=0.0, key="mr_massa")
            
            if st.button("Hitung Massa", key="btn_massa"):
                massa = n * mr
                st.success(f"""
                <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
                    <h4>Hasil Perhitungan:</h4>
                    <p>Massa {nama} = <b>{massa:.4f} gram</b></p>
                    <p>Detail: {n} mol × {mr} g/mol = {massa:.4f} gram</p>
                </div>
                """, unsafe_allow_html=True)

        elif pilihan == "Tekanan":
            st.markdown("""
            <div style="background-color:#e1f5fe;padding:15px;border-radius:10px;">
                <h3>🔹 Tekanan Gas</h3>
                <p>Menghitung tekanan gas dari jumlah mol, suhu, dan volume</p>
                <p><b>Rumus:</b> P = (n × R × T) / V</p>
            </div>
            """, unsafe_allow_html=True)
            
            nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Misal: Nitrogen")
            n = st.number_input("Jumlah Mol (n) [mol]", min_value=0.0, key="n_tekanan")
            T = konversi_suhu_input("Suhu", "satuan_t_tekanan", "T_input_tekanan")
            V = konversi_volume_input("Volume", "satuan_v_tekanan", "V_tekanan")
            
            if st.button("Hitung Tekanan", key="btn_tekanan"):
                P = (n * R * T) / V
                st.success(f"""
                <div style="background-color:#e8f5e9;padding:15px;border-radius:10px;">
                    <h4>Hasil Perhitungan:</h4>
                    <p>Tekanan {nama} = <b>{P:.6f} atm</b></p>
                    <p>Detail: ({n} × {R} × {T}) / {V} = {P:.6f} atm</p>
                </div>
                """, unsafe_allow_html=True)

        # [Tambahkan bagian Volume dan Jumlah Mol dengan format yang sama...]

# Halaman Ensiklopedia Gas
elif menu == "📚 Ensiklopedia Gas":
    st.title("📚 Ensiklopedia Gas Ideal")
    st.markdown("""
    <div style="background-color:#f5f5f5;padding:20px;border-radius:10px;margin-bottom:20px;">
        <h3 style="color:#0d47a1;">💡 Database Lengkap Gas Ideal</h3>
        <p>Pilih kategori gas untuk melihat informasi detail:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Kategori Gas
    gas_categories = {
        "Gas Umum": ["Hidrogen (H₂)", "Oksigen (O₂)", "Nitrogen (N₂)", "Karbon Dioksida (CO₂)"],
        "Gas Mulia": ["Helium (He)", "Neon (Ne)", "Argon (Ar)", "Kripton (Kr)"],
        "Hidrokarbon": ["Metana (CH₄)", "Etana (C₂H₆)", "Propana (C₃H₈)", "Butana (C₄H₁₀)"],
        "Gas Industri": ["Amonia (NH₃)", "Klorin (Cl₂)", "Fluorin (F₂)", "Sulfur Dioksida (SO₂)"]
    }
    
    # Pilih Kategori
    selected_category = st.selectbox("Pilih Kategori Gas", list(gas_categories.keys()))
    
    # Tampilkan gas dalam kategori terpilih sebagai tombol
    st.markdown(f"### 🗂️ Gas dalam Kategori: {selected_category}")
    selected_gas = st.radio(
        "Pilih Gas:",
        gas_categories[selected_category],
        horizontal=True
    )
    
    st.markdown("---")
    
    # Database Gas
    gas_database = {
        "Hidrogen (H₂)": {
            "icon": "🚀",
            "color": "#ffcdd2",
            "info": {
                "🧪 Rumus & Struktur": {
                    "content": "Hidrogen adalah unsur kimia dengan simbol H dan nomor atom 1. Pada kondisi standar, hidrogen adalah gas diatomik (H₂) yang tidak berwarna, tidak berbau, sangat mudah terbakar, dan merupakan unsur paling ringan di alam semesta.",
                    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hydrogen-3D-vdW.png/320px-Hydrogen-3D-vdW.png"
                },
                "📊 Sifat Fisika": {
                    "content": """
                    - Massa molar: 2.016 g/mol
                    - Titik leleh: -259.16 °C (13.99 K)
                    - Titik didih: -252.87 °C (20.28 K)
                    - Densitas: 0.08988 g/L (STP)
                    - Fase pada suhu kamar: Gas
                    - Tidak berwarna dan tidak berbau
                    - Konduktivitas termal: 0.1805 W/(m·K)
                    """
                },
                # [Tambahkan kategori info lainnya...]
            }
        },
        # [Tambahkan gas lainnya...]
    }
    
    # Tampilkan informasi gas terpilih
    if selected_gas in gas_database:
        gas_info = gas_database[selected_gas]
        st.markdown(f"""
        <div style="background-color:{gas_info['color']};padding:20px;border-radius:10px;margin-bottom:20px;">
            <h2>{gas_info['icon']} {selected_gas}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        tabs = st.tabs(list(gas_info["info"].keys()))
        
        for tab, category in zip(tabs, gas_info["info"].items()):
            with tab:
                st.markdown(f"""
                <div style="background-color:#ffffff;padding:15px;border-radius:10px;">
                    {category[1]["content"]}
                </div>
                """, unsafe_allow_html=True)
                
                if "image" in category[1]:
                    st.image(category[1]["image"], width=200)
    else:
        st.warning("Informasi untuk gas ini sedang dalam pengembangan.")
    
    st.markdown("---")
    st.markdown("""
    <div style="background-color:#e3f2fd;padding:15px;border-radius:10px;">
        <h4>📌 Catatan Penting:</h4>
        <p>Semua informasi yang ditampilkan adalah untuk tujuan edukasi. Selalu ikuti protokol keselamatan saat menangani bahan kimia.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:gray;padding:10px;">
    <p>© 2025 Kalkulator Gas Ideal | Dibangun dengan Streamlit | Kelompok LPK Poltek AKA</p>
</div>
""", unsafe_allow_html=True)
