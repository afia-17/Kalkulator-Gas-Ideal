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
        "icon": "🎈",
        "category": "Gas Monoatomik",
        "description": "Gas tidak berwarna dan tidak berbau, sangat ringan. Tidak mudah terbakar dan digunakan secara luas dalam balon, pendinginan MRI, serta sebagai atmosfer inert untuk pengelasan.",
        "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-545286316-433fb3d67bad4c7ebb4002f93bd67232.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "He",
                "Massa Molar": "4.003 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-272.2 °C (0.95 K)",
                "Titik Didih": "-268.928 °C (4.222 K)",
                "Densitas (STP)": "0.1786 g/L",
                "Kalor Jenis": "5.193 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Dapat menyebabkan asfiksia dalam ruang tertutup",
                "Penanganan": "Gunakan di area berventilasi, hindari inhalasi berlebihan"
            }
        },
        "aplikasi": "Balon, pendingin MRI, atmosfer inert untuk pengelasan"
    },
    "Argon (Ar)": {
        "icon": "⚡",
        "category": "Gas Monoatomik",
        "description": "Gas mulia yang sangat stabil dan inert, digunakan dalam pengelasan dan sebagai atmosfer pelindung.",
        "image": "https://images.unsplash.com/photo-1628595351029-c2bf17511435?ixlib=rb-4.0.3",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ar",
                "Massa Molar": "39.948 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-189.34 °C (83.81 K)",
                "Titik Didih": "-185.848 °C (87.302 K)",
                "Densitas (STP)": "1.784 g/L",
                "Kalor Jenis": "0.520 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam konsentrasi tinggi",
                "Penanganan": "Gunakan ventilasi yang memadai"
            }
        },
        "aplikasi": "Pengelasan, lampu pijar, atmosfer inert"
    },
    "Metana (CH₄)": {
        "icon": "🔥",
        "category": "Gas Hidrokarbon",
        "description": "Komponen utama gas alam, bahan bakar fosil yang penting.",
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?ixlib=rb-4.0.3",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CH₄",
                "Massa Molar": "16.04 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Tetrahedral"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-182.5 °C (90.65 K)",
                "Titik Didih": "-161.5 °C (111.65 K)",
                "Densitas (STP)": "0.717 g/L",
                "Kalor Jenis": "2.20 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (5-15% di udara)",
                "Penanganan": "Hindari sumber api, gunakan detektor gas"
            }
        },
        "aplikasi": "Bahan bakar, produksi hidrogen, bahan kimia"
    }
}

# ===========================================
# FUNGSI KALKULATOR GAS IDEAL
# ===========================================

def hitung_massa_molar(n, m):
    """Menghitung massa molar dari mol dan massa"""
    return m / n if n != 0 else 0

def hitung_tekanan(n, R, T, V):
    """Menghitung tekanan menggunakan PV = nRT"""
    return (n * R * T) / V if V != 0 else 0

def hitung_volume(n, R, T, P):
    """Menghitung volume menggunakan PV = nRT"""
    return (n * R * T) / P if P != 0 else 0

def hitung_mol(P, V, R, T):
    """Menghitung jumlah mol menggunakan PV = nRT"""
    return (P * V) / (R * T) if (R * T) != 0 else 0

def hitung_massa(n, Mr):
    """Menghitung massa dari mol dan massa molar"""
    return n * Mr

# ===========================================
# SIDEBAR NAVIGATION
# ===========================================
st.sidebar.title("⚗️ MENU NAVIGASI")
menu = st.sidebar.selectbox(
    "Pilih Menu:",
    ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
)

# ===========================================
# HALAMAN BERANDA
# ===========================================
if menu == "🏠 Beranda":
    # Set background untuk beranda
    st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-header"><h1>🧪 SELAMAT DATANG DI CHEMGASMASTER</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
        <h2>🎯 Tentang ChemGasMaster</h2>
        <p style="font-size: 18px; line-height: 1.8;">
        ChemGasMaster adalah aplikasi komprehensif untuk mempelajari sifat-sifat gas ideal dan melakukan perhitungan terkait hukum gas. 
        Aplikasi ini dilengkapi dengan:</p>
        
        <ul style="font-size: 16px; line-height: 1.6;">
        <li>🧮 <strong>Kalkulator Gas Ideal</strong> - Perhitungan PV = nRT</li>
        <li>📚 <strong>Ensiklopedia Gas</strong> - Database lengkap berbagai jenis gas</li>
        <li>⚠️ <strong>Panduan Keselamatan</strong> - Informasi keselamatan laboratorium</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <h2>⚛️ Hukum Gas Ideal</h2>
        <div style="text-align: center; font-size: 28px; color: #1976d2; font-weight: bold; margin: 20px 0;">
        PV = nRT
        </div>
        
        <div class="conversion-box">
        <strong>Keterangan:</strong><br>
        <strong>P</strong> = Tekanan (atm, Pa, mmHg)<br>
        <strong>V</strong> = Volume (L, mL, m³)<br>
        <strong>n</strong> = Jumlah mol (mol)<br>
        <strong>R</strong> = Konstanta gas ideal<br>
        <strong>T</strong> = Suhu (K, °C)
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <h3>🎯 Konstanta Gas Ideal (R)</h3>
        <div class="conversion-box">
        <strong>R = 0.08206 L·atm/(mol·K)</strong><br>
        <strong>R = 8.314 J/(mol·K)</strong><br>
        <strong>R = 62.36 L·mmHg/(mol·K)</strong>
        </div>
        
        <h3>🌡️ Konversi Suhu</h3>
        <div class="conversion-box">
        <strong>K = °C + 273.15</strong><br>
        <strong>°C = K - 273.15</strong>
        </div>
        
        <h3>📏 Konversi Tekanan</h3>
        <div class="conversion-box">
        <strong>1 atm = 760 mmHg</strong><br>
        <strong>1 atm = 101,325 Pa</strong><br>
        <strong>1 atm = 1.01325 bar</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    # Set background untuk kalkulator
    st.markdown('<div class="kalkulator-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-header"><h1>🧮 KALKULATOR GAS IDEAL</h1></div>', unsafe_allow_html=True)
    
    # Tab untuk berbagai perhitungan
    tab1, tab2, tab3, tab4 = st.tabs(["⚖️ Hitung Massa", "📊 Hitung Tekanan", "📏 Hitung Volume", "🧪 Hitung Mol"])
    
    with tab1:
        st.markdown("""
        <div class="tab-container calc-card">
        <h3>⚖️ Menghitung Massa Gas</h3>
        <p>Gunakan rumus: <strong>m = n × Mr</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            n_massa = st.number_input("🧪 Jumlah mol (n)", value=1.0, step=0.1, format="%.3f")
            Mr = st.number_input("⚛️ Massa molar (Mr) g/mol", value=32.0, step=0.1, format="%.3f")
        
        with col2:
            if st.button("🧮 Hitung Massa", type="primary"):
                massa = hitung_massa(n_massa, Mr)
                st.markdown(f"""
                <div class="result-card">
                <h4>📊 Hasil Perhitungan:</h4>
                <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">
                Massa = {massa:.3f} gram
                </div>
                <p><strong>Rumus:</strong> m = n × Mr = {n_massa} × {Mr} = {massa:.3f} g</p>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="tab-container calc-card">
        <h3>📊 Menghitung Tekanan Gas</h3>
        <p>Gunakan rumus: <strong>P = nRT/V</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            n_tekanan = st.number_input("🧪 Jumlah mol (n)", value=1.0, step=0.1, format="%.3f", key="n_p")
            R_tekanan = st.selectbox("⚗️ Konstanta R", 
                                   options=[0.08206, 8.314, 62.36],
                                   format_func=lambda x: f"{x} {'L·atm/(mol·K)' if x==0.08206 else 'J/(mol·K)' if x==8.314 else 'L·mmHg/(mol·K)'}")
        
        with col2:
            T_tekanan = st.number_input("🌡️ Suhu (K)", value=273.15, step=1.0, format="%.2f", key="T_p")
            V_tekanan = st.number_input("📏 Volume (L)", value=22.4, step=0.1, format="%.3f", key="V_p")
        
        if st.button("🧮 Hitung Tekanan", type="primary"):
            tekanan = hitung_tekanan(n_tekanan, R_tekanan, T_tekanan, V_tekanan)
            unit = "atm" if R_tekanan == 0.08206 else "Pa" if R_tekanan == 8.314 else "mmHg"
            st.markdown(f"""
            <div class="result-card">
            <h4>📊 Hasil Perhitungan:</h4>
            <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">
            Tekanan = {tekanan:.3f} {unit}
            </div>
            <p><strong>Rumus:</strong> P = nRT/V = ({n_tekanan} × {R_tekanan} × {T_tekanan})/{V_tekanan} = {tekanan:.3f} {unit}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="tab-container calc-card">
        <h3>📏 Menghitung Volume Gas</h3>
        <p>Gunakan rumus: <strong>V = nRT/P</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            n_volume = st.number_input("🧪 Jumlah mol (n)", value=1.0, step=0.1, format="%.3f", key="n_v")
            R_volume = st.selectbox("⚗️ Konstanta R", 
                                  options=[0.08206, 8.314, 62.36],
                                  format_func=lambda x: f"{x} {'L·atm/(mol·K)' if x==0.08206 else 'J/(mol·K)' if x==8.314 else 'L·mmHg/(mol·K)'}",
                                  key="R_v")
        
        with col2:
            T_volume = st.number_input("🌡️ Suhu (K)", value=273.15, step=1.0, format="%.2f", key="T_v")
            P_volume = st.number_input("📊 Tekanan", value=1.0, step=0.1, format="%.3f", key="P_v")
        
        if st.button("🧮 Hitung Volume", type="primary"):
            volume = hitung_volume(n_volume, R_volume, T_volume, P_volume)
            unit = "atm" if R_volume == 0.08206 else "Pa" if R_volume == 8.314 else "mmHg"
            st.markdown(f"""
            <div class="result-card">
            <h4>📊 Hasil Perhitungan:</h4>
            <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">
            Volume = {volume:.3f} L
            </div>
            <p><strong>Rumus:</strong> V = nRT/P = ({n_volume} × {R_volume} × {T_volume})/{P_volume} = {volume:.3f} L</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("""
        <div class="tab-container calc-card">
        <h3>🧪 Menghitung Jumlah Mol</h3>
        <p>Gunakan rumus: <strong>n = PV/RT</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            P_mol = st.number_input("📊 Tekanan", value=1.0, step=0.1, format="%.3f", key="P_n")
            V_mol = st.number_input("📏 Volume (L)", value=22.4, step=0.1, format="%.3f", key="V_n")
        
        with col2:
            R_mol = st.selectbox("⚗️ Konstanta R", 
                               options=[0.08206, 8.314, 62.36],
                               format_func=lambda x: f"{x} {'L·atm/(mol·K)' if x==0.08206 else 'J/(mol·K)' if x==8.314 else 'L·mmHg/(mol·K)'}",
                               key="R_n")
            T_mol = st.number_input("🌡️ Suhu (K)", value=273.15, step=1.0, format="%.2f", key="T_n")
        
        if st.button("🧮 Hitung Mol", type="primary"):
            mol = hitung_mol(P_mol, V_mol, R_mol, T_mol)
            unit = "atm" if R_mol == 0.08206 else "Pa" if R_mol == 8.314 else "mmHg"
            st.markdown(f"""
            <div class="result-card">
            <h4>📊 Hasil Perhitungan:</h4>
            <div style="font-size: 24px; font-weight: bold; color: #2e7d32;">
            Jumlah mol = {mol:.3f} mol
            </div>
            <p><strong>Rumus:</strong> n = PV/RT = ({P_mol} × {V_mol})/({R_mol} × {T_mol}) = {mol:.3f} mol</p>
            </div>
            """, unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    # Set background untuk ensiklopedia
    st.markdown('<div class="ensiklopedia-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-header"><h1>📚 ENSIKLOPEDIA GAS</h1></div>', unsafe_allow_html=True)
    
    # Pilihan gas
    gas_pilihan = st.selectbox(
        "🔍 Pilih Gas untuk Dipelajari:",
        list(GAS_DATABASE.keys())
    )
    
    if gas_pilihan:
        gas_data = GAS_DATABASE[gas_pilihan]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class="gas-card">
            <h2>{gas_data['icon']} {gas_pilihan}</h2>
            <p style="font-size: 18px; line-height: 1.6;">
            <strong>Kategori:</strong> {gas_data['category']}<br>
            <strong>Deskripsi:</strong> {gas_data['description']}
            </p>
            
            <h3>🎯 Aplikasi Utama:</h3>
            <div class="conversion-box">
            {gas_data['aplikasi']}
            </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="gas-card">
            <h3>🖼️ Visualisasi Molekul</h3>
            <div style="text-align: center; font-size: 80px; margin: 20px 0;">
            """ + gas_data['icon'] + """
            </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tabel properti
        for kategori, properties in gas_data['properties'].items():
            st.markdown(f"""
            <div class="gas-card">
            <h3>{kategori}</h3>
            <table class="property-table">
            """, unsafe_allow_html=True)
            
            for prop, nilai in properties.items():
                st.markdown(f"""
                <tr>
                <th style="width: 40%;">{prop}</th>
                <td>{nilai}</td>
                </tr>
                """, unsafe_allow_html=True)
            
            st.markdown("</table></div>", unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    # Set background untuk keselamatan
    st.markdown('<div class="keselamatan-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-header"><h1>⚠️ PANDUAN KESELAMATAN LABORATORIUM</h1></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🚨 Simbol Bahaya", "🛡️ Alat Pelindung", "🚨 Prosedur Darurat"])
    
    with tab1:
        st.markdown("""
        <div class="tab-container safety-card">
        <h3>🚨 Simbol-Simbol Bahaya Kimia</h3>
        </div>
        """, unsafe_allow_html=True)
        
        simbol_bahaya = {
            "💥 Eksplosif": "Dapat meledak dengan panas, gesekan, atau benturan",
            "🔥 Mudah Terbakar": "Dapat terbakar dengan mudah di udara",
            "⚡ Pengoksidasi": "Dapat menyebabkan atau memperparah kebakaran",
            "🧪 Korosif": "Dapat menyebabkan luka bakar pada kulit dan mata",
            "☠️ Beracun": "Dapat menyebabkan keracunan serius atau kematian",
            "⚠️ Berbahaya": "Dapat menyebabkan iritasi atau kerusakan ringan",
            "🌊 Berbahaya bagi Lingkungan": "Dapat mencemari lingkungan",
            "⚗️ Gas Bertekanan": "Dapat meledak jika dipanaskan"
        }
        
        for simbol, penjelasan in simbol_bahaya.items():
            st.markdown(f"""
            <div class="safety-card">
            <h4>{simbol}</h4>
            <p>{penjelasan}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="tab-container safety-card">
        <h3>🛡️ Alat Pelindung Diri (APD)</h3>
        </div>
        """, unsafe_allow_html=True)
        
        apd = {
            "🥽 Kacamata Keselamatan": "Melindungi mata dari percikan bahan kimia",
            "🧤 Sarung Tangan": "Melindungi tangan dari kontak langsung dengan bahan kimia",
            "🥼 Jas Laboratorium": "Melindungi pakaian dan kulit dari tumpahan",
            "👞 Sepatu Tertutup": "Melindungi kaki dari tumpahan dan pecahan",
            "😷 Masker/Respirator": "Melindungi sistem pernapasan dari uap berbahaya",
            "🚿 Eye Wash": "Untuk membilas mata jika terkena bahan kimia",
            "🚿 Safety Shower": "Untuk membilas tubuh jika terkena bahan kimia"
        }
        
        for alat, fungsi in apd.items():
            st.markdown(f"""
            <div class="safety-card">
            <h4>{alat}</h4>
            <p>{fungsi}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="tab-container safety-card">
        <h3>🚨 Prosedur Keadaan Darurat</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="safety-card">
        <h4>🔥 Kebakaran</h4>
        <ol>
        <li>Aktifkan alarm kebakaran</li>
        <li>Evakuasi area dengan tenang</li>
        <li>Gunakan alat pemadam yang sesuai</li>
        <li>Jangan gunakan air untuk kebakaran listrik atau minyak</li>
        </ol>
        </div>
        
        <div class="safety-card">
        <h4>☠️ Keracunan</h4>
        <ol>
        <li>Pindahkan korban dari sumber bahaya</li>
        <li>Berikan pertolongan pertama sesuai MSDS</li>
        <li>Hubungi petugas medis segera</li>
        <li>Bawa kemasan bahan kimia untuk referensi</li>
        </ol>
        </div>
        
        <div class="safety-card">
        <h4>🧪 Tumpahan Bahan Kimia</h4>
        <ol>
        <li>Isolasi area tumpahan</li>
        <li>Gunakan APD yang sesuai</li>
        <li>Bersihkan dengan prosedur yang benar</li>
        <li>Ventilasi area jika diperlukan</li>
        </ol>
        </div>
        
        <div class="safety-card">
        <h4>📞 Nomor Darurat</h4>
        <ul>
        <li><strong>Pemadam Kebakaran:</strong> 113</li>
        <li><strong>Ambulans:</strong> 118</li>
        <li><strong>Polisi:</strong> 110</li>
        <li><strong>Pusat Informasi Keracunan:</strong> (021) 4250767</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("""
<br><br>
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); backdrop-filter: blur(10px); border-radius: 15px; margin-top: 30px;">
<p style="color: #666; font-size: 14px;">
© 2024 ChemGasMaster | Aplikasi Pembelajaran Kimia Gas Ideal<br>
Dibuat dengan ❤️ menggunakan Streamlit
</p>
</div>
""", unsafe_allow_html=True)
