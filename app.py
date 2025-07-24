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
        "description": "Gas tidak berwarna, dapat memancarkan warna oranye kemerahan jika berada pada medan listrik bertegangan tinggi.",
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
        "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()-d2f99b9e8c1c4f7da5e8c4b0829f8b7d.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "He",
                "Massa Molar": "4.003 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-272.20 °C (0.95 K)",
                "Titik Didih": "-268.93 °C (4.22 K)",
                "Densitas (STP)": "0.1785 g/L",
                "Kalor Jenis": "5.193 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam ruang tertutup, tekanan tinggi",
                "Penanganan": "Gunakan ventilasi memadai, simpan sesuai standar tabung gas"
            }
        },
        "aplikasi": "Balon cuaca, pendingin MRI, pengelasan, pengisi balon"
    },
    "Argon (Ar)": {
        "icon": "⚡",
        "category": "Gas Monoatomik",
        "description": "Gas mulia yang inert, menyusun 0.93% atmosfer Bumi. Digunakan dalam pengelasan dan lampu pijar.",
        "image": "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/argon-element-symbol-from-periodic-table-serge-averbukh.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ar",
                "Massa Molar": "39.948 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-189.35 °C (83.80 K)",
                "Titik Didih": "-185.85 °C (87.30 K)",
                "Densitas (STP)": "1.784 g/L",
                "Kalor Jenis": "0.520 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam konsentrasi tinggi",
                "Penanganan": "Pastikan ventilasi memadai saat digunakan"
            }
        },
        "aplikasi": "Pengelasan TIG, lampu pijar, produksi kristal silikon"
    },
    "Metana (CH₄)": {
        "icon": "🔥",
        "category": "Gas Organik",
        "description": "Hidrokarbon paling sederhana, komponen utama gas alam. Bahan bakar penting untuk energi.",
        "image": "https://chem.libretexts.org/@api/deki/files/71864/methane.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CH₄",
                "Massa Molar": "16.04 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau (dalam bentuk murni)",
                "Struktur": "Tetrahedral"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-182.5 °C (90.65 K)",
                "Titik Didih": "-161.6 °C (111.55 K)",
                "Densitas (STP)": "0.717 g/L",
                "Kalor Jenis": "2.220 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (5-15% di udara), gas rumah kaca",
                "Penanganan": "Hindari sumber api, gunakan sistem deteksi kebocoran"
            }
        },
        "aplikasi": "Bahan bakar rumah tangga, pembangkit listrik, bahan baku kimia"
    }
}

# ===========================================
# FUNGSI PERHITUNGAN GAS IDEAL
# ===========================================
def hitung_gas_ideal(tipe, **kwargs):
    """
    Menghitung berbagai parameter gas ideal
    PV = nRT dimana:
    P = tekanan (atm)
    V = volume (L)
    n = jumlah mol
    R = konstanta gas ideal (0.0821 L·atm/(mol·K))
    T = suhu (K)
    """
    R = 0.0821  # L·atm/(mol·K)
    
    if tipe == "massa":
        P = kwargs['tekanan']
        V = kwargs['volume']
        T = kwargs['suhu'] + 273.15  # Konversi ke Kelvin
        Mr = kwargs['massa_molekul']
        
        # PV = nRT → n = PV/RT
        n = (P * V) / (R * T)
        massa = n * Mr
        return massa, n
        
    elif tipe == "tekanan":
        n = kwargs['mol']
        V = kwargs['volume']
        T = kwargs['suhu'] + 273.15
        
        # PV = nRT → P = nRT/V
        P = (n * R * T) / V
        return P
        
    elif tipe == "volume":
        P = kwargs['tekanan']
        n = kwargs['mol']
        T = kwargs['suhu'] + 273.15
        
        # PV = nRT → V = nRT/P
        V = (n * R * T) / P
        return V
        
    elif tipe == "mol":
        P = kwargs['tekanan']
        V = kwargs['volume']
        T = kwargs['suhu'] + 273.15
        
        # PV = nRT → n = PV/RT
        n = (P * V) / (R * T)
        return n

def konversi_suhu(suhu, dari, ke):
    """Konversi suhu antara Celsius, Kelvin, dan Fahrenheit"""
    if dari == ke:
        return suhu
    
    # Konversi ke Celsius terlebih dahulu
    if dari == "K":
        celsius = suhu - 273.15
    elif dari == "F":
        celsius = (suhu - 32) * 5/9
    else:  # dari == "C"
        celsius = suhu
    
    # Konversi dari Celsius ke target
    if ke == "K":
        return celsius + 273.15
    elif ke == "F":
        return celsius * 9/5 + 32
    else:  # ke == "C"
        return celsius

def konversi_tekanan(tekanan, dari, ke):
    """Konversi tekanan antara atm, Pa, bar, torr, mmHg"""
    konversi_ke_atm = {
        "atm": 1,
        "Pa": 101325,
        "bar": 1.01325,
        "torr": 760,
        "mmHg": 760,
        "kPa": 101.325,
        "psi": 14.696
    }
    
    # Konversi ke atm
    atm = tekanan / konversi_ke_atm[dari]
    
    # Konversi dari atm ke target
    return atm * konversi_ke_atm[ke]

def konversi_volume(volume, dari, ke):
    """Konversi volume antara L, mL, m³, cm³"""
    konversi_ke_liter = {
        "L": 1,
        "mL": 0.001,
        "m³": 1000,
        "cm³": 0.001,
        "dm³": 1
    }
    
    # Konversi ke liter
    liter = volume * konversi_ke_liter[dari]
    
    # Konversi dari liter ke target
    return liter / konversi_ke_liter[ke]

# ===========================================
# FUNGSI UNTUK MENAMPILKAN BACKGROUND
# ===========================================
def set_background(menu):
    """Set background berdasarkan menu yang dipilih"""
    if menu == "Beranda":
        st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
    elif menu == "Kalkulator Gas":
        st.markdown('<div class="kalkulator-bg"></div>', unsafe_allow_html=True)
    elif menu == "Ensiklopedia Gas":
        st.markdown('<div class="ensiklopedia-bg"></div>', unsafe_allow_html=True)
    elif menu == "Panduan Keselamatan":
        st.markdown('<div class="keselamatan-bg"></div>', unsafe_allow_html=True)

# ===========================================
# SIDEBAR MENU
# ===========================================
st.sidebar.title("🧪 ChemGasMaster")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Beranda", "Kalkulator Gas", "Ensiklopedia Gas", "Panduan Keselamatan"]
)

# Set background berdasarkan menu
set_background(menu)

# ===========================================
# BERANDA
# ===========================================
if menu == "Beranda":
    st.markdown('<div class="main-header"><h1>🧪 ChemGasMaster</h1></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <h2>🌟 Selamat Datang di ChemGasMaster!</h2>
    <p style="font-size: 18px; line-height: 1.8;">
    ChemGasMaster adalah aplikasi komprehensif untuk mempelajari dan menghitung sifat-sifat gas ideal. 
    Aplikasi ini dilengkapi dengan kalkulator canggih, ensiklopedia gas lengkap, dan panduan keselamatan laboratorium.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card calc-card">
        <h3>⚗️ Persamaan Gas Ideal</h3>
        <div style="text-align: center; font-size: 28px; margin: 20px 0; color: #1565c0; font-weight: bold;">
        PV = nRT
        </div>
        <ul style="font-size: 16px; line-height: 2;">
        <li><strong>P</strong> = Tekanan (atm, Pa, bar)</li>
        <li><strong>V</strong> = Volume (L, mL, m³)</li>
        <li><strong>n</strong> = Jumlah mol (mol)</li>
        <li><strong>R</strong> = Konstanta gas ideal</li>
        <li><strong>T</strong> = Suhu mutlak (K)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card result-card">
        <h3>🔬 Konstanta Gas Ideal (R)</h3>
        <table style="width: 100%; font-size: 14px;">
        <tr><td><strong>0.0821</strong></td><td>L·atm/(mol·K)</td></tr>
        <tr><td><strong>8.314</strong></td><td>J/(mol·K)</td></tr>
        <tr><td><strong>0.08314</strong></td><td>L·bar/(mol·K)</td></tr>
        <tr><td><strong>62.36</strong></td><td>L·torr/(mol·K)</td></tr>
        </table>
        <p style="margin-top: 15px; font-style: italic; color: #2e7d32;">
        💡 Pilih konstanta yang sesuai dengan satuan yang Anda gunakan!
        </p>
        </div>
        """, unsafe_allow_html=True)

    # Fitur Aplikasi
    st.markdown("""
    <div class="card gas-card">
    <h3>🚀 Fitur Unggulan</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px;">
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.8); border-radius: 15px;">
            <div style="font-size: 40px;">🧮</div>
            <h4>Kalkulator Canggih</h4>
            <p>Hitung massa, tekanan, volume, dan mol dengan presisi tinggi</p>
        </div>
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.8); border-radius: 15px;">
            <div style="font-size: 40px;">📚</div>
            <h4>Ensiklopedia Lengkap</h4>
            <p>Database gas dengan sifat fisika dan kimia detail</p>
        </div>
        <div style="text-align: center; padding: 20px; background: rgba(255,255,255,0.8); border-radius: 15px;">
            <div style="font-size: 40px;">🛡️</div>
            <h4>Panduan Keselamatan</h4>
            <p>Informasi keselamatan laboratorium dan penanganan gas</p>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ===========================================
# KALKULATOR GAS
# ===========================================
elif menu == "Kalkulator Gas":
    st.markdown('<div class="main-header"><h1>🧮 Kalkulator Gas Ideal</h1></div>', unsafe_allow_html=True)
    
    # Tab untuk berbagai kalkulasi
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Hitung Massa", "🌡️ Hitung Tekanan", "📏 Hitung Volume", "⚛️ Hitung Mol"])
    
    with tab1:
        st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
        st.subheader("💫 Menghitung Massa Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tekanan = st.number_input("Tekanan (atm):", min_value=0.01, max_value=1000.0, value=1.0, step=0.01)
            volume = st.number_input("Volume (L):", min_value=0.001, max_value=10000.0, value=1.0, step=0.001)
            
        with col2:
            suhu = st.number_input("Suhu (°C):", min_value=-273.0, max_value=2000.0, value=25.0, step=0.1)
            massa_molekul = st.number_input("Massa Molekul (g/mol):", min_value=1.0, max_value=500.0, value=28.014, step=0.001)
        
        if st.button("🔬 Hitung Massa", key="massa"):
            massa, mol = hitung_gas_ideal("massa", tekanan=tekanan, volume=volume, suhu=suhu, massa_molekul=massa_molekul)
            
            st.markdown(f"""
            <div class="result-card">
            <h3>📊 Hasil Perhitungan</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div style="text-align: center; padding: 20px; background: rgba(76,175,80,0.1); border-radius: 10px;">
                    <h2 style="color: #2e7d32; margin: 0;">{massa:.4f} g</h2>
                    <p style="margin: 5px 0;">Massa Gas</p>
                </div>
                <div style="text-align: center; padding: 20px; background: rgba(33,150,243,0.1); border-radius: 10px;">
                    <h2 style="color: #1565c0; margin: 0;">{mol:.4f} mol</h2>
                    <p style="margin: 5px 0;">Jumlah Mol</p>
                </div>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Konversi satuan
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.write("🔄 **Konversi Satuan Massa:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"• **Gram:** {massa:.4f} g")
                st.write(f"• **Kilogram:** {massa/1000:.6f} kg")
            with col2:
                st.write(f"• **Miligram:** {massa*1000:.2f} mg")
                st.write(f"• **Pound:** {massa*0.00220462:.6f} lb")
            with col3:
                st.write(f"• **Ounce:** {massa*0.035274:.4f} oz")
                st.write(f"• **Ton:** {massa/1000000:.9f} ton")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
        st.subheader("🌡️ Menghitung Tekanan Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            mol_p = st.number_input("Jumlah Mol:", min_value=0.001, max_value=1000.0, value=1.0, step=0.001, key="mol_p")
            volume_p = st.number_input("Volume (L):", min_value=0.001, max_value=10000.0, value=1.0, step=0.001, key="vol_p")
            
        with col2:
            suhu_p = st.number_input("Suhu (°C):", min_value=-273.0, max_value=2000.0, value=25.0, step=0.1, key="temp_p")
        
        if st.button("🔬 Hitung Tekanan", key="tekanan"):
            tekanan_hasil = hitung_gas_ideal("tekanan", mol=mol_p, volume=volume_p, suhu=suhu_p)
            
            st.markdown(f"""
            <div class="result-card">
            <h3>📊 Hasil Perhitungan</h3>
            <div style="text-align: center; padding: 30px; background: rgba(255,152,0,0.1); border-radius: 15px;">
                <h1 style="color: #ef6c00; margin: 0; font-size: 48px;">{tekanan_hasil:.4f}</h1>
                <p style="font-size: 24px; margin: 5px 0;">atm</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Konversi satuan tekanan
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.write("🔄 **Konversi Satuan Tekanan:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"• **Atmosfer:** {tekanan_hasil:.4f} atm")
                st.write(f"• **Pascal:** {konversi_tekanan(tekanan_hasil, 'atm', 'Pa'):.2f} Pa")
            with col2:
                st.write(f"• **Bar:** {konversi_tekanan(tekanan_hasil, 'atm', 'bar'):.4f} bar")
                st.write(f"• **kPa:** {konversi_tekanan(tekanan_hasil, 'atm', 'kPa'):.4f} kPa")
            with col3:
                st.write(f"• **Torr:** {konversi_tekanan(tekanan_hasil, 'atm', 'torr'):.2f} torr")
                st.write(f"• **psi:** {konversi_tekanan(tekanan_hasil, 'atm', 'psi'):.4f} psi")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
        st.subheader("📏 Menghitung Volume Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tekanan_v = st.number_input("Tekanan (atm):", min_value=0.01, max_value=1000.0, value=1.0, step=0.01, key="tek_v")
            mol_v = st.number_input("Jumlah Mol:", min_value=0.001, max_value=1000.0, value=1.0, step=0.001, key="mol_v")
            
        with col2:
            suhu_v = st.number_input("Suhu (°C):", min_value=-273.0, max_value=2000.0, value=25.0, step=0.1, key="temp_v")
        
        if st.button("🔬 Hitung Volume", key="volume"):
            volume_hasil = hitung_gas_ideal("volume", tekanan=tekanan_v, mol=mol_v, suhu=suhu_v)
            
            st.markdown(f"""
            <div class="result-card">
            <h3>📊 Hasil Perhitungan</h3>
            <div style="text-align: center; padding: 30px; background: rgba(156,39,176,0.1); border-radius: 15px;">
                <h1 style="color: #7b1fa2; margin: 0; font-size: 48px;">{volume_hasil:.4f}</h1>
                <p style="font-size: 24px; margin: 5px 0;">Liter</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Konversi satuan volume
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.write("🔄 **Konversi Satuan Volume:**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"• **Liter:** {volume_hasil:.4f} L")
                st.write(f"• **Mililiter:** {konversi_volume(volume_hasil, 'L', 'mL'):.2f} mL")
            with col2:
                st.write(f"• **Meter Kubik:** {konversi_volume(volume_hasil, 'L', 'm³'):.6f} m³")
                st.write(f"• **cm³:** {konversi_volume(volume_hasil, 'L', 'cm³'):.2f} cm³")
            with col3:
                st.write(f"• **dm³:** {konversi_volume(volume_hasil, 'L', 'dm³'):.4f} dm³")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="tab-container calc-card">', unsafe_allow_html=True)
        st.subheader("⚛️ Menghitung Jumlah Mol")
        
        col1, col2 = st.columns(2)
        
        with col1:
            tekanan_n = st.number_input("Tekanan (atm):", min_value=0.01, max_value=1000.0, value=1.0, step=0.01, key="tek_n")
            volume_n = st.number_input("Volume (L):", min_value=0.001, max_value=10000.0, value=1.0, step=0.001, key="vol_n")
            
        with col2:
            suhu_n = st.number_input("Suhu (°C):", min_value=-273.0, max_value=2000.0, value=25.0, step=0.1, key="temp_n")
        
        if st.button("🔬 Hitung Mol", key="mol"):
            mol_hasil = hitung_gas_ideal("mol", tekanan=tekanan_n, volume=volume_n, suhu=suhu_n)
            
            st.markdown(f"""
            <div class="result-card">
            <h3>📊 Hasil Perhitungan</h3>
            <div style="text-align: center; padding: 30px; background: rgba(244,67,54,0.1); border-radius: 15px;">
                <h1 style="color: #c62828; margin: 0; font-size: 48px;">{mol_hasil:.4f}</h1>
                <p style="font-size: 24px; margin: 5px 0;">mol</p>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Informasi tambahan tentang mol
            st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
            st.write("🔄 **Informasi Mol:**")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"• **Jumlah Molekul:** {mol_hasil * 6.022e23:.2e}")
                st.write(f"• **Millimol:** {mol_hasil * 1000:.2f} mmol")
            with col2:
                st.write(f"• **Kilomol:** {mol_hasil / 1000:.6f} kmol")
                st.write(f"• **Volume STP:** {mol_hasil * 22.4:.4f} L")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ===========================================
# ENSIKLOPEDIA GAS
# ===========================================
elif menu == "Ensiklopedia Gas":
    st.markdown('<div class="main-header"><h1>📚 Ensiklopedia Gas</h1></div>', unsafe_allow_html=True)
    
    # Pilihan gas
    gas_names = list(GAS_DATABASE.keys())
    selected_gas = st.selectbox("🔍 Pilih Gas untuk Dipelajari:", gas_names)
    
    if selected_gas:
        gas_data = GAS_DATABASE[selected_gas]
        
        # Header gas
        st.markdown(f"""
        <div class="gas-card">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="font-size: 80px; margin-right: 20px;">{gas_data['icon']}</div>
            <div>
                <h1 style="margin: 0; color: #e65100;">{selected_gas}</h1>
                <h3 style="margin: 5px 0; color: #ff9800;">{gas_data['category']}</h3>
            </div>
        </div>
        <p style="font-size: 18px; line-height: 1.6; color: #5d4037;">
        {gas_data['description']}
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Gambar gas
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Tabel sifat-sifat
            for kategori, sifat in gas_data['properties'].items():
                st.markdown(f"""
                <div class="gas-card">
                <h3>{kategori}</h3>
                <table class="property-table">
                """, unsafe_allow_html=True)
                
                for prop, nilai in sifat.items():
                    st.markdown(f"""
                    <tr>
                        <td><strong>{prop}</strong></td>
                        <td>{nilai}</td>
                    </tr>
                    """, unsafe_allow_html=True)
                
                st.markdown("</table></div>", unsafe_allow_html=True)
        
        with col2:
            try:
                st.image(gas_data['image'], caption=f"Struktur {selected_gas}", use_column_width=True)
            except:
                st.markdown(f"""
                <div style="text-align: center; padding: 50px; background: rgba(0,0,0,0.1); border-radius: 15px;">
                    <div style="font-size: 100px;">{gas_data['icon']}</div>
                    <p>Struktur {selected_gas}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Aplikasi
        st.markdown(f"""
        <div class="result-card">
        <h3>🚀 Aplikasi dan Penggunaan</h3>
        <p style="font-size: 16px; line-height: 1.8;">
        {gas_data['aplikasi']}
        </p>
        </div>
        """, unsafe_allow_html=True)

# ===========================================
# PANDUAN KESELAMATAN
# ===========================================
elif menu == "Panduan Keselamatan":
    st.markdown('<div class="main-header"><h1>🛡️ Panduan Keselamatan Laboratorium</h1></div>', unsafe_allow_html=True)
    
    # Tab keselamatan
    tab1, tab2, tab3 = st.tabs(["⚠️ Simbol Bahaya", "🥽 Alat Pelindung", "🚨 Prosedur Darurat"])
    
    with tab1:
        st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
        st.subheader("⚠️ Simbol-Simbol Bahaya Kimia")
        
        bahaya_data = [
            {"simbol": "☠️", "nama": "Toksik", "bahaya": "Beracun jika terhirup, tertelan, atau kontak kulit", "tindakan": "Gunakan sarung tangan, masker, dan hindari kontak langsung"},
            {"simbol": "🔥", "nama": "Mudah Terbakar", "bahaya": "Dapat terbakar dengan mudah", "tindakan": "Jauhkan dari sumber api, panas, dan percikan api"},
            {"simbol": "💥", "nama": "Eksplosif", "bahaya": "Dapat meledak jika terkena panas atau benturan", "tindakan": "Hindari benturan, gesekan, dan sumber panas"},
            {"simbol": "⚡", "nama": "Pengoksidasi", "bahaya": "Dapat mempercepat pembakaran", "tindakan": "Hindari kontak dengan bahan organik dan reduktor"},
            {"simbol": "☢️", "nama": "Radioaktif", "bahaya": "Memancarkan radiasi berbahaya", "tindakan": "Gunakan peralatan khusus dan batasi waktu paparan"},
            {"simbol": "⚠️", "nama": "Korosif", "bahaya": "Dapat merusak kulit dan logam", "tindakan": "Gunakan APD lengkap dan ventilasi baik"}
        ]
        
        for item in bahaya_data:
            st.markdown(f"""
            <div style="display: flex; align-items: center; margin: 20px 0; padding: 20px; background: rgba(255,255,255,0.9); border-radius: 15px; border-left: 5px solid #f44336;">
                <div style="font-size: 60px; margin-right: 20px;">{item['simbol']}</div>
                <div style="flex: 1;">
                    <h4 style="color: #c62828; margin: 0;">{item['nama']}</h4>
                    <p style="margin: 5px 0; color: #d32f2f;"><strong>Bahaya:</strong> {item['bahaya']}</p>
                    <p style="margin: 5px 0; color: #388e3c;"><strong>Tindakan:</strong> {item['tindakan']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
        st.subheader("🥽 Alat Pelindung Diri (APD)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card">
            <h4>👁️ Pelindung Mata</h4>
            <ul>
            <li><strong>Kacamata Safety:</strong> Melindungi dari percikan bahan kimia</li>
            <li><strong>Face Shield:</strong> Perlindungan wajah menyeluruh</li>
            <li><strong>Goggles:</strong> Kedap udara untuk gas berbahaya</li>
            </ul>
            </div>
            
            <div class="card">
            <h4>👐 Pelindung Tangan</h4>
            <ul>
            <li><strong>Sarung Tangan Nitrile:</strong> Tahan bahan kimia</li>
            <li><strong>Sarung Tangan Latex:</strong> Untuk prosedur umum</li>
            <li><strong>Sarung Tangan Heat-Resistant:</strong> Tahan panas tinggi</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card">
            <h4>💨 Pelindung Pernapasan</h4>
            <ul>
            <li><strong>Masker N95:</strong> Filter partikel halus</li>
            <li><strong>Respirator:</strong> Perlindungan dari gas beracun</li>
            <li><strong>SCBA:</strong> Untuk area dengan oksigen rendah</li>
            </ul>
            </div>
            
            <div class="card">
            <h4>👔 Pelindung Tubuh</h4>
            <ul>
            <li><strong>Lab Coat:</strong> Perlindungan dasar laboratorium</li>
            <li><strong>Apron:</strong> Tahan bahan kimia korosif</li>
            <li><strong>Suit Hazmat:</strong> Perlindungan menyeluruh</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-container safety-card">', unsafe_allow_html=True)
        st.subheader("🚨 Prosedur Darurat")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="card result-card">
            <h4>🔥 Kebakaran</h4>
            <ol>
            <li><strong>RACE:</strong> Rescue, Alarm, Confine, Extinguish</li>
            <li>Evakuasi area dengan aman</li>
            <li>Aktifkan alarm kebakaran</li>
            <li>Gunakan APAR yang sesuai:
                <ul>
                <li>Kelas A: Air</li>
                <li>Kelas B: Foam/CO₂</li>
                <li>Kelas C: CO₂/Dry Chemical</li>
                </ul>
            </li>
            <li>Hubungi pemadam kebakaran</li>
            </ol>
            </div>
            
            <div class="card calc-card">
            <h4>💧 Tumpahan Bahan Kimia</h4>
            <ol>
            <li>Isolasi area tumpahan</li>
            <li>Gunakan APD lengkap</li>
            <li>Serap dengan bahan penyerap</li>
            <li>Netralkan jika perlu</li>
            <li>Buang sesuai prosedur limbah B3</li>
            <li>Dokumentasikan insiden</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="card gas-card">
            <h4>🤕 Kontak dengan Bahan Kimia</h4>
            <ol>
            <li><strong>Kulit:</strong> Bilas dengan air mengalir 15-20 menit</li>
            <li><strong>Mata:</strong> Bilas dengan eyewash 15 menit</li>
            <li><strong>Terhirup:</strong> Pindah ke udara segar</li>
            <li><strong>Tertelan:</strong> Jangan memuntahkan, minum air</li>
            <li>Hubungi medical emergency</li>
            <li>Bawa Safety Data Sheet (SDS)</li>
            </ol>
            </div>
            
            <div class="card safety-card">
            <h4>📞 Nomor Darurat</h4>
            <ul style="font-size: 18px; line-height: 2;">
            <li><strong>Pemadam Kebakaran:</strong> 113</li>
            <li><strong>Ambulans:</strong> 118/119</li>
            <li><strong>Polisi:</strong> 110</li>
            <li><strong>PLN Gangguan:</strong> 123</li>
            <li><strong>Pertamina:</strong> 500-000</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; background: rgba(255,255,255,0.1); border-radius: 15px; margin-top: 30px;">
<p><strong>🧪 ChemGasMaster v2.0</strong></p>
<p>Aplikasi Pembelajaran Gas Ideal Terlengkap</p>
<p style="font-size: 12px;">© 2024 - Dibuat dengan ❤️ untuk pendidikan kimia</p>
</div>
""", unsafe_allow_html=True)
