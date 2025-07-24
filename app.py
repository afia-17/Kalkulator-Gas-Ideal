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
        0% { 
            transform: translateY(100vh) scale(0) rotate(0deg); 
            opacity: 0; 
            border-radius: 50%; 
        }
        10% { 
            opacity: 1; 
            border-radius: 50%; 
        }
        50% { 
            border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; 
            transform: translateY(50vh) scale(1.5) rotate(180deg); 
        }
        90% { 
            opacity: 1; 
            border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; 
        }
        100% { 
            transform: translateY(-20vh) scale(2) rotate(360deg); 
            opacity: 0; 
            border-radius: 50%; 
        }
    }
    
    @keyframes molecule-rotate {
        0% { transform: rotate(0deg) scale(1) skew(0deg); }
        25% { transform: rotate(90deg) scale(1.3) skew(5deg); }
        50% { transform: rotate(180deg) scale(0.8) skew(-5deg); }
        75% { transform: rotate(270deg) scale(1.1) skew(3deg); }
        100% { transform: rotate(360deg) scale(1) skew(0deg); }
    }
    
    @keyframes gradient-shift {
        0% { 
            background-position: 0% 50%; 
            filter: hue-rotate(0deg) brightness(1); 
        }
        20% { 
            background-position: 100% 0%; 
            filter: hue-rotate(72deg) brightness(1.2); 
        }
        40% { 
            background-position: 100% 100%; 
            filter: hue-rotate(144deg) brightness(0.9); 
        }
        60% { 
            background-position: 0% 100%; 
            filter: hue-rotate(216deg) brightness(1.1); 
        }
        80% { 
            background-position: 0% 0%; 
            filter: hue-rotate(288deg) brightness(1.3); 
        }
        100% { 
            background-position: 0% 50%; 
            filter: hue-rotate(360deg) brightness(1); 
        }
    }
    
    @keyframes pulse {
        0% { transform: scale(1) rotate(0deg); opacity: 0.6; }
        33% { transform: scale(1.4) rotate(120deg); opacity: 1; }
        66% { transform: scale(0.8) rotate(240deg); opacity: 0.8; }
        100% { transform: scale(1) rotate(360deg); opacity: 0.6; }
    }
    
    @keyframes lightning {
        0%, 85%, 100% { 
            background-color: transparent; 
            box-shadow: none; 
        }
        5%, 15% { 
            background-color: rgba(255, 255, 0, 0.4); 
            box-shadow: 0 0 50px rgba(255, 255, 0, 0.6); 
        }
        10% { 
            background-color: rgba(255, 255, 255, 0.3); 
            box-shadow: 0 0 100px rgba(255, 255, 255, 0.8); 
        }
    }
    
    @keyframes matrix-rain {
        0% { transform: translateY(-100vh) translateX(0); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(100vh) translateX(50px); opacity: 0; }
    }
    
    @keyframes starfield {
        0% { transform: scale(0) rotate(0deg); opacity: 0; }
        50% { transform: scale(1) rotate(180deg); opacity: 1; }
        100% { transform: scale(0) rotate(360deg); opacity: 0; }
    }

    /* BERANDA - Ultra Futuristic Molecular Theme */
    .beranda-bg {
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(200, 200, 255, 0.2) 0%, transparent 50%),
            linear-gradient(45deg, 
                #667eea 0%, 
                #764ba2 12%, 
                #f093fb 25%, 
                #f5576c 37%, 
                #4facfe 50%,
                #00f2fe 62%,
                #43e97b 75%,
                #38f9d7 87%,
                #667eea 100%);
        background-size: 800% 800%, 600% 600%, 400% 400%, 1000% 1000%;
        animation: gradient-shift 15s ease infinite;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        overflow: hidden;
    }
    
    .beranda-bg::before {
        content: '🌟 ⚗️ 🧪 🔬 ⚛️ 🧬 💎 🌡️ ⚡ 🎆 ✨ 🌈';
        position: absolute;
        top: 15%;
        left: 0;
        right: 0;
        font-size: 5rem;
        opacity: 0.25;
        text-align: center;
        animation: float 8s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 
            0 0 10px rgba(255,255,255,0.8),
            0 0 20px rgba(255,255,255,0.6),
            0 0 30px rgba(255,255,255,0.4);
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.8));
    }
    
    .beranda-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: 
            radial-gradient(circle at 25% 25%, rgba(255,255,255,0.4) 1px, transparent 1px),
            radial-gradient(circle at 75% 75%, rgba(255,255,255,0.3) 2px, transparent 2px),
            radial-gradient(circle at 50% 50%, rgba(255,255,255,0.35) 1.5px, transparent 1.5px),
            radial-gradient(circle at 10% 90%, rgba(255,255,255,0.2) 5px, transparent 5px),
            radial-gradient(circle at 90% 10%, rgba(255,255,255,0.25) 6px, transparent 6px);
        background-size: 120px 120px, 180px 180px, 100px 100px, 200px 200px, 160px 160px;
        animation: molecule-rotate 20s linear infinite;
        filter: blur(0.5px);
    }

    /* KALKULATOR - Ultra Advanced Laboratory Theme */
    .kalkulator-bg {
        background: 
            conic-gradient(from 0deg at 30% 30%, 
                #667eea 0deg, 
                #764ba2 72deg, 
                #f093fb 144deg, 
                #f5576c 216deg, 
                #4facfe 288deg, 
                #667eea 360deg),
            conic-gradient(from 180deg at 70% 70%, 
                #00f2fe 0deg, 
                #43e97b 60deg, 
                #38f9d7 120deg, 
                #667eea 180deg, 
                #764ba2 240deg, 
                #00f2fe 360deg),
            linear-gradient(135deg, 
                rgba(102, 126, 234, 0.8) 0%,
                rgba(118, 75, 162, 0.8) 25%,
                rgba(240, 147, 251, 0.8) 50%,
                rgba(245, 87, 108, 0.8) 75%,
                rgba(79, 172, 254, 0.8) 100%);
        background-size: 600% 600%, 800% 800%, 400% 400%;
        animation: gradient-shift 12s ease infinite;
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
                transparent 25px,
                rgba(255,255,255,0.1) 25px,
                rgba(255,255,255,0.1) 50px),
            repeating-linear-gradient(90deg,
                transparent,
                transparent 30px,
                rgba(255,255,255,0.08) 30px,
                rgba(255,255,255,0.08) 60px);
        animation: float 10s ease-in-out infinite;
        filter: blur(0.5px);
    }
    
    .kalkulator-bg::after {
        content: '🔬 ⚗️ 🧪 📊 🔍 ⚡ 🌡️ ⚖️ 🎯 🔥 💫 ⭐';
        position: absolute;
        bottom: 15%;
        left: 0;
        right: 0;
        font-size: 4rem;
        opacity: 0.3;
        text-align: center;
        animation: pulse 5s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 
            0 0 15px rgba(255,255,255,0.9),
            0 0 30px rgba(255,255,255,0.7),
            0 0 45px rgba(255,255,255,0.5);
        filter: drop-shadow(0 0 15px rgba(255,255,255,0.9));
    }

    /* ENSIKLOPEDIA - Ultra Magical Library Theme */
    .ensiklopedia-bg {
        background: 
            radial-gradient(ellipse at top left, rgba(255, 154, 158, 0.5) 0%, transparent 70%),
            radial-gradient(ellipse at top right, rgba(254, 207, 239, 0.5) 0%, transparent 70%),
            radial-gradient(ellipse at bottom left, rgba(168, 237, 234, 0.5) 0%, transparent 70%),
            radial-gradient(ellipse at bottom right, rgba(255, 154, 158, 0.5) 0%, transparent 70%),
            linear-gradient(45deg, 
                #ff9a9e 0%,
                #fecfef 15%,  
                #fecfef 30%,
                #ff9a9e 45%,
                #a8edea 60%,
                #fed6e3 75%,
                #d299c2 90%,
                #ff9a9e 100%);
        background-size: 400% 400%, 500% 500%, 600% 600%, 450% 450%, 800% 800%;
        animation: gradient-shift 18s ease infinite;
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
            radial-gradient(circle at 20% 20%, rgba(255,255,255,0.4) 1px, transparent 1px),
            radial-gradient(circle at 80% 80%, rgba(255,255,255,0.3) 2px, transparent 2px),
            radial-gradient(circle at 40% 60%, rgba(255,255,255,0.35) 1.5px, transparent 1.5px),
            radial-gradient(circle at 60% 40%, rgba(255,255,255,0.25) 2.5px, transparent 2.5px),
            radial-gradient(circle at 10% 90%, rgba(255,255,255,0.3) 3px, transparent 3px);
        background-size: 60px 60px, 90px 90px, 75px 75px, 120px 120px, 150px 150px;
        animation: starfield 15s ease-in-out infinite;
    }
    
    .ensiklopedia-bg::after {
        content: '📚 🧬 ⚛️ 🔬 💎 🌟 📖 🎯 🧭 🔮 ✨ 🌈';
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 6rem;
        opacity: 0.2;
        animation: molecule-rotate 25s linear infinite;
        pointer-events: none;
        text-shadow: 
            0 0 20px rgba(255,255,255,0.8),
            0 0 40px rgba(255,255,255,0.6),
            0 0 60px rgba(255,255,255,0.4);
        filter: drop-shadow(0 0 20px rgba(255,255,255,0.8));
    }

    /* KESELAMATAN - Ultra Dramatic Warning Theme */
    .keselamatan-bg {
        background: 
            conic-gradient(from 45deg at 25% 25%, 
                #ff7675 0deg, 
                #fd79a8 45deg, 
                #fdcb6e 90deg, 
                #e17055 135deg, 
                #ff6b6b 180deg, 
                #ee5a24 225deg,
                #ff3838 270deg,
                #ff9f43 315deg,
                #ff7675 360deg),
            conic-gradient(from 225deg at 75% 75%, 
                #ee5a24 0deg, 
                #ff7675 60deg, 
                #fd79a8 120deg, 
                #fdcb6e 180deg, 
                #e17055 240deg, 
                #ff6b6b 300deg,
                #ee5a24 360deg),
            linear-gradient(135deg, 
                rgba(255, 118, 117, 0.9) 0%,
                rgba(253, 121, 168, 0.9) 20%,
                rgba(253, 203, 110, 0.9) 40%,
                rgba(225, 112, 85, 0.9) 60%,
                rgba(255, 107, 107, 0.9) 80%,
                rgba(238, 90, 36, 0.9) 100%);
        background-size: 500% 500%, 700% 700%, 300% 300%;
        animation: gradient-shift 8s ease infinite;
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
            repeating-conic-gradient(from 0deg at 20% 20%, 
                transparent 0deg 30deg, 
                rgba(255,255,255,0.2) 30deg 60deg,
                transparent 60deg 90deg,
                rgba(255,255,255,0.15) 90deg 120deg),
            repeating-conic-gradient(from 90deg at 80% 80%, 
                transparent 0deg 40deg, 
                rgba(255,255,255,0.18) 40deg 80deg,
                transparent 80deg 120deg,
                rgba(255,255,255,0.12) 120deg 160deg);
        background-size: 80px 80px, 120px 120px;
        animation: lightning 2s infinite;
        filter: blur(0.5px);
    }
    
    .keselamatan-bg::after {
        content: '⚠️ 🚨 ☠️ 🔥 ⚡ 🛡️ 🚫 ⛔ 💀 🧯 🚒 ⚠️';
        position: absolute;
        top: 25%;
        left: 0;
        right: 0;
        font-size: 5rem;
        opacity: 0.25;
        text-align: center;
        animation: pulse 3s ease-in-out infinite;
        pointer-events: none;
        text-shadow: 
            0 0 10px rgba(255,255,255,0.9),
            0 0 20px rgba(255,255,0,0.7),
            0 0 30px rgba(255,0,0,0.5);
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.9));
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
        background: 
            radial-gradient(circle, 
                rgba(255,255,255,0.9) 0%, 
                rgba(255,255,255,0.6) 30%,
                rgba(255,255,255,0.3) 60%,
                rgba(255,255,255,0.1) 100%);
        border-radius: 50%;
        animation: bubble 25s infinite linear;
        box-shadow: 
            0 0 10px rgba(255,255,255,0.6),
            0 0 20px rgba(255,255,255,0.4),
            0 0 30px rgba(255,255,255,0.2);
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
        padding-bottom: 15px;
        text-shadow: 
            2px 2px 4px rgba(0,0,0,0.1),
            0 0 10px rgba(13,71,161,0.3);
        background: 
            linear-gradient(135deg, 
                rgba(255,255,255,0.98) 0%, 
                rgba(255,255,255,0.95) 100%);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        backdrop-filter: blur(20px);
        box-shadow: 
            0 10px 40px rgba(0,0,0,0.2),
            0 0 20px rgba(13,71,161,0.1);
        border: 2px solid rgba(255,255,255,0.4);
    }
    
    .card {
        padding: 30px;
        border-radius: 25px;
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.15),
            0 0 20px rgba(255,255,255,0.1);
        margin-bottom: 30px;
        background: 
            linear-gradient(135deg, 
                rgba(255,255,255,0.99) 0%, 
                rgba(255,255,255,0.96) 100%) !important;
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255,255,255,0.4);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 
            0 15px 40px rgba(0,0,0,0.2),
            0 0 30px rgba(255,255,255,0.2);
    }
    
    .calc-card {
        background: linear-gradient(135deg, 
            rgba(227, 242, 253, 0.99) 0%, 
            rgba(187, 222, 251, 0.99) 100%) !important;
        border-left: 6px solid #2196f3;
        box-shadow: 
            0 12px 35px rgba(33, 150, 243, 0.25),
            0 0 25px rgba(33, 150, 243, 0.1);
    }
    
    .result-card {
        background: linear-gradient(135deg, 
            rgba(232, 245, 233, 0.99) 0%, 
            rgba(200, 230, 201, 0.99) 100%) !important;
        border-left: 6px solid #4caf50;
        box-shadow: 
            0 12px 35px rgba(76, 175, 80, 0.25),
            0 0 25px rgba(76, 175, 80, 0.1);
    }
    
    .gas-card {
        background: linear-gradient(135deg, 
            rgba(255, 243, 224, 0.99) 0%, 
            rgba(255, 224, 178, 0.99) 100%) !important;
        border-left: 6px solid #ff9800;
        box-shadow: 
            0 12px 35px rgba(255, 152, 0, 0.25),
            0 0 25px rgba(255, 152, 0, 0.1);
    }
    
    .safety-card {
        background: linear-gradient(135deg, 
            rgba(255, 235, 238, 0.99) 0%, 
            rgba(255, 205, 210, 0.99) 100%) !important;
        border-left: 6px solid #f44336;
        box-shadow: 
            0 12px 35px rgba(244, 67, 54, 0.25),
            0 0 25px rgba(244, 67, 54, 0.1);
    }
    
    .conversion-box {
        background: linear-gradient(135deg, 
            rgba(245, 245, 245, 0.98) 0%, 
            rgba(250, 250, 250, 0.98) 100%);
        padding: 15px;
        border-radius: 12px;
        margin: 15px 0;
        border: 2px dashed #9e9e9e;
        backdrop-filter: blur(15px);
        box-shadow: 
            0 6px 20px rgba(0,0,0,0.1),
            0 0 15px rgba(255,255,255,0.5);
        transition: all 0.3s ease;
    }
    
    .conversion-box:hover {
        transform: translateY(-2px);
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.15),
            0 0 20px rgba(255,255,255,0.7);
    }
    
    .property-table {
        width: 100%;
        border-collapse: collapse;
        background: rgba(255,255,255,0.98);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 
            0 10px 30px rgba(0,0,0,0.15),
            0 0 20px rgba(255,255,255,0.1);
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    .property-table th {
        background: linear-gradient(135deg, 
            rgba(13, 71, 161, 0.98) 0%, 
            rgba(25, 118, 210, 0.98) 100%);
        color: white;
        padding: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        font-weight: bold;
    }
    
    .property-table td {
        padding: 15px;
        border-bottom: 1px solid #ddd;
        background: rgba(255,255,255,0.95);
        transition: background 0.3s ease;
    }
    
    .property-table td:hover {
        background: rgba(255,255,255,1);
    }
    
    /* Ultra Enhanced tab styling */
    .tab-container {
        padding: 30px;
        background: 
            linear-gradient(135deg, 
                rgba(255, 255, 255, 0.99) 0%, 
                rgba(255, 255, 255, 0.96) 100%) !important;
        border-radius: 25px;
        box-shadow: 
            0 12px 35px rgba(0,0,0,0.18),
            0 0 25px rgba(255,255,255,0.2);
        margin-top: 25px;
        backdrop-filter: blur(25px);
        border: 2px solid rgba(255,255,255,0.4);
        transition: all 0.3s ease;
    }
    
    .tab-container:hover {
        transform: translateY(-3px);
        box-shadow: 
            0 18px 45px rgba(0,0,0,0.25),
            0 0 35px rgba(255,255,255,0.3);
    }
    
    /* Ultra Enhanced sidebar */
    .css-1d391kg {
        background: 
            linear-gradient(135deg, 
                rgba(255, 255, 255, 0.2) 0%, 
                rgba(255, 255, 255, 0.1) 100%) !important;
        backdrop-filter: blur(25px) !important;
        border-right: 2px solid rgba(255,255,255,0.3) !important;
        box-shadow: 0 0 30px rgba(255,255,255,0.1) !important;
    }
    
    /* Ultra Enhanced buttons */
    .stButton > button {
        background: linear-gradient(45deg, 
            #667eea 0%, 
            #764ba2 50%, 
            #667eea 100%) !important;
        border: none !important;
        border-radius: 30px !important;
        transition: all 0.4s ease !important;
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.3),
            0 0 20px rgba(102,126,234,0.3) !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        padding: 12px 25px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.05) !important;
        box-shadow: 
            0 15px 45px rgba(0,0,0,0.4),
            0 0 30px rgba(118,75,162,0.5) !important;
        background: linear-gradient(45deg, 
            #764ba2 0%, 
            #667eea 50%, 
            #764ba2 100%) !important;
    }
    
    /* Ultra Enhanced selectbox and inputs */
    .stSelectbox > div > div {
        background: 
            linear-gradient(135deg, 
                rgba(255,255,255,0.95) 0%, 
                rgba(255,255,255,0.9) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 12px !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stSelectbox > div > div:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
    }
    
    .stNumberInput > div > div > input {
        background: 
            linear-gradient(135deg, 
                rgba(255,255,255,0.95) 0%, 
                rgba(255,255,255,0.9) 100%) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 12px !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus {
        transform: translateY(-2px) !important;
        box-shadow: 
            0 8px 25px rgba(0,0,0,0.15),
            0 0 15px rgba(102,126,234,0.3) !important;
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
        index=0
    )
    st.markdown("---")
    st.markdown("""
    <div class="card gas-card">
        <small>ℹ️ Menggunakan persamaan gas ideal: PV=nRT (R=0.0821 L·atm/mol·K)</small>
    </div>
    """, unsafe_allow_html=True)

# Fungsi untuk menerapkan background berdasarkan menu
def apply_background(menu_name):
    if menu_name == "🏠 Beranda":
        st.markdown('<div class="beranda-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>', unsafe_allow_html=True)
    elif menu_name == "🧮 Kalkulator Gas":
        st.markdown('<div class="kalkulator-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>', unsafe_allow_html=True)
    elif menu_name == "📚 Ensiklopedia Gas":
        st.markdown('<div class="ensiklopedia-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>', unsafe_allow_html=True)
    elif menu_name == "⚠️ Panduan Keselamatan":
        st.markdown('<div class="keselamatan-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;"></div>', unsafe_allow_html=True)

# Terapkan background sesuai menu yang dipilih
apply_background(menu)

# ===========================================
# HALAMAN UTAMA (BERANDA)
# ===========================================
if menu == "🏠 Beranda":
    st.markdown("<h1 class='main-header'>ChemGasMaster</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card calc-card">
        <h3>Selamat Datang di Aplikasi ChemGasMaster!</h3>
        <p>Platform lengkap untuk analisis gas ideal dan informasi kimia.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Persamaan Gas Ideal dengan penjelasan
    st.latex(r'''PV = nRT''')
    
    cols = st.columns([3, 2])
    with cols[0]:
        st.markdown("""
        <div style="margin-top:20px;">
            <h4>Persamaan Gas Ideal:</h4>
            <p><b>P</b> = Tekanan (atm)</p>
            <p><b>V</b> = Volume (L)</p>
            <p><b>n</b> = Jumlah mol (mol)</p>
            <p><b>R</b> = Konstanta gas = 0.0821 L·atm/mol·K</p>
            <p><b>T</b> = Suhu (K)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div style="margin-top:20px;">
            <h4>Fakta Menarik:</h4>
            <p>🎚️ <b>Gas Ideal Tidak Nyata</b> - Hanya model matematis yang sempurna</p>
            <p>🌡️ <b>Kondisi Ideal</b> - Tekanan rendah & suhu tinggi</p>
            <p>🧪 <b>1 mol gas</b> = 6.022×10²³ molekul</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Visualisasi variabel
    st.markdown("<h4 style='margin-top:30px;'>Variabel Utama:</h4>", unsafe_allow_html=True)
    var_cols = st.columns(4)
    variables = [
        ("P", "Tekanan", "Mengukur gaya gas<br>pada wadah", "#ffcdd2"),
        ("V", "Volume", "Ruang yang<br>ditempati gas", "#c8e6c9"),
        ("n", "Jumlah Mol", "Banyaknya<br>partikel gas", "#bbdefb"),
        ("T", "Suhu", "Ukuran energi<br>kinetik partikel", "#fff9c4")
    ]
    
    for col, (var, name, desc, color) in zip(var_cols, variables):
        with col:
            st.markdown(f"""
            <div style="background:{color};padding:15px;border-radius:10px;height:150px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
                <h3 style="margin:5px 0;">{var}</h3>
                <p style="margin:5px 0;font-weight:bold;">{name}</p>
                <p style="margin:5px 0;font-size:0.8em;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Contoh aplikasi
    st.markdown("""
    <div class="card" style="margin-top:30px;">
        <h4>💡 Contoh Aplikasi Persamaan Gas Ideal:</h4>
        <ul>
            <li>Menghitung volume gas yang dihasilkan dalam reaksi kimia</li>
            <li>Memahami perilaku gas dalam sistem tertutup</li>
            <li>Memprediksi pengaruh perubahan suhu terhadap tekanan gas</li>
            <li>Mendesain sistem pneumatik dan hidrolik</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips Penggunaan
    st.markdown("""
    <div class="card gas-card" style="margin-top:20px;">
        <h4>🔧 Tips Menggunakan Aplikasi:</h4>
        <ol>
            <li>Pilih menu <b>Kalkulator Gas</b> untuk perhitungan</li>
            <li>Gunakan <b>Ensiklopedia Gas</b> untuk informasi detail</li>
            <li>Pelajari <b>Panduan Keselamatan</b> sebelum bekerja dengan gas</li>
            <li>Pastikan satuan yang digunakan konsisten</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS 
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    # Header dengan animasi partikel
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0d47a1, #2196F3);
                 padding: 25px;
                 border-radius: 15px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;">
        <h1 style="color: white; text-align: center; margin: 0; z-index: 2; position: relative;">
             🧪✨ Kalkulator Gas Ideal ✨⚗️
        </h1>
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
            <div class="tab-container" style="border-left: 5px solid #FF9800;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪</div>
                    <div>
                        <h2 style="margin: 0; color: #FF9800;">Kalkulator Massa Gas</h2>
                        <div style="background: #FFF3E0; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> Massa = n (mol) × Mr (g/mol)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            cols = st.columns(3)
            with cols[0]:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_massa", placeholder="Contoh: Oksigen", label_visibility="collapsed")

            with cols[1]:
                st.markdown('<div class="input-label">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_massa", step=0.1, format="%.2f", label_visibility="collapsed")

            with cols[2]:
                st.markdown('<div class="input-label">Massa Molar (Mr)</div>', unsafe_allow_html=True)
                mr = st.number_input("Massa Molar (Mr)", min_value=0.0, key="mr_massa", step=0.01, format="%.2f", label_visibility="collapsed")
            
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("⚖️ Hitung Massa", key="btn_massa", use_container_width=True, type="primary"):
                massa = n * mr
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #FF9800;
                            animation: fadeIn 0.5s ease-in-out;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">⚖️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #E65100;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Massa <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #E65100; font-weight: bold; font-size: 1.5em; margin: 0;">{massa:.4f} gram</p>
                            </div>
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
            <div class="tab-container" style="border-left: 5px solid #F44336;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🎚️</div>
                    <div>
                        <h2 style="margin: 0; color: #F44336;">Kalkulator Tekanan Gas</h2>
                        <div style="background: #FFEBEE; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> P = [n (mol) × R × T (K)] / V (L)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_tekanan", placeholder="Contoh: Nitrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_tekanan", step=0.1, format="%.2f", label_visibility="collapsed")
                
            with col2:
                st.markdown('<div class="input-label">Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="tekanan_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="tekanan_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Volume</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    V_input = st.number_input("Volume", min_value=0.0, key="tekanan_vol_input", label_visibility="collapsed")
                with col2d:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="tekanan_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🎚️ Hitung Tekanan", key="btn_tekanan", use_container_width=True, type="primary"):
                P = (n * R * T) / V
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #FFEBEE, #FFCDD2);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #F44336;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🎚️</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #C62828;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Tekanan <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #C62828; font-weight: bold; font-size: 1.5em; margin: 0;">{P:.2f} atm</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab3:
        # Kalkulator Volume
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #4CAF50;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🫙</div>
                    <div>
                        <h2 style="margin: 0; color: #4CAF50;">Kalkulator Volume Gas</h2>
                        <div style="background: #E8F5E9; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> V = [n (mol) × R × T (K)] / P (atm)
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_volume", placeholder="Contoh: Hidrogen", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Jumlah Mol (n)</div>', unsafe_allow_html=True)
                n = st.number_input("Jumlah Mol (n)", min_value=0.0, key="n_volume", step=0.1, format="%.2f", label_visibility="collapsed")
                
            with col2:
                st.markdown('<div class="input-label">Suhu</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="volume_suhu_input", label_visibility="collapsed")
                with col2b:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="volume_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Tekanan</div>', unsafe_allow_html=True)
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
                
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🫙 Hitung Volume", key="btn_volume", use_container_width=True, type="primary"):
                V = (n * R * T) / P
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #4CAF50;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">📦</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #2E7D32;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Volume <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #2E7D32; font-weight: bold; font-size: 1.5em; margin: 0;">{V:.2f} L</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    with tab4:
        # Kalkulator Mol
        with st.container():
            st.markdown("""
            <div class="tab-container" style="border-left: 5px solid #9C27B0;">
                <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                    <div style="font-size: 40px;">🧪 </div>
                    <div>
                        <h2 style="margin: 0; color: #9C27B0;">Kalkulator Jumlah Mol</h2>
                        <div style="background: #F3E5F5; padding: 8px 12px; border-radius: 8px; display: inline-block;">
                            <b>Rumus:</b> n = [P (atm) × V (L) / (R × T (K)]
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="input-label">Nama Gas</div>', unsafe_allow_html=True)
                nama = st.text_input("Nama Gas", key="nama_mol", placeholder="Contoh: Karbon Dioksida", label_visibility="collapsed")
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Tekanan</div>', unsafe_allow_html=True)
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
                        🔄 Konversi: {P_input} {satuan_tekanan} = {P:.2f} atm
                    </div>
                    """, unsafe_allow_html=True)
                
            with col2:
                st.markdown('<div class="input-label">Volume</div>', unsafe_allow_html=True)
                col2a, col2b = st.columns([3,1])
                with col2a:
                    V_input = st.number_input("Volume", min_value=0.0, key="mol_vol_input", label_visibility="collapsed")
                with col2b:
                    satuan_vol = st.selectbox("Satuan Volume", ["L", "m³", "mL"], key="mol_vol_unit", label_visibility="collapsed")
                
                if satuan_vol == "m³":
                    V = V_input * 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} m³ = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                elif satuan_vol == "mL":
                    V = V_input / 1000
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {V_input} mL = {V:.4f} L
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    V = V_input
                
                st.markdown('<div class="input-label" style="margin-top: 15px;">Suhu</div>', unsafe_allow_html=True)
                col2c, col2d = st.columns([3,1])
                with col2c:
                    T_input = st.number_input("Suhu", min_value=-273.0, key="mol_suhu_input", label_visibility="collapsed")
                with col2d:
                    satuan = st.selectbox("Satuan Suhu", ["K", "°C"], key="mol_suhu_unit", label_visibility="collapsed")
                
                if satuan == "°C":
                    T = T_input + 273.15
                    st.markdown(f"""
                    <div class="conversion-box">
                        🔄 Konversi: {T_input}°C = {T:.2f} K
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    T = T_input
                
            st.markdown("</div>", unsafe_allow_html=True)

            if st.button("🧪 Hitung Mol", key="btn_mol", use_container_width=True, type="primary"):
                n = (P * V) / (R * T)
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #F3E5F5, #E1BEE7);
                            padding: 20px;
                            border-radius: 15px;
                            margin-top: 20px;
                            border-left: 5px solid #9C27B0;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <div style="font-size: 30px;">🔬</div>
                        <div>
                            <h3 style="margin: 0 0 10px 0; color: #7B1FA2;">Hasil Perhitungan</h3>
                            <div style="display: flex; align-items: baseline; gap: 10px;">
                                <p style="margin: 0; font-size: 1.2em;">Jumlah mol <b>{nama if nama else 'gas'}</b> =</p>
                                <p style="color: #7B1FA2; font-weight: bold; font-size: 1.5em; margin: 0;">{n:.2f} mol</p>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # Catatan edukasi di bagian bawah
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
                padding: 20px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 5px solid #2196F3;">
        <div style="display: flex; align-items: center; gap: 15px;">
            <div style="font-size: 30px;">💡</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #0D47A1;">Tips Ahli Kimia</h3>
                <p style="margin: 0;">
                    Untuk hasil terbaik, pastikan semua satuan konsisten dengan konstanta gas R 
                    (0.0821 L·atm/mol·K). Gunakan suhu dalam Kelvin dan tekanan dalam atm.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    st.markdown("<h1 class='main-header'>📚 Ensiklopedia Gas</h1>", unsafe_allow_html=True)
    
    selected_gas = st.selectbox(
        "Pilih Gas", 
        list(GAS_DATABASE.keys()),
        format_func=lambda x: f"{GAS_DATABASE[x]['icon']} {x}"
    )
    
    gas = GAS_DATABASE[selected_gas]
    
    # Header Gas
    col1, col2 = st.columns([3,1])
    with col1:
        st.markdown(f"""
        <h2>{gas['icon']} {selected_gas}</h2>
        <p><i>{gas['description']}</i></p>
        <p><b>Kategori:</b> {gas['category']}</p>
        <p><b>Aplikasi:</b> {gas['aplikasi']}</p>
        """, unsafe_allow_html=True)
    with col2:
        st.image(gas["image"], width=200)
    
    # Tab Informasi
    tabs = st.tabs(list(gas["properties"].keys()))
    
    for tab, (category, props) in zip(tabs, gas["properties"].items()):
        with tab:
            st.markdown(f"""
            <table class="property-table">
                {"".join(f"<tr><td><b>{key}</b></td><td>{value}</td></tr>" for key, value in props.items())}
            </table>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    st.markdown("<h1 class='main-header'>⚠️ Panduan Keselamatan Gas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🚧 Simbol Bahaya Umum</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:200px;background:#ffebee;padding:15px;border-radius:10px;">
                <h4>🔥 Mudah Terbakar</h4>
                <p>Contoh: Hidrogen, Metana</p>
                <p>• Jauhkan dari sumber api</p>
                <p>• Gunakan di area berventilasi</p>
            </div>
            <div style="flex:1;min-width:200px;background:#fff8e1;padding:15px;border-radius:10px;">
                <h4>☠️ Beracun</h4>
                <p>Contoh: Klorin, Amonia</p>
                <p>• Gunakan alat pelindung diri</p>
                <p>• Hindari inhalasi langsung</p>
            </div>
            <div style="flex:1;min-width:200px;background:#e8f5e9;padding:15px;border-radius:10px;">
                <h4>💨 Pengoksidasi</h4>
                <p>Contoh: Oksigen, Fluorin</p>
                <p>• Hindari kontak dengan bahan organik</p>
                <p>• Simpan terpisah dari bahan reduktor</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card safety-card">
        <h3>🛡️ Alat Pelindung Diri (APD)</h3>
        <div style="display:flex;flex-wrap:wrap;gap:15px;margin-top:15px;">
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2090/2090004.png" width="80">
                <p><b>Masker Gas</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/2797/2797688.png" width="80">
                <p><b>Sarung Tangan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/10984/10984307.png" width="80">
                <p><b>Kaca Mata Keselamatan</b></p>
            </div>
            <div style="flex:1;min-width:150px;text-align:center;">
                <img src="https://cdn-icons-png.flaticon.com/512/3000/3000504.png" width="80">
                <p><b>Jas Laboratorium</b></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card safety-card">
        <h3>🚨 Prosedur Darurat</h3>
        <ol>
            <li>Segera evakuasi area jika terjadi kebocoran gas</li>
            <li>Gunakan APD yang sesuai sebelum menangani gas</li>
            <li>Hindari sumber api atau percikan listrik</li>
            <li>Ventilasi area dengan membuka jendela atau pintu</li>
            <li>Hubungi petugas berwenang jika diperlukan</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#666;padding:20px;">
    <p>© 2025 ChemGasMaster | Kelompok 7 Kelas 1A</p>
</div>
""", unsafe_allow_html=True)
