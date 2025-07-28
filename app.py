import streamlit as st
import math

def main():
    st.set_page_config(
        page_title="ChemGasMaster",
        page_icon="⚗️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS dengan background baru
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }
    
    /* Background untuk Calculator */
    .calculator-bg {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .calculator-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
    }
    
    .calculator-content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Background untuk Encyclopedia */
    .encyclopedia-bg {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .encyclopedia-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
    }
    
    .encyclopedia-content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Background untuk Safety Guide */
    .safety-bg {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .safety-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
    }
    
    .safety-content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Background untuk Unit Converter */
    .converter-bg {
        background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        position: relative;
        overflow: hidden;
    }
    
    .converter-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border-radius: 15px;
    }
    
    .converter-content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .stNumberInput > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.2rem;
        font-weight: bold;
    }
    
    .info-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .gas-table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .gas-table th {
        background: #667eea;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    
    .gas-table td {
        padding: 12px;
        border-bottom: 1px solid #dee2e6;
    }
    
    .gas-table tr:hover {
        background-color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>⚗️ ChemGasMaster</h1>
        <p>Aplikasi Lengkap untuk Perhitungan Gas Kimia</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.title("🧭 Navigasi")
    menu = st.sidebar.selectbox(
        "Pilih Menu:",
        ["🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan", "🔄 Konversi Unit"]
    )
    
    if menu == "🧮 Kalkulator Gas":
        calculator_section()
    elif menu == "📚 Ensiklopedia Gas":
        encyclopedia_section()
    elif menu == "⚠️ Panduan Keselamatan":
        safety_section()
    elif menu == "🔄 Konversi Unit":
        unit_converter_section()

def calculator_section():
    st.markdown('<div class="calculator-bg"><div class="calculator-content">', unsafe_allow_html=True)
    
    st.title("🧮 Kalkulator Gas")
    
    calc_type = st.selectbox(
        "Pilih jenis perhitungan:",
        ["Hukum Gas Ideal", "Hukum Boyle", "Hukum Charles", "Hukum Gay-Lussac", "Hukum Avogadro"]
    )
    
    if calc_type == "Hukum Gas Ideal":
        st.subheader("Hukum Gas Ideal: PV = nRT")
        
        col1, col2 = st.columns(2)
        
        with col1:
            P = st.number_input("Tekanan (P) dalam atm:", min_value=0.0, value=1.0, step=0.1)
            V = st.number_input("Volume (V) dalam L:", min_value=0.0, value=22.4, step=0.1)
        
        with col2:
            n = st.number_input("Jumlah mol (n):", min_value=0.0, value=1.0, step=0.1)
            T = st.number_input("Suhu (T) dalam K:", min_value=0.0, value=273.15, step=0.1)
        
        R = 0.0821  # L⋅atm/(mol⋅K)
        
        if st.button("Hitung", key="ideal_gas"):
            result = P * V / (n * R)
            st.markdown(f"""
            <div class="result-box">
                Hasil Perhitungan Hukum Gas Ideal:<br>
                Suhu Teoritis = {result:.2f} K<br>
                = {result - 273.15:.2f} °C
            </div>
            """, unsafe_allow_html=True)
    
    elif calc_type == "Hukum Boyle":
        st.subheader("Hukum Boyle: P₁V₁ = P₂V₂")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Kondisi Awal:**")
            P1 = st.number_input("Tekanan awal (P₁) dalam atm:", min_value=0.0, value=1.0, step=0.1)
            V1 = st.number_input("Volume awal (V₁) dalam L:", min_value=0.0, value=10.0, step=0.1)
        
        with col2:
            st.write("**Kondisi Akhir:**")
            P2 = st.number_input("Tekanan akhir (P₂) dalam atm:", min_value=0.0, value=2.0, step=0.1)
        
        if st.button("Hitung Volume Akhir", key="boyle"):
            V2 = (P1 * V1) / P2
            st.markdown(f"""
            <div class="result-box">
                Volume Akhir (V₂) = {V2:.2f} L
            </div>
            """, unsafe_allow_html=True)
    
    elif calc_type == "Hukum Charles":
        st.subheader("Hukum Charles: V₁/T₁ = V₂/T₂")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Kondisi Awal:**")
            V1 = st.number_input("Volume awal (V₁) dalam L:", min_value=0.0, value=10.0, step=0.1)
            T1 = st.number_input("Suhu awal (T₁) dalam K:", min_value=0.0, value=273.15, step=0.1)
        
        with col2:
            st.write("**Kondisi Akhir:**")
            T2 = st.number_input("Suhu akhir (T₂) dalam K:", min_value=0.0, value=373.15, step=0.1)
        
        if st.button("Hitung Volume Akhir", key="charles"):
            V2 = (V1 * T2) / T1
            st.markdown(f"""
            <div class="result-box">
                Volume Akhir (V₂) = {V2:.2f} L
            </div>
            """, unsafe_allow_html=True)
    
    elif calc_type == "Hukum Gay-Lussac":
        st.subheader("Hukum Gay-Lussac: P₁/T₁ = P₂/T₂")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Kondisi Awal:**")
            P1 = st.number_input("Tekanan awal (P₁) dalam atm:", min_value=0.0, value=1.0, step=0.1)
            T1 = st.number_input("Suhu awal (T₁) dalam K:", min_value=0.0, value=273.15, step=0.1)
        
        with col2:
            st.write("**Kondisi Akhir:**")
            T2 = st.number_input("Suhu akhir (T₂) dalam K:", min_value=0.0, value=373.15, step=0.1)
        
        if st.button("Hitung Tekanan Akhir", key="gay_lussac"):
            P2 = (P1 * T2) / T1
            st.markdown(f"""
            <div class="result-box">
                Tekanan Akhir (P₂) = {P2:.2f} atm
            </div>
            """, unsafe_allow_html=True)
    
    elif calc_type == "Hukum Avogadro":
        st.subheader("Hukum Avogadro: V₁/n₁ = V₂/n₂")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Kondisi Awal:**")
            V1 = st.number_input("Volume awal (V₁) dalam L:", min_value=0.0, value=22.4, step=0.1)
            n1 = st.number_input("Jumlah mol awal (n₁):", min_value=0.0, value=1.0, step=0.1)
        
        with col2:
            st.write("**Kondisi Akhir:**")
            n2 = st.number_input("Jumlah mol akhir (n₂):", min_value=0.0, value=2.0, step=0.1)
        
        if st.button("Hitung Volume Akhir", key="avogadro"):
            V2 = (V1 * n2) / n1
            st.markdown(f"""
            <div class="result-box">
                Volume Akhir (V₂) = {V2:.2f} L
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

def encyclopedia_section():
    st.markdown('<div class="encyclopedia-bg"><div class="encyclopedia-content">', unsafe_allow_html=True)
    
    st.title("📚 Ensiklopedia Gas")
    
    gas_list = [
        "Hidrogen (H₂)", "Oksigen (O₂)", "Nitrogen (N₂)", "Karbon Dioksida (CO₂)", 
        "Karbon Monoksida (CO)", "Amonia (NH₃)", "Metana (CH₄)", "Helium (He)"
    ]
    
    selected_gas = st.selectbox("Pilih gas untuk informasi lengkap:", gas_list)
    
    gas_data = {
        "Hidrogen (H₂)": {
            "formula": "H₂",
            "molecular_weight": "2.016 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Diatomik, ikatan tunggal",
            "density": "0.08988 g/L (STP)",
            "boiling_point": "-252.87°C",
            "melting_point": "-259.16°C",
            "solubility": "Sedikit larut dalam air",
            "hazards": "Gas mudah terbakar, dapat meledak",
            "first_aid": "Jika terhirup dalam konsentrasi tinggi, pindah ke udara segar",
            "storage": "Simpan dalam wadah bertekanan di tempat kering dan sejuk"
        },
        "Oksigen (O₂)": {
            "formula": "O₂",
            "molecular_weight": "31.998 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Diatomik, ikatan ganda",
            "density": "1.429 g/L (STP)",
            "boiling_point": "-182.96°C",
            "melting_point": "-218.79°C",
            "solubility": "Sedikit larut dalam air",
            "hazards": "Oksidator kuat, meningkatkan risiko kebakaran",
            "first_aid": "Umumnya aman, hindari konsentrasi sangat tinggi",
            "storage": "Simpan di tempat sejuk, jauhkan dari bahan mudah terbakar"
        },
        "Nitrogen (N₂)": {
            "formula": "N₂",
            "molecular_weight": "28.014 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Diatomik, ikatan tripel",
            "density": "1.2506 g/L (STP)",
            "boiling_point": "-195.79°C",
            "melting_point": "-210.00°C",
            "solubility": "Sedikit larut dalam air",
            "hazards": "Dapat menyebabkan sesak napas dalam ruang tertutup",
            "first_aid": "Jika sesak napas, pindah ke udara segar",
            "storage": "Simpan dalam wadah bertekanan di tempat sejuk"
        },
        "Karbon Dioksida (CO₂)": {
            "formula": "CO₂",
            "molecular_weight": "44.01 g/mol",
            "appearance": "Gas tak berwarna, sedikit berbau asam",
            "structure": "Linear, ikatan ganda",
            "density": "1.977 g/L (STP)",
            "boiling_point": "-78.5°C (sublimasi)",
            "melting_point": "-56.6°C (tekanan tinggi)",
            "solubility": "Larut dalam air membentuk asam karbonat",
            "hazards": "Dapat menyebabkan sesak napas, asfiksia",
            "first_aid": "Pindah ke udara segar, berikan oksigen jika perlu",
            "storage": "Simpan dalam wadah bertekanan di tempat sejuk"
        },
        "Karbon Monoksida (CO)": {
            "formula": "CO",
            "molecular_weight": "28.01 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Diatomik, ikatan tripel",
            "density": "1.250 g/L (STP)",
            "boiling_point": "-191.5°C",
            "melting_point": "-205.02°C",
            "solubility": "Sedikit larut dalam air",
            "hazards": "Sangat beracun, menyebabkan keracunan CO",
            "first_aid": "Segera pindah ke udara segar, berikan oksigen, hubungi medis",
            "storage": "Simpan dengan ventilasi baik, gunakan detektor CO"
        },
        "Amonia (NH₃)": {
            "formula": "NH₃",
            "molecular_weight": "17.031 g/mol",
            "appearance": "Gas tak berwarna, berbau menyengat",
            "structure": "Piramidal, ikatan polar",
            "density": "0.7710 g/L (STP)",
            "boiling_point": "-33.34°C",
            "melting_point": "-77.73°C",
            "solubility": "Sangat larut dalam air",
            "hazards": "Korosif, iritasi mata dan saluran pernapasan",
            "first_aid": "Bilas mata dengan air, pindah ke udara segar",
            "storage": "Simpan di tempat sejuk, gunakan APD"
        },
        "Metana (CH₄)": {
            "formula": "CH₄",
            "molecular_weight": "16.04 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Tetrahedral",
            "density": "0.7168 g/L (STP)",
            "boiling_point": "-161.5°C",
            "melting_point": "-182.5°C",
            "solubility": "Sedikit larut dalam air",
            "hazards": "Mudah terbakar, dapat meledak",
            "first_aid": "Jika kebocoran, ventilasi area, hindari sumber api",
            "storage": "Simpan dalam wadah bertekanan, jauhkan dari panas"
        },
        "Helium (He)": {
            "formula": "He",
            "molecular_weight": "4.003 g/mol",
            "appearance": "Gas tak berwarna, tak berbau",
            "structure": "Gas mulia, atom tunggal",
            "density": "0.1786 g/L (STP)",
            "boiling_point": "-268.93°C",
            "melting_point": "-272.20°C (tekanan tinggi)",
            "solubility": "Tidak larut dalam air",
            "hazards": "Tidak beracun, tapi dapat menyebabkan asfiksia",
            "first_aid": "Jika sesak napas, pindah ke udara segar",
            "storage": "Simpan dalam wadah bertekanan di tempat sejuk"
        }
    }
    
    if selected_gas in gas_data:
        data = gas_data[selected_gas]
        
        st.subheader(f"Informasi Lengkap: {selected_gas}")
        
        # Informasi Dasar
        st.markdown("### 🧪 Informasi Dasar")
        st.markdown(f"""
        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <table class="gas-table">
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Rumus
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['formula']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Massa Molar
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['molecular_weight']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Penampilan
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['appearance']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Struktur
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['structure']}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
        # Sifat Fisika
        st.markdown("### 🌡️ Sifat Fisika")
        st.markdown(f"""
        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <table class="gas-table">
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Densitas (STP)
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['density']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Titik Didih
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['boiling_point']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Titik Lebur
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['melting_point']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Kelarutan
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['solubility']}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
        # Keselamatan
        st.markdown("### ⚠️ Informasi Keselamatan")
        st.markdown(f"""
        <div style="background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <table class="gas-table">
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Bahaya
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['hazards']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Pertolongan Pertama
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['first_aid']}
                    </td>
                </tr>
                <tr>
                    <td style="padding: 12px; font-weight: bold; background: #f8f9fa; width: 40%; border-bottom: 1px solid #dee2e6;">
                        Penyimpanan
                    </td>
                    <td style="padding: 12px; background: white; border-bottom: 1px solid #dee2e6;">
                        {data['storage']}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

def safety_section():
    st.markdown('<div class="safety-bg"><div class="safety-content">', unsafe_allow_html=True)
    
    st.title("⚠️ Panduan Keselamatan")
    
    safety_categories = [
        "Prosedur Umum Keselamatan",
        "Alat Pelindung Diri (APD)",
        "Penanganan Gas Beracun",
        "Penanganan Gas Mudah Terbakar",
        "Prosedur Darurat",
        "Ventilasi dan Penyimpanan"
    ]
    
    selected_category = st.selectbox("Pilih kategori keselamatan:", safety_categories)
    
    if selected_category == "Prosedur Umum Keselamatan":
        st.subheader("🛡️ Prosedur Umum Keselamatan")
        
        st.markdown("""
        <div class="info-box">
            <h4>📋 Checklist Keselamatan Dasar:</h4>
            <ul>
                <li>Selalu baca Safety Data Sheet (SDS) sebelum bekerja dengan gas</li>
                <li>Pastikan area kerja memiliki ventilasi yang memadai</li>
                <li>Gunakan APD yang sesuai untuk jenis gas yang ditangani</li>
                <li>Periksa kebocoran pada sistem gas secara berkala</li>
                <li>Jangan pernah bekerja sendirian dengan gas berbahaya</li>
                <li>Pastikan alat pemadam api tersedia dan mudah dijangkau</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="warning-box">
            <h4>⚠️ Larangan Mutlak:</h4>
            <ul>
                <li>Jangan merokok atau membuat api dekat gas mudah terbakar</li>
                <li>Jangan menggunakan gas untuk keperluan selain yang ditentukan</li>
                <li>Jangan memodifikasi atau memperbaiki peralatan gas tanpa izin</li>
                <li>Jangan menyimpan gas di tempat yang tidak sesuai</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif selected_category == "Alat Pelindung Diri (APD)":
        st.subheader("🥽 Alat Pelindung Diri (APD)")
        
        st.markdown("""
        ### APD Berdasarkan Jenis Gas:
        
        **Gas Korosif (NH₃, HCl, dll):**
        - Respirator dengan filter kimia
        - Kacamata pengaman tertutup
        - Sarung tangan tahan kimia (nitrile/neoprene)
        - Pakaian pelindung tahan kimia
        
        **Gas Beracun (CO, H₂S, dll):**
        - Self-Contained Breathing Apparatus (SCBA)
        - Detektor gas portabel
        - Pakaian pelindung penuh
        - Sepatu safety anti-statis
        
        **Gas Mudah Terbakar (H₂, CH₄, dll):**
        - Pakaian anti-statis
        - Sepatu safety anti-percik api
        - Kacamata safety
        - Sarung tangan isolasi
        """)
    
    elif selected_category == "Penanganan Gas Beracun":
        st.subheader("☠️ Penanganan Gas Beracun")
        
        st.markdown("""
        <div class="warning-box">
            <h4>🚨 Gas Sangat Beracun:</h4>
            <p><strong>Karbon Monoksida (CO):</strong></p>
            <ul>
                <li>Konsentrasi 0.1% dapat mematikan dalam 1 jam</li>
                <li>Gejala: pusing, mual, sakit kepala, pingsan</li>
                <li>Pertolongan: pindah ke udara segar, oksigen, hubungi medis</li>
            </ul>
            
            <p><strong>Hidrogen Sulfida (H₂S):</strong></p>
            <ul>
                <li>Berbau telur busuk pada konsentrasi rendah</li>
                <li>Pada konsentrasi tinggi merusak indera penciuman</li>
                <li>Pertolongan: hindari area, gunakan SCBA, evakuasi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### Prosedur Penanganan:
        1. **Deteksi Dini:** Gunakan detektor gas kontinyu
        2. **Isolasi Area:** Batasi akses ke area berisiko
        3. **Ventilasi:** Pastikan ventilasi memadai
        4. **Monitoring:** Pantau konsentrasi secara berkala
        5. **Evakuasi:** Siapkan jalur evakuasi darurat
        """)
    
    elif selected_category == "Penanganan Gas Mudah Terbakar":
        st.subheader("🔥 Penanganan Gas Mudah Terbakar")
        
        st.markdown("""
        ### Klasifikasi Bahaya Kebakaran:
        
        **Hidrogen (H₂):**
        - Batas mudah terbakar: 4-75% di udara
        - Energi ignisi sangat rendah
        - Nyala tidak terlihat di siang hari
        
        **Metana (CH₄):**
        - Batas mudah terbakar: 5-15% di udara
        - Lebih ringan dari udara, cenderung naik
        - Dapat terakumulasi di langit-langit
        
        ### Pencegahan Kebakaran:
        """)
        
        st.markdown("""
        <div class="info-box">
            <h4>🛡️ Sistem Pencegahan:</h4>
            <ul>
                <li>Sistem deteksi gas otomatis</li>
                <li>Ventilasi paksa dengan sensor</li>
                <li>Grounding dan bonding peralatan</li>
                <li>Eliminasi sumber ignisi</li>
                <li>Sistem supresi otomatis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif selected_category == "Prosedur Darurat":
        st.subheader("🚨 Prosedur Darurat")
        
        st.markdown("""
        ### Tanggap Darurat Kebocoran Gas:
        
        **Langkah Immediate (0-5 menit):**
        1. Aktifkan alarm darurat
        2. Hentikan sumber kebocoran jika aman
        3. Evakuasi personel dari area bahaya
        4. Hubungi tim tanggap darurat
        
        **Langkah Jangka Pendek (5-30 menit):**
        1. Isolasi area dengan jarak aman
        2. Monitoring konsentrasi gas
        3. Ventilasi area jika memungkinkan
        4. Siapkan peralatan darurat
        
        **Pemulihan:**
        1. Konfirmasi area aman dengan detektor
        2. Investigasi penyebab kebocoran
        3. Perbaikan dan testing sistem
        4. Dokumentasi insiden
        """)
        
        st.markdown("""
        <div class="warning-box">
            <h4>📞 Kontak Darurat:</h4>
            <ul>
                <li>Pemadam Kebakaran: 113</li>
                <li>Ambulans: 118/119</li>
                <li>Polisi: 110</li>
                <li>Tim Tanggap Darurat Internal: [Nomor Internal]</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    elif selected_category == "Ventilasi dan Penyimpanan":
        st.subheader("💨 Ventilasi dan Penyimpanan")
        
        st.markdown("""
        ### Sistem Ventilasi:
        
        **Ventilasi Umum:**
        - Minimum 6-12 ACH (Air Changes per Hour)
        - Intake udara dari area bersih
        - Exhaust di titik tertinggi untuk gas ringan
        - Exhaust di titik terendah untuk gas berat
        
        **Ventilasi Lokal:**
        - Fume hood untuk gas beracun
        - Local exhaust di titik kebocoran potensial
        - Sistem interlock dengan detektor gas
        """)
        
        st.markdown("""
        ### Penyimpanan Gas:
        
        **Prinsip Dasar:**
        - Pisahkan gas berdasarkan kompabilitas
        - Simpan di area berventilasi baik
        - Jauhkan dari sumber panas dan ignisi
        - Label yang jelas dan mudah dibaca
        - Sistem restraint untuk tabung gas
        
        **Matriks Kompatibilitas:**
        """)
        
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <table class="gas-table">
                <tr>
                    <th>Gas</th>
                    <th>Dapat Disimpan Dengan</th>
                    <th>Tidak Boleh Dengan</th>
                </tr>
                <tr>
                    <td>Oksigen</td>
                    <td>Gas inert (He, Ar, N₂)</td>
                    <td>Gas mudah terbakar, oli, gemuk</td>
                </tr>
                <tr>
                    <td>Hidrogen</td>
                    <td>Gas inert</td>
                    <td>Oksigen, gas pengoksidasi</td>
                </tr>
                <tr>
                    <td>Amonia</td>
                    <td>Gas inert</td>
                    <td>Halogen, asam</td>
                </tr>
                <tr>
                    <td>CO₂</td>
                    <td>Gas inert, oksigen</td>
                    <td>Logam alkali</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

def unit_converter_section():
    st.markdown('<div class="converter-bg"><div class="converter-content">', unsafe_allow_html=True)
    
    st.title("🔄 Konversi Unit")
    
    conversion_type = st.selectbox(
        "Pilih jenis konversi:",
        ["Tekanan", "Volume", "Suhu", "Massa", "Konsentrasi"]
    )
    
    if conversion_type == "Tekanan":
        st.subheader("📏 Konversi Tekanan")
        
        col1, col2 = st.columns(2)
        
        with col1:
            pressure_value = st.number_input("Masukkan nilai tekanan:", min_value=0.0, value=1.0, step=0.1)
            from_unit = st.selectbox("Dari unit:", ["atm", "bar", "Pa", "kPa", "mmHg", "psi"])
        
        with col2:
            to_unit = st.selectbox("Ke unit:", ["atm", "bar", "Pa", "kPa", "mmHg", "psi"])
        
        # Konversi ke Pa sebagai unit dasar
        to_pa_factors = {
            "atm": 101325,
            "bar": 100000,
            "Pa": 1,
            "kPa": 1000,
            "mmHg": 133.322,
            "psi": 6894.76
        }
        
        if st.button("Konversi Tekanan"):
            # Konversi ke Pa dulu, kemudian ke unit tujuan
            pa_value = pressure_value * to_pa_factors[from_unit]
            result = pa_value / to_pa_factors[to_unit]
            
            st.markdown(f"""
            <div class="result-box">
                {pressure_value} {from_unit} = {result:.6f} {to_unit}
            </div>
            """, unsafe_allow_html=True)
    
    elif conversion_type == "Volume":
        st.subheader("📦 Konversi Volume")
        
        col1, col2 = st.columns(2)
        
        with col1:
            volume_value = st.number_input("Masukkan nilai volume:", min_value=0.0, value=1.0, step=0.1)
            from_unit = st.selectbox("Dari unit:", ["L", "mL", "m³", "cm³", "ft³", "gal"])
        
        with col2:
            to_unit = st.selectbox("Ke unit:", ["L", "mL", "m³", "cm³", "ft³", "gal"])
        
        # Konversi ke Liter sebagai unit dasar
        to_l_factors = {
            "L": 1,
            "mL": 0.001,
            "m³": 1000,
            "cm³": 0.001,
            "ft³": 28.3168,
            "gal": 3.78541
        }
        
        if st.button("Konversi Volume"):
            l_value = volume_value * to_l_factors[from_unit]
            result = l_value / to_l_factors[to_unit]
            
            st.markdown(f"""
            <div class="result-box">
                {volume_value} {from_unit} = {result:.6f} {to_unit}
            </div>
            """, unsafe_allow_html=True)
    
    elif conversion_type == "Suhu":
        st.subheader("🌡️ Konversi Suhu")
        
        col1, col2 = st.columns(2)
        
        with col1:
            temp_value = st.number_input("Masukkan nilai suhu:", value=25.0, step=0.1)
            from_unit = st.selectbox("Dari unit:", ["°C", "°F", "K", "°R"])
        
        with col2:
            to_unit = st.selectbox("Ke unit:", ["°C", "°F", "K", "°R"])
        
        if st.button("Konversi Suhu"):
            # Konversi ke Celsius dulu
            if from_unit == "°C":
                celsius = temp_value
            elif from_unit == "°F":
                celsius = (temp_value - 32) * 5/9
            elif from_unit == "K":
                celsius = temp_value - 273.15
            elif from_unit == "°R":
                celsius = (temp_value - 491.67) * 5/9
            
            # Konversi dari Celsius ke unit tujuan
            if to_unit == "°C":
                result = celsius
            elif to_unit == "°F":
                result = celsius * 9/5 + 32
            elif to_unit == "K":
                result = celsius + 273.15
            elif to_unit == "°R":
                result = celsius * 9/5 + 491.67
            
            st.markdown(f"""
            <div class="result-box">
                {temp_value} {from_unit} = {result:.2f} {to_unit}
            </div>
            """, unsafe_allow_html=True)
    
    elif conversion_type == "Massa":
        st.subheader("⚖️ Konversi Massa")
        
        col1, col2 = st.columns(2)
        
        with col1:
            mass_value = st.number_input("Masukkan nilai massa:", min_value=0.0, value=1.0, step=0.1)
            from_unit = st.selectbox("Dari unit:", ["g", "kg", "mg", "lb", "oz", "ton"])
        
        with col2:
            to_unit = st.selectbox("Ke unit:", ["g", "kg", "mg", "lb", "oz", "ton"])
        
        # Konversi ke gram sebagai unit dasar
        to_g_factors = {
            "g": 1,
            "kg": 1000,
            "mg": 0.001,
            "lb": 453.592,
            "oz": 28.3495,
            "ton": 1000000
        }
        
        if st.button("Konversi Massa"):
            g_value = mass_value * to_g_factors[from_unit]
            result = g_value / to_g_factors[to_unit]
            
            st.markdown(f"""
            <div class="result-box">
                {mass_value} {from_unit} = {result:.6f} {to_unit}
            </div>
            """, unsafe_allow_html=True)
    
    elif conversion_type == "Konsentrasi":
        st.subheader("⚗️ Konversi Konsentrasi Gas")
        
        st.write("Konversi antara ppm, mg/m³, dan % volume untuk gas pada kondisi standar")
        
        col1, col2 = st.columns(2)
        
        with col1:
            conc_value = st.number_input("Masukkan nilai konsentrasi:", min_value=0.0, value=100.0, step=0.1)
            from_unit = st.selectbox("Dari unit:", ["ppm", "mg/m³", "% vol"])
            molecular_weight = st.number_input("Massa molekul gas (g/mol):", min_value=1.0, value=28.0, step=0.1)
        
        with col2:
            to_unit = st.selectbox("Ke unit:", ["ppm", "mg/m³", "% vol"])
        
        if st.button("Konversi Konsentrasi"):
            # Konversi ke ppm sebagai unit dasar (pada STP: 25°C, 1 atm)
            if from_unit == "ppm":
                ppm_value = conc_value
            elif from_unit == "mg/m³":
                ppm_value = conc_value * 24.45 / molecular_weight
            elif from_unit == "% vol":
                ppm_value = conc_value * 10000
            
            # Konversi dari ppm ke unit tujuan
            if to_unit == "ppm":
                result = ppm_value
            elif to_unit == "mg/m³":
                result = ppm_value * molecular_weight / 24.45
            elif to_unit == "% vol":
                result = ppm_value / 10000
            
            st.markdown(f"""
            <div class="result-box">
                {conc_value} {from_unit} = {result:.6f} {to_unit}<br>
                (pada kondisi standar: 25°C, 1 atm)
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
