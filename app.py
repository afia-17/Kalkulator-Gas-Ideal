import streamlit as st

st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

R = 0.0821  # Konstanta gas ideal (atm·L/mol·K)

# Sidebar menu
st.sidebar.title("🧪 Kalkulator Gas Ideal")
menu = st.sidebar.radio("Navigasi Menu", ["Beranda", "Kalkulator", "Library"])

# ===== BERANDA =====
if menu == "Beranda":
    st.title("Selamat Datang!")
    st.markdown("""
    Aplikasi ini membantu kamu menghitung sifat-sifat gas menggunakan hukum **PV = nRT**:

    ✅ Massa gas  
    ✅ Tekanan gas  
    ✅ Volume gas  
    ✅ Jumlah mol gas  

    Juga tersedia **Library Gas Mulia** untuk info kimia, PBK, dan K3L-nya.
    """)
    st.markdown("#### 👨‍🔬 Kelompok 1 - Analisis Kimia")
    st.markdown("- Nama 1\n- Nama 2\n- Nama 3\n- Nama 4\n- Nama 5")

# ===== KALKULATOR =====
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    tabs = st.tabs(["Massa Gas", "Tekanan", "Volume", "Mol"])

    with tabs[0]:
        nama = st.text_input("Nama gas", key="massa_nama")
        n = st.number_input("Mol", key="massa_n", min_value=0.0)
        mr = st.number_input("Mr", key="massa_mr", min_value=0.0)
        if st.button("Hitung Massa"):
            st.success(f"Massa {nama}: {n * mr:.4f} gram")

    with tabs[1]:
        nama = st.text_input("Nama gas", key="P_nama")
        n = st.number_input("Mol", key="P_n", min_value=0.0)
        T = st.number_input("Suhu (K)", key="P_T", min_value=0.0)
        V = st.number_input("Volume (L)", key="P_V", min_value=0.0)
        if st.button("Hitung Tekanan"):
            if V > 0:
                P = (n * R * T) / V
                st.success(f"Tekanan {nama}: {P:.4f} atm")

    with tabs[2]:
        nama = st.text_input("Nama gas", key="V_nama")
        n = st.number_input("Mol", key="V_n", min_value=0.0)
        T = st.number_input("Suhu (K)", key="V_T", min_value=0.0)
        P = st.number_input("Tekanan (atm)", key="V_P", min_value=0.0)
        if st.button("Hitung Volume"):
            if P > 0:
                V = (n * R * T) / P
                st.success(f"Volume {nama}: {V:.4f} L")

    with tabs[3]:
        nama = st.text_input("Nama gas", key="n_nama")
        P = st.number_input("Tekanan (atm)", key="n_P", min_value=0.0)
        V = st.number_input("Volume (L)", key="n_V", min_value=0.0)
        T = st.number_input("Suhu (K)", key="n_T", min_value=0.0)
        if st.button("Hitung Mol"):
            if T > 0:
                n = (P * V) / (R * T)
                st.success(f"Mol {nama}: {n:.4f} mol")

# ===== LIBRARY =====
elif menu == "Library":
    st.title("📚 Library Gas Mulia")
    pilihan = st.selectbox("Pilih gas:", [
        "Helium (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)", "Xenon (Xe)", "Radon (Rn)"
    ])

    info = {
        "Helium (He)": {
            "rumus": "He",
            "sifat": "Ringan, inert, tidak mudah terbakar",
            "pbk": "Asfiksia dalam ruangan tertutup",
            "k3l": "Gunakan ventilasi, simpan tabung aman"
        },
        "Neon (Ne)": {
            "rumus": "Ne",
            "sifat": "Inert, digunakan untuk lampu neon",
            "pbk": "Asfiksia bila dalam jumlah besar",
            "k3l": "Waspada kebocoran, simpan tabung dingin"
        },
        "Argon (Ar)": {
            "rumus": "Ar",
            "sifat": "Inert, berat dari udara",
            "pbk": "Menggantikan oksigen dalam ruangan tertutup",
            "k3l": "Simpan tabung tegak, hindari panas"
        },
        "Krypton (Kr)": {
            "rumus": "Kr",
            "sifat": "Jarang, tidak reaktif",
            "pbk": "Asfiksia dalam ruang tertutup",
            "k3l": "Gunakan APD jika digunakan di laboratorium"
        },
        "Xenon (Xe)": {
            "rumus": "Xe",
            "sifat": "Digunakan dalam anestesi & lampu flash",
            "pbk": "Efek sedatif/anestetik",
            "k3l": "Gunakan APD, simpan dengan aman"
        },
        "Radon (Rn)": {
            "rumus": "Rn",
            "sifat": "Radioaktif, berbahaya",
            "pbk": "Karsinogenik, bersifat radioaktif",
            "k3l": "Gunakan detektor radiasi, hindari paparan"
        }
    }

    st.markdown(f"**🔬 Rumus Molekul:** {info[pilihan]['rumus']}")
    st.markdown(f"**⚗️ Sifat:** {info[pilihan]['sifat']}")
    st.markdown(f"**☣️ PBK:** {info[pilihan]['pbk']}")
    st.markdown(f"**🦺 K3L:** {info[pilihan]['k3l']}")
