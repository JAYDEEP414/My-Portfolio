# app.py
import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Jaydeep Sutar | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS ====================
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&display=swap');
    
    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Global Styles */
    .stApp {
        background: #050816;
        color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
    }
    
    .main .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
    
    /* Animated Background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 30%, rgba(0, 245, 255, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.1) 0%, transparent 60%);
        z-index: -1;
        pointer-events: none;
    }
    
    /* Navigation */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: rgba(5, 8, 22, 0.85);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(0, 245, 255, 0.2);
        padding: 1rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .navbar-logo {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00F5FF, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .navbar-links {
        display: flex;
        gap: 2rem;
    }
    
    .navbar-links a {
        color: #FFFFFF;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .navbar-links a:hover {
        color: #00F5FF;
        text-shadow: 0 0 10px rgba(0, 245, 255, 0.8);
    }
    
    /* Hero Section */
    .hero-container {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
        padding: 6rem 2rem 2rem 2rem;
    }
    
    .hero-greeting {
        font-family: 'Orbitron', sans-serif;
        color: #00F5FF;
        font-size: 1.2rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }
    
    .hero-name {
        font-family: 'Orbitron', sans-serif;
        font-size: 4.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00F5FF 0%, #7C3AED 50%, #38BDF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: fadeInUp 1s ease;
        text-shadow: 0 0 80px rgba(0, 245, 255, 0.3);
        line-height: 1.1;
    }
    
    .hero-title {
        font-size: 2rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 1.5rem;
        min-height: 3rem;
    }
    
    .hero-title #typed-text {
        background: linear-gradient(90deg, #00F5FF, #38BDF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .cursor {
        display: inline-block;
        width: 3px;
        background: #00F5FF;
        animation: blink 1s infinite;
        margin-left: 4px;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.7);
        max-width: 700px;
        margin: 0 auto 2.5rem auto;
        line-height: 1.6;
    }
    
    .hero-buttons {
        display: flex;
        gap: 1.5rem;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 2rem;
    }
    
    .btn-primary, .btn-secondary {
        padding: 0.9rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;
        transition: all 0.4s ease;
        border: none;
        font-family: 'Poppins', sans-serif;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        color: #FFFFFF;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3);
    }
    
    .btn-primary:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 245, 255, 0.5);
    }
    
    .btn-secondary {
        background: rgba(255, 255, 255, 0.05);
        color: #FFFFFF;
        border: 2px solid rgba(0, 245, 255, 0.4);
        backdrop-filter: blur(10px);
    }
    
    .btn-secondary:hover {
        background: rgba(0, 245, 255, 0.1);
        border-color: #00F5FF;
        transform: translateY(-3px);
    }
    
    .social-icons {
        display: flex;
        gap: 1.2rem;
        justify-content: center;
        margin-top: 1.5rem;
    }
    
    .social-icon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 245, 255, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #FFFFFF;
        font-size: 1.3rem;
        transition: all 0.3s ease;
        text-decoration: none;
        backdrop-filter: blur(10px);
    }
    
    .social-icon:hover {
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        transform: translateY(-5px) rotate(360deg);
        box-shadow: 0 10px 25px rgba(0, 245, 255, 0.5);
    }
    
    /* Section Styles */
    .section {
        padding: 5rem 2rem;
        max-width: 1300px;
        margin: 0 auto;
        position: relative;
    }
    
    .section-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #00F5FF 0%, #7C3AED 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.6);
        margin-bottom: 3rem;
        font-size: 1.1rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    /* Glass Card */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 245, 255, 0.1), transparent);
        transition: left 0.6s ease;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-10px);
        border-color: #00F5FF;
        box-shadow: 0 20px 60px rgba(0, 245, 255, 0.2);
    }
    
    /* About Card */
    .about-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 25px;
        padding: 3rem;
        font-size: 1.15rem;
        line-height: 1.9;
        color: rgba(255, 255, 255, 0.85);
        position: relative;
        overflow: hidden;
    }
    
    .about-card::after {
        content: '</>';
        position: absolute;
        top: 1rem;
        right: 2rem;
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem;
        color: rgba(0, 245, 255, 0.2);
        font-weight: bold;
    }
    
    .stat-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        border-color: #00F5FF;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3);
    }
    
    .stat-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        margin-top: 0.5rem;
        letter-spacing: 1px;
    }
    
    /* Skill Cards */
    .skill-category {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        height: 100%;
        transition: all 0.4s ease;
    }
    
    .skill-category:hover {
        transform: translateY(-10px);
        border-color: #00F5FF;
        box-shadow: 0 20px 50px rgba(0, 245, 255, 0.2);
    }
    
    .skill-category-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.3rem;
        color: #00F5FF;
        margin-bottom: 1.5rem;
        font-weight: 700;
        text-align: center;
    }
    
    .skill-badge {
        display: inline-block;
        background: rgba(0, 245, 255, 0.1);
        border: 1px solid rgba(0, 245, 255, 0.4);
        color: #FFFFFF;
        padding: 0.5rem 1rem;
        margin: 0.3rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .skill-badge:hover {
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 245, 255, 0.4);
    }
    
    /* Project Cards */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        height: 100%;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        border-color: #00F5FF;
        box-shadow: 0 20px 50px rgba(0, 245, 255, 0.3);
    }
    
    .project-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .project-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.3rem;
        color: #FFFFFF;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .project-description {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .tech-badge {
        display: inline-block;
        background: rgba(124, 58, 237, 0.15);
        border: 1px solid rgba(124, 58, 237, 0.4);
        color: #C4B5FD;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Experience Timeline */
    .timeline-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        position: relative;
        border-left: 4px solid #00F5FF;
        transition: all 0.4s ease;
    }
    
    .timeline-card:hover {
        transform: translateX(10px);
        border-color: #00F5FF;
        box-shadow: -10px 10px 40px rgba(0, 245, 255, 0.2);
    }
    
    .timeline-date {
        color: #00F5FF;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .timeline-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
    }
    
    .timeline-company {
        color: #38BDF8;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    .timeline-list {
        color: rgba(255, 255, 255, 0.8);
        line-height: 1.8;
        padding-left: 1.2rem;
    }
    
    /* Achievement Cards */
    .achievement-card {
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.1), rgba(124, 58, 237, 0.1));
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        height: 100%;
        transition: all 0.4s ease;
    }
    
    .achievement-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 245, 255, 0.3);
    }
    
    .achievement-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .achievement-text {
        color: #FFFFFF;
        font-size: 1rem;
        line-height: 1.5;
        font-weight: 500;
    }
    
    /* Contact Form */
    .contact-info-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.3s ease;
    }
    
    .contact-info-card:hover {
        transform: translateX(10px);
        border-color: #00F5FF;
    }
    
    .contact-icon {
        font-size: 2rem;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .contact-info-label {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .contact-info-value {
        color: #FFFFFF;
        font-size: 1.05rem;
        font-weight: 500;
    }
    
    /* Streamlit Input Overrides */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 245, 255, 0.3) !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        padding: 0.75rem 1rem !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #00F5FF !important;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.3) !important;
    }
    
    .stTextInput label, .stTextArea label {
        color: #00F5FF !important;
        font-weight: 500 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00F5FF, #7C3AED) !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 15px 40px rgba(0, 245, 255, 0.5) !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 2rem 2rem 2rem;
        border-top: 1px solid rgba(0, 245, 255, 0.2);
        margin-top: 4rem;
        color: rgba(255, 255, 255, 0.6);
    }
    
    .footer-heart {
        color: #00F5FF;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 245, 255, 0.5); }
        50% { box-shadow: 0 0 40px rgba(0, 245, 255, 0.8); }
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-name { font-size: 2.5rem; }
        .hero-title { font-size: 1.3rem; }
        .section-title { font-size: 2rem; }
        .navbar-links { display: none; }
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #050816;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00F5FF, #7C3AED);
        border-radius: 10px;
    }

    /* ============ 3D UI ADDITIONS (tilt + depth only) ============ */
    .glass-card, .project-card, .skill-category, .timeline-card,
    .achievement-card, .stat-box, .about-card {
        transform-style: preserve-3d;
        will-change: transform;
    }

    .section {
        perspective: 1400px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== 3D SCROLL-AWARE BACKGROUND ====================
def three_js_background():
    """
    Full-page, scroll-reactive 3D background rendered with Three.js.
    Escapes the Streamlit iframe so it sits fixed behind every section
    (instead of being confined to the hero) and reacts to page scroll
    with data-analyst themed 3D objects: a rotating bar chart, a floating
    trend line, a wireframe "spreadsheet" grid, and two data-globe spheres.
    """
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            html, body { margin: 0; padding: 0; overflow: hidden; background: transparent; }
            #canvas-container { width: 100%; height: 100%; }
            canvas { display: block; }
        </style>
    </head>
    <body>
        <div id="canvas-container"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            // ---- Escape the Streamlit iframe so this canvas becomes a
            // ---- fixed, full-viewport background layer for the whole page.
            (function attachFullPage() {
                try {
                    const frame = window.frameElement;
                    if (frame) {
                        frame.style.position = 'fixed';
                        frame.style.top = '0';
                        frame.style.left = '0';
                        frame.style.width = '100vw';
                        frame.style.height = '100vh';
                        frame.style.zIndex = '-1';
                        frame.style.pointerEvents = 'none';
                        frame.style.border = 'none';
                        let el = frame.parentElement;
                        while (el && el.tagName !== 'BODY') {
                            el.style.zIndex = el.style.zIndex || 'auto';
                            el = el.parentElement;
                        }
                    }
                } catch (e) { /* cross-origin fallback: stays as normal block */ }
            })();

            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setClearColor(0x000000, 0);
            container.appendChild(renderer.domElement);

            const rootGroup = new THREE.Group();
            scene.add(rootGroup);

            // ---- Particle field ----
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 2600;
            const posArray = new Float32Array(particlesCount * 3);
            const colorArray = new Float32Array(particlesCount * 3);
            for (let i = 0; i < particlesCount * 3; i++) {
                posArray[i] = (Math.random() - 0.5) * 18;
            }
            for (let i = 0; i < particlesCount; i++) {
                const c = Math.random();
                if (c < 0.5) { colorArray[i*3]=0; colorArray[i*3+1]=0.96; colorArray[i*3+2]=1; }
                else { colorArray[i*3]=0.49; colorArray[i*3+1]=0.23; colorArray[i*3+2]=0.93; }
            }
            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorArray, 3));
            const particlesMaterial = new THREE.PointsMaterial({
                size: 0.015, vertexColors: true, transparent: true, opacity: 0.75, blending: THREE.AdditiveBlending
            });
            const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
            rootGroup.add(particlesMesh);

            // ---- Data globes (wireframe icosahedrons) ----
            const sphere = new THREE.Mesh(
                new THREE.IcosahedronGeometry(2, 2),
                new THREE.MeshBasicMaterial({ color: 0x00F5FF, wireframe: true, transparent: true, opacity: 0.18 })
            );
            sphere.position.set(4.5, 0.5, -3);
            rootGroup.add(sphere);

            const sphere2 = new THREE.Mesh(
                new THREE.IcosahedronGeometry(1.4, 1),
                new THREE.MeshBasicMaterial({ color: 0x7C3AED, wireframe: true, transparent: true, opacity: 0.18 })
            );
            sphere2.position.set(-4.5, -1, -3);
            rootGroup.add(sphere2);

            // ---- 3D bar chart (data analyst motif) ----
            const chartGroup = new THREE.Group();
            chartGroup.position.set(-5.5, -1.6, -4);
            const barCount = 6;
            const barMeshes = [];
            for (let i = 0; i < barCount; i++) {
                const h = 0.6 + Math.random() * 1.6;
                const geo = new THREE.BoxGeometry(0.35, h, 0.35);
                const t = i / (barCount - 1);
                const color = new THREE.Color().lerpColors(new THREE.Color(0x00F5FF), new THREE.Color(0x7C3AED), t);
                const mat = new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.55 });
                const bar = new THREE.Mesh(geo, mat);
                bar.position.set(i * 0.5 - (barCount * 0.5 * 0.5), h / 2, 0);
                bar.userData = { baseHeight: h, phase: i * 0.7 };
                chartGroup.add(bar);
                barMeshes.push(bar);
            }
            rootGroup.add(chartGroup);

            // ---- Floating trend line (line chart motif) ----
            const linePoints = [];
            for (let i = 0; i < 10; i++) {
                linePoints.push(new THREE.Vector3(i * 0.55 - 2.5, Math.sin(i * 0.9) * 0.6, 0));
            }
            const lineGeo = new THREE.BufferGeometry().setFromPoints(linePoints);
            const lineMat = new THREE.LineBasicMaterial({ color: 0x38BDF8, transparent: true, opacity: 0.6 });
            const trendLine = new THREE.Line(lineGeo, lineMat);
            trendLine.position.set(2.8, 2.3, -5);
            rootGroup.add(trendLine);

            // ---- Wireframe "spreadsheet" grid ----
            const grid = new THREE.GridHelper(6, 10, 0x7C3AED, 0x00F5FF);
            grid.material.transparent = true;
            grid.material.opacity = 0.12;
            grid.position.set(0, -3, -6);
            rootGroup.add(grid);

            camera.position.z = 6;

            // ---- Mouse parallax ----
            let mouseX = 0, mouseY = 0;
            document.addEventListener('mousemove', (e) => {
                mouseX = (e.clientX / window.innerWidth) * 2 - 1;
                mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
            });
            try {
                window.parent.document.addEventListener('mousemove', (e) => {
                    mouseX = (e.clientX / window.parent.innerWidth) * 2 - 1;
                    mouseY = -(e.clientY / window.parent.innerHeight) * 2 + 1;
                });
            } catch (e) {}

            // ---- Scroll-reactive rotation ----
            let scrollFraction = 0;
            function updateScrollFraction() {
                try {
                    const doc = window.parent.document.documentElement;
                    const scrollTop = window.parent.scrollY || doc.scrollTop || 0;
                    const scrollHeight = Math.max(doc.scrollHeight - window.parent.innerHeight, 1);
                    scrollFraction = Math.min(Math.max(scrollTop / scrollHeight, 0), 1);
                } catch (e) { /* cross-origin: no-op, static scene still animates */ }
            }
            try { window.parent.addEventListener('scroll', updateScrollFraction, { passive: true }); } catch (e) {}
            setInterval(updateScrollFraction, 300);

            let t = 0;
            function animate() {
                requestAnimationFrame(animate);
                t += 0.016;

                particlesMesh.rotation.y += 0.0006;
                particlesMesh.rotation.x += 0.0002;

                sphere.rotation.x += 0.003;
                sphere.rotation.y += 0.005;
                sphere2.rotation.x -= 0.002;
                sphere2.rotation.y -= 0.003;

                // Scroll drives overall scene rotation + depth for a "3D while scrolling" feel
                rootGroup.rotation.y = scrollFraction * Math.PI * 0.6 - 0.3;
                rootGroup.position.z = -scrollFraction * 3;
                chartGroup.rotation.y = 0.3 + scrollFraction * Math.PI * 0.4;
                trendLine.position.y = 2.3 + Math.sin(t * 0.6) * 0.2 - scrollFraction * 1.5;
                grid.rotation.z = scrollFraction * 0.4;

                barMeshes.forEach((bar) => {
                    const s = 1 + Math.sin(t * 1.2 + bar.userData.phase) * 0.12;
                    bar.scale.y = s;
                });

                camera.position.x += (mouseX * 0.6 - camera.position.x) * 0.04;
                camera.position.y += (mouseY * 0.4 - camera.position.y) * 0.04;
                camera.lookAt(scene.position);

                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """, height=0)

# ==================== 3D TILT INTERACTION FOR CARDS ====================
def inject_tilt_effect():
    """
    Adds a subtle real-time 3D tilt (perspective rotateX/rotateY) to the
    existing glass/project/skill/timeline/achievement/stat cards as the
    mouse moves over them. Purely a visual/3D-UI enhancement — no content,
    layout, or section changes.
    """
    components.html("""
    <script>
    (function() {
        const SELECTORS = '.glass-card, .project-card, .skill-category, .timeline-card, .achievement-card, .stat-box, .about-card';
        function initTilt() {
            let doc;
            try { doc = window.parent.document; } catch (e) { return; }
            const cards = doc.querySelectorAll(SELECTORS);
            cards.forEach((card) => {
                if (card.dataset.tiltInit) return;
                card.dataset.tiltInit = "true";
                card.style.transformStyle = 'preserve-3d';
                card.style.transition = 'transform 0.15s ease-out, box-shadow 0.15s ease-out';
                card.addEventListener('mousemove', (e) => {
                    const rect = card.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    const cx = rect.width / 2;
                    const cy = rect.height / 2;
                    const rotateX = ((y - cy) / cy) * -6;
                    const rotateY = ((x - cx) / cx) * 6;
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02,1.02,1.02)`;
                });
                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1,1,1)';
                });
            });
        }
        initTilt();
        setInterval(initTilt, 1200); // re-attach after Streamlit re-renders
    })();
    </script>
    """, height=0)

# ==================== HERO SECTION ====================
def hero_section():
    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;600;700;800;900&display=swap');
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { background-color: transparent; color: #FFFFFF; font-family: 'Poppins', sans-serif; width: 100vw; height: 100vh; }
            .hero { min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 2rem; position: relative; z-index: 1; }
            .hero-content { position: relative; z-index: 2; perspective: 1200px; }
            .greeting { font-family: 'Orbitron', sans-serif; color: #00F5FF; font-size: 1rem; letter-spacing: 6px; text-transform: uppercase; margin-bottom: 1rem; }
            .name { font-family: 'Orbitron', sans-serif; font-size: clamp(2.5rem, 6vw, 5rem); font-weight: 900; background: linear-gradient(135deg, #00F5FF 0%, #7C3AED 50%, #38BDF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1.5rem; line-height: 1.1; filter: drop-shadow(0 0 30px rgba(0, 245, 255, 0.3)); transform-style: preserve-3d; }
            .typed-container { font-size: clamp(1.2rem, 3vw, 2rem); font-weight: 600; margin-bottom: 1.5rem; min-height: 3rem; }
            .typed-text { background: linear-gradient(90deg, #00F5FF, #38BDF8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
            .cursor { display: inline-block; width: 4px; height: 1.5rem; background: #00F5FF; animation: blink 0.8s infinite; margin-left: 4px; vertical-align: middle; }
            @keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }
            .description { font-size: clamp(1rem, 1.5vw, 1.2rem); color: rgba(255, 255, 255, 0.75); max-width: 700px; margin: 0 auto 2.5rem auto; line-height: 1.7; }
            .buttons { display: flex; gap: 1.2rem; justify-content: center; flex-wrap: wrap; margin-bottom: 2rem; }
            .btn { padding: 0.9rem 2rem; border-radius: 50px; font-weight: 600; font-size: 1rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer; transition: all 0.4s ease; border: none; }
            .btn-primary { background: linear-gradient(135deg, #00F5FF, #7C3AED); color: #FFFFFF; box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3); }
            .btn-secondary { background: rgba(255, 255, 255, 0.05); color: #FFFFFF; border: 2px solid rgba(0, 245, 255, 0.5); backdrop-filter: blur(10px); }
            
            /* Social Icons */
            .social-links { display: flex; gap: 1.5rem; justify-content: center; margin-top: 1rem; }
            .social-btn { 
                width: 50px; height: 50px; border-radius: 50%; background: rgba(255, 255, 255, 0.05); 
                border: 1px solid rgba(0, 245, 255, 0.3); color: #FFFFFF; display: flex; align-items: center; 
                justify-content: center; font-size: 1.4rem; text-decoration: none; transition: all 0.4s ease; 
            }
            .social-btn:hover { transform: translateY(-5px); border-color: #00F5FF; box-shadow: 0 0 15px rgba(0, 245, 255, 0.5); background: rgba(0, 245, 255, 0.1); }
        </style>
    </head>
    <body>
        <div class="hero">
            <div class="hero-content" id="hero-tilt">
                <div class="greeting">// Welcome to my Portfolio</div>
                <h1 class="name">Jaydeep Rajaram Sutar</h1>
                <div class="typed-container">
                    <span class="typed-text" id="typed"></span><span class="cursor"></span>
                </div>
                <p class="description">I transform raw data into meaningful insights, interactive dashboards, and predictive models.</p>
                <div class="buttons">
                    <a href="#projects" class="btn btn-primary">🚀 View Projects</a>
                    <a href="#contact" class="btn btn-secondary">💬 Contact Me</a>
                </div>
                <div class="social-links">
                    <a href="https://www.linkedin.com/in/jaydeep-sutar-414j1307/" target="_blank" class="social-btn"><i class="fab fa-linkedin-in"></i></a>
                    <a href="https://github.com/JAYDEEP414" target="_blank" class="social-btn"><i class="fab fa-github"></i></a>
                    <a href="mailto:jaydeepsutar001@gmail.com" class="social-btn"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
        </div>
        <script>
            // Gentle 3D tilt on the hero block itself, following the cursor
            const heroTilt = document.getElementById('hero-tilt');
            document.addEventListener('mousemove', (e) => {
                const rx = ((e.clientY / window.innerHeight) - 0.5) * -6;
                const ry = ((e.clientX / window.innerWidth) - 0.5) * 6;
                heroTilt.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
            });

            const titles = ["Data Analyst", "Python Developer", "SQL Specialist"];
            let tIdx = 0, cIdx = 0, isDel = false;
            function type() {
                const full = titles[tIdx];
                document.getElementById('typed').textContent = isDel ? full.substring(0, cIdx-1) : full.substring(0, cIdx+1);
                cIdx = isDel ? cIdx - 1 : cIdx + 1;
                let speed = isDel ? 50 : 100;
                if(!isDel && cIdx === full.length) { speed = 2000; isDel = true; }
                else if(isDel && cIdx === 0) { isDel = false; tIdx = (tIdx + 1) % titles.length; speed = 500; }
                setTimeout(type, speed);
            }
            type();
        </script>
    </body>
    </html>
    """, height=800, scrolling=False)

# ==================== ABOUT SECTION ====================
def about_section():
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Get to know me</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="about-card">
            <p style="margin-bottom: 1.5rem;">
                👋 Hello! I'm <span style="color: #00F5FF; font-weight: 600;">Jaydeep Rajaram Sutar</span>, 
                a passionate Data Analyst and Computer Science student based in Pune, Maharashtra.
            </p>
            <p style="margin-bottom: 1.5rem;">
                I specialize in <span style="color: #38BDF8;">Python, SQL, Power BI, Excel, and Machine Learning</span>. 
                I enjoy transforming raw data into actionable insights and building interactive dashboards 
                that support data-driven decision-making.
            </p>
            <p>
                I have completed <span style="color: #7C3AED; font-weight: 600;">two data analytics internships</span> 
                and worked on real-world projects involving data cleaning, exploratory data analysis, SQL querying, 
                Power BI dashboards, and predictive modeling.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div class="stat-box">
                <div class="stat-number">2+</div>
                <div class="stat-label">Internships</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">5+</div>
                <div class="stat-label">Projects</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100K+</div>
                <div class="stat-label">Records Analyzed</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">20%</div>
                <div class="stat-label">Data Quality ↑</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== SKILLS SECTION ====================
def skills_section():
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// My Tech Stack</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Skills & Expertise</h2>', unsafe_allow_html=True)
    
    skills_data = [
        {"icon": "📊", "title": "Data Analysis", "skills": ["Excel", "SQL", "Python", "Power BI"]},
        {"icon": "📈", "title": "Data Visualization", "skills": ["Power BI", "Plotly", "Matplotlib", "Seaborn"]},
        {"icon": "💻", "title": "Programming", "skills": ["Python", "SQL", "DAX"]},
        {"icon": "🐍", "title": "Python Libraries", "skills": ["Pandas", "NumPy", "Scikit-learn"]},
        {"icon": "🗄️", "title": "Databases", "skills": ["MySQL", "PostgreSQL"]},
        {"icon": "🔧", "title": "Tools & IDEs", "skills": ["Git", "GitHub", "Jupyter", "VS Code"]},
    ]
    
    cols = st.columns(3)
    for idx, skill in enumerate(skills_data):
        with cols[idx % 3]:
            badges_html = "".join([f'<span class="skill-badge">{s}</span>' for s in skill["skills"]])
            st.markdown(f"""
            <div class="skill-category">
                <div style="text-align: center; font-size: 3rem; margin-bottom: 1rem;">{skill["icon"]}</div>
                <div class="skill-category-title">{skill["title"]}</div>
                <div style="text-align: center;">{badges_html}</div>
            </div>
            <div style="height: 1.5rem;"></div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== EXPERIENCE SECTION ====================
def experience_section():
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Professional Journey</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="timeline-card">
        <div class="timeline-date">📅 JAN 2025 – FEB 2025</div>
        <div class="timeline-title">Data Analytics Trainee Intern</div>
        <div class="timeline-company">🏢 MedTourEasy</div>
        <ul class="timeline-list">
            <li>Analyzed lifespan differences between left- and right-handed individuals</li>
            <li>Cleaned and processed <strong style="color:#00F5FF;">10,000+ records</strong> for accurate analysis</li>
            <li>Improved data accuracy by approximately <strong style="color:#00F5FF;">20%</strong></li>
            <li>Performed exploratory data analysis and statistical visualization</li>
            <li>Found approximately <strong style="color:#38BDF8;">9% higher average lifespan</strong> in right-handed individuals</li>
            <li>Delivered a comprehensive data-driven report under mentor guidance</li>
        </ul>
    </div>
    
    <div class="timeline-card">
        <div class="timeline-date">📅 AUG 2024 – JAN 2025</div>
        <div class="timeline-title">Data Analyst Intern</div>
        <div class="timeline-company">🏢 Sanity Technologies Pvt Ltd</div>
        <ul class="timeline-list">
            <li>Assisted in data extraction, cleaning, and preprocessing pipelines</li>
            <li>Performed ad-hoc analysis using complex <strong style="color:#00F5FF;">SQL queries</strong></li>
            <li>Built strong skills in <strong style="color:#38BDF8;">Power BI, SQL, and Excel</strong></li>
            <li>Generated actionable business insights from real-world datasets</li>
            <li>Collaborated with cross-functional teams on data initiatives</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== PROJECTS SECTION ====================
def projects_section():
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Featured Work</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "icon": "🚦",
            "title": "City Traffic Violation Analytics",
            "description": "Comprehensive Power BI dashboard analyzing traffic violations across Indian cities. Identified peak violation hours, fine trends, and patterns to support traffic management decisions.",
            "tech": ["Power BI", "SQL", "Excel", "DAX"]
        },
        {
            "icon": "🚗",
            "title": "Ride Booking Analytics Dashboard",
            "description": "Interactive Power BI dashboard tracking bookings, revenue, cancellations, and customer ratings. Built with advanced DAX measures, dynamic slicers, and KPI cards.",
            "tech": ["Power BI", "DAX", "Excel"]
        },
        {
            "icon": "🗃️",
            "title": "Ride Booking Data Analysis (SQL)",
            "description": "Deep analysis of 100K+ ride booking records using MySQL. Extracted customer behavior patterns, revenue insights, and operational metrics through complex queries.",
            "tech": ["MySQL", "SQL", "Data Analysis"]
        },
        {
            "icon": "❤️",
            "title": "Heart Disease Risk Analysis",
            "description": "Interactive Power BI dashboard analyzing heart disease risk factors across patient demographics. Identified age cholesterol smoking diabetes and lifestyle patterns to support healthcare.",
            "tech": ["Python", "Jupyter Notebook", "Power BI", "DAX"]
        },
        {
            "icon": "🛒",
            "title": "E-Commerce Sales Analytics",
            "description": "Comprehensive Power BI dashboard analyzing e-commerce sales profit discounts and customer purchasing trends. Identified top-performing products.",
            "tech": ["Python", "Jupyter Notebook", "Power BI", "DAX"]
        },
    ]
    
    cols = st.columns(3)
    for idx, project in enumerate(projects):
        with cols[idx % 3]:
            tech_badges = "".join([f'<span class="tech-badge">{t}</span>' for t in project["tech"]])
            st.markdown(f"""
            <div class="project-card">
                <span class="project-icon">{project["icon"]}</span>
                <div class="project-title">{project["title"]}</div>
                <p class="project-description">{project["description"]}</p>
                <div style="margin-bottom: 1.5rem;">{tech_badges}</div>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
                    <a href="https://github.com/JAYDEEP414" target="_blank" 
                       style="text-decoration: none; padding: 0.5rem 1rem; background: rgba(0, 245, 255, 0.1); 
                       border: 1px solid #00F5FF; border-radius: 25px; color: #00F5FF; font-size: 0.85rem; font-weight: 600;">
                        ⚡ GitHub
                    </a>
                    <a href="https://app.powerbi.com/groups/me/list?experience=power-bi" style="text-decoration: none; padding: 0.5rem 1rem; background: rgba(124, 58, 237, 0.1); 
                       border: 1px solid #7C3AED; border-radius: 25px; color: #C4B5FD; font-size: 0.85rem; font-weight: 600;">
                        🔗 Live Demo
                    </a>
                </div>
            </div>
            <div style="height: 1.5rem;"></div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== ANALYTICS DASHBOARD SECTION ====================
def analytics_section():
    st.markdown('<div id="analytics"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Live Analytics</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Skills Dashboard</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar Chart - Skill Proficiency
        categories = ['Python', 'SQL', 'Power BI', 'Excel', 'Machine Learning', 'Data Viz']
        values = [90, 92, 88, 95, 75, 85]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(0, 245, 255, 0.2)',
            line=dict(color='#00F5FF', width=3),
            marker=dict(size=10, color='#7C3AED'),
            name='Proficiency'
        ))
        fig_radar.update_layout(
            polar=dict(
                bgcolor='rgba(0,0,0,0)',
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor='rgba(0, 245, 255, 0.2)',
                    color='white'
                ),
                angularaxis=dict(
                    gridcolor='rgba(0, 245, 255, 0.2)',
                    color='white'
                )
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', family='Poppins'),
            title=dict(text='<b>Skill Proficiency Radar</b>', font=dict(size=18, color='#00F5FF')),
            height=400
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with col2:
        # Pie Chart - Technology Usage
        labels = ['Python', 'SQL', 'Power BI', 'Excel', 'ML/AI']
        values_pie = [30, 25, 20, 15, 10]
        colors = ['#00F5FF', '#7C3AED', '#38BDF8', '#A78BFA', '#22D3EE']
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=labels,
            values=values_pie,
            hole=0.5,
            marker=dict(colors=colors, line=dict(color='#050816', width=2)),
            textfont=dict(color='white', family='Poppins', size=13),
            textinfo='label+percent'
        )])
        fig_pie.update_layout(
            showlegend=True,
            legend=dict(font=dict(color='white', family='Poppins')),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title=dict(text='<b>Technology Usage Distribution</b>', font=dict(size=18, color='#00F5FF')),
            height=400,
            annotations=[dict(text='Tech<br>Stack', x=0.5, y=0.5, font_size=18, showarrow=False, font_color='#00F5FF')]
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Bar Chart - Project Completion
        projects_names = ['Traffic Analytics', 'Ride Booking BI', 'Ride Booking SQL', 'Healthcare', 'Resume Builder']
        completion = [100, 100, 100, 95, 100]
        
        fig_bar = go.Figure(data=[go.Bar(
            x=projects_names,
            y=completion,
            marker=dict(
                color=completion,
                colorscale=[[0, '#7C3AED'], [1, '#00F5FF']],
                line=dict(color='#00F5FF', width=1)
            ),
            text=completion,
            textposition='outside',
            textfont=dict(color='#00F5FF', family='Orbitron', size=14)
        )])
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', family='Poppins'),
            title=dict(text='<b>Project Completion Rate (%)</b>', font=dict(size=18, color='#00F5FF')),
            xaxis=dict(gridcolor='rgba(0, 245, 255, 0.1)', color='white'),
            yaxis=dict(gridcolor='rgba(0, 245, 255, 0.1)', color='white', range=[0, 110]),
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col4:
        # Timeline - Internship Experience
        timeline_data = pd.DataFrame([
            dict(Task="Sanity Technologies", Start='2024-08-01', Finish='2025-01-31', Resource="Data Analyst Intern"),
            dict(Task="MedTourEasy", Start='2025-01-15', Finish='2025-02-28', Resource="Data Analytics Trainee"),
        ])
        
        fig_timeline = px.timeline(
            timeline_data, 
            x_start="Start", 
            x_end="Finish", 
            y="Task",
            color="Resource",
            color_discrete_sequence=['#00F5FF', '#7C3AED']
        )
        fig_timeline.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', family='Poppins'),
            title=dict(text='<b>Internship Timeline</b>', font=dict(size=18, color='#00F5FF')),
            xaxis=dict(gridcolor='rgba(0, 245, 255, 0.1)', color='white'),
            yaxis=dict(gridcolor='rgba(0, 245, 255, 0.1)', color='white'),
            height=400,
            legend=dict(font=dict(color='white'))
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== ACHIEVEMENTS SECTION ====================
def achievements_section():
    st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Milestones</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Achievements</h2>', unsafe_allow_html=True)
    
    achievements = [
        {"icon": "🎯", "text": "Completed two data analytics internships"},
        {"icon": "💎", "text": "Processed and analyzed 100K+ records using SQL"},
        {"icon": "📊", "text": "Built multiple interactive Power BI dashboards"},
        {"icon": "🚀", "text": "Improved data quality by approximately 20%"},
        {"icon": "🏆", "text": "Delivered mentor-reviewed analytical reports"},
        {"icon": "🎓", "text": "Pursuing B.Sc. Computer Science at SPPU"},
    ]
    
    cols = st.columns(3)
    for idx, ach in enumerate(achievements):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="achievement-card">
                <div class="achievement-icon">{ach["icon"]}</div>
                <div class="achievement-text">{ach["text"]}</div>
            </div>
            <div style="height: 1.5rem;"></div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== EDUCATION SECTION ====================
def education_section():
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Academic Background</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="timeline-card">
            <div class="timeline-date">🎓 PRESENT (Final Year)</div>
            <div class="timeline-title">Bachelor of Science in Computer Science</div>
            <div class="timeline-company">📍 Savitribai Phule Pune University, Pune</div>
            <p style="color: rgba(255,255,255,0.8); margin-top: 1rem; line-height: 1.7;">
                Pursuing a comprehensive computer science degree with focus on:
            </p>
            <ul class="timeline-list" style="margin-top: 0.5rem;">
                <li>Data Analysis & Statistics</li>
                <li>Power BI & Business Intelligence</li>
                <li>Database Management Systems</li>
                <li>Python Programming & Algorithms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="timeline-card">
            <div class="timeline-date">📜 CERTIFICATIONS</div>
            <div class="timeline-title">Professional Certifications</div>
            <div class="timeline-company">🌟 Industry Recognized</div>
            <ul class="timeline-list" style="margin-top: 1rem;">
                <li><strong style="color:#00F5FF;">Certified Power BI Analyst</strong>
                    <br><span style="font-size:0.9rem; opacity:0.7;">Business intelligence & dashboard development</span>
                </li>
                <br>
                <li><strong style="color:#00F5FF;">Data Analyst Certification</strong>
                    <br><span style="font-size:0.9rem; opacity:0.7;">End-to-end data analysis & visualization</span>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== RESUME SECTION ====================
def resume_section():
    st.markdown('<div id="resume"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// My Credentials</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Resume</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem 2rem;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">📄</div>
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00F5FF; margin-bottom: 1rem; font-size: 1.5rem;">
                Jaydeep_Sutar_Resume.pdf
            </h3>
            <p style="color: rgba(255,255,255,0.7); margin-bottom: 2rem; line-height: 1.7;">
                Download my complete resume to learn more about my experience, education, projects, and technical skills as a Data Analyst.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <a href="mailto:jaydeepsutar001@gmail.com?subject=Resume Request" 
                   style="text-decoration: none; padding: 0.9rem 2rem; background: linear-gradient(135deg, #00F5FF, #7C3AED); 
                          color: white; border-radius: 50px; font-weight: 600; box-shadow: 0 10px 30px rgba(0, 245, 255, 0.3);">
                    📥 Request Resume
                </a>
                <a href="https://www.linkedin.com/in/jaydeep-sutar-414j1307/" target="_blank"
                   style="text-decoration: none; padding: 0.9rem 2rem; background: rgba(255,255,255,0.05); 
                          color: white; border-radius: 50px; font-weight: 600; border: 2px solid rgba(0, 245, 255, 0.5);">
                    👤 View LinkedIn
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== CONTACT SECTION ====================

def contact_section():
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">// Let\'s Connect</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Get In Touch</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])

    # ================= LEFT COLUMN =================
    with col1:
        st.markdown("""
        <div class="contact-info-card">
            <div class="contact-icon">📍</div>
            <div>
                <div class="contact-info-label">Location</div>
                <div class="contact-info-value">Pune, Maharashtra, India</div>
            </div>
        </div>

        <div class="contact-info-card">
            <div class="contact-icon">📧</div>
            <div>
                <div class="contact-info-label">Email</div>
                <div class="contact-info-value">jaydeepsutar001@gmail.com</div>
            </div>
        </div>

        <div class="contact-info-card">
            <div class="contact-icon">📱</div>
            <div>
                <div class="contact-info-label">Phone</div>
                <div class="contact-info-value">+91 9022869184</div>
            </div>
        </div>

        <div class="contact-info-card">
            <div class="contact-icon">🌐</div>
            <div>
                <div class="contact-info-label">Social</div>
                <div class="contact-info-value">
                    <a href="https://github.com/JAYDEEP414" target="_blank"
                       style="color:#00F5FF; text-decoration:none; margin-right:1rem;">
                       GitHub
                    </a>
                    <a href="https://www.linkedin.com/in/jaydeep-sutar-414j1307/" target="_blank"
                       style="color:#00F5FF; text-decoration:none;">
                       LinkedIn
                    </a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ================= RIGHT COLUMN =================
    with col2:
        # Open card container
        st.markdown("""
        <div class="glass-card">
            <h3 style="
                font-family: 'Orbitron', sans-serif;
                color: #00F5FF;
                margin-bottom: 1.5rem;
                font-size: 1.3rem;">
                💬 Send a Message
            </h3>
        """, unsafe_allow_html=True)

        # Streamlit form MUST stay inside the same column
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("👤 Your Name", placeholder="John Doe")
            email = st.text_input("📧 Your Email", placeholder="john@example.com")
            subject = st.text_input("📝 Subject", placeholder="Job Opportunity")
            message = st.text_area(
                "💭 Your Message",
                placeholder="Hi Jaydeep, I'd like to discuss...",
                height=120
            )

            submit = st.form_submit_button("🚀 Send Message")

            if submit:
                if name and email and message:
                    try:
                        import smtplib
                        from email.mime.text import MIMEText
                        from email.mime.multipart import MIMEMultipart

                        # Gmail settings
                        sender_email = "jaydeepsutar001@gmail.com"
                        app_password = "jjojfhloqbomuiqp"

                        # Create email
                        msg = MIMEMultipart()
                        msg["From"] = sender_email
                        msg["To"] = sender_email
                        msg["Subject"] = (
                            f"Portfolio Contact Form: "
                            f"{subject if subject else 'New Message'}"
                        )

                        body = f"""
New message from your portfolio website

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

                        msg.attach(MIMEText(body, "plain"))

                        # Send email
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender_email, app_password)
                        server.send_message(msg)
                        server.quit()

                        st.success(
                            "✅ Message sent successfully! "
                            "I will get back to you soon."
                        )

                    except Exception as e:
                        st.error(f"❌ Failed to send message: {e}")
                else:
                    st.error("⚠️ Please fill out all required fields.")

        # Close card container AFTER the form
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==================== FOOTER ====================
def footer():
    st.markdown("""
    <div class="footer">
        <div style="font-family: 'Orbitron', sans-serif; color: #00F5FF; font-size: 1.2rem; margin-bottom: 0.5rem; font-weight: 700;">
            JAYDEEP RAJARAM SUTAR
        </div>
        <p style="margin-bottom: 1rem;">Data Analyst | Python Developer | SQL Specialist</p>
        <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1.5rem; flex-wrap: wrap;">
            <a href="https://github.com/JAYDEEP414" target="_blank" style="color: #00F5FF; text-decoration: none;">GitHub</a>
            <a href="https://www.linkedin.com/in/jaydeep-sutar-414j1307/" target="_blank" style="color: #00F5FF; text-decoration: none;">LinkedIn</a>
            <a href="mailto:jaydeepsutar001@gmail.com" style="color: #00F5FF; text-decoration: none;">Email</a>
        </div>
        <p style="opacity: 0.6; font-size: 0.9rem;">
            © 2025 Jaydeep Sutar. Designed with <span class="footer-heart">♥</span> using Python, Streamlit & Three.js
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== NAVIGATION ====================
def navigation():
    st.markdown("""
    <div class="navbar">
        <div class="navbar-logo">⚡ JAY's.ANALYTICS</div>
        <div class="navbar-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#experience">Experience</a>
            <a href="#projects">Projects</a>
            <a href="#analytics">Analytics</a>
            <a href="#education">Education</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    <div style="height: 70px;"></div>
    """, unsafe_allow_html=True)

# ==================== MAIN APP ====================
def main():
    load_css()
    three_js_background()   # full-page, scroll-reactive 3D background (data bars, trend line, grid, globes)
    inject_tilt_effect()    # real-time 3D tilt on cards as you move the mouse
    navigation()
    hero_section()
    about_section()
    skills_section()
    experience_section()
    projects_section()
    analytics_section()
    achievements_section()
    education_section()
    resume_section()
    contact_section()
    footer()

if __name__ == "__main__":
    main()
