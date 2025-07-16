import streamlit as st

st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

# Inisialisasi tampilan awal
if 'halaman' not in st.session_state:
    st.session_state.halaman = 'awal'

# Halaman Awal
if st.session_state.halaman == 'awal':
    st.title("🧪 Kalkulator Gas Ideal (PV = nRT)")
    st.markdown("""
    Selamat datang di **Kalkulator Gas Ideal**!

    Aplikasi ini membantu menghitung:
    - Massa gas
    - Tekanan gas
    - Volume gas
    - Jumlah mol gas

    Juga tersedia **Library gas mulia** untuk melihat sifat dan keamanannya.

    ---
    """)

    st.markdown("👨‍🔬 Dibuat oleh: **Kelompok 1 Analisis Kimia**")
    st.markdown("- Nama 1\n- Nama 2\n- Nama 3\n- Nama 4\n- Nama 5")

    if st.button("➡️ Masuk Aplikasi"):
        st.session_state.halaman = 'main'
        st.rerun()

# Halaman Utama: Kalkulator + Library
elif st.session_state.halaman == 'main':
    menu = st.tabs(["Kalkulator", "Library"])

    R = 0.0821  # Konstanta gas ideal dalam atm·L/mol·K

    # Tab Kalkulator
    with menu[0]:
        st.header("🧮 Kalkulator Gas Ideal")
        tab_kalk = st.tabs(["Massa Gas", "Tekanan", "Volume", "Mol"])

        # Massa Gas
        with tab_kalk[0]:
            st.subheader("🔹 Massa Gas")
            nama = st.text_input("Nama gas", key="massa_nama")
            n = st.number_input("Jumlah mol (mol)", min_value=0.0, key="massa_n")
            mr = st.number_input("Massa molar (g/mol)", min_value=0.0, key="massa_mr")
            if st.button("Hitung Massa"):
                massa = n * mr
                st.success(f"Massa gas {nama}: {massa:.4f} gram")

        # Tekanan Gas
        with tab_kalk[1]:
            st.subheader("🔹 Tekanan Gas")
            nama = st.text_input("Nama gas", key="P_nama")
            n = st.number_input("Mol (mol)", min_value=0.0, key="P_n")
            T = st.number_input("Suhu (K)", min_value=0.0, key="P_T")
            V = st.number_input("Volume (L)", min_value=0.0, key="P_V")
            if st.button("Hitung Tekanan"):
                if V > 0:
                    P = (n * R * T) / V
                    st.success(f"Tekanan gas {nama}: {P:.4f} atm")
                else:
                    st.error("Volume tidak boleh nol")

        # Volume Gas
        with tab_kalk[2]:
            st.subheader("🔹 Volume Gas")
            nama = st.text_input("Nama gas", key="V_nama")
            n = st.number_input("Mol (mol)", min_value=0.0, key="V_n")
            T = st.number_input("Suhu (K)", min_value=0.0, key="V_T")
            P = st.number_input("Tekanan (atm)", min_value=0.0, key="V_P")
            if st.button("Hitung Volume"):
                if P > 0:
                    V = (n * R * T) / P
                    st.success(f"Volume gas {nama}: {V:.4f} liter")
                else:
                    st.error("Tekanan tidak boleh nol")

        # Jumlah Mol Gas
        with tab_kalk[3]:
            st.subheader("🔹 Jumlah Mol Gas")
            nama = st.text_input("Nama gas", key="n_nama")
            P = st.number_input("Tekanan (atm)", min_value=0.0, key="n_P")
            V = st.number_input("Volume (L)", min_value=0.0, key="n_V")
            T = st.number_input("Suhu (K)", min_value=0.0, key="n_T")
            if st.button("Hitung Mol"):
                if T > 0:
                    n = (P * V) / (R * T)
                    st.success(f"Jumlah mol gas {nama}: {n:.4f} mol")
                else:
                    st.error("Suhu tidak boleh nol")

    # Tab Library
    with menu[1]:
        st.header("📚 Library Gas Mulia")
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
        st.markdown(f"**⚗️ Sifat Fisika & Kimia:** {info[pilihan]['sifat']}")
        st.markdown(f"**☣️ PBK:** {info[pilihan]['pbk']}")
        st.markdown(f"**🦺 K3L:** {info[pilihan]['k3l']}")
