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
# CSS CUSTOM + BACKGROUND UNTUK SETIAP MENU
# ===========================================
st.markdown("""
<style>
    /* Ultra Creative Background Animations */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg) scale(1); }
        25% { transform: translateY(-40px) rotate(90deg) scale(1.1); }
        50% { transform: translateY(-20px) rotate(180deg) scale(0.9); }
        75% { transform: translateY(-60px) rotate(270deg) scale(1.2); }
        100% { transform: translateY(0px) rotate(360deg) scale(1); }
    }
    
    @keyframes bubble {
        0% { transform: translateY(100vh) scale(0) rotate(0deg); opacity: 0; }
        10% { opacity: 1; }
        50% { transform: translateY(50vh) scale(1.5) rotate(180deg); opacity: 0.8; }
        90% { opacity: 1; }
        100% { transform: translateY(-100vh) scale(2) rotate(360deg); opacity: 0; }
    }
    
    @keyframes molecule-rotate {
        0% { transform: rotate(0deg) scale(1) translateX(0px); }
        25% { transform: rotate(90deg) scale(1.3) translateX(20px); }
        50% { transform: rotate(180deg) scale(0.8) translateX(-20px); }
        75% { transform: rotate(270deg) scale(1.1) translateX(10px); }
        100% { transform: rotate(360deg) scale(1) translateX(0px); }
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 0%; transform: rotate(0deg); }
        25% { background-position: 100% 0%; transform: rotate(90deg); }
        50% { background-position: 100% 100%; transform: rotate(180deg); }
        75% { background-position: 0% 100%; transform: rotate(270deg); }
        100% { background-position: 0% 0%; transform: rotate(360deg); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1) rotate(0deg); opacity: 0.6; }
        25% { transform: scale(1.2) rotate(90deg); opacity: 0.8; }
        50% { transform: scale(0.8) rotate(180deg); opacity: 1; }
        75% { transform: scale(1.1) rotate(270deg); opacity: 0.7; }
        100% { transform: scale(1) rotate(360deg); opacity: 0.6; }
    }
    
    @keyframes lightning {
        0%, 85%, 100% { background-color: transparent; box-shadow: none; }
        5%, 10% { background-color: rgba(255, 255, 0, 0.4); box-shadow: 0 0 50px rgba(255, 255, 0, 0.8); }
        15%, 20% { background-color: rgba(255, 100, 100, 0.3); box-shadow: 0 0 30px rgba(255, 100, 100, 0.6); }
    }
    
    @keyframes wave {
        0% { transform: translateX(-100%) skewX(0deg); }
        50% { transform: translateX(0%) skewX(15deg); }
        100% { transform: translateX(100%) skewX(0deg); }
    }
    
    @keyframes spiral {
        0% { transform: rotate(0deg) translateX(50px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(50px) rotate(-360deg); }
    }

    /* BERANDA - Ultra Creative Molecular Universe */
    .beranda-bg {
        background: 
            radial-gradient(circle at 20% 20%, #667eea 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, #764ba2 0%, transparent 50%),
            radial-gradient(circle at 40% 60%, #f093fb 0%, transparent 50%),
            radial-gradient(circle at 60% 40%, #f5576c 0%, transparent 50%),
            linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        background-size: 800% 800%, 600% 600%, 400% 400%, 500% 500%, 100% 100%;
        animation: gradient-shift 12s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .beranda-bg::before {
        content: '⚗️ 🧪 🔬 ⚛️ 🧬 💎 🌡️ ⚡ 🌟 💫 🔥 ❄️';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        font-size: 6rem;
        opacity: 0.2;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
        animation: float 8s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 0 0 30px rgba(255,255,255,0.8), 0 0 60px rgba(255,255,255,0.4);
        filter: blur(1px);
    }
    
    .beranda-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.4) 8px, transparent 8px),
            radial-gradient(circle at 75% 75%, rgba(255,255,255,0.3) 12px, transparent 12px),
            radial-gradient(circle at 50% 50%, rgba(255,255,255,0.35) 6px, transparent 6px),
            radial-gradient(circle at 10% 90%, rgba(255,255,255,0.25) 10px, transparent 10px),
            radial-gradient(circle at 90% 10%, rgba(255,255,255,0.3) 14px, transparent 14px);
        background-size: 200px 200px, 300px 300px, 150px 150px, 250px 250px, 180px 180px;
        animation: spiral 20s linear infinite;
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.5));
    }

    /* KALKULATOR - Ultra Dynamic Laboratory */
    .kalkulator-bg {
        background: 
            conic-gradient(from 0deg at 30% 30%, #667eea, #764ba2, #f093fb, #f5576c, #4facfe, #00f2fe, #667eea),
            conic-gradient(from 180deg at 70% 70%, #00f2fe, #4facfe, #f5576c, #f093fb, #764ba2, #667eea, #00f2fe),
            linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8));
        background-size: 600% 600%, 400% 400%, 100% 100%;
        animation: gradient-shift 8s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .kalkulator-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            repeating-linear-gradient(45deg,
                transparent,
                transparent 20px,
                rgba(255,255,255,0.15) 20px,
                rgba(255,255,255,0.15) 40px),
            repeating-linear-gradient(-45deg,
                transparent,
                transparent 30px,
                rgba(255,255,255,0.1) 30px,
                rgba(255,255,255,0.1) 60px),
            repeating-linear-gradient(90deg,
                transparent,
                transparent 25px,
                rgba(255,255,255,0.08) 25px,
                rgba(255,255,255,0.08) 50px);
        animation: wave 15s ease-in-out infinite;
        filter: blur(0.5px);
    }
    
    .kalkulator-bg::after {
        content: '🔬 ⚗️ 🧪 📊 🔍 ⚡ 🌡️ ⚖️ 🧮 📐 🔢 ⚙️';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        font-size: 4rem;
        opacity: 0.25;
        display: flex;
        justify-content: space-around;
        animation: pulse 6s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 0 0 20px rgba(255,255,255,0.9), 0 0 40px rgba(255,255,255,0.5);
        transform-origin: center bottom;
    }

    /* ENSIKLOPEDIA - Mystical Knowledge Realm */
    .ensiklopedia-bg {
        background: 
            radial-gradient(ellipse at top left, #ff9a9e 0%, transparent 70%),
            radial-gradient(ellipse at top right, #fecfef 0%, transparent 70%),
            radial-gradient(ellipse at bottom left, #a8edea 0%, transparent 70%),
            radial-gradient(ellipse at bottom right, #fed6e3 0%, transparent 70%),
            linear-gradient(45deg, rgba(255, 154, 158, 0.6), rgba(254, 207, 239, 0.6));
        background-size: 800% 800%, 600% 600%, 700% 700%, 500% 500%, 100% 100%;
        animation: gradient-shift 15s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .ensiklopedia-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image:
            radial-gradient(circle at 20% 20%, rgba(255,255,255,0.4) 4px, transparent 4px),
            radial-gradient(circle at 80% 80%, rgba(255,255,255,0.3) 6px, transparent 6px),
            radial-gradient(circle at 60% 40%, rgba(255,255,255,0.35) 3px, transparent 3px),
            radial-gradient(circle at 40% 80%, rgba(255,255,255,0.25) 5px, transparent 5px),
            radial-gradient(circle at 80% 20%, rgba(255,255,255,0.3) 7px, transparent 7px);
        background-size: 120px 120px, 180px 180px, 90px 90px, 150px 150px, 200px 200px;
        animation: float 12s ease-in-out infinite reverse;
        filter: drop-shadow(0 0 8px rgba(255,255,255,0.4));
    }
    
    .ensiklopedia-bg::after {
        content: '📚 🧬 ⚛️ 🔬 💎 🌟 📖 🎯 🔍 📊 🧪 ⚗️';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 7rem;
        opacity: 0.2;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        animation: molecule-rotate 18s linear infinite;
        pointer-events: none;
        text-shadow: 0 0 35px rgba(255,255,255,0.7), 0 0 70px rgba(255,255,255,0.3);
        filter: blur(1px);
    }

    /* KESELAMATAN - Dramatic Warning Zone */
    .keselamatan-bg {
        background: 
            conic-gradient(from 45deg at 25% 25%, #ff7675, #fd79a8, #fdcb6e, #e17055, #ff6b6b, #ee5a24, #ff7675),
            conic-gradient(from 225deg at 75% 75%, #ee5a24, #ff6b6b, #e17055, #fdcb6e, #fd79a8, #ff7675, #ee5a24),
            radial-gradient(circle at center, rgba(255, 118, 117, 0.8), rgba(238, 90, 36, 0.8));
        background-size: 500% 500%, 400% 400%, 100% 100%;
        animation: gradient-shift 5s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .keselamatan-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            repeating-conic-gradient(from 0deg at 30% 30%, 
                transparent 0deg 60deg, 
                rgba(255,255,255,0.15) 60deg 120deg),
            repeating-conic-gradient(from 90deg at 70% 70%, 
                transparent 0deg 45deg, 
                rgba(255,255,255,0.12) 45deg 90deg),
            repeating-conic-gradient(from 180deg at 50% 50%, 
                transparent 0deg 30deg, 
                rgba(255,255,255,0.1) 30deg 60deg);
        background-size: 150px 150px, 200px 200px, 100px 100px;
        animation: lightning 2s infinite, spiral 10s linear infinite;
        filter: blur(0.5px);
    }
    
    .keselamatan-bg::after {
        content: '⚠️ 🚨 ☠️ 🔥 ⚡ 🛡️ 🚫 ⛔ 💀 🆘 ☢️ ⚠️';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        font-size: 5rem;
        opacity: 0.25;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
        animation: pulse 3s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 0 0 25px rgba(255,255,255,0.8), 0 0 50px rgba(255,255,255,0.4);
        filter: drop-shadow(0 0 10px rgba(255, 0, 0, 0.5));
    }

    /* Ultra Enhanced floating particles */
    .floating-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        background: radial-gradient(circle, 
            rgba(255,255,255,0.9) 0%, 
            rgba(255,255,255,0.6) 30%, 
            rgba(255,255,255,0.3) 60%, 
            rgba(255,255,255,0.1) 100%);
        border-radius: 50%;
        animation: bubble 25s infinite linear;
        box-shadow: 
            0 0 20px rgba(255,255,255,0.8),
            0 0 40px rgba(255,255,255,0.4),
            inset 0 0 10px rgba(255,255,255,0.6);
        filter: blur(0.5px);
    }
    
    .particle:nth-child(1) { left: 5%; width: 30px; height: 30px; animation-delay: 0s; }
    .particle:nth-child(2) { left: 15%; width: 25px; height: 25px; animation-delay: 4s; }
    .particle:nth-child(3) { left: 25%; width: 35px; height: 35px; animation-delay: 8s; }
    .particle:nth-child(4) { left: 35%; width: 20px; height: 20px; animation-delay: 12s; }
    .particle:nth-child(5) { left: 45%; width: 28px; height: 28px; animation-delay: 16s; }
    .particle:nth-child(6) { left: 55%; width: 32px; height: 32px; animation-delay: 20s; }
    .particle:nth-child(7) { left: 65%; width: 22px; height: 22px; animation-delay: 24s; }
    .particle:nth-child(8) { left: 75%; width: 26px; height: 26px; animation-delay: 28s; }
    .particle:nth-child(9) { left: 85%; width: 30px; height: 30px; animation-delay: 32s; }
    .particle:nth-child(10) { left: 95%; width: 24px; height: 24px; animation-delay: 36s; }

    /* Ultra Enhanced card styling */
    .main-header {
        color: #0d47a1;
        border-bottom: 3px solid #0d47a1;
        padding: 25px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2);
        background: rgba(255,255,255,0.98);
        border-radius: 20px;
        margin-bottom: 25px;
        backdrop-filter: blur(25px);
        box-shadow: 
            0 15px 40px rgba(0,0,0,0.3),
            0 5px 15px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.8);
        border: 2px solid rgba(255,255,255,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: wave 3s ease-in-out infinite;
    }
    
    .card {
        padding: 30px;
        border-radius: 25px;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.2),
            0 5px 15px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.9);
        margin-bottom: 30px;
        background: rgba(255,255,255,0.99) !important;
        backdrop-filter: blur(30px);
        border: 2px solid rgba(255,255,255,0.4);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 
            0 25px 50px rgba(0,0,0,0.3),
            0 10px 25px rgba(0,0,0,0.15);
    }
    
    .calc-card {
        background: linear-gradient(135deg, rgba(227, 242, 253, 0.99) 0%, rgba(187, 222, 251, 0.99) 100%) !important;
        border-left: 8px solid #2196f3;
        box-shadow: 
            0 15px 40px rgba(33, 150, 243, 0.3),
            0 5px 15px rgba(33, 150, 243, 0.2);
    }
    
    .result-card {
        background: linear-gradient(135deg, rgba(232, 245, 233, 0.99) 0%, rgba(200, 230, 201, 0.99) 100%) !important;
        border-left: 8px solid #4caf50;
        box-shadow: 
            0 15px 40px rgba(76, 175, 80, 0.3),
            0 5px 15px rgba(76, 175, 80, 0.2);
    }
    
    .gas-card {
        background: linear-gradient(135deg, rgba(255, 243, 224, 0.99) 0%, rgba(255, 224, 178, 0.99) 100%) !important;
        border-left: 8px solid #ff9800;
        box-shadow: 
            0 15px 40px rgba(255, 152, 0, 0.3),
            0 5px 15px rgba(255, 152, 0, 0.2);
    }
    
    .safety-card {
        background: linear-gradient(135deg, rgba(255, 235, 238, 0.99) 0%, rgba(255, 205, 210, 0.99) 100%) !important;
        border-left: 8px solid #f44336;
        box-shadow: 
            0 15px 40px rgba(244, 67, 54, 0.3),
            0 5px 15px rgba(244, 67, 54, 0.2);
    }
    
    .conversion-box {
        background: linear-gradient(135deg, rgba(245, 245, 245, 0.98), rgba(235, 235, 235, 0.98));
        padding: 15px;
        border-radius: 15px;
        margin: 15px 0;
        border: 3px dashed #9e9e9e;
        backdrop-filter: blur(15px);
        box-shadow: 
            0 8px 20px rgba(0,0,0,0.15),
            inset 0 1px 0 rgba(255,255,255,0.8);
        position: relative;
        overflow: hidden;
    }
    
    .conversion-box::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(158,158,158,0.1), transparent);
        animation: wave 4s ease-in-out infinite;
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        background: rgba(255,255,255,0.98);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 
            0 15px 35px rgba(0,0,0,0.2),
            0 5px 15px rgba(0,0,0,0.1);
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    .property-table th {
        background: linear-gradient(135deg, rgba(13, 71, 161, 0.98), rgba(25, 118, 210, 0.98));
        color: white;
        padding: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .property-table th::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: wave 5s ease-in-out infinite;
    }
    
    .property-table td {
        padding: 15px;
        border-bottom: 2px solid #ddd;
        background: rgba(255,255,255,0.95);
        transition: all 0.3s ease;
    }
    
    .property-table td:hover {
        background: rgba(245,245,245,0.98);
        transform: scale(1.02);
    }
    
    /* Ultra Enhanced tab styling */
    .tab-container {
        padding: 30px;
        background: rgba(255, 255, 255, 0.99) !important;
        border-radius: 25px;
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.2),
            0 10px 20px rgba(0,0,0,0.1),
            inset 0 1px 0 rgba(255,255,255,0.9);
        margin-top: 25px;
        backdrop-filter: blur(30px);
        border: 2px solid rgba(255,255,255,0.4);
        position: relative;
        overflow: hidden;
    }
    
    .tab-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.05), transparent);
        animation: wave 6s ease-in-out infinite;
    }
    
    /* Ultra Enhanced sidebar */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.2) !important;
        backdrop-filter: blur(30px) !important;
        border-right: 2px solid rgba(255,255,255,0.3) !important;
        box-shadow: 5px 0 20px rgba(0,0,0,0.1) !important;
    }
    
    /* Ultra Enhanced buttons */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb) !important;
        border: none !important;
        border-radius: 30px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            0 10px 25px rgba(0,0,0,0.4),
            0 5px 15px rgba(0,0,0,0.2),
            inset 0 1px 0 rgba(255,255,255,0.3) !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: wave 2s ease-in-out infinite;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 
            0 20px 40px rgba(0,0,0,0.5),
            0 10px 25px rgba(0,0,0,0.3) !important;
        background: linear-gradient(45deg, #764ba2, #f093fb, #667eea) !important;
    }
    
    /* Ultra Enhanced inputs */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 15px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
    }
    
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.95) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 15px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        transform: scale(1.02) !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
    }
</style>
""", unsafe_allow_html=True)

# Tambahkan floating particles
st.markdown("""
<div class="floating-particles">
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
</div>
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
        "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()-
