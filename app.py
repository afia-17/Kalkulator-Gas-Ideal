import streamlit as st
import base64

# Konfigurasi Halaman
st.set_page_config(
    page_title="GasMaster Pro",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Custom
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
    .conversion-box {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        border: 1px dashed #9e9e9e;
    }
</style>
""", unsafe_allow_html=True)

# Fungsi Konversi
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

# Menu Sidebar
with st.sidebar:
    st.title("GasMaster Pro")
    st.markdown("---")
    menu = st.radio(
        "MENU UTAMA",
        ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas"],
        index=0
    )
    st.markdown("---")
    st.markdown("""
    <div style="padding:10px;border-radius:8px;background:#f5f5f5;">
        <small>ℹ️ Menggunakan persamaan gas ideal: PV=nRT (R=0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)

# Halaman Beranda
if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>GasMaster Pro</h1>", unsafe_allow_html=True)
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
            <div style="background:{color};padding:15px;border-radius:10px;text-align:center;">
                <h3>{var}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# Halaman Kalkulator Gas
elif menu == "🧮 Kalkulator Gas":
    st.markdown("<h1 class='main-header'>🧮 Kalkulator Gas Ideal</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📏 Massa Gas", "⚖️ Tekanan", "📦 Volume", "🧪 Jumlah Mol"])
    R = 0.0821  # L.atm/mol.K

    with tab1:
        st.markdown("""
        <div style="padding:20px;border-radius:15px;background:#e3f2fd;border-left:5px solid #2196f3;">
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
            <div style="padding:20px;border-radius:15px;background:#e8f5e9;border-left:5px solid #4caf50;">
                <h4>Hasil Perhitungan:</h4>
                <p>Massa {nama} = <b>{massa:.4f} gram</b></p>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div style="padding:20px;border-radius:15px;background:#e3f2fd;border-left:5px solid #2196f3;">
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
            <div style="padding:20px;border-radius:15px;background:#e8f5e9;border-left:5px solid #4caf50;">
                <h4>Hasil Perhitungan:</h4>
                <p>Tekanan {nama} = <b>{P:.6f} atm</b></p>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div style="padding:20px;border-radius:15px;background:#e3f2fd;border-left:5px solid #2196f3;">
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
            <div style="padding:20px;border-radius:15px;background:#e8f5e9;border-left:5px solid #4caf50;">
                <h4>Hasil Perhitungan:</h4>
                <p>Volume {nama} = <b>{V:.4f} L</b></p>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.markdown("""
        <div style="padding:20px;border-radius:15px;background:#e3f2fd;border-left:5px solid #2196f3;">
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
            <div style="padding:20px;border-radius:15px;background:#e8f5e9;border-left:5px solid #4caf50;">
                <h4>Hasil Perhitungan:</h4>
                <p>Jumlah mol {nama} = <b>{n:.4f} mol</b></p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;padding:20px;">
    <p>© 2023 GasMaster Pro</p>
</div>
""", unsafe_allow_html=True)
