import streamlit as st

st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

# Inisialisasi session state
if 'show_calc' not in st.session_state:
    st.session_state.show_calc = False

# Halaman Awal
if not st.session_state.show_calc:
    st.title("🧪 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("""
    Selamat datang di **Kalkulator Gas Ideal** berbasis Web!
    
    Aplikasi ini dapat membantu menghitung berbagai parameter gas menggunakan hukum:
    \n\n**PV = nRT**

    Fitur yang tersedia:
    - Menghitung massa gas
    - Menghitung tekanan
    - Menghitung volume
    - Menghitung jumlah mol gas

    ---
    """)
    
    st.markdown("#### 👨‍🔬 Dibuat oleh: Kelompok 2 Kelas 1A")
    st.markdown("- Afia Hikmawati\n- Ikbal (tambahkan sesuai anggota)")
    
    if st.button("➡️ Masuk ke Kalkulator"):
        st.session_state.show_calc = True
        st.experimental_rerun()

# Halaman Kalkulator
else:
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("Gunakan tab di bawah untuk menghitung berbagai parameter gas.")

    tabs = st.tabs(["Massa Gas", "Tekanan Gas", "Volume Gas", "Jumlah Mol Gas"])
    R = 0.0821  # Konstanta gas ideal (atm·L/mol·K)

    # Tab 1: Massa Gas
    with tabs[0]:
        st.subheader("🔹 Hitung Massa Gas")
        nama_gas1 = st.text_input("Nama gas", key="gas1")
        mol1 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol1")
        mr1 = st.number_input("Massa molar (g/mol)", min_value=0.0, key="mr1")
        if st.button("Tampilkan Massa Gas"):
            massa = mol1 * mr1
            st.success(f"Massa gas {nama_gas1}: {massa:.4f} gram")

    # Tab 2: Tekanan Gas
    with tabs[1]:
        st.subheader("🔹 Hitung Tekanan Gas")
        nama_gas2 = st.text_input("Nama gas", key="gas2")
        mol2 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol2")
        T2 = st.number_input("Suhu (K)", min_value=0.0, key="T2")
        V2 = st.number_input("Volume (L)", min_value=0.0, key="V2")
        if st.button("Tampilkan Tekanan Gas"):
            if V2 > 0:
                P = (mol2 * R * T2) / V2
                st.success(f"Tekanan gas {nama_gas2}: {P:.4f} atm")
            else:
                st.error("Volume tidak boleh nol")

    # Tab 3: Volume Gas
    with tabs[2]:
        st.subheader("🔹 Hitung Volume Gas")
        nama_gas3 = st.text_input("Nama gas", key="gas3")
        mol3 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol3")
        T3 = st.number_input("Suhu (K)", min_value=0.0, key="T3")
        P3 = st.number_input("Tekanan (atm)", min_value=0.0, key="P3")
        if st.button("Tampilkan Volume Gas"):
            if P3 > 0:
                V = (mol3 * R * T3) / P3
                st.success(f"Volume gas {nama_gas3}: {V:.4f} liter")
            else:
                st.error("Tekanan tidak boleh nol")

    # Tab 4: Jumlah Mol Gas
    with tabs[3]:
        st.subheader("🔹 Hitung Jumlah Mol Gas")
        nama_gas4 = st.text_input("Nama gas", key="gas4")
        P4 = st.number_input("Tekanan (atm)", min_value=0.0, key="P4")
        V4 = st.number_input("Volume (L)", min_value=0.0, key="V4")
        T4 = st.number_input("Suhu (K)", min_value=0.0, key="T4")
        if st.button("Tampilkan Jumlah Mol Gas"):
            if T4 > 0:
                n = (P4 * V4) / (R * T4)
                st.success(f"Jumlah mol gas {nama_gas4}: {n:.4f} mol")
            else:
                st.error("Suhu tidak boleh nol")
