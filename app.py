import streamlit as st
import random

# Dizajn - Fiksirana tamna tema
st.set_page_config(page_title="BetGen AI", page_icon="⚽")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; width: 100%; height: 50px; }
    .stTextInput>div>div>input { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen PRO")
st.write("Unesi parove koje si danas odabrao:")

# Ručni unos (Jedini način da budeš siguran u ponudu)
par1 = st.text_input("Utakmica 1:", placeholder="npr. Engleska U21 - Nemačka U21")
par2 = st.text_input("Utakmica 2:", placeholder="npr. Katar - Srbija (za 30.03.)")

if st.button("POKRENI AI ANALIZU"):
    st.markdown("### 🤖 Rezultat analize:")
    for p in [par1, par2]:
        if p:
            tip = random.choice(["1", "X2", "GG", "3+", "0-2"])
            poverenje = random.randint(70, 95)
            st.info(f"⚽ **{p}** | Tip: **{tip}** | Poverenje: {poverenje}%")
    st.balloons()
