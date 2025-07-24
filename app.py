# ===========================================
# APLIKASI KALKULATOR GAS IDEAL + ENSIKLOPEDIA + PANDUAN KESELAMATAN
# ===========================================
import streamlit as st
import math

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
# KONSTANTA
# ===========================================
R_LITER_ATM = 0.08206  # L·atm/(mol·K)
R_PASCAL = 8.314       # J/(mol·K)

# ===========================================
# DATABASE GAS LENGKAP
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
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/O2.jpg",
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
        "category": "Gas Mulia",
        "description": "Gas mulia yang dapat memancarkan cahaya oranye-merah saat dialiri listrik.",
        "image": "https://www.thoughtco.com/thmb/WjJCGpnJuSx3xprsfEgIdwBdoGc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/neon-atom-element-structure-58b82dc23df78c353cdaf542.jpg",
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
        "category": "Gas Mulia",
        "description": "Gas mulia paling ringan kedua, sangat stabil dan tidak mudah terbakar.",
        "image": "https://www.thoughtco.com/thmb/BxnUK8w8vNvJvgJvKKrMJLJ3o9A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/helium-atom-element-structure-58b82dc23df78c353cdaf541.jpg",
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
                "Penanganan": "Aman digunakan, tidak mudah terbakar"
            }
        },
        "aplikasi": "Balon, pendingin MRI, atmosfer inert untuk pengelasan"
    },
    "Argon (Ar)": {
        "icon": "⚡",
        "category": "Gas Mulia",
        "description": "Gas mulia yang paling banyak di atmosfer setelah nitrogen dan oksigen (0.93%).",
        "image": "https://www.thoughtco.com/thmb/kZJvKKrMJLJ3o9A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/argon-atom-element-structure-58b82dc23df78c353cdaf543.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Ar",
                "Massa Molar": "39.948 g/mol",
                "Penampilan": "Gas tak berwarna, tak berbau",
                "Struktur": "Monoatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-189.35 °C (83.8 K)",
                "Titik Didih": "-185.85 °C (87.3 K)",
                "Densitas (STP)": "1.784 g/L",
                "Kalor Jenis": "0.520 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Asfiksia dalam ruang tertutup",
                "Penanganan": "Gunakan ventilasi yang memadai"
            }
        },
        "aplikasi": "Pengelasan, lampu pijar, atmosfer inert"
    },
    "Metana (CH₄)": {
        "icon": "🔥",
        "category": "Hidrokarbon",
        "description": "Hidrokarbon paling sederhana, komponen utama gas alam.",
        "image": "https://www.chemtube3d.com/images/gallery/organicsjpgs/methane.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "CH₄",
                "Massa Molar": "16.04 g/mol",
                "Penampilan": "Gas tak berwarna",
                "Struktur": "Tetrahedral"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-182.5 °C (90.65 K)",
                "Titik Didih": "-161.6 °C (111.55 K)",
                "Densitas (STP)": "0.717 g/L",
                "Kalor Jenis": "2.200 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat mudah terbakar (5-15% di udara)",
                "Penanganan": "Hindari sumber api, gunakan di area berventilasi"
            }
        },
        "aplikasi": "Bahan bakar, pemanas, bahan baku petrokimia"
    },
    "Amonia (NH₃)": {
        "icon": "🧪",
        "category": "Senyawa Nitrogen",
        "description": "Gas dengan bau menyengat, penting dalam industri pupuk.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/NH3.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "NH₃",
                "Massa Molar": "17.03 g/mol",
                "Penampilan": "Gas tak berwarna, bau menyengat",
                "Struktur": "Piramidal trigonal"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-77.73 °C (195.42 K)",  
                "Titik Didih": "-33.34 °C (239.81 K)",
                "Densitas (STP)": "0.771 g/L",
                "Kalor Jenis": "2.175 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Korosif, iritasi mata dan saluran pernapasan",
                "Penanganan": "Gunakan APD lengkap, ventilasi baik"
            }
        },
        "aplikasi": "Pupuk, pendingin, pembersih"
    },
    "Klorin (Cl₂)": {
        "icon": "☠️",
        "category": "Halogen",
        "description": "Gas berwarna kuning-hijau dengan bau menyengat, beracun.",
        "image": "https://www.chemtube3d.com/images/gallery/inorganicsjpgs/Cl2.jpg",
        "properties": {
            "🧪 Identitas Molekul": {
                "Rumus": "Cl₂",
                "Massa Molar": "70.91 g/mol",
                "Penampilan": "Gas kuning-hijau, bau menyengat",
                "Struktur": "Diatomik"
            },
            "⚛️ Sifat Fisika": {
                "Titik Leleh": "-101.5 °C (171.65 K)",
                "Titik Didih": "-34.04 °C (239.11 K)",
                "Densitas (STP)": "3.214 g/L",
                "Kalor Jenis": "0.479 J/(g·K)"
            },
            "⚠️ Keselamatan": {
                "Bahaya": "Sangat beracun, korosif terhadap logam",
                "Penanganan": "Gunakan masker gas, ventilasi ekstrim"
            }
        },
        "aplikasi": "Disinfektan air, pemutih, industri plastik PVC"
    }
}

# ===========================================
# FUNGSI UTILITAS
# ===========================================
def calculate_ideal_gas(P=None, V=None, n=None, T=None, R=R_LITER_ATM):
    """
    Menghitung parameter gas ideal menggunakan PV = nRT
    """
    if P is not None and V is not None and n is not None:
        T_calc = (P * V) / (n * R)
        return {"T": T_calc, "unit": "K"}
    elif P is not None and V is not None and T is not None:
        n_calc = (P * V) / (R * T)
        return {"n": n_calc, "unit": "mol"}
    elif P is not None and n is not None and T is not None:
        V_calc = (n * R * T) / P
        return {"V": V_calc, "unit": "L"}
    elif V is not None and n is not None and T is not None:
        P_calc = (n * R * T) / V
        return {"P": P_calc, "unit": "atm"}
    else:
        return None

def kelvin_to_celsius(K):
    return K - 273.15

def celsius_to_kelvin(C):
    return C + 273.15

def convert_units(value, from_unit, to_unit, unit_type):
    """Konversi unit untuk berbagai jenis pengukuran"""
    conversions = {
        "pressure": {
            "atm": 1,
            "Pa": 101325,
            "kPa": 101.325,
            "mmHg": 760,
            "bar": 1.01325
        },
        "volume": {
            "L": 1,
            "mL": 1000,
            "m³": 0.001,
            "cm³": 1000
        },
        "temperature": {
            "K": 1,
            "°C": 1,  # Special handling needed
            "°F": 1   # Special handling needed
        }
    }
    
    if unit_type == "temperature":
        if from_unit == "°C" and to_unit == "K":
            return celsius_to_kelvin(value)
        elif from_unit == "K" and to_unit == "°C":
            return kelvin_to_celsius(value)
        else:
            return value
    else:
        return value * conversions[unit_type][to_unit] / conversions[unit_type][from_unit]

# ===========================================
# SIDEBAR MENU
# ===========================================
st.sidebar.title("🧪 ChemGasMaster")
st.sidebar.markdown("---")

# Menu selection
menu = st.sidebar.selectbox(
    "🔬 Pilih Menu:",
    ["🏠 Beranda", "🧮 Kalkulator Gas", "📚 Ensiklopedia Gas", "⚠️ Panduan Keselamatan"]
)

# ===========================================
# HALAMAN BERANDA
# ===========================================
if menu == "🏠 Beranda":
    # Add background class
    st.markdown('<div class="beranda-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">🧪 ChemGasMaster - Portal Kimia Gas</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h2>🎯 Selamat Datang di ChemGasMaster!</h2>
            <p style="font-size: 18px; line-height: 1.8;">
            <strong>ChemGasMaster</strong> adalah aplikasi web interaktif yang dirancang untuk membantu 
            mahasiswa, peneliti, dan profesional dalam mempelajari dan menghitung properti gas ideal. 
            Aplikasi ini menggabungkan teori kimia dengan teknologi modern untuk memberikan pengalaman 
            belajar yang optimal.
            </p>
            
            <h3>🚀 Fitur Unggulan:</h3>
            <ul style="font-size: 16px; line-height: 1.6;">
                <li><strong>🧮 Kalkulator Gas Ideal:</strong> Hitung PV, nRT dengan mudah dan akurat</li>
                <li><strong>📚 Ensiklopedia Gas:</strong> Database lengkap berbagai jenis gas</li>
                <li><strong>⚠️ Panduan Keselamatan:</strong> Informasi keselamatan laboratorium</li>
                <li><strong>🎨 Interface Modern:</strong> Desain responsif dan user-friendly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>📐 Persamaan Gas Ideal</h3>
            <div style="text-align: center; font-size: 24px; margin: 20px 0; padding: 20px; background: linear-gradient(135deg, #e3f2fd, #bbdefb); border-radius: 15px;">
                <strong>PV = nRT</strong>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 20px;">
                <div><strong>P</strong> = Tekanan (atm, Pa, mmHg)</div>
                <div><strong>V</strong> = Volume (L, mL, m³)</div>
                <div><strong>n</strong> = Jumlah mol (mol)</div>
                <div><strong>R</strong> = Konstanta gas (0.08206 L·atm/mol·K)</div>
                <div><strong>T</strong> = Suhu (K, °C)</div>
                <div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <h3>📊 Statistik Aplikasi</h3>
            <div style="text-align: center;">
                <div style="font-size: 2rem; color: #2196f3; font-weight: bold;">10+</div>
                <div>Jenis Gas dalam Database</div>
                <hr>
                <div style="font-size: 2rem; color: #4caf50; font-weight: bold;">4</div>
                <div>Mode Kalkulasi</div>
                <hr>
                <div style="font-size: 2rem; color: #ff9800; font-weight: bold;">∞</div>
                <div>Kemungkinan Perhitungan</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
            <h3>🎓 Tips Penggunaan</h3>
            <ol style="font-size: 14px; line-height: 1.6;">
                <li>Pastikan menggunakan unit yang konsisten</li>
                <li>Selalu konversi suhu ke Kelvin untuk perhitungan</li>
                <li>Periksa kondisi STP (0°C, 1 atm) jika diperlukan</li>
                <li>Gunakan panduan keselamatan sebelum eksperimen</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# ===========================================
# HALAMAN KALKULATOR GAS
# ===========================================
elif menu == "🧮 Kalkulator Gas":
    # Add background class
    st.markdown('<div class="kalkulator-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">🧮 Kalkulator Gas Ideal</h1>', unsafe_allow_html=True)
    
    # Tabs untuk berbagai mode kalkulasi
    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Hitung Tekanan", "📏 Hitung Volume", "🧪 Hitung Mol", "🌡️ Hitung Suhu"])
    
    with tab1:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("📊 Perhitungan Tekanan Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="calc-card">', unsafe_allow_html=True)
            st.markdown("#### 📝 Input Parameter")
            
            V_input = st.number_input("Volume (L)", min_value=0.001, value=22.4, format="%.3f")
            n_input = st.number_input("Jumlah mol (mol)", min_value=0.001, value=1.0, format="%.3f")
            T_input_C = st.number_input("Suhu (°C)", value=0.0, format="%.2f")
            
            T_input_K = celsius_to_kelvin(T_input_C)
            
            if st.button("🔍 Hitung Tekanan", key="calc_P"):
                result = calculate_ideal_gas(V=V_input, n=n_input, T=T_input_K)
                if result:
                    P_calc = result["P"]
                    st.session_state.pressure_result = P_calc
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 📈 Hasil Perhitungan")
            
            if 'pressure_result' in st.session_state:
                P = st.session_state.pressure_result
                
                st.success(f"✅ **Tekanan = {P:.4f} atm**")
                
                # Konversi ke unit lain
                st.markdown("**🔄 Konversi Unit:**")
                st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
                st.write(f"• **Pascal (Pa):** {P * 101325:.2f} Pa")
                st.write(f"• **mmHg:** {P * 760:.2f} mmHg") 
                st.write(f"• **kPa:** {P * 101.325:.2f} kPa")
                st.write(f"• **bar:** {P * 1.01325:.4f} bar")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Interpretasi hasil
                if P < 0.1:
                    st.info("💡 Tekanan sangat rendah - kondisi vakum tinggi")
                elif P > 10:
                    st.warning("⚠️ Tekanan tinggi - gunakan peralatan tahan tekanan")
                else:
                    st.info("✅ Tekanan dalam rentang normal")
            else:
                st.info("👆 Masukkan parameter dan klik tombol hitung")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("📏 Perhitungan Volume Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="calc-card">', unsafe_allow_html=True)
            st.markdown("#### 📝 Input Parameter")
            
            P_input = st.number_input("Tekanan (atm)", min_value=0.001, value=1.0, format="%.3f")
            n_input_v = st.number_input("Jumlah mol (mol)", min_value=0.001, value=1.0, format="%.3f", key="n_vol")
            T_input_C_v = st.number_input("Suhu (°C)", value=0.0, format="%.2f", key="T_vol")
            
            T_input_K_v = celsius_to_kelvin(T_input_C_v)
            
            if st.button("📏 Hitung Volume", key="calc_V"):
                result = calculate_ideal_gas(P=P_input, n=n_input_v, T=T_input_K_v)
                if result:
                    V_calc = result["V"]
                    st.session_state.volume_result = V_calc
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 📈 Hasil Perhitungan")
            
            if 'volume_result' in st.session_state:
                V = st.session_state.volume_result
                
                st.success(f"✅ **Volume = {V:.4f} L**")
                
                # Konversi ke unit lain
                st.markdown("**🔄 Konversi Unit:**")
                st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
                st.write(f"• **Mililiter (mL):** {V * 1000:.2f} mL")
                st.write(f"• **Meter kubik (m³):** {V * 0.001:.6f} m³") 
                st.write(f"• **Sentimeter kubik (cm³):** {V * 1000:.2f} cm³")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Interpretasi hasil
                if V < 1:
                    st.info("💡 Volume kecil - cocok untuk eksperimen skala laboratorium")
                elif V > 100:
                    st.warning("⚠️ Volume besar - pastikan ruangan memadai")
                else:
                    st.info("✅ Volume dalam rentang normal")
            else:
                st.info("👆 Masukkan parameter dan klik tombol hitung")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("🧪 Perhitungan Jumlah Mol")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="calc-card">', unsafe_allow_html=True)
            st.markdown("#### 📝 Input Parameter")
            
            P_input_n = st.number_input("Tekanan (atm)", min_value=0.001, value=1.0, format="%.3f", key="P_mol")
            V_input_n = st.number_input("Volume (L)", min_value=0.001, value=22.4, format="%.3f", key="V_mol")
            T_input_C_n = st.number_input("Suhu (°C)", value=0.0, format="%.2f", key="T_mol")
            
            T_input_K_n = celsius_to_kelvin(T_input_C_n)
            
            if st.button("🧪 Hitung Mol", key="calc_n"):
                result = calculate_ideal_gas(P=P_input_n, V=V_input_n, T=T_input_K_n)
                if result:
                    n_calc = result["n"]
                    st.session_state.mol_result = n_calc
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 📈 Hasil Perhitungan")
            
            if 'mol_result' in st.session_state:
                n = st.session_state.mol_result
                
                st.success(f"✅ **Jumlah mol = {n:.6f} mol**")
                
                # Konversi ke unit lain
                st.markdown("**🔄 Konversi Unit:**")
                st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
                st.write(f"• **Milimol (mmol):** {n * 1000:.3f} mmol")
                st.write(f"• **Mikromol (μmol):** {n * 1000000:.1f} μmol")
                st.write(f"• **Molekul:** {n * 6.022e23:.2e} molekul")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Interpretasi hasil
                if n < 0.001:
                    st.info("💡 Jumlah mol sangat kecil - eksperimen mikro")
                elif n > 10:
                    st.warning("⚠️ Jumlah mol besar - pastikan keamanan")
                else:
                    st.info("✅ Jumlah mol dalam rentang normal")
            else:
                st.info("👆 Masukkan parameter dan klik tombol hitung")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("🌡️ Perhitungan Suhu Gas")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="calc-card">', unsafe_allow_html=True)
            st.markdown("#### 📝 Input Parameter")
            
            P_input_t = st.number_input("Tekanan (atm)", min_value=0.001, value=1.0, format="%.3f", key="P_temp")
            V_input_t = st.number_input("Volume (L)", min_value=0.001, value=22.4, format="%.3f", key="V_temp")
            n_input_t = st.number_input("Jumlah mol (mol)", min_value=0.001, value=1.0, format="%.3f", key="n_temp")
            
            if st.button("🌡️ Hitung Suhu", key="calc_T"):
                result = calculate_ideal_gas(P=P_input_t, V=V_input_t, n=n_input_t)
                if result:
                    T_calc = result["T"]
                    st.session_state.temp_result = T_calc
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("#### 📈 Hasil Perhitungan")
            
            if 'temp_result' in st.session_state:
                T_K = st.session_state.temp_result
                T_C = kelvin_to_celsius(T_K)
                
                st.success(f"✅ **Suhu = {T_K:.2f} K**")
                
                # Konversi ke unit lain
                st.markdown("**🔄 Konversi Unit:**")
                st.markdown('<div class="conversion-box">', unsafe_allow_html=True)
                st.write(f"• **Celsius (°C):** {T_C:.2f} °C")
                st.write(f"• **Fahrenheit (°F):** {(T_C * 9/5) + 32:.2f} °F")
                st.write(f"• **Rankine (°R):** {T_K * 9/5:.2f} °R")
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Interpretasi hasil
                if T_K < 273.15:
                    st.warning("❄️ Suhu di bawah titik beku air")
                elif T_K > 373.15:
                    st.warning("🔥 Suhu di atas titik didih air")
                else:
                    st.info("✅ Suhu dalam rentang normal air cair")
            else:
                st.info("👆 Masukkan parameter dan klik tombol hitung")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ===========================================
# HALAMAN ENSIKLOPEDIA GAS
# ===========================================
elif menu == "📚 Ensiklopedia Gas":
    # Add background class
    st.markdown('<div class="ensiklopedia-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">📚 Ensiklopedia Gas</h1>', unsafe_allow_html=True)
    
    # Filter berdasarkan kategori
    categories = ["Semua"] + list(set([gas_data["category"] for gas_data in GAS_DATABASE.values()]))
    selected_category = st.selectbox("🔍 Filter berdasarkan kategori:", categories)
    
    # Filter gas berdasarkan kategori
    if selected_category == "Semua":
        filtered_gases = GAS_DATABASE
    else:
        filtered_gases = {name: data for name, data in GAS_DATABASE.items() if data["category"] == selected_category}
    
    # Grid layout untuk menampilkan gas
    gas_names = list(filtered_gases.keys())
    
    for i in range(0, len(gas_names), 2):
        cols = st.columns(2)
        
        for j, col in enumerate(cols):
            if i + j < len(gas_names):
                gas_name = gas_names[i + j]
                gas_data = filtered_gases[gas_name]
                
                with col:
                    st.markdown('<div class="gas-card">', unsafe_allow_html=True)
                    
                    # Header gas
                    st.markdown(f"""
                    <div style="text-align: center; margin-bottom: 20px;">
                        <div style="font-size: 4rem; margin-bottom: 10px;">{gas_data['icon']}</div>
                        <h3 style="color: #ff9800; margin: 0;">{gas_name}</h3>
                        <p style="color: #666; font-style: italic; margin: 5px 0;">{gas_data['category']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Deskripsi
                    st.markdown(f"**📖 Deskripsi:**")
                    st.write(gas_data["description"])
                    
                    # Aplikasi
                    st.markdown(f"**🎯 Aplikasi:**")
                    st.write(gas_data["aplikasi"])
                    
                    # Button untuk detail
                    if st.button(f"🔍 Detail {gas_name.split('(')[0]}", key=f"detail_{gas_name}"):
                        st.session_state.selected_gas = gas_name
                    
                    st.markdown('</div>', unsafe_allow_html=True)
    
    # Detail gas yang dipilih
    if 'selected_gas' in st.session_state:
        selected_gas = st.session_state.selected_gas
        gas_data = GAS_DATABASE[selected_gas]
        
        st.markdown("---")
        st.markdown(f'<h2 style="text-align: center; color: #ff9800;">🔬 Detail {selected_gas}</h2>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown(f"""
            <div style="text-align: center; padding: 30px; background: linear-gradient(135deg, rgba(255,152,0,0.1), rgba(255,152,0,0.05)); border-radius: 20px; margin-bottom: 20px;">
                <div style="font-size: 6rem; margin-bottom: 15px;">{gas_data['icon']}</div>
                <h3 style="color: #ff9800; margin: 10px 0;">{selected_gas}</h3>
                <p style="color: #666; font-style: italic;">{gas_data['category']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**📖 Deskripsi Lengkap:**")
            st.write(gas_data["description"])
            st.markdown(f"**🎯 Aplikasi Industri:**")
            st.write(gas_data["aplikasi"])
        
        # Tabel properti
        st.markdown("### 📊 Properti Kimia dan Fisika")
        
        for category, properties in gas_data["properties"].items():
            st.markdown(f"#### {category}")
            
            # Create table
            table_html = '<table class="property-table">'
            table_html += '<thead><tr><th>Properti</th><th>Nilai</th></tr></thead><tbody>'
            
            for prop, value in properties.items():
                table_html += f'<tr><td><strong>{prop}</strong></td><td>{value}</td></tr>'
            
            table_html += '</tbody></table>'
            st.markdown(table_html, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# ===========================================
# HALAMAN PANDUAN KESELAMATAN
# ===========================================
elif menu == "⚠️ Panduan Keselamatan":
    # Add background class
    st.markdown('<div class="keselamatan-bg"></div>', unsafe_allow_html=True)
    
    st.markdown('<h1 class="main-header">⚠️ Panduan Keselamatan Laboratorium</h1>', unsafe_allow_html=True)
    
    # Tabs untuk berbagai aspek keselamatan
    tab1, tab2, tab3, tab4 = st.tabs(["🚨 Simbol Bahaya", "🛡️ APD", "🚨 Prosedur Darurat", "📋 Checklist"])
    
    with tab1:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("🚨 Simbol-Simbol Bahaya Kimia")
        
        # Simbol bahaya dalam grid
        hazard_symbols = [
            {"symbol": "☠️", "name": "Beracun", "description": "Dapat menyebabkan keracunan serius atau kematian", "color": "#f44336"},
            {"symbol": "🔥", "name": "Mudah Terbakar", "description": "Dapat terbakar dengan mudah pada suhu rendah", "color": "#ff9800"},
            {"symbol": "💥", "name": "Eksplosif", "description": "Dapat meledak dengan percikan atau panas", "color": "#e91e63"},
            {"symbol": "🧪", "name": "Korosif", "description": "Dapat merusak kulit, mata, atau material", "color": "#9c27b0"},
            {"symbol": "⚡", "name": "Oksidator", "description": "Dapat menyebabkan atau memperparah kebakaran", "color": "#2196f3"},
            {"symbol": "🌡️", "name": "Berbahaya", "description": "Dapat menyebabkan iritasi atau bahaya kesehatan", "color": "#ff5722"}
        ]
        
        cols = st.columns(3)
        for i, symbol_data in enumerate(hazard_symbols):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="safety-card" style="text-align: center; padding: 20px; margin: 10px 0;">
                    <div style="font-size: 3rem; margin-bottom: 10px;">{symbol_data['symbol']}</div>
                    <h4 style="color: {symbol_data['color']}; margin: 10px 0;">{symbol_data['name']}</h4>
                    <p style="font-size: 14px; line-height: 1.4;">{symbol_data['description']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("🛡️ Alat Pelindung Diri (APD)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="safety-card">
                <h4>👓 Pelindung Mata dan Wajah</h4>
                <ul>
                    <li><strong>Kacamata Keselamatan:</strong> Untuk perlindungan dasar dari percikan</li>
                    <li><strong>Kacamata Goggle:</strong> Perlindungan menyeluruh dari gas dan uap</li>
                    <li><strong>Face Shield:</strong> Perlindungan wajah dari percikan bahan kimia</li>
                </ul>
                
                <h4>👐 Pelindung Tangan</h4>
                <ul>
                    <li><strong>Sarung Tangan Nitrile:</strong> Tahan terhadap sebagian besar bahan kimia</li>
                    <li><strong>Sarung Tangan Latex:</strong> Untuk perlindungan dasar</li>
                    <li><strong>Sarung Tangan Neoprene:</strong> Tahan asam dan basa kuat</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="safety-card">
                <h4>👔 Pelindung Tubuh</h4>
                <ul>
                    <li><strong>Jas Laboratorium:</strong> Perlindungan dasar dari percikan</li>
                    <li><strong>Apron Kimia:</strong> Perlindungan ekstra untuk asam kuat</li>
                    <li><strong>Suit Kimia:</strong> Perlindungan menyeluruh untuk bahan berbahaya</li>
                </ul>
                
                <h4>👃 Pelindung Pernapasan</h4>
                <ul>
                    <li><strong>Masker Debu:</strong> Untuk partikel halus</li>
                    <li><strong>Respirator:</strong> Untuk uap kimia berbahaya</li>
                    <li><strong>SCBA:</strong> Untuk atmosfer sangat berbahaya</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("🚨 Prosedur Keadaan Darurat")
        
        # Emergency procedures
        st.markdown("""
        <div class="safety-card">
            <h4>🔥 Prosedur Kebakaran</h4>
            <ol style="font-size: 16px; line-height: 1.6;">
                <li><strong>ALARM:</strong> Aktifkan alarm kebakaran</li>
                <li><strong>EVAKUASI:</strong> Keluar melalui jalur evakuasi terdekat</li>
                <li><strong>TUTUP:</strong> Tutup semua sumber gas dan listrik jika aman</li>
                <li><strong>PANGGIL:</strong> Hubungi pemadam kebakaran (113)</li>
                <li><strong>TITIK KUMPUL:</strong> Berkumpul di titik aman yang telah ditentukan</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="safety-card">
                <h4>☠️ Keracunan Gas</h4>
                <ol>
                    <li>Pindahkan korban ke udara segar</li>
                    <li>Periksa pernapasan dan nadi</li>
                    <li>Berikan bantuan pernapasan jika perlu</li>
                    <li>Hubungi layanan medis darurat</li>
                    <li>Jangan biarkan korban sendirian</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="safety-card">
                <h4>🧪 Tumpahan Bahan Kimia</h4>
                <ol>
                    <li>Evakuasi area terdampak</li>
                    <li>Gunakan APD lengkap</li>
                    <li>Hentikan sumber tumpahan</li>
                    <li>Serap dengan bahan penyerap</li>
                    <li>Ventilasi area yang terkontaminasi</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="tab-container">', unsafe_allow_html=True)
        st.subheader("📋 Checklist Keselamatan Harian")
        
        st.markdown("""
        <div class="safety-card">
            <h4>✅ Sebelum Memulai Kerja</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div>
                    <input type="checkbox" disabled> APD lengkap telah dikenakan<br>
                    <input type="checkbox" disabled> Ventilasi laboratorium berfungsi<br>
                    <input type="checkbox" disabled> Safety shower dapat diakses<br>
                    <input type="checkbox" disabled> Eyewash station berfungsi<br>
                    <input type="checkbox" disabled> Alat pemadam tersedia<br>
                </div>
                <div>
                    <input type="checkbox" disabled> MSDS bahan kimia dibaca<br>
                    <input type="checkbox" disabled> Jalur evakuasi diketahui<br>
                    <input type="checkbox" disabled> Peralatan darurat diperiksa<br>
                    <input type="checkbox" disabled> Nomor darurat tersedia<br>
                    <input type="checkbox" disabled> Rekan kerja mengetahui aktivitas<br>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="safety-card">
            <h4>🔚 Setelah Selesai Kerja</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div>
                    <input type="checkbox" disabled> Semua bahan kimia disimpan aman<br>
                    <input type="checkbox" disabled> Peralatan dibersihkan<br>
                    <input type="checkbox" disabled> Sumber gas ditutup<br>
                    <input type="checkbox" disabled> Ventilasi tetap menyala<br>
                    <input type="checkbox" disabled> Limbah dibuang sesuai prosedur<br>
                </div>
                <div>
                    <input type="checkbox" disabled> Area kerja bersih<br>
                    <input type="checkbox" disabled> APD dicuci/disimpan<br>
                    <input type="checkbox" disabled> Dokumentasi lengkap<br>
                    <input type="checkbox" disabled> Peralatan darurat diperiksa<br>
                    <input type="checkbox" disabled> Laporan insiden (jika ada)<br>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Kontak darurat
        st.markdown("""
        <div class="safety-card">
            <h4>📞 Kontak Darurat</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 16px;">
                <div>
                    <strong>🚨 Emergency:</strong> 112<br>
                    <strong>🔥 Pemadam Kebakaran:</strong> 113<br>
                    <strong>🚑 Ambulans:</strong> 118<br>
                </div>
                <div>
                    <strong>👨‍⚕️ Poison Control:</strong> 021-4250767<br>
                    <strong>🏥 RS Terdekat:</strong> [Sesuaikan lokasi]<br>
                    <strong>🔧 Maintenance:</strong> [Internal]<br>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ===========================================
# FOOTER
# ===========================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05)); border-radius: 15px; margin-top: 30px;">
    <h4 style="color: #0d47a1;">🧪 ChemGasMaster</h4>
    <p style="color: #666; margin: 10px 0;">Aplikasi Kimia Gas Interaktif untuk Pembelajaran dan Penelitian</p>
    <p style="font-size: 14px; color: #999;">© 2024 ChemGasMaster. Dibuat dengan ❤️ menggunakan Streamlit</p>
    <div style="margin-top: 15px;">
        <span style="margin: 0 10px;">⚗️ Chemistry</span>
        <span style="margin: 0 10px;">🔬 Science</span>
        <span style="margin: 0 10px;">🧮 Mathematics</span>
        <span style="margin: 0 10px;">📚 Education</span>
    </div>
</div>
""", unsafe_allow_html=True)
