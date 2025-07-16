import streamlit as st

st.title("🧪 Kalkulator Gas Ideal")

tab1, tab2, tab3, tab4 = st.tabs(["Massa Gas", "Tekanan Gas", "Volume Gas", "Jumlah Mol Gas"])

R = 0.0821  # Konstanta gas ideal dalam L·atm/mol·K

# Tab 1: Massa Gas
with tab1:
    st.subheader("🔹 Hitung Massa Gas (gram = mol × Mr)")
    nama_gas1 = st.text_input("Nama Gas", key="gas1")
    mol1 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol1")
    mr1 = st.number_input("Massa molar (Mr) dalam g/mol", min_value=0.0, key="mr1")
    
    if st.button("Tampilkan Massa Gas"):
        massa = mol1 * mr1
        st.success(f"Massa {nama_gas1} = {massa:.4f} gram")

# Tab 2: Tekanan Gas
with tab2:
    st.subheader("🔹 Hitung Tekanan Gas (P = nRT / V)")
    nama_gas2 = st.text_input("Nama Gas", key="gas2")
    mol2 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol2")
    suhu2 = st.number_input("Suhu (K)", min_value=0.0, key="suhu2")
    volume2 = st.number_input("Volume (L)", min_value=0.0, key="vol2")
    
    if st.button("Tampilkan Tekanan Gas"):
        if volume2 > 0:
            tekanan = (mol2 * R * suhu2) / volume2
            st.success(f"Tekanan {nama_gas2} = {tekanan:.4f} atm")
        else:
            st.error("Volume tidak boleh nol")

# Tab 3: Volume Gas
with tab3:
    st.subheader("🔹 Hitung Volume Gas (V = nRT / P)")
    nama_gas3 = st.text_input("Nama Gas", key="gas3")
    mol3 = st.number_input("Jumlah mol (mol)", min_value=0.0, key="mol3")
    suhu3 = st.number_input("Suhu (K)", min_value=0.0, key="suhu3")
    tekanan3 = st.number_input("Tekanan (atm)", min_value=0.0, key="tek3")
    
    if st.button("Tampilkan Volume Gas"):
        if tekanan3 > 0:
            volume = (mol3 * R * suhu3) / tekanan3
            st.success(f"Volume {nama_gas3} = {volume:.4f} L")
        else:
            st.error("Tekanan tidak boleh nol")

# Tab 4: Jumlah Mol Gas
with tab4:
    st.subheader("🔹 Hitung Jumlah Mol Gas (n = PV / RT)")
    nama_gas4 = st.text_input("Nama Gas", key="gas4")
    tekanan4 = st.number_input("Tekanan (atm)", min_value=0.0, key="tek4")
    volume4 = st.number_input("Volume (L)", min_value=0.0, key="vol4")
    suhu4 = st.number_input("Suhu (K)", min_value=0.0, key="suhu4")

    if st.button("Tampilkan Jumlah Mol Gas"):
        if suhu4 > 0:
            mol = (tekanan4 * volume4) / (R * suhu4)
            st.success(f"Jumlah mol {nama_gas4} = {mol:.4f} mol")
        else:
            st.error("Suhu tidak boleh nol")
