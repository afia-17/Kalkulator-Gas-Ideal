import streamlit as st

st.set_page_config(page_title="Kalkulator Gas Ideal", layout="centered")

R = 0.0821  # Konstanta gas ideal (atm·L/mol·K)

# Sidebar Menu
st.sidebar.title("🧪 Kalkulator Gas Ideal")
menu = st.sidebar.radio("Navigasi", ["Beranda", "Kalkulator", "Library"])

# ===================== BERANDA =====================
if menu == "Beranda":
    st.title("Selamat Datang di Aplikasi Kalkulator Gas Ideal")
    st.markdown("""
    Aplikasi ini dibuat untuk membantu perhitungan **massa, tekanan, volume, dan mol gas** berdasarkan hukum **PV = nRT**.

    Selain itu, tersedia juga informasi **gas ideal** seperti sifat kimia, fisika, serta aspek **PBK** dan **K3L**.

    ---
    """)
    st.markdown("### 👨‍🔬 Kelompok 1 - Analisis Kimia")
    st.markdown("- Nama 1\n- Nama 2\n- Nama 3\n- Nama 4\n- Nama 5")

# ===================== KALKULATOR =====================
elif menu == "Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal (PV = nRT)")
    tab = st.tabs(["Massa Gas", "Tekanan", "Volume", "Mol"])

    # MASSA
    with tab[0]:
        st.subheader("🔹 Hitung Massa Gas")
        nama = st.text_input("Nama gas", key="massa_nama")
        n = st.number_input("Mol (n)", min_value=0.0, key="massa_n")
        mr = st.number_input("Massa molar (g/mol)", min_value=0.0, key="massa_mr")
        if st.button("Hitung Massa"):
            massa = n * mr
            st.success(f"Massa gas {nama}: {massa:.4f} gram")

    # TEKANAN
    with tab[1]:
        st.subheader("🔹 Hitung Tekanan Gas")
        nama = st.text_input("Nama gas", key="P_nama")
        n = st.number_input("Mol (n)", min_value=0.0, key="P_n")
        T = st.number_input("Suhu (K)", min_value=0.0, key="P_T")
        V = st.number_input("Volume (L)", min_value=0.0, key="P_V")
        if st.button("Hitung Tekanan"):
            if V > 0:
                P = (n * R * T) / V
                st.success(f"Tekanan gas {nama}: {P:.4f} atm")
            else:
                st.error("Volume tidak boleh nol.")

    # VOLUME
    with tab[2]:
        st.subheader("🔹 Hitung Volume Gas")
        nama = st.text_input("Nama gas", key="V_nama")
        n = st.number_input("Mol (n)", min_value=0.0, key="V_n")
        T = st.number_input("Suhu (K)", min_value=0.0, key="V_T")
        P = st.number_input("Tekanan (atm)", min_value=0.0, key="V_P")
        if st.button("Hitung Volume"):
            if P > 0:
                V = (n * R * T) / P
                st.success(f"Volume gas {nama}: {V:.4f} L")
            else:
                st.error("Tekanan tidak boleh nol.")

    # MOL
    with tab[3]:
        st.subheader("🔹 Hitung Jumlah Mol Gas")
        nama = st.text_input("Nama gas", key="n_nama")
        P = st.number_input("Tekanan (atm)", min_value=0.0, key="n_P")
        V = st.number_input("Volume (L)", min_value=0.0, key="n_V")
        T = st.number_input("Suhu (K)", min_value=0.0, key="n_T")
        if st.button("Hitung Mol"):
            if T > 0:
                n = (P * V) / (R * T)
                st.success(f"Jumlah mol gas {nama}: {n:.4f} mol")
            else:
                st.error("Suhu tidak boleh nol.")

# ===================== LIBRARY =====================
elif menu == "Library":
    st.title("📚 Library Gas Ideal")

    gas_list = [
        "Gas ideal",  # Placeholder awal
        "Helium (He)",
        "Neon (Ne)",
        "Argon (Ar)",
        "Krypton (Kr)",
        "Xenon (Xe)",
        "Radon (Rn)"
    ]

    pilihan = st.selectbox("Pilih gas ideal:", gas_list)

    info = {
        "Helium (He)": {
            "rumus": "He",
            "sifat": "Ringan, tidak reaktif, digunakan untuk balon & cryogenics",
            "pbk": "Dapat menyebabkan asfiksia di ruang tertutup",
            "k3l": "Gunakan di ruang berventilasi, simpan tabung aman"
        },
        "Neon (Ne)": {
            "rumus": "Ne",
            "sifat": "Tidak berwarna, digunakan dalam lampu neon",
            "pbk": "Risiko rendah, tapi tetap dapat sebabkan asfiksia",
            "k3l": "Simpan dalam silinder tekan, hindari suhu tinggi"
        },
        "Argon (Ar)": {
            "rumus": "Ar",
            "sifat": "Lebih berat dari udara, tidak berwarna, inert",
            "pbk": "Menggantikan O₂ di ruang tertutup → risiko sesak napas",
            "k3l": "Pastikan ventilasi baik, gunakan alat pelindung"
        },
        "Krypton (Kr)": {
            "rumus": "Kr",
            "sifat": "Inert, jarang ditemukan, digunakan di fotografi",
            "pbk": "Bisa menekan oksigen di udara",
            "k3l": "Simpan tabung tegak & aman"
        },
        "Xenon (Xe)": {
            "rumus": "Xe",
            "sifat": "Digunakan dalam anestesi & lampu kilat",
            "pbk": "Efek anestetik pada konsentrasi tinggi",
            "k3l": "Gunakan APD, hindari paparan berlebih"
        },
        "Radon (Rn)": {
            "rumus": "Rn",
            "sifat": "Radioaktif, produk peluruhan uranium",
            "pbk": "Karsinogenik — penyebab kanker paru",
            "k3l": "Gunakan detektor radiasi, hindari ruangan tertutup"
        }
    }

    if pilihan == "Gas ideal":
        st.info("Silakan pilih gas ideal untuk melihat informasi lengkap.")
    else:
        st.markdown(f"**🔬 Rumus Molekul:** {info[pilihan]['rumus']}")
        st.markdown(f"**⚗️ Sifat Kimia dan Fisika:** {info[pilihan]['sifat']}")
        st.markdown(f"**☣️ PBK (Potensi Bahaya & Keamanan):** {info[pilihan]['pbk']}")
        st.markdown(f"**🦺 K3L (Kesehatan, Keselamatan, Lingkungan):** {info[pilihan]['k3l']}")
