# ===========================================
# APLIKASI KALKULATOR GAS IDEAL + ENSIKLOPEDIA
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
    .input-container {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .input-number {
        flex: 3;
    }
    .input-unit {
        flex: 1;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# FUNGSI KONVERSI YANG DIPERBAIKI
# ===========================================
def konversi_suhu(label, key_prefix):
    st.markdown(f'<div class="input-container"><div class="input-number">{label}</div>', unsafe_allow_html=True)
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
    st.markdown(f'<div class="input-container"><div class="input-number">{label}</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3,1])
    with col1:
        P_input = st.number_input(label, min_value=0.0, key=f"{key_prefix}_input", label_visibility="collapsed")
    with col2:
        satuan = st.selectbox("Satuan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg", "L.atm"], 
                            key=f"{key_prefix}_unit", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if satuan == "Pa":
        P = P_input / 101325
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} Pa = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    elif satuan == "kPa":
        P = P_input / 101.325
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} kPa = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    elif satuan == "hPa":
        P = P_input / 1013.25
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} hPa = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    elif satuan == "bar":
        P = P_input / 1.01325
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} bar = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    elif satuan in ["Torr", "mmHg"]:
        P = P_input / 760
        st.markdown(f"""
        <div class="conversion-box">
            🔄 Konversi: {P_input} {satuan} = {P:.6f} atm
        </div>
        """, unsafe_allow_html=True)
    elif satuan == "L.atm":
        P = P_input
        st.markdown(f"""
        <div class="conversion-box">
            🔄 1 L·atm = 1 atm (tidak perlu konversi)
        </div>
        """, unsafe_allow_html=True)
    else:
        P = P_input
    return P

def konversi_volume(label, key_prefix):
    st.markdown(f'<div class="input-container"><div class="input-number">{label}</div>', unsafe_allow_html=True)
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
# BAGIAN LAIN TETAP SAMA
# ===========================================
# [DATABASE GAS, MENU SIDEBAR, HALAMAN UTAMA, DLL...]
# Tetap sama seperti kode sebelumnya, hanya fungsi konversi yang diubah
