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
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "He",
                "Massa Molar": "4.003 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-272.2 °C (0.95 K)",
                "Titik Didih": "-268.93 °C (4.22 K)",
                "Densitas (STP)": "0.1786 g/L",
                "Kalor Jenis": "5.193 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam konsentrasi tinggi",
                "Penanganan": "Gunakan ventilasi baik, hindari inhalasi berlebihan"
            }
        },
        "aplikasi": "Balon, pendingin MRI, atmosfer inert"
    },
    "Argon (Ar)": {
        "icon": "⚛️",
        "category": "Gas Monoatomik",
        "description": "Gas mulia ketiga paling melimpah di atmosfer Bumi, sangat inert dan stabil.",
        "image": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=800",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ar",
                "Massa Molar": "39.948 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-189.3 °C (83.85 K)",
                "Titik Didih": "-185.85 °C (87.3 K)",
                "Densitas (STP)": "1.784 g/L",
                "Kalor Jenis": "0.520 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam ruang tertutup",
                "Penanganan": "Gunakan ventilasi memadai"
            }
        },
        "aplikasi": "Pengelasan, lampu pijar, penelitian laboratorium"
    },
    "Metana (CH₄)": {
        "icon": "🔥",
        "category": "Gas Organik",
        "description": "Gas alam utama, hidrokarbon paling sederhana dan bahan bakar penting.",
        "image": "https://images.unsplash.com/photo-1611273426858-450d8e3c9fce?w=800",
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
                "Kalor Jenis": "2.220 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (5-15% di udara)",
                "Penanganan": "Hindari percikan api dan sumber panas"
            }
        },
        "aplikasi": "Bahan bakar, produksi hidrogen, petrokimia"
    }
}

# ===========================================
# FUNGSI PERHITUNGAN GAS IDEAL
# ===========================================
def hitung_gas_ideal(diketahui, nilai_diketahui, dicari):
    """
    Menghitung besaran gas ideal menggunakan persamaan PV = nRT
    R = 0.08206 L·atm/(mol·K) atau 8.314 J/(mol·K)
    """
    R = 0.08206  # L·atm/(mol·K)
    
    hasil = {}
    
    # Konversi input ke unit standar jika diperlukan
    if "P" in diketahui and "atm" not in str(nilai_diketahui["P"]):
        # Konversi dari bar, Pa, dll ke atm jika diperlukan
        pass
    
    if dicari == "massa":
        # Hitung mol terlebih dahulu menggunakan PV = nRT
        # n = PV/RT
        P = nilai_diketahui["P"]
        V = nilai_diketahui["V"] 
        T = nilai_diketahui["T"] + 273.15  # Konversi ke Kelvin
        MM = nilai_diketahui["MM"]
        
        n = (P * V) / (R * T)
        massa = n * MM
        
        hasil["mol"] = round(n, 6)
        hasil["massa"] = round(massa, 4)
        hasil["rumus"] = "m = n × MM = (PV/RT) × MM"
        hasil["substitusi"] = f"m = ({P} × {V})/(0.08206 × {T:.2f}) × {MM}"
        
    elif dicari == "tekanan":
        # P = nRT/V atau P = (m/MM)RT/V
        if "massa" in diketahui:
            m = nilai_diketahui["massa"]
            MM = nilai_diketahui["MM"]
            n = m / MM
        else:
            n = nilai_diketahui["n"]
            
        V = nilai_diketahui["V"]
        T = nilai_diketahui["T"] + 273.15
        
        P = (n * R * T) / V
        
        hasil["tekanan"] = round(P, 4)
        hasil["rumus"] = "P = nRT/V"
        hasil["substitusi"] = f"P = ({n:.4f} × 0.08206 × {T:.2f})/{V}"
        
    elif dicari == "volume":
        # V = nRT/P
        if "massa" in diketahui:
            m = nilai_diketahui["massa"]
            MM = nilai_diketahui["MM"]
            n = m / MM
        else:
            n = nilai_diketahui["n"]
            
        P = nilai_diketahui["P"]
        T = nilai_diketahui["T"] + 273.15
        
        V = (n * R * T) / P
        
        hasil["volume"] = round(V, 4)
        hasil["rumus"] = "V = nRT/P"
        hasil["substitusi"] = f"V = ({n:.4f} × 0.08206 × {T:.2f})/{P}"
        
    elif dicari == "mol":
        # n = PV/RT
        P = nilai_diketahui["P"]
        V = nilai_diketahui["V"]
        T = nilai_diketahui["T"] + 273.15
        
        n = (P * V) / (R * T)
        
        hasil["mol"] = round(n, 6)
        hasil["rumus"] = "n = PV/RT"
        hasil["substitusi"] = f"n = ({P} × {V})/(0.08206 × {T:.2f})"
    
    return hasil

# ===========================================
# FUNGSI UTAMA APLIKASI
# ===========================================
def main():
    # Header Utama dengan Background Dinamis
    current_page = st.session_state.get('current_page', 'Beranda')
    
    # Set background sesuai halaman
    if current_page == 'Beranda':
        st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
    elif current_page == 'Kalkulator Gas':
        st.markdown('<div class="kalkulator-bg"></div>', unsafe_allow_html=True)
    elif current_page == 'Ensiklopedia Gas':
        st.markdown('<div class="ensiklopedia-bg"></div>', unsafe_allow_html=True)
    elif current_page == 'Panduan Keselamatan':
        st.markdown('<div class="keselamatan-bg"></div>', unsafe_allow_html=True)
    
    # Header utama
    st.markdown("""
    <div class="main-header">
        <h1 style="text-align: center; font-size: 3.5rem; margin: 0;">
            ⚗️ ChemGasMaster 🧪
        </h1>
        <h3 style="text-align: center; color: #666; margin-top: 15px; font-weight: 300;">
            🔬 Kalkulator Gas Ideal, Ensiklopedia & Panduan Keselamatan 🔬
        </h3>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar untuk navigasi
    st.sidebar.title("🧭 Menu Navigasi")
    st.sidebar.markdown("---")
    
    menu_options = {
        "🏠 Beranda": "Beranda",
        "🧮 Kalkulator Gas": "Kalkulator Gas", 
        "📚 Ensiklopedia Gas": "Ensiklopedia Gas",
        "⚠️ Panduan Keselamatan": "Panduan Keselamatan"
    }
    
    selected = st.sidebar.radio("Pilih Menu:", list(menu_options.keys()))
    current_page = menu_options[selected]
    st.session_state['current_page'] = current_page
    
    # =======================================
    # HALAMAN BERANDA
    # =======================================
    if current_page == "Beranda":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.markdown("## 🎯 Selamat Datang di ChemGasMaster!")
        
        st.markdown("""
        ### 🧪 Tentang Aplikasi
        
        **ChemGasMaster** adalah aplikasi komprehensif untuk:
        - 🧮 **Perhitungan Gas Ideal** menggunakan persamaan PV = nRT
        - 📚 **Ensiklopedia Gas** dengan database lengkap sifat-sifat gas
        - ⚠️ **Panduan Keselamatan** untuk penanganan gas berbahaya
        
        ### ⚛️ Persamaan Gas Ideal
        
        **PV = nRT**
        
        Dimana:
        - **P** = Tekanan (atm)
        - **V** = Volume (L) 
        - **n** = Jumlah mol (mol)
        - **R** = Konstanta gas ideal (0.08206 L·atm/mol·K)
        - **T** = Suhu (K)
        """)
        
        # Contoh perhitungan
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.markdown("### 📊 Contoh Perhitungan")
            st.markdown("""
            **Soal:** Berapa volume 2 mol gas pada 25°C dan 1 atm?
            
            **Penyelesaian:**
            - n = 2 mol
            - T = 25°C = 298.15 K  
            - P = 1 atm
            - R = 0.08206 L·atm/mol·K
            
            V = nRT/P = (2 × 0.08206 × 298.15)/1 = **48.9 L**
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.markdown("### 🔄 Konversi Suhu")
            st.markdown("""
            **Celsius ke Kelvin:**
            K = °C + 273.15
            
            **Kelvin ke Celsius:**  
            °C = K - 273.15
            
            **Contoh:**
            25°C = 25 + 273.15 = **298.15 K**
            """)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # =======================================
    # HALAMAN KALKULATOR GAS
    # =======================================
    elif current_page == "Kalkulator Gas":
        st.markdown("## 🧮 Kalkulator Gas Ideal")
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "🏋️ Hitung Massa", 
            "🎈 Hitung Tekanan",
            "📏 Hitung Volume", 
            "⚗️ Hitung Mol"
        ])
        
        with tab1:
            st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
            st.markdown("### 🏋️ Menghitung Massa Gas")
            
            col1, col2 = st.columns(2)
            with col1:
                P_massa = st.number_input("Tekanan (atm)", value=1.0, min_value=0.001, key="p_massa")
                V_massa = st.number_input("Volume (L)", value=22.4, min_value=0.001, key="v_massa")
            with col2:
                T_massa = st.number_input("Suhu (°C)", value=25.0, key="t_massa")
                MM_massa = st.number_input("Massa Molar (g/mol)", value=28.0, min_value=0.001, key="mm_massa")
            
            if st.button("🧮 Hitung Massa", key="btn_massa"):
                nilai_input = {
                    "P": P_massa,
                    "V": V_massa, 
                    "T": T_massa,
                    "MM": MM_massa
                }
                
                hasil = hitung_gas_ideal(["P", "V", "T", "MM"], nilai_input, "massa")
                
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown("### 🎯 Hasil Perhitungan")
                st.success(f"**Jumlah mol:** {hasil['mol']} mol")
                st.success(f"**Massa gas:** {hasil['massa']} gram")
                
                st.markdown("#### 📝 Langkah Perhitungan:")
                st.info(f"**Rumus:** {hasil['rumus']}")
                st.info(f"**Substitusi:** {hasil['substitusi']}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab2:
            st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
            st.markdown("### 🎈 Menghitung Tekanan Gas")
            
            col1, col2 = st.columns(2)
            with col1:
                massa_P = st.number_input("Massa (gram)", value=10.0, min_value=0.001, key="massa_p")
                MM_P = st.number_input("Massa Molar (g/mol)", value=28.0, min_value=0.001, key="mm_p")
            with col2:
                V_P = st.number_input("Volume (L)", value=5.0, min_value=0.001, key="v_p")
                T_P = st.number_input("Suhu (°C)", value=25.0, key="t_p")
            
            if st.button("🧮 Hitung Tekanan", key="btn_tekanan"):
                nilai_input = {
                    "massa": massa_P,
                    "MM": MM_P,
                    "V": V_P,
                    "T": T_P
                }
                
                hasil = hitung_gas_ideal(["massa", "MM", "V", "T"], nilai_input, "tekanan")
                
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown("### 🎯 Hasil Perhitungan")
                st.success(f"**Tekanan gas:** {hasil['tekanan']} atm")
                
                st.markdown("#### 📝 Langkah Perhitungan:")
                st.info(f"**Rumus:** {hasil['rumus']}")
                st.info(f"**Substitusi:** {hasil['substitusi']}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab3:
            st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
            st.markdown("### 📏 Menghitung Volume Gas")
            
            col1, col2 = st.columns(2)
            with col1:
                n_V = st.number_input("Jumlah mol", value=1.0, min_value=0.001, key="n_v")
                T_V = st.number_input("Suhu (°C)", value=25.0, key="t_v")
            with col2:
                P_V = st.number_input("Tekanan (atm)", value=1.0, min_value=0.001, key="p_v")
            
            if st.button("🧮 Hitung Volume", key="btn_volume"):
                nilai_input = {
                    "n": n_V,
                    "T": T_V,
                    "P": P_V
                }
                
                hasil = hitung_gas_ideal(["n", "T", "P"], nilai_input, "volume")
                
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown("### 🎯 Hasil Perhitungan")  
                st.success(f"**Volume gas:** {hasil['volume']} L")
                
                st.markdown("#### 📝 Langkah Perhitungan:")
                st.info(f"**Rumus:** {hasil['rumus']}")
                st.info(f"**Substitusi:** {hasil['substitusi']}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab4:
            st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
            st.markdown("### ⚗️ Menghitung Jumlah Mol")
            
            col1, col2 = st.columns(2)
            with col1:
                P_mol = st.number_input("Tekanan (atm)", value=1.0, min_value=0.001, key="p_mol")
                V_mol = st.number_input("Volume (L)", value=22.4, min_value=0.001, key="v_mol")
            with col2:
                T_mol = st.number_input("Suhu (°C)", value=0.0, key="t_mol")
            
            if st.button("🧮 Hitung Mol", key="btn_mol"):
                nilai_input = {
                    "P": P_mol,
                    "V": V_mol,
                    "T": T_mol
                }
                
                hasil = hitung_gas_ideal(["P", "V", "T"], nilai_input, "mol")
                
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown("### 🎯 Hasil Perhitungan")
                st.success(f"**Jumlah mol:** {hasil['mol']} mol")
                
                st.markdown("#### 📝 Langkah Perhitungan:")
                st.info(f"**Rumus:** {hasil['rumus']}")
                st.info(f"**Substitusi:** {hasil['substitusi']}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # =======================================
    # HALAMAN ENSIKLOPEDIA GAS
    # =======================================
    elif current_page == "Ensiklopedia Gas":
        st.markdown("## 📚 Ensiklopedia Gas")
        
        # Filter berdasarkan kategori
        categories = ["Semua"] + list(set([gas_data["category"] for gas_data in GAS_DATABASE.values()]))
        selected_category = st.selectbox("🔍 Filter berdasarkan kategori:", categories)
        
        # Filter gas berdasarkan kategori
        if selected_category == "Semua":
            filtered_gases = GAS_DATABASE
        else:
            filtered_gases = {name: data for name, data in GAS_DATABASE.items() 
                            if data["category"] == selected_category}
        
        # Tampilkan gas dalam grid
        gases_per_row = 2
        gas_names = list(filtered_gases.keys())
        
        for i in range(0, len(gas_names), gases_per_row):
            cols = st.columns(gases_per_row)
            
            for j, col in enumerate(cols):
                if i + j < len(gas_names):
                    gas_name = gas_names[i + j]
                    gas_info = filtered_gases[gas_name]
                    
                    with col:
                        st.markdown('<div class="gas-card">', unsafe_allow_html=True)
                        
                        # Header gas
                        st.markdown(f"""
                        ### {gas_info['icon']} {gas_name}
                        **Kategori:** {gas_info['category']}
                        """)
                        
                        # Deskripsi
                        st.markdown(f"**Deskripsi:** {gas_info['description']}")
                        
                        # Gambar (jika ada)
                        if gas_info.get('image'):
                            st.image(gas_info['image'], width=300)
                        
                        # Tampilkan properti dalam expander
                        with st.expander("🔬 Lihat Detail Properti"):
                            for category, props in gas_info['properties'].items():
                                st.markdown(f"#### {category}")
                                
                                # Buat tabel properti
                                st.markdown('<table class="property-table">', unsafe_allow_html=True)
                                st.markdown('<tr><th>Properti</th><th>Nilai</th></tr>', unsafe_allow_html=True)
                                
                                for prop, value in props.items():
                                    st.markdown(f'<tr><td><strong>{prop}</strong></td><td>{value}</td></tr>', 
                                              unsafe_allow_html=True)
                                
                                st.markdown('</table>', unsafe_allow_html=True)
                                st.markdown("---")
                        
                        # Aplikasi
                        st.markdown(f"**🏭 Aplikasi:** {gas_info['aplikasi']}")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
    
    # =======================================
    # HALAMAN PANDUAN KESELAMATAN
    # =======================================
    elif current_page == "Panduan Keselamatan":
        st.markdown("## ⚠️ Panduan Keselamatan Laboratorium")
        
        tab1, tab2, tab3 = st.tabs([
            "⚠️ Simbol Bahaya",
            "🛡️ Alat Pelindung", 
            "🚨 Prosedur Darurat"
        ])
        
        with tab1:
            st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
            st.markdown("### ⚠️ Simbol-Simbol Bahaya Kimia")
            
            hazard_symbols = {
                "💥": {
                    "nama": "Eksplosif",
                    "bahaya": "Dapat meledak dengan adanya panas, percikan, gesekan, atau benturan",
                    "contoh": "TNT, nitrogliserin, amonium nitrat",
                    "pencegahan": "Hindari panas, gesekan, benturan, dan percikan api"
                },
                "🔥": {
                    "nama": "Mudah Terbakar", 
                    "bahaya": "Dapat terbakar dengan mudah pada suhu kamar",
                    "contoh": "Alkohol, bensin, aseton",
                    "pencegahan": "Jauhkan dari sumber panas, percikan api, dan permukaan panas"
                },
                "🧪": {
                    "nama": "Korosif",
                    "bahaya": "Dapat menyebabkan luka bakar pada kulit dan kerusakan pada mata",
                    "contoh": "Asam sulfat, natrium hidroksida",
                    "pencegahan": "Gunakan sarung tangan dan pelindung mata"
                },
                "☠️": {
                    "nama": "Beracun",
                    "bahaya": "Dapat menyebabkan keracunan serius atau kematian",
                    "contoh": "Merkuri, sianida, pestisida",
                    "pencegahan": "Hindari kontak langsung dan inhalasi"
                },
                "⚡": {
                    "nama": "Pengoksidasi",
                    "bahaya": "Dapat menyebabkan atau memperparah kebakaran",
                    "contoh": "Hidrogen peroksida, kalium permanganat",
                    "pencegahan": "Jauhkan dari bahan organik dan reduktor"
                },
                "🌫️": {
                    "nama": "Gas Bertekanan",
                    "bahaya": "Dapat meledak jika terkena panas atau bocor",
                    "contoh": "Tabung oksigen, nitrogen, argon",
                    "pencegahan": "Simpan di tempat sejuk, periksa kebocoran"
                }
            }
            
            for symbol, info in hazard_symbols.items():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    st.markdown(f"<div style='font-size: 4rem; text-align: center;'>{symbol}</div>", 
                              unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    **{info['nama']}**
                    
                    **Bahaya:** {info['bahaya']}
                    
                    **Contoh:** {info['contoh']}
                    
                    **Pencegahan:** {info['pencegahan']}
                    """)
                
                st.markdown("---")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab2:
            st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
            st.markdown("### 🛡️ Alat Pelindung Diri (APD)")
            
            ppe_items = {
                "👓": {
                    "nama": "Pelindung Mata",
                    "fungsi": "Melindungi mata dari percikan bahan kimia dan partikel berbahaya",
                    "jenis": "Kacamata safety, goggle, face shield",
                    "penggunaan": "Wajib digunakan saat bekerja dengan bahan kimia"
                },
                "🧤": {
                    "nama": "Sarung Tangan",
                    "fungsi": "Melindungi tangan dari bahan kimia korosif dan beracun",
                    "jenis": "Latex, nitrile, PVC, neoprene",
                    "penggunaan": "Pilih material sesuai dengan jenis bahan kimia"
                },
                "👕": {
                    "nama": "Jas Laboratorium",
                    "fungsi": "Melindungi tubuh dan pakaian dari percikan bahan kimia",
                    "jenis": "Katun, polyester tahan api",
                    "penggunaan": "Selalu dikancing rapat, lengan panjang"
                },
                "👟": {
                    "nama": "Sepatu Safety",
                    "fungsi": "Melindungi kaki dari tumpahan dan benda jatuh",
                    "jenis": "Sepatu tertutup, anti slip",
                    "penggunaan": "Hindari sandal atau sepatu terbuka"
                },
                "😷": {
                    "nama": "Pelindung Pernapasan",
                    "fungsi": "Melindungi dari inhalasi gas dan uap berbahaya",
                    "jenis": "Masker debu, respirator, masker gas",
                    "penggunaan": "Sesuai dengan jenis kontaminan udara"
                }
            }
            
            for symbol, info in ppe_items.items():
                col1, col2 = st.columns([1, 4])
                
                with col1:
                    st.markdown(f"<div style='font-size: 3rem; text-align: center;'>{symbol}</div>", 
                              unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    **{info['nama']}**
                    
                    **Fungsi:** {info['fungsi']}
                    
                    **Jenis:** {info['jenis']}
                    
                    **Penggunaan:** {info['penggunaan']}
                    """)
                
                st.markdown("---")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with tab3:
            st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
            st.markdown("### 🚨 Prosedur Keadaan Darurat")
            
            emergency_procedures = {
                "🔥 Kebakaran": {
                    "langkah": [
                        "1. Tetap tenang dan jangan panik",
                        "2. Matikan sumber api dan listrik jika memungkinkan",
                        "3. Gunakan alat pemadam api yang sesuai",
                        "4. Evakuasi area jika api tidak terkendali", 
                        "5. Hubungi pemadam kebakaran"
                    ],
                    "alat": "APAR (CO₂, busa, dry powder)",
                    "pencegahan": "Periksa alat pemadam secara berkala"
                },
                "☠️ Keracunan Gas": {
                    "langkah": [
                        "1. Pindahkan korban ke udara segar",
                        "2. Longgarkan pakaian yang ketat",
                        "3. Berikan pernapasan buatan jika perlu",
                        "4. Hubungi medis segera",
                        "5. Jangan memberikan makanan atau minuman"
                    ],
                    "alat": "Masker oksigen, ventilasi darurat",
                    "pencegahan": "Gunakan sistem ventilasi yang baik"
                },
                "🧪 Tumpahan Kimia": {
                    "langkah": [
                        "1. Kenakan APD yang sesuai",
                        "2. Ventilasi area tumpahan", 
                        "3. Serap dengan bahan absorben",
                        "4. Netralkan jika diperlukan",
                        "5. Buang limbah sesuai prosedur"
                    ],
                    "alat": "Spill kit, bahan absorben, netralizer",
                    "pencegahan": "Simpan bahan kimia dengan benar"
                },
                "⚡ Kontak dengan Kulit": {
                    "langkah": [
                        "1. Segera bilas dengan air bersih 15-20 menit",
                        "2. Lepas pakaian yang terkontaminasi",
                        "3. Jangan gosok area yang terkena",
                        "4. Hubungi medis jika iritasi berlanjut",
                        "5. Dokumentasikan incident"
                    ],
                    "alat": "Emergency shower, air bersih",
                    "pencegahan": "Selalu gunakan sarung tangan"
                }
            }
            
            for emergency, info in emergency_procedures.items():
                st.markdown(f"#### {emergency}")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Langkah-Langkah:**")
                    for step in info['langkah']:
                        st.markdown(f"- {step}")
                
                with col2:
                    st.markdown(f"**Alat yang Dibutuhkan:** {info['alat']}")
                    st.markdown(f"**Pencegahan:** {info['pencegahan']}")
                
                st.markdown("---")
            
            # Nomor darurat
            st.markdown("### 📞 Nomor Darurat")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.error("🚒 **Pemadam Kebakaran**\n113")
            with col2:
                st.error("🚑 **Ambulans**\n118 / 119")  
            with col3:
                st.error("👮 **Polisi**\n110")
            
            st.markdown('</div>', unsafe_allow_html=True)

# ===========================================
# MENJALANKAN APLIKASI
# ===========================================
if __name__ == "__main__":
    main()
