# ===========================================
# APLIKASI KALKULATOR GAS IDEAL + ENSIKLOPEDIA + PANDUAN KESELAMATAN
# ===========================================
import streamlit as st
import base64

# Konfigurasi Halaman
st.set_page_config(
    page_title="ChemGasMaster",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================
# CSS SUPER KREATIF + BACKGROUND SPEKTAKULER UNTUK SETIAP MENU
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
    .safety-card {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        border-left: 5px solid #f44336;
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
    .gas-icon {
        font-size: 24px;
        margin-right: 10px;
    }
    
    /* ========================================= */
    /* 🏠 BACKGROUND BERANDA - LABORATORIUM AJAIB */
    /* ========================================= */
    .beranda-bg {
        background: 
            radial-gradient(circle at 20% 20%, rgba(138, 43, 226, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(30, 144, 255, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, rgba(255, 20, 147, 0.1) 0%, transparent 50%),
            linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.08;
        animation: beranda-pulse 15s ease-in-out infinite;
    }
    
    .beranda-molekul {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        pointer-events: none;
        overflow: hidden;
    }
    
    .molekul {
        position: absolute;
        width: 8px;
        height: 8px;
        background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(100,200,255,0.4) 100%);
        border-radius: 50%;
        animation: molekul-dance 20s infinite linear;
        box-shadow: 0 0 10px rgba(100,200,255,0.3);
    }
    
    .molekul:nth-child(1) { left: 10%; animation-delay: 0s; animation-duration: 25s; }
    .molekul:nth-child(2) { left: 20%; animation-delay: 3s; animation-duration: 30s; }
    .molekul:nth-child(3) { left: 30%; animation-delay: 6s; animation-duration: 22s; }
    .molekul:nth-child(4) { left: 40%; animation-delay: 9s; animation-duration: 28s; }
    .molekul:nth-child(5) { left: 50%; animation-delay: 12s; animation-duration: 26s; }
    .molekul:nth-child(6) { left: 60%; animation-delay: 15s; animation-duration: 24s; }
    .molekul:nth-child(7) { left: 70%; animation-delay: 18s; animation-duration: 32s; }
    .molekul:nth-child(8) { left: 80%; animation-delay: 21s; animation-duration: 27s; }
    .molekul:nth-child(9) { left: 90%; animation-delay: 24s; animation-duration: 29s; }
    
    .ikatan-kimia {
        position: absolute;
        width: 2px;
        height: 50px;
        background: linear-gradient(to bottom, rgba(255,255,255,0.3), transparent);
        animation: ikatan-bergerak 8s ease-in-out infinite;
    }
    
    /* ========================================= */
    /* 🧮 BACKGROUND KALKULATOR - RUMUS MATEMATIKA TERBANG */
    /* ========================================= */
    .kalkulator-bg {
        background: 
            conic-gradient(from 0deg at 50% 50%, 
                rgba(255, 154, 158, 0.1) 0deg, 
                rgba(254, 207, 239, 0.1) 90deg, 
                rgba(255, 206, 84, 0.1) 180deg, 
                rgba(255, 154, 158, 0.1) 270deg, 
                rgba(254, 207, 239, 0.1) 360deg),
            linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #fad0c4 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.06;
        animation: kalkulator-rotate 30s linear infinite;
    }
    
    .rumus-terbang {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        pointer-events: none;
        overflow: hidden;
    }
    
    .rumus {
        position: absolute;
        font-size: 14px;
        font-weight: bold;
        color: rgba(255, 100, 150, 0.3);
        animation: rumus-melayang 25s infinite linear;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 5px rgba(255, 100, 150, 0.2);
    }
    
    .rumus:nth-child(1) { left: 5%; animation-delay: 0s; }
    .rumus:nth-child(2) { left: 15%; animation-delay: 4s; }
    .rumus:nth-child(3) { left: 25%; animation-delay: 8s; }
    .rumus:nth-child(4) { left: 35%; animation-delay: 12s; }
    .rumus:nth-child(5) { left: 45%; animation-delay: 16s; }
    .rumus:nth-child(6) { left: 55%; animation-delay: 20s; }
    .rumus:nth-child(7) { left: 65%; animation-delay: 24s; }
    .rumus:nth-child(8) { left: 75%; animation-delay: 28s; }
    .rumus:nth-child(9) { left: 85%; animation-delay: 32s; }
    .rumus:nth-child(10) { left: 95%; animation-delay: 36s; }
    
    /* ========================================= */
    /* 📚 BACKGROUND ENSIKLOPEDIA - HALAMAN BUKU AJAIB */
    /* ========================================= */
    .ensiklopedia-bg {
        background: 
            radial-gradient(ellipse at top left, rgba(102, 126, 234, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at bottom right, rgba(118, 75, 162, 0.15) 0%, transparent 50%),
            radial-gradient(ellipse at center, rgba(255, 255, 255, 0.1) 0%, transparent 70%),
            linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.05;
        animation: ensiklopedia-breathe 20s ease-in-out infinite;
    }
    
    .halaman-terbang {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        pointer-events: none;
        overflow: hidden;
    }
    
    .halaman {
        position: absolute;
        width: 30px;
        height: 40px;
        background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(200,200,255,0.2) 100%);
        border-radius: 3px;
        animation: halaman-jatuh 15s infinite linear;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .halaman:nth-child(1) { left: 8%; animation-delay: 0s; animation-duration: 18s; }
    .halaman:nth-child(2) { left: 18%; animation-delay: 2s; animation-duration: 22s; }
    .halaman:nth-child(3) { left: 28%; animation-delay: 4s; animation-duration: 16s; }
    .halaman:nth-child(4) { left: 38%; animation-delay: 6s; animation-duration: 20s; }
    .halaman:nth-child(5) { left: 48%; animation-delay: 8s; animation-duration: 24s; }
    .halaman:nth-child(6) { left: 58%; animation-delay: 10s; animation-duration: 19s; }
    .halaman:nth-child(7) { left: 68%; animation-delay: 12s; animation-duration: 21s; }
    .halaman:nth-child(8) { left: 78%; animation-delay: 14s; animation-duration: 17s; }
    .halaman:nth-child(9) { left: 88%; animation-delay: 16s; animation-duration: 23s; }
    
    .bintang-pengetahuan {
        position: absolute;
        width: 4px;
        height: 4px;
        background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(255,215,0,0.4) 100%);
        border-radius: 50%;
        animation: bintang-berkelip 3s ease-in-out infinite;
    }
    
    /* ========================================= */
    /* ⚠️ BACKGROUND KESELAMATAN - ZONA BAHAYA DINAMIS */
    /* ========================================= */
    .keselamatan-bg {
        background: 
            repeating-conic-gradient(from 0deg at 30% 30%, 
                rgba(255, 107, 107, 0.1) 0deg, 
                rgba(254, 202, 87, 0.1) 45deg, 
                transparent 90deg, 
                rgba(255, 107, 107, 0.1) 135deg),
            repeating-conic-gradient(from 45deg at 70% 70%, 
                rgba(254, 202, 87, 0.1) 0deg, 
                rgba(255, 107, 107, 0.1) 45deg, 
                transparent 90deg, 
                rgba(254, 202, 87, 0.1) 135deg),
            linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -3;
        opacity: 0.04;
        animation: keselamatan-warning 8s ease-in-out infinite;
    }
    
    .peringatan-bergerak {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -2;
        pointer-events: none;
        overflow: hidden;
    }
    
    .simbol-bahaya {
        position: absolute;
        font-size: 20px;
        color: rgba(255, 107, 107, 0.3);
        animation: bahaya-berputar 12s infinite linear;
        text-shadow: 0 0 10px rgba(255, 107, 107, 0.2);
    }
    
    .simbol-bahaya:nth-child(1) { left: 10%; top: 20%; animation-delay: 0s; }
    .simbol-bahaya:nth-child(2) { left: 30%; top: 40%; animation-delay: 2s; }
    .simbol-bahaya:nth-child(3) { left: 50%; top: 60%; animation-delay: 4s; }
    .simbol-bahaya:nth-child(4) { left: 70%; top: 80%; animation-delay: 6s; }
    .simbol-bahaya:nth-child(5) { left: 90%; top: 30%; animation-delay: 8s; }
    .simbol-bahaya:nth-child(6) { left: 20%; top: 70%; animation-delay: 10s; }
    
    .garis-peringatan {
        position: absolute;
        width: 100%;
        height: 2px;
        background: repeating-linear-gradient(
            90deg,
            rgba(255, 107, 107, 0.2) 0px,
            rgba(255, 107, 107, 0.2) 20px,
            transparent 20px,
            transparent 40px
        );
        animation: garis-bergerak 5s linear infinite;
    }
    
    /* ========================================= */
    /* ANIMASI SPEKTAKULER */
    /* ========================================= */
    @keyframes beranda-pulse {
        0%, 100% { opacity: 0.08; transform: scale(1); }
        50% { opacity: 0.12; transform: scale(1.02); }
    }
    
    @keyframes molekul-dance {
        0% { transform: translateY(100vh) rotate(0deg) scale(0.5); opacity: 0; }
        10% { opacity: 1; }
        50% { transform: translateY(50vh) rotate(180deg) scale(1); opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-50px) rotate(360deg) scale(0.5); opacity: 0; }
    }
    
    @keyframes ikatan-bergerak {
        0%, 100% { transform: translateX(0px) rotate(0deg); opacity: 0.3; }
        50% { transform: translateX(20px) rotate(10deg); opacity: 0.7; }
    }
    
    @keyframes kalkulator-rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes rumus-melayang {
        0% { transform: translateY(100vh) translateX(0px) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        50% { transform: translateY(50vh) translateX(50px) rotate(180deg); opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-50px) translateX(-30px) rotate(360deg); opacity: 0; }
    }
    
    @keyframes ensiklopedia-breathe {
        0%, 100% { opacity: 0.05; }
        50% { opacity: 0.08; }
    }
    
    @keyframes halaman-jatuh {
        0% { transform: translateY(-50px) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        50% { transform: translateY(50vh) rotate(45deg); opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(100vh) rotate(90deg); opacity: 0; }
    }
    
    @keyframes bintang-berkelip {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.5); }
    }
    
    @keyframes keselamatan-warning {
        0%, 100% { opacity: 0.04; }
        25% { opacity: 0.08; }
        50% { opacity: 0.06; }
        75% { opacity: 0.1; }
    }
    
    @keyframes bahaya-berputar {
        0% { transform: rotate(0deg) scale(1); opacity: 0.3; }
        25% { transform: rotate(90deg) scale(1.2); opacity: 0.6; }
        50% { transform: rotate(180deg) scale(1); opacity: 0.3; }
        75% { transform: rotate(270deg) scale(1.2); opacity: 0.6; }
        100% { transform: rotate(360deg) scale(1); opacity: 0.3; }
    }
    
    @keyframes garis-bergerak {
        0% { transform: translateX(-40px); }
        100% { transform: translateX(40px); }
    }
    
    /* ========================================= */
    /* EFEK HOVER INTERAKTIF */
    /* ========================================= */
    .content-overlay {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .content-overlay::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s ease;
        opacity: 0;
    }
    
    .content-overlay:hover::before {
        animation: shimmer 1.5s ease-in-out;
    }
    
    .content-overlay:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.4);
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); opacity: 0; }
        50% { opacity: 1; }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); opacity: 0; }
    }
    
    /* ========================================= */
    /* PARTIKEL KHUSUS UNTUK SETIAP MENU */
    /* ========================================= */
    .partikel-khusus {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
        overflow: hidden;
    }
    
    .partikel-atom {
        position: absolute;
        width: 6px;
        height: 6px;
        background: radial-gradient(circle, rgba(100,200,255,0.8) 0%, rgba(50,150,255,0.3) 100%);
        border-radius: 50%;
        animation: atom-orbit 15s infinite linear;
        box-shadow: 0 0 15px rgba(100,200,255,0.4);
    }
    
    .partikel-angka {
        position: absolute;
        font-size: 12px;
        font-weight: bold;
        color: rgba(255, 100, 150, 0.4);
        animation: angka-terbang 20s infinite linear;
        font-family: 'Arial', sans-serif;
    }
    
    .partikel-buku {
        position: absolute;
        width: 8px;
        height: 10px;
        background: linear-gradient(135deg, rgba(255,255,255,0.6) 0%, rgba(200,200,255,0.3) 100%);
        border-radius: 1px;
        animation: buku-berputar 18s infinite linear;
        box-shadow: 0 1px 5px rgba(0,0,0,0.1);
    }
    
    .partikel-peringatan {
        position: absolute;
        font-size: 16px;
        color: rgba(255, 107, 107, 0.4);
        animation: peringatan-kedip 10s infinite ease-in-out;
        text-shadow: 0 0 8px rgba(255, 107, 107, 0.3);
    }
    
    @keyframes atom-orbit {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-50px) rotate(720deg); opacity: 0; }
    }
    
    @keyframes angka-terbang {
        0% { transform: translateY(100vh) translateX(0px); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-50px) translateX(100px); opacity: 0; }
    }
    
    @keyframes buku-berputar {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-50px) rotate(180deg); opacity: 0; }
    }
    
    @keyframes peringatan-kedip {
        0%, 100% { opacity: 0.2; transform: scale(1); }
        25% { opacity: 0.6; transform: scale(1.1); }
        50% { opacity: 0.4; transform: scale(1); }
        75% { opacity: 0.8; transform: scale(1.2); }
    }
    
    /* ========================================= */
    /* EFEK KHUSUS TAMBAHAN */
    /* ========================================= */
    .cahaya-latar {
        position: fixed;
        top: 50%;
        left: 50%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        border-radius: 50%;
        transform: translate(-50%, -50%);
        animation: cahaya-berkedip 8s ease-in-out infinite;
        z-index: -1;
    }
    
    @keyframes cahaya-berkedip {
        0%, 100% { opacity: 0.3; transform: translate(-50%, -50%) scale(1); }
        50% { opacity: 0.7; transform: translate(-50%, -50%) scale(1.2); }
    }
</style>
""", unsafe_allow_html=True)

# ===========================================
# DATABASE GAS
# ===========================================
GAS_DATABASE = {
    "Hidrogen (H₂)": {
        "icon": "🚀",
        "category": "Gas Diatomik",
        "description": "Unsur paling ringan di alam semesta dengan sifat unik sebagai bahan bakar masa depan.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/H2.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "H₂",
                "Massa Molar": "2.016 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan tunggal"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-259.16 °C (13.99 K)",
                "Titik Didih": "-252.87 °C (20.28 K)",
                "Densitas (STP)": "0.08988 g/L",
                "Kalor Jenis": "14.304 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (4-75% di udara)",
                "Penanganan": "Gunakan di area berventilasi, hindari percikan api"
            }
        },
        "aplikasi": "Bahan bakar roket, produksi amonia, hidrogenasi minyak"
    },
    "Oksigen (O₂)": {
        "icon": "💨",
        "category": "Gas Diatomik",
        "description": "Gas vital untuk kehidupan dan pembakaran, menyusun 21% atmosfer Bumi.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/O2_-.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "O₂",
                "Massa Molar": "32.00 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Diatomik, ikatan rangkap"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-218.79 °C (54.36 K)",
                "Titik Didih": "-182.96 °C (90.19 K)",
                "Densitas (STP)": "1.429 g/L",
                "Kalor Jenis": "0.918 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Meningkatkan risiko kebakaran",
                "Penanganan": "Hindari kontak dengan bahan organik"
            }
        },
        "aplikasi": "Penggunaan medis, industri baja, pengolahan air"
    },
    "Nitrogen (N₂)": {
        "icon": "🌬️",
        "category": "Gas Diatomik",
        "description": "Gas inert yang menyusun 78% atmosfer Bumi, penting untuk berbagai aplikasi industri.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/N2.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "N₂",
                "Massa Molar": "28.014 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Diatomik, ikatan rangkap tiga"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-210.00 °C (63.15 K)",
                "Titik Didih": "-195.79 °C (77.36 K)",
                "Densitas (STP)": "1.2506 g/L",
                "Kalor Jenis": "1.040 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Dapat menyebabkan asfiksia",
                "Penanganan": "Gunakan di area berventilasi baik"
            }
        },
        "aplikasi": "Pembuatan amonia, pendingin, atmosfer inert"
    },
    "Karbon Dioksida (CO₂)": {
        "icon": "🌫️",
        "category": "Gas Poliatomik",
        "description": "Gas rumah kaca yang penting untuk fotosintesis tanaman.",
        "image": "https://www.chemtube3d.com/images/gallery/JPGfiles%20structures/I606ST04.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CO₂",
                "Massa Molar": "44.01 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Linear, ikatan rangkap"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-78.5 °C (194.65 K)",
                "Titik Didih": "-56.6 °C (216.55 K)",
                "Densitas (STP)": "1.977 g/L",
                "Kalor Jenis": "0.839 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Dapat menyebabkan sesak napas",
                "Penanganan": "Hindari area tertutup tanpa ventilasi"
            }
        },
        "aplikasi": "Minuman berkarbonasi, pemadam kebakaran"
    }, 
    "Neon (Ne)": {
        "icon": "💡",
        "category": "Gas Monoatomik",
        "description": "Gas tidak berwarna, dapat memancarkan warna oranye kemerahan jika berada pada medan listrik bertegangan tinggi. Dapat digunakan sebagai pengisi lampu neon, penangkal petir, pengisi tabung televisi, dan dalam wujud cair neon dapat digunakan sebagai zat pendingir.",
        "image": "https://png.pngtree.com/thumb_back/fh260/background/20220426/pngtree-mendeleevs-periodic-table-luminescent-noble-gases-chemical-symbol-chemical-science-photo-image_30134580.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ne",
                "Massa Molar": "20.18 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-248.59 °C (24.56 K)",
                "Titik Didih": "-246.046 °C (27.104 K)",
                "Densitas (STP)": "0.89 g/L",
                "Kalor Jenis": "0.904 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Tekanan tinggi, asfiksia dalam ruang tertutup",
                "Penanganan": "Gunakan ventilasi baik dan simpan dalam tabung bertekanan sesuai standar"
            }
        },
        "aplikasi": "Lampu neon, pendingin kriogenik, alat elektronik"
    },  
    "Helium (He)": {
    "icon": "🎚️",
    "category": "Gas Monoatomik",
    "description": "Gas tidak berwarna dan tidak berbau, sangat ringan. Tidak mudah terbakar dan digunakan secara luas dalam balon, pendinginan MRI, serta sebagai atmosfer inert untuk pengelasan.",
    "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/186450350-56a132cb5f9b58b7d0bcf751.jpg",
    "properties": {
      "🧪 Identitas Molekul": {
        "Rumus": "He",
        "Massa Molar": "4.00 g/mol",
        "Penampilan": "Gas tak berwarna",
        "Struktur": "Monoatomik"
      },
      "⚛️ Sifat Fisika": {
        "Titik Leleh": "-272.2 °C (0.95 K)",
        "Titik Didih": "-268.93 °C (4.22 K)",
        "Densitas (STP)": "0.18 g/L",
        "Kalor Jenis": "5.19 J/(g·K)"
      },
      "⚠️ Keselamatan": {
        "Bahaya": "Asfiksia jika menggantikan oksigen",
        "Penanganan": "Gunakan dalam ruang berventilasi"
      }
    },
    "aplikasi": "Balon, pendingin MRI, pengelasan, pengujian kebocoran"
    }, 
    "Argon (Ar)": {
    "icon": "🔏",
    "category": "Gas Monoatomik",
    "description": "Gas inert, tidak reaktif secara kimia. Digunakan dalam pengelasan, bola lampu pijar, dan sebagai atmosfer pelindung dalam pembuatan semikonduktor.",
    "image": "https://www.vallalandco.com/Air-Products-Theni/1723628095.jpg",
    "properties": {
      "🧪 Identitas Molekul": {
        "Rumus": "Ar",
        "Massa Molar": "39.95 g/mol",
        "Penampilan": "Gas tak berwarna",
        "Struktur": "Monoatomik"
      },
      "⚛️ Sifat Fisika": {
        "Titik Leleh": "-189.35 °C (83.8 K)",
        "Titik Didih": "-185.85 °C (87.3 K)",
        "Densitas (STP)": "1.78 g/L",
        "Kalor Jenis": "0.52 J/(g·K)"
      },
      "⚠️ Keselamatan": {
        "Bahaya": "Tidak beracun namun dapat menyebabkan asfiksia",
        "Penanganan": "Ventilasi baik saat digunakan dalam ruang tertutup"
      }
    },
    "aplikasi": "Pengelasan, bola lampu, atmosfer inert industri"
  },
}

# ===========================================
# MENU SIDEBAR
# ===========================================
with st.sidebar:
    st.title("ChemGasMaster")
    st.markdown("---")
    menu = st.radio(
        "MENU UTAMA",
        ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"],
        index=0,
        key="main_menu_radio"
    )
    st.markdown("---")
    st.markdown("""
    <div class="card gas-card">
        <small>ℹ️ Menggunakan persamaan gas ideal: PV=nRT (R=0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# BACKGROUND SPEKTAKULER BERDASARKAN MENU
# ===========================================
if menu == "🏠 Beranda":
    st.markdown("""
    <div class="beranda-bg"></div>
    <div class="beranda-molekul">
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="molekul"></div>
        <div class="ikatan-kimia" style="left: 15%; top: 30%;"></div>
        <div class="ikatan-kimia" style="left: 45%; top: 60%;"></div>
        <div class="ikatan-kimia" style="left: 75%; top: 20%;"></div>
    </div>
    <div class="partikel-khusus">
        <div class="partikel-atom" style="left: 10%; animation-delay: 0s;"></div>
        <div class="partikel-atom" style="left: 30%; animation-delay: 3s;"></div>
        <div class="partikel-atom" style="left: 50%; animation-delay: 6s;"></div>
        <div class="partikel-atom" style="left: 70%; animation-delay: 9s;"></div>
        <div class="partikel-atom" style="left: 90%; animation-delay: 12s;"></div>
    </div>
    <div class="cahaya-latar"></div>
    """, unsafe_allow_html=True)

elif menu == "🧮 Kalkulator Gas":
    st.markdown("""
    <div class="kalkulator-bg"></div>
    <div class="rumus-terbang">
        <div class="rumus">PV = nRT</div>
        <div class="rumus">P = nRT/V</div>
        <div class="rumus">V = nRT/P</div>
        <div class="rumus">n = PV/RT</div>
        <div class="rumus">T = PV/nR</div>
        <div class="rumus">R = 0.0821</div>
        <div class="rumus">∆H = nCp∆T</div>
        <div class="rumus">ρ = PM/RT</div>
        <div class="rumus">M = mRT/PV</div>
        <div class="rumus">χ = n/ntotal</div>
    </div>
    <div class="partikel-khusus">
        <div class="partikel-angka" style="left: 5%; animation-delay: 0s;">∑</div>
        <div class="partikel-angka" style="left: 15%; animation-delay: 2s;">∫</div>
        <div class="partikel-angka" style="left: 25%; animation-delay: 4s;">π</div>
        <div class="partikel-angka" style="left: 35%; animation-delay: 6s;">∞</div>
        <div class="partikel-angka" style="left: 45%; animation-delay: 8s;">√</div>
        <div class="partikel-angka" style="left: 55%; animation-delay: 10s;">±</div>
        <div class="partikel-angka" style="left: 65%; animation-delay: 12s;">≈</div>
        <div class="partikel-angka" style="left: 75%; animation-delay: 14s;">≡</div>
        <div class="partikel-angka" style="left: 85%; animation-delay: 16s;">∆</div>
        <div class="partikel-angka" style="left: 95%; animation-delay: 18s;">Ω</div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "📚 Ensiklopedia Gas":
    st.markdown("""
    <div class="ensiklopedia-bg"></div>
    <div class="halaman-terbang">
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="halaman"></div>
        <div class="bintang-pengetahuan" style="left: 20%; top: 25%;"></div>
        <div class="bintang-pengetahuan" style="left: 40%; top: 45%;"></div>
        <div class="bintang-pengetahuan" style="left: 60%; top: 65%;"></div>
        <div class="bintang-pengetahuan" style="left: 80%; top: 35%;"></div>
    </div>
    <div class="partikel-khusus">
        <div class="partikel-buku" style="left: 8%; animation-delay: 0s;"></div>
        <div class="partikel-buku" style="left: 18%; animation-delay: 2s;"></div>
        <div class="partikel-buku" style="left: 28%; animation-delay: 4s;"></div>
        <div class="partikel-buku" style="left: 38%; animation-delay: 6s;"></div>
        <div class="partikel-buku" style="left: 48%; animation-delay: 8s;"></div>
        <div class="partikel-buku" style="left: 58%; animation-delay: 10s;"></div>
        <div class="partikel-buku" style="left: 68%; animation-delay: 12s;"></div>
        <div class="partikel-buku" style="left: 78%; animation-delay: 14s;"></div>
        <div class="partikel-buku" style="left: 88%; animation-delay: 16s;"></div>
    </div>
    """, unsafe_allow_html=True)

elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("""
    <div class="keselamatan-bg"></div>
    <div class="peringatan-bergerak">
        <div class="simbol-bahaya">⚠️</div>
        <div class="simbol-bahaya">🔥</div>
        <div class="simbol-bahaya">☠️</div>
        <div class="simbol-bahaya">⚡</div>
        <div class="simbol-bahaya">🚫</div>
        <div class="simbol-bahaya">☢️</div>
        <div class="garis-peringatan" style="top: 20%;"></div>
        <div class="garis-peringatan" style="top: 40%;"></div>
        <div class="garis-peringatan" style="top: 60%;"></div>
        <div class="garis-peringatan" style="top: 80%;"></div>
    </div>
    <div class="partikel-khusus">
        <div class="partikel-peringatan" style="left: 12%; top: 15%; animation-delay: 0s;">🛡️</div>
        <div class="partikel-peringatan" style="left: 32%; top: 35%; animation-delay: 2s;">🚨</div>
        <div class="partikel-peringatan" style="left: 52%; top: 55%; animation-delay: 4s;">⛑️</div>
        <div class="partikel-peringatan" style="left: 72%; top: 75%; animation-delay: 6s;">🧯</div>
        <div class="partikel-peringatan" style="left: 92%; top: 25%; animation-delay: 8s;">🚪</div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>🧪✨ ChemGasMaster - Laboratorium Digital Ajaib ✨🧪</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card calc-card content-overlay">
        <h3>🎉 Selamat Datang di Dunia Kimia yang Menakjubkan!</h3>
        <p>🚀 Platform revolusioner untuk menjelajahi misteri gas ideal dengan teknologi interaktif terdepan!</p>
        <p>🌟 Rasakan pengalaman belajar kimia yang tak terlupakan dengan visualisasi spektakuler dan perhitungan presisi tinggi!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan penjelasan
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown("""
        <div class="content-overlay" style="margin-top:20px;">
            <h4>🔬 Persamaan Ajaib Gas Ideal:</h4>
            <p>🎯 <b>P</b> = Tekanan (atm) - Kekuatan gas menekan dinding wadah</p>
            <p>📦 <b>V</b> = Volume (L) - Ruang yang dikuasai molekul gas</p>
            <p>⚛️ <b>n</b> = Jumlah mol (mol) - Pasukan molekul yang bertempur</p>
            <p>🌟 <b>R</b> = Konstanta gas = 0.0821 L·atm/mol·K - Kunci rahasia alam semesta</p>
            <p>🌡️ <b>T</b> = Suhu (K) - Energi kinetik yang menggerakkan molekul</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="content-overlay" style="margin-top:20px;">
            <h4>✨ Fakta Spektakuler:</h4>
            <p>🎚️ <b>Gas Ideal = Mimpi Sempurna</b> - Model matematis tanpa cacat</p>
            <p>🌡️ <b>Kondisi Ajaib</b> - Tekanan rendah & suhu tinggi = Keajaiban terjadi</p>
            <p>🧪 <b>1 mol gas</b> = 602.214.076.000.000.000.000.000 molekul!</p>
            <p>🚀 <b>Kecepatan Molekul</b> - Bergerak lebih cepat dari peluru!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualisasi variabel
    st.markdown("<h4 style='margin-top:30px;'>🎯 Prajurit Variabel Gas Ideal:</h4>", unsafe_allow_html=True)
    var_cols = st.columns(4)
    variables = [
        ("P", "Tekanan", "Kekuatan dahsyat<br>molekul gas", "#ffcdd2"),
        ("V", "Volume", "Istana tempat<br>molekul berdansa", "#c8e6c9"),
        ("n", "Jumlah Mol", "Pasukan molekul<br>yang tak terhitung", "#bbdefb"),
        ("T", "Suhu", "Api semangat<br>molekul bergerak", "#fff9c4")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div class="content-overlay" style="background:{color};padding:15px;border-radius:10px;height:150px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
                <h3 style="margin:5px 0;">{var}</h3>
                <p style="margin:5px 0;font-weight:bold;">{name}</p>
                <p style="margin:5px 0;font-size:0.8em;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contoh aplikasi
    st.markdown("""
    <div class="card content-overlay" style="margin-top:30px;">
        <h4>💡 Keajaiban Aplikasi Gas Ideal di Dunia Nyata:</h4>
        <ul>
            <li>🧪 <b>Laboratorium Kimia</b> - Menghitung volume gas hasil reaksi dengan presisi tinggi</li>
            <li>🔬 <b>Industri Farmasi</b> - Memahami perilaku gas dalam proses produksi obat</li>
            <li>🌡️ <b>Meteorologi</b> - Memprediksi perubahan cuaca berdasarkan tekanan atmosfer</li>
            <li>⚙️ <b>Teknik Mesin</b> - Mendesain sistem pneumatik dan hidrolik canggih</li>
            <li>🚀 <b>Teknologi Antariksa</b> - Menghitung bahan bakar roket untuk misi luar angkasa</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips Penggunaan
    st.markdown("""
    <div class="card gas-card content-overlay" style="margin-top:20px;">
        <h4>🔧 Panduan Menjadi Master Kimia Gas:</h4>
        <ol>
            <li>🧮 <b>Kalkulator Gas</b> - Senjata utama untuk perhitungan presisi tinggi</li>
            <li>📚 <b>Ensiklopedia Gas</b> - Perpustakaan pengetahuan tak terbatas</li>
            <li>⚠️ <b>Panduan Keselamatan</b> - Perisai pelindung sebelum bertarung dengan gas</li>
            <li>📏 <b>Konsistensi Satuan</b> - Kunci sukses mendapatkan hasil akurat</li>
            <li>🎯 <b>Latihan Rutin</b> - Asah kemampuan hingga menjadi ahli sejati</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    # Header dengan animasi partikel
    st.markdown("""
    <div class="content-overlay" style="background: linear-gradient(135deg, #0d47a1, #2196F3);
                 padding: 25px;
                 border-radius: 15px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <h1 style="color: white; text-align: center; margin: 0; z-index: 2; position: relative;">
              🧪✨ Mesin Kalkulator Gas Ideal Super Canggih ✨⚗️
        </h1>
        <p style="color: rgba(255,255,255,0.9); text-align: center; margin: 10px 0 0 0; z-index: 2; position: relative;">
            🚀 Teknologi Perhitungan Presisi Tinggi untuk Para Ahli Kimia Masa Depan! 🚀
        </p>
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; z-index: 1;">
            <div class="particle" style="--size: 3px; --duration: 15s; --delay: 0s; --x: 20%; --y: 30%"></div>
            <div class="particle" style="--size: 5px; --duration: 20s; --delay: 2s; --x: 70%; --y: 10%"></div>
            <div class="particle" style="--size: 4px; --duration: 18s; --delay: 4s; --x: 40%; --y: 60%"></div>
        </div>
    </div>
    <style>
        @keyframes float {
            0% { transform: translate(0, 0) rotate(0deg); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translate(var(--x-end), var(--y-end)) rotate(360deg); opacity: 0; }
        }
        .particle {
            position: absolute;
            width: var(--size);
            height: var(--size);
            background: rgba(255,255,255,0.5);
            border-radius: 50%;
            animation: float var(--duration) var(--delay) infinite linear;
            --x-end: calc(var(--x) - 50%);
            --y-end: calc(var(--y) - 50%);
        }
        .tab-container {
            padding: 20px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-top: 15px;
        }
        .input-label {
            font-weight: bold;
            margin-bottom: 8px;
            display: block;
        }
        .conversion-box {
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 8px;
            margin: 10px 0;
            border: 1px dashed #9e9e9e;
            font-size: 0.9em;
        }
    </style>
    """, unsafe_allow_html=True)

    # Style untuk tabs
    tab_style = """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            padding: 0 20px;
            border-radius: 10px;
            transition: all 0.3s ease;
            background: #f0f2f6 !important;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .stTabs [data-baseweb="tab"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #2196F3, #0d47a1) !important;
            color: white !important;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(33, 150, 243, 0.3);
        }
    </style>
    """
    st.markdown(tab_style, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "⚖️ Hitung Massa", 
        "🎚️ Hitung Tekanan",
        "🫙 Hitung Volume",
        "🧪 Hitung Mol"
    ])
    
    R = 0.0821  # Konstanta gas ideal

    with tab1:
        # Kalkulator Massa
        with st.container():
            st.markdown("""
            <div class="tab-container content-overlay" style="border-left: 5px solid #FF9800;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #FF9800;">🏆 Kalkulator Massa Gas Super Akurat</h2>
                        <div style="background: #FFF3E0; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>⚡ Rumus Ajaib:</b> Massa = n (mol) × Mr (g/mol)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            cols = st.columns(3)
            with cols[0]:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Contoh: Oksigen", label_visibility="collapsed")
            with cols[1]:
                st.markdown('<div class="input-label">⚛️ Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f", label_visibility="collapsed")
            with cols[2]:
                st.markdown('<div class="input-label">🧮 Massa Molar (Mr)</div>', unsafe_allow_html=True)
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f", label_visibility="collapsed")
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("⚖️ 🚀 Hitung Massa Sekarang!", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr
                
                st.markdown(f"""
                <div class="content-overlay" style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #FF9800;
                            animation: fadeIn 0.5s ease-in-out;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #E65100;">🎉 Hasil Perhitungan Spektakuler!</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Massa <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #E65100; font-weight: bold; font-size: 1.5em; margin: 0;">{massa:.4f} gram</p>
                            </div>
                            <p style="margin: 10px 0 0 0; font-size: 0.9em; color: #666;">
                                ✨ Perhitungan dilakukan dengan presisi tinggi menggunakan teknologi canggih!
                            </p>
                        </div>
                    </div>
                </div>
                <style>
                    @keyframes fadeIn {{
                        from {{ opacity: 0; transform: translateY(10px); }}
                        to {{ opacity: 1; transform: translateY(0); }}
                    }}
                </style>
                """, unsafe_allow_html=True)
                
                st.balloons()

    with tab2:
        # Kalkulator Tekanan
        with st.container():
            st.markdown("""
            <div class="tab-container content-overlay" style="border-left: 5px solid #F44336;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; color: #F44336;">🔥 Kalkulator Tekanan Gas Ultra Modern</h2>
                        <div style="background: #FFEBEE; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>⚡ Rumus Dahsyat:</b> P = [n (mol) × R × T (K)] / V (L)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">⚛️ Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="input-label">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="tekanan_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="tekanan_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Ajaib: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">📦 Volume</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    V_input = st.number_input("Volume", min_value=0.0, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Spektakuler: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Menakjubkan: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🎚️ 🚀 Hitung Tekanan Sekarang!", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div class="content-overlay" style="background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #F44336;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #C62828;">🎉 Hasil Perhitungan Luar Biasa!</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #C62828; font-weight: bold; font-size: 1.5em; margin: 0;">{P:.2f} atm</p>
                            </div>
                            <p style="margin: 10px 0 0 0; font-size: 0.9em; color: #666;">
                                ⚡ Kekuatan tekanan gas telah berhasil dihitung dengan akurasi tinggi!
                            </p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown("""
            <div class="tab-container content-overlay" style="border-left: 5px solid #4CAF50;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🫙</div>
                    <div>
                        <h2 style="margin: 0; color: #4CAF50;">🌟 Kalkulator Volume Gas Revolusioner</h2>
                        <div style="background: #E8F5E9; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>⚡ Rumus Magis:</b> V = [n (mol) × R × T (K)] / P (atm)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_volume", placeholder="Contoh: Hidrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">⚛️ Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f", label_visibility="collapsed")
            
            with col2:
                st.markdown('<div class="input-label">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="volume_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="volume_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Transformasi Hebat: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    P_input = st.number_input("Tekanan", min_value=0.0, key="volume_tekanan_input", label_visibility="collapsed")
                with col2d:
                    satuan_tekanan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key="volume_tekanan_unit", label_visibility="collapsed")
                
                if satuan_tekanan == "Pa":
                    P = P_input / 101325
                elif satuan_tekanan == "kPa":
                    P = P_input / 101.325
                elif satuan_tekanan == "hPa":
                    P = P_input / 1013.25
                elif satuan_tekanan == "bar":
                    P = P_input / 1.01325
                elif satuan_tekanan in ["Torr", "mmHg"]:
                    P = P_input / 760
                else:
                    P = P_input
                
                if satuan_tekanan != "atm":
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Fantastis: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🫙 🚀 Hitung Volume Sekarang!", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div class="content-overlay" style="background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #4CAF50;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #2E7D32;">🎉 Hasil Perhitungan Menakjubkan!</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Volume <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #2E7D32; font-weight: bold; font-size: 1.5em; margin: 0;">{V:.2f} L</p>
                            </div>
                            <p style="margin: 10px 0 0 0; font-size: 0.9em; color: #666;">
                                🌟 Ruang yang ditempati gas telah berhasil dikalkulasi dengan sempurna!
                            </p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown("""
            <div class="tab-container content-overlay" style="border-left: 5px solid #9C27B0;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪 </div>
                    <div>
                        <h2 style="margin: 0; color: #9C27B0;">⚛️ Kalkulator Jumlah Mol Super Canggih</h2>
                        <div style="background: #F3E5F5; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>⚡ Rumus Ajaib:</b> n = [P (atm) × V (L)] / [R × T (K)]
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">🏷️ Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_mol", placeholder="Contoh: Karbon Dioksida", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🎚️ Tekanan</div>', unsafe_allow_html=True)
                col1a, col1b = st.columns([3,1])
                with col1a:
                    P_input = st.number_input("Tekanan", min_value=0.0, key="mol_tekanan_input", label_visibility="collapsed")
                with col1b:
                    satuan_tekanan = st.selectbox("Satuan Tekanan", ["atm", "Pa", "kPa", "hPa", "bar", "Torr", "mmHg"], key="mol_tekanan_unit", label_visibility="collapsed")
                
                if satuan_tekanan == "Pa":
                    P = P_input / 101325
                elif satuan_tekanan == "kPa":
                    P = P_input / 101.325
                elif satuan_tekanan == "hPa":
                    P = P_input / 1013.25
                elif satuan_tekanan == "bar":
                    P = P_input / 1.01325
                elif satuan_tekanan in ["Torr", "mmHg"]:
                    P = P_input / 760
                else:
                    P = P_input
                
                if satuan_tekanan != "atm":
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Luar Biasa: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="input-label">📦 Volume</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    V_input = st.number_input("Volume", min_value=0.0, key="mol_vol_input", label_visibility="collapsed")
                with col2b:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="mol_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Dahsyat: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi Hebat: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">🌡️ Suhu</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="mol_suhu_input", label_visibility="collapsed")
                with col2d:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="mol_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Transformasi Ajaib: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🧪 🚀 Hitung Mol Sekarang!", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div class="content-overlay" style="background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #9C27B0;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #7B1FA2;">🎉 Hasil Perhitungan Spektakuler!</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Jumlah mol <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #7B1FA2; font-weight: bold; font-size: 1.5em; margin: 0;">{n:.2f} mol</p>
                            </div>
                            <p style="margin: 10px 0 0 0; font-size: 0.9em; color: #666;">
                                ⚛️ Pasukan molekul gas telah berhasil dihitung dengan presisi tinggi!
                            </p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah
    st.markdown("""
    <div class="content-overlay" style="background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
                padding: 20px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 5px solid #2196F3;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 30px;">💡</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #0D47A1;">🧙‍♂️ Tips Rahasia Para Master Kimia</h3>
                <p style="margin: 0;">
                    🎯 Untuk hasil yang sempurna, pastikan semua satuan konsisten dengan konstanta gas R 
                    (0.0821 L·atm/mol·K). Gunakan suhu dalam Kelvin dan tekanan dalam atm untuk akurasi maksimal!
                </p>
                <p style="margin: 10px 0 0 0; font-size: 0.9em; color: #666;">
                    ⚡ Pro tip: Selalu periksa kembali konversi satuan untuk menghindari kesalahan perhitungan!
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.markdown("<h1 class='main-header'>📚✨ Ensiklopedia Gas - Perpustakaan Pengetahuan Tak Terbatas ✨📚</h1>", unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "🔍 Pilih Gas untuk Dijelajahi", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}",
        key="gas_selector"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <div class="content-overlay">
            <h2>{gas['icon']} {selected_gas}</h2>
            <p style="font-style: italic; font-size: 1.1em; color: #555;"><i>🌟 {gas['description']}</i></p>
            <p><b>📂 Kategori:</b> <span style="color: #2196F3; font-weight: bold;">{gas['category']}</span></p>
            <p><b>🔬 Aplikasi Menakjubkan:</b> <span style="color: #4CAF50; font-weight: bold;">{gas['aplikasi']}</span></p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["image"], width=200, caption=f"🧪 Struktur {selected_gas}")
    
    # Tab Informasi
    tabs = st.tabs(list(gas["properties"].keys()))
    
    for tab, (category, props) in zip(tabs, gas["properties"].items()):
        with tab:
            st.markdown(f"""
            <div class="content-overlay">
                <h3 style="color: #0D47A1; margin-bottom: 20px;">{category}</h3>
                <table class="property-table">
                    {"".join(f"<tr><td><b>🔹 {key}</b></td><td style='color: #333;'>{value}</td></tr>" for key, value in props.items())}
                </table>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("<h1 class='main-header'>⚠️🛡️ Panduan Keselamatan Gas - Zona Perlindungan Maksimal 🛡️⚠️</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card content-overlay">
        <h3>🚧 Simbol Bahaya yang Wajib Diketahui</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:200px;background:#ffebee;padding:15px;border-radius:10px;">
                <h4>🔥 Mudah Terbakar</h4>
                <p><b>Contoh:</b> Hidrogen, Metana</p>
                <p>• 🚫 Jauhkan dari sumber api</p>
                <p>• 🌬️ Gunakan di area berventilasi</p>
                <p>• 🧯 Siapkan alat pemadam</p>
            </div>
            <div style="flex:1;min-width:200px;background:#fff8e1;padding:15px;border-radius:10px;">
                <h4>☠️ Beracun</h4>
                <p><b>Contoh:</b> Klorin, Amonia</p>
                <p>• 🛡️ Gunakan alat pelindung diri</p>
                <p>• 🚫 Hindari inhalasi langsung</p>
                <p>• 🏥 Siapkan pertolongan pertama</p>
            </div>
            <div style="flex:1;min-width:200px;background:#e8f5e9;padding:15px;border-radius:10px;">
                <h4>💨 Pengoksidasi</h4>
                <p><b>Contoh:</b> Oksigen, Fluorin</p>
                <p>• ⚠️ Hindari kontak dengan bahan organik</p>
                <p>• 📦 Simpan terpisah dari bahan reduktor</p>
                <p>• 🧪 Gunakan wadah khusus</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card content-overlay">
        <h3>🛡️ Arsenal Alat Pelindung Diri (APD) Super Lengkap</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2090/2090004.png" width="80">
                <p><b>🎭 Masker Gas</b></p>
                <p style="font-size:0.9em;">Pelindung sistem pernapasan</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2797/2797688.png" width="80">
                <p><b>🧤 Sarung Tangan</b></p>
                <p style="font-size:0.9em;">Pelindung tangan dari bahan kimia</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/10984/10984307.png" width="80">
                <p><b>👓 Kacamata Keselamatan</b></p>
                <p style="font-size:0.9em;">Pelindung mata dari percikan</p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3000/3000504.png" width="80">
                <p><b>🥼 Jas Laboratorium</b></p>
                <p style="font-size:0.9em;">Pelindung tubuh menyeluruh</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card safety-card content-overlay">
        <h3>🚨 Protokol Darurat Super Cepat</h3>
        <ol style="font-size: 1.1em; line-height: 1.8;">
            <li>🚪 <b>Evakuasi Kilat</b> - Segera tinggalkan area jika terjadi kebocoran gas</li>
            <li>🛡️ <b>APD Wajib</b> - Gunakan alat pelindung diri yang sesuai sebelum menangani gas</li>
            <li>🔥 <b>No Fire Zone</b> - Hindari sumber api atau percikan listrik</li>
            <li>🌬️ <b>Ventilasi Maksimal</b> - Buka semua jendela dan pintu untuk sirkulasi udara</li>
            <li>📞 <b>Panggil Bantuan</b> - Hubungi petugas berwenang jika diperlukan</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card content-overlay" style="background: linear-gradient(135deg, #E1F5FE, #B3E5FC); border-left: 5px solid #03A9F4;">
        <h3>📋 Checklist Keselamatan Harian Super Lengkap</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 15px;">
            <div>
                <h4>✅ Sebelum Memulai Kerja:</h4>
                <ul>
                    <li>🔍 Periksa kondisi tabung gas secara menyeluruh</li>
                    <li>🌬️ Pastikan sistem ventilasi berfungsi optimal</li>
                    <li>🛡️ Siapkan dan kenakan APD lengkap</li>
                    <li>🧯 Cek ketersediaan alat pemadam kebakaran</li>
                    <li>📋 Review prosedur keselamatan terbaru</li>
                </ul>
            </div>
            <div>
                <h4>⚠️ Selama Bekerja:</h4>
                <ul>
                    <li>📊 Monitor tekanan gas secara berkala</li>
                    <li>🚫 Hindari area dengan ventilasi terbatas</li>
                    <li>🔥 Jangan merokok atau menyalakan api</li>
                    <li>📢 Laporkan setiap anomali dengan segera</li>
                    <li>👥 Jaga komunikasi dengan tim kerja</li>
                </ul>
            </div>
            <div>
                <h4>🔒 Setelah Selesai Kerja:</h4>
                <ul>
                    <li>🔐 Tutup semua katup gas dengan rapat</li>
                    <li>📦 Simpan tabung di tempat yang aman</li>
                    <li>🧹 Bersihkan area kerja dari kontaminan</li>
                    <li>📝 Dokumentasikan penggunaan gas</li>
                    <li>🔄 Lakukan inspeksi akhir menyeluruh</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card content-overlay" style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2); border-left: 5px solid #FF9800;">
        <h3>🎯 Tips Pro untuk Keselamatan Maksimal</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-top: 15px;">
            <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px;">
                <h4>🧠 Mental Preparation</h4>
                <p>• 📚 Pelajari MSDS (Material Safety Data Sheet) setiap gas</p>
                <p>• 🎯 Fokus penuh saat bekerja dengan gas berbahaya</p>
                <p>• 🤝 Selalu bekerja dengan sistem buddy</p>
            </div>
            <div style="background: rgba(255,255,255,0.7); padding: 15px; border-radius: 10px;">
                <h4>🔧 Technical Excellence</h4>
                <p>• 🔍 Gunakan detektor gas untuk monitoring</p>
                <p>• ⚖️ Kalibrasi alat ukur secara berkala</p>
                <p>• 🛠️ Maintenance peralatan sesuai jadwal</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER SPEKTAKULER
# ===========================================
st.markdown("---")
st.markdown("""
<div class="content-overlay" style="text-align:center;color:#666;padding:30px;margin-top:30px;background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);">
    <h3 style="color: #0D47A1; margin-bottom: 15px;">🧪✨ ChemGasMaster ✨🧪</h3>
    <p style="font-size: 1.1em; margin-bottom: 10px;">© 2025 ChemGasMaster | Kelompok 7 Kelas 1A</p>
    <p style="font-size:0.9em;margin-top:10px;color:#555;">
        🚀 Dibuat dengan ❤️ dan teknologi canggih untuk pembelajaran kimia yang revolusioner
    </p>
    <p style="font-size:0.8em;margin-top:15px;color:#777;">
        🌟 "Mengubah cara dunia memahami gas ideal, satu perhitungan pada satu waktu" 🌟
    </p>
    <div style="margin-top: 20px;">
        <span style="font-size: 1.5em;">⚗️🧬🔬⚛️🧪</span>
    </div>
</div>
""", unsafe_allow_html=True)

