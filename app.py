# ===========================================
# HALAMAN UTAMA - DESAIN PREMIUM
# ===========================================
if menu == "🏠 Beranda":
    # CSS Khusus untuk Halaman Utama
    st.markdown("""
    <style>
        .hero-section {
            background: linear-gradient(135deg, #0d47a1 0%, #1976d2 100%);
            color: white;
            padding: 3rem 2rem;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(13,71,161,0.3);
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }
        .hero-section::after {
            content: "";
            background: url('https://cdn-icons-png.flaticon.com/512/2693/2693188.png');
            opacity: 0.1;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            position: absolute;
            z-index: 0;
            background-size: 200px;
            background-repeat: repeat;
        }
        .hero-content {
            position: relative;
            z-index: 1;
        }
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
            height: 100%;
            border-top: 4px solid;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0,0,0,0.15);
        }
        .gas-equation {
            background: #f5f5f5;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            margin: 2rem 0;
            border: 1px solid #e0e0e0;
        }
        .variable-card {
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            transition: all 0.3s;
        }
        .variable-card:hover {
            transform: scale(1.05);
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-content">
            <h1 style="margin:0;font-size:2.8rem;font-weight:700;">MASTER GAS PRO</h1>
            <p style="margin:0.5rem 0 0;font-size:1.3rem;opacity:0.9;">Platform Komprehensif untuk Analisis Gas Ideal</p>
            <div style="margin-top:1.5rem;">
                <span style="display:inline-block;background:rgba(255,255,255,0.2);padding:8px 16px;border-radius:50px;margin:0 5px;">🧪 Kimia</span>
                <span style="display:inline-block;background:rgba(255,255,255,0.2);padding:8px 16px;border-radius:50px;margin:0 5px;">📊 Fisika</span>
                <span style="display:inline-block;background:rgba(255,255,255,0.2);padding:8px 16px;border-radius:50px;margin:0 5px;">⚠️ K3L</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Fitur Unggulan
    st.markdown("## ✨ Fitur Unggulan")
    
    feature_cols = st.columns(3)
    features = [
        {"icon": "🧮", "title": "Kalkulator Gas", "desc": "Hitung massa, tekanan, volume, dan mol gas ideal", "color": "#2196f3"},
        {"icon": "📚", "title": "Ensiklopedia Gas", "desc": "Database 50+ gas dengan data lengkap", "color": "#4caf50"},
        {"icon": "🛡️", "title": "Panduan Keselamatan", "desc": "Protokol penanganan bahan berbahaya", "color": "#ff9800"}
    ]
    
    for col, feature in zip(feature_cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card" style="border-color:{feature['color']}">
                <div style="font-size:2.5rem;margin-bottom:1rem;color:{feature['color']}">{feature['icon']}</div>
                <h3 style="margin:0 0 0.5rem 0;color:{feature['color']}">{feature['title']}</h3>
                <p style="margin:0;color:#555;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Persamaan Gas Ideal
    st.markdown("## ⚗️ Persamaan Gas Ideal")
    st.markdown("""
    <div class="gas-equation">
        <div style="font-size:1.5rem;margin-bottom:1rem;">PV = nRT</div>
        <p style="margin:0;color:#555;">Persamaan dasar yang menghubungkan tekanan (P), volume (V), jumlah mol (n), dan suhu (T) suatu gas ideal</p>
    </div>
    """, unsafe_allow_html=True)

    # Variabel dalam Persamaan
    st.markdown("### Variabel dalam Persamaan")
    
    var_cols = st.columns(4)
    variables = [
        {"symbol": "P", "name": "Tekanan", "unit": "atm", "color": "#ff5252"},
        {"symbol": "V", "name": "Volume", "unit": "L", "color": "#4caf50"},
        {"symbol": "n", "name": "Mol", "unit": "mol", "color": "#2196f3"},
        {"symbol": "T", "name": "Suhu", "unit": "K", "color": "#ff9800"}
    ]
    
    for col, var in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div class="variable-card" style="background:{var['color']}20;border:1px solid {var['color']}30;">
                <div style="font-size:2rem;font-weight:bold;color:{var['color']}">{var['symbol']}</div>
                <h4 style="margin:0.5rem 0;color:{var['color']}">{var['name']}</h4>
                <p style="margin:0;color:#555;">Satuan: {var['unit']}</p>
            </div>
            """, unsafe_allow_html=True)

    # Konstanta Gas
    st.markdown("""
    <div style="background:#e3f2fd;padding:1rem;border-radius:12px;margin-top:2rem;text-align:center;">
        <h4 style="margin:0;">Konstanta Gas Ideal (R) = 0.0821 L·atm/mol·K</h4>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# ENSIKLOPEDIA GAS - LENGKAP
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    # CSS Khusus
    st.markdown("""
    <style>
        .gas-header {
            background: linear-gradient(135deg, #4caf50 0%, #2e7d32 100%);
            color: white;
            padding: 2rem;
            border-radius: 16px;
            margin-bottom: 2rem;
        }
        .gas-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-left: 5px solid;
        }
        .property-table {
            width: 100%;
            border-collapse: collapse;
        }
        .property-table th {
            background-color: #f5f5f5;
            padding: 10px;
            text-align: left;
        }
        .property-table td {
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        .tab-content {
            padding: 1rem;
            background: #f9f9f9;
            border-radius: 0 0 12px 12px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header Ensiklopedia
    st.markdown("""
    <div class="gas-header">
        <h1 style="margin:0;">📚 Ensiklopedia Gas</h1>
        <p style="margin:0.5rem 0 0;font-size:1.1rem;">Database lengkap berbagai jenis gas ideal</p>
    </div>
    """, unsafe_allow_html=True)

    # Daftar Gas Lengkap
    GAS_DATABASE = {
        "Hidrogen (H₂)": {
            "icon": "🚀",
            "kategori": "Gas Diatomik",
            "deskripsi": "Unsur paling ringan di alam semesta dengan sifat unik sebagai bahan bakar masa depan.",
            "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Hydrogen-3D-vdW.png/320px-Hydrogen-3D-vdW.png",
            "warna": "#2196f3",
            "detail": {
                "🧪 Identitas Molekul": {
                    "Rumus Molekul": "H₂",
                    "Massa Molar": "2.016 g/mol",
                    "Penampilan": "Gas tak berwarna, tak berbau",
                    "Struktur": "Diatomik, ikatan kovalen tunggal"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-259.16 °C (13.99 K)",
                    "Titik Didih": "-252.87 °C (20.28 K)",
                    "Densitas (STP)": "0.08988 g/L",
                    "Kalor Jenis": "14.304 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Sangat mudah terbakar",
                    "Energi Ikatan": "436 kJ/mol",
                    "Reaksi Khas": "2H₂ + O₂ → 2H₂O (eksotermik)",
                    "Potensial Reduksi": "0 V (standar)"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Sangat mudah terbakar",
                    "Rentang Mudah Terbakar": "4-75% di udara",
                    "Pertolongan Pertama": "Jauhkan dari sumber api, beri udara segar",
                    "Penyimpanan": "Tabung bertekanan, jauh dari oksidator"
                }
            },
            "aplikasi": "Bahan bakar roket, produksi amonia, hidrogenasi minyak"
        },
        "Oksigen (O₂)": {
            "icon": "💨",
            "kategori": "Gas Diatomik",
            "deskripsi": "Gas vital untuk kehidupan dan pembakaran, menyusun 21% atmosfer Bumi.",
            "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Oxygen_molecule.png/320px-Oxygen_molecule.png",
            "warna": "#f44336",
            "detail": {
                "🧪 Identitas Molekul": {
                    "Rumus Molekul": "O₂",
                    "Massa Molar": "32.00 g/mol",
                    "Penampilan": "Gas tak berwarna",
                    "Struktur": "Diatomik, ikatan kovalen rangkap"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-218.79 °C (54.36 K)",
                    "Titik Didih": "-182.96 °C (90.19 K)",
                    "Densitas (STP)": "1.429 g/L",
                    "Kalor Jenis": "0.918 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Oksidator kuat",
                    "Energi Ikatan": "498 kJ/mol",
                    "Reaksi Khas": "Mendukung pembakaran",
                    "Potensial Reduksi": "+1.23 V"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Meningkatkan risiko kebakaran",
                    "Konsentrasi Aman": "<23.5% di udara",
                    "Pertolongan Pertama": "Berikan udara normal",
                    "Penyimpanan": "Jauh dari bahan mudah terbakar"
                }
            },
            "aplikasi": "Penggunaan medis, industri baja, pengolahan air"
        },
        "Nitrogen (N₂)": {
            "icon": "🌬️",
            "kategori": "Gas Diatomik",
            "deskripsi": "Gas inert yang menyusun 78% atmosfer Bumi, penting untuk berbagai aplikasi industri.",
            "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Nitrogen-3D-vdW.png/320px-Nitrogen-3D-vdW.png",
            "warna": "#9c27b0",
            "detail": {
                "🧪 Identitas Molekul": {
                    "Rumus Molekul": "N₂",
                    "Massa Molar": "28.014 g/mol",
                    "Penampilan": "Gas tak berwarna, tak berbau",
                    "Struktur": "Diatomik, ikatan rangkap tiga"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-210.00 °C (63.15 K)",
                    "Titik Didih": "-195.79 °C (77.36 K)",
                    "Densitas (STP)": "1.2506 g/L",
                    "Kalor Jenis": "1.040 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Sangat stabil",
                    "Energi Ikatan": "945 kJ/mol",
                    "Reaksi Khas": "Hampir inert pada suhu kamar",
                    "Potensial Reduksi": "Sukar direduksi"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Dapat menyebabkan asfiksia",
                    "Konsentrasi Aman": "Tidak beracun tetapi menggantikan O₂",
                    "Pertolongan Pertama": "Berikan udara segar",
                    "Penyimpanan": "Tabung bertekanan, ventilasi baik"
                }
            },
            "aplikasi": "Pembuatan amonia, pendingin, atmosfer inert"
        },
        "Karbon Dioksida (CO₂)": {
            "icon": "🍃",
            "kategori": "Gas Triatomik",
            "deskripsi": "Gas rumah kaca penting yang dihasilkan dari respirasi dan pembakaran bahan organik.",
            "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Carbon_dioxide_3D_ball.png/320px-Carbon_dioxide_3D_ball.png",
            "warna": "#4caf50",
            "detail": {
                "🧪 Identitas Molekul": {
                    "Rumus Molekul": "CO₂",
                    "Massa Molar": "44.01 g/mol",
                    "Penampilan": "Gas tak berwarna",
                    "Struktur": "Linear, ikatan rangkap"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-56.56 °C (216.59 K)",
                    "Titik Didih": "-78.5 °C (194.65 K)",
                    "Densitas (STP)": "1.977 g/L",
                    "Kalor Jenis": "0.839 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Bereaksi dengan air membentuk asam karbonat",
                    "Energi Ikatan": "C=O: 799 kJ/mol",
                    "Reaksi Khas": "CO₂ + H₂O ⇌ H₂CO₃",
                    "Kelarutan": "1.45 g/L dalam air (25°C)"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Asfiksia pada konsentrasi tinggi",
                    "Konsentrasi Aman": "<5000 ppm (8 jam)",
                    "Pertolongan Pertama": "Bawa ke udara segar",
                    "Penyimpanan": "Tabung bertekanan, area berventilasi"
                }
            },
            "aplikasi": "Minuman berkarbonasi, pemadam api, pendingin"
        },
        "Metana (CH₄)": {
            "icon": "🔥",
            "kategori": "Hidrokarbon",
            "deskripsi": "Komponen utama gas alam dan salah satu gas rumah kaca yang poten.",
            "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Methane-3D-space-filling.svg/320px-Methane-3D-space-filling.svg.png",
            "warna": "#ff9800",
            "detail": {
                "🧪 Identitas Molekul": {
                    "Rumus Molekul": "CH₄",
                    "Massa Molar": "16.04 g/mol",
                    "Penampilan": "Gas tak berwarna, tak berbau*",
                    "Struktur": "Tetrahedral"
                },
                "📊 Sifat Fisika": {
                    "Titik Leleh": "-182.5 °C (90.65 K)",
                    "Titik Didih": "-161.5 °C (111.65 K)",
                    "Densitas (STP)": "0.717 kg/m³",
                    "Kalor Jenis": "2.22 J/(g·K)"
                },
                "⚗️ Sifat Kimia": {
                    "Kereaktifan": "Mudah terbakar",
                    "Energi Ikatan": "C-H: 413 kJ/mol",
                    "Reaksi Khas": "CH₄ + 2O₂ → CO₂ + 2H₂O",
                    "Potensial Pembakaran": "55.5 MJ/kg"
                },
                "⚠️ Keselamatan": {
                    "Bahaya Utama": "Sangat mudah terbakar",
                    "Rentang Mudah Terbakar": "4.4-17% di udara",
                    "Pertolongan Pertama": "Jauhkan dari sumber api",
                    "Penyimpanan": "Tabung bertekanan, area berventilasi"
                }
            },
            "aplikasi": "Bahan bakar, produksi hidrogen, pupuk"
        }
    }

    # Pilih Gas
    selected_gas = st.selectbox(
        "🔍 Pilih Gas untuk Melihat Detail", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Tampilkan Detail Gas
    st.markdown(f"""
    <div class="gas-card" style="border-color:{gas['warna']}">
        <div style="display:flex;gap:20px;align-items:center;margin-bottom:15px;">
            <div style="flex:1;">
                <h2 style="margin:0;color:{gas['warna']}">{gas['icon']} {selected_gas}</h2>
                <p style="margin:5px 0;font-size:1.1rem;"><i>{gas['deskripsi']}</i></p>
                <div style="display:flex;gap:10px;">
                    <span style="background:{gas['warna']}20;color:{gas['warna']};padding:4px 10px;border-radius:50px;font-size:0.9em;">{gas['kategori']}</span>
                    <span style="background:#f5f5f5;padding:4px 10px;border-radius:50px;font-size:0.9em;">{gas['aplikasi']}</span>
                </div>
            </div>
            <img src="{gas['gambar']}" width="150" style="border-radius:10px;">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tab Informasi
    tabs = st.tabs(list(gas["detail"].keys()))
    
    for tab, (kategori, detail) in zip(tabs, gas["detail"].items()):
        with tab:
            st.markdown(f"""
            <div style="background:#f9f9f9;padding:1.5rem;border-radius:0 0 12px 12px;">
                <table class="property-table">
                    {"".join(f"<tr><td width='30%'><b>{key}</b></td><td>{value}</td></tr>" for key, value in detail.items())}
                </table>
            </div>
            """, unsafe_allow_html=True)

    # Kategori Gas Lainnya
    st.markdown("### 🌐 Kategori Gas Lainnya")
    
    categories = {
        "Gas Mulia": ["Helium (He)", "Neon (Ne)", "Argon (Ar)"],
        "Gas Asam": ["Hidrogen Klorida (HCl)", "Hidrogen Sulfida (H₂S)"],
        "Gas Industri": ["Amonia (NH₃)", "Klorin (Cl₂)", "Sulfur Dioksida (SO₂)"],
        "Hidrokarbon": ["Etana (C₂H₆)", "Propana (C₃H₈)", "Butana (C₄H₁₀)"]
    }
    
    cols = st.columns(len(categories))
    for col, (category, gases) in zip(cols, categories.items()):
        with col:
            st.markdown(f"""
            <div style="background:#f5f5f5;padding:1rem;border-radius:12px;">
                <h4 style="margin:0 0 10px 0;">{category}</h4>
                <ul style="margin:0;padding-left:20px;">
                    {"".join(f"<li>{gas}</li>" for gas in gases)}
                </ul>
            </div>
            """, unsafe_allow_html=True)
