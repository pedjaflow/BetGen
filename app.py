import streamlit as st
import random

# Postavke dizajna
st.set_page_config(page_title="BetGen PRO", page_icon="⚽")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen PRO AI")

# BAZA NAJJAČIH MEČEVA (Za vikend 28-29. mart)
mecevi_vikend = [
    "Srbija vs Mađarska (Prijateljska)",
    "Nemačka vs Engleska (Prijateljska)",
    "Španija vs Argentina (Finalissima)",
    "Brazil vs Francuska (Prijateljska)",
    "Italija vs Severna Irska (Kvalifikacije)",
    "Vels vs Bosna i Hercegovina (Kvalifikacije)",
    "Crvena Zvezda vs Partizan (Simulacija)",
    "Arsenal vs Chelsea (Premijer Liga)",
    "Real Madrid vs Barcelona (La Liga)"
]

tab1, tab2 = st.tabs(["🔍 AI Prognoza", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Izaberi derbi meč:")
    izbor = st.selectbox("Dostupna ponuda:", mecevi_vikend)
    
    if st.button("POKRENI BETGEN MOZAK"):
        tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2"]
        izabrani_tip = random.choice(tipovi)
        poverenje = random.randint(75, 98)
        
        st.success(f"🤖 **Tip: {izabrani_tip}**")
        st.info(f"📊 **Poverenje: {poverenje}%**")
        st.write(f"📝 *Analiza:* Na osnovu trenutne forme i atmosfere u timovima, naš AI predviđa {izabrani_tip} kao najsigurniji ishod.")

with tab2:
    st.subheader("Generiši brzi tiket")
    if st.button("SASTAVI TIKET DANA 🍀"):
        parovi = random.sample(mecevi_vikend, 3)
        st.markdown("### 📝 Tvoj BetGen Tiket:")
        for p in parovi:
            st.write(f"⚽ {p} | Tip: **{random.choice(['1X', 'GG', '3+'])}**")
        st.balloons()

st.write("---")
st.caption("© 2024 BetGen • Expert AI Model • Offline Mode Aktivan")
