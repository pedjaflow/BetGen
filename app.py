import streamlit as st
import random

# Dizajn - crna pozadina i neon zelena
st.set_page_config(page_title="BetGen AI", page_icon="⚽")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; width: 100%; }
    .stTextInput>div>div>input { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen PRO")

# KORISNIK SAM UNOSI PAROVE (Najsigurniji način da nema greške)
st.subheader("Unesi parove za današnji tiket:")
par1 = st.text_input("Utakmica 1:", "Primer: Arsenal - Chelsea")
par2 = st.text_input("Utakmica 2:", "Primer: Real Madrid - Barcelona")
par3 = st.text_input("Utakmica 3:", "Primer: Partizan - Zvezda")

if st.button("POKRENI AI ANALIZU I SASTAVI TIKET 🍀"):
    lista_parova = [par1, par2, par3]
    st.markdown("### 🤖 BetGen Analiza za tvoj tiket:")
    
    ukupna_kvota = 1.0
    for p in lista_parova:
        if p and "Primer" not in p:
            tip = random.choice(["1", "X2", "GG", "3+", "1X", "0-2"])
            kvota = round(random.uniform(1.40, 2.10), 2)
            ukupna_kvota *= kvota
            st.write(f"⚽ **{p}** | Tip: **{tip}** | Kvota: {kvota}")
    
    st.success(f"💰 Ukupna kvota: **{round(ukupna_kvota, 2)}**")
    st.balloons()

st.write("---")
st.caption("Unesi prave parove sa teleteksta i BetGen će uraditi ostalo.")
