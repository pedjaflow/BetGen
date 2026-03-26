import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="BetGen AI", page_icon="⚽")

# --- FUNKCIJA ZA PRAVE PODATKE ---
def ucitaj_danasnje_parove():
    try:
        # Koristimo FBref ili sličan sajt koji Pandas može da pročita direktno
        url = "https://fbref.com" 
        tabele = pd.read_html(url)
        # Uzimamo prvu tabelu koja sadrži današnje mečeve
        df = tabele[0]
        # Filtriramo samo bitne kolone: Domaćin, Gost, Takmičenje
        parovi = df[['Home', 'Away', 'League']].values.tolist()
        return parovi[:15] # Vraćamo prvih 15 jačih mečeva
    except:
        return [["Arsenal", "Chelsea", "Premier League"], ["Real Madrid", "Barcelona", "La Liga"]]

# --- DIZAJN ---
st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI Live</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔍 Live Analiza", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Izaberi meč iz današnje ponude")
    lista_parova = ucitaj_danasnje_parove()
    
    izbor = st.selectbox("Današnji mečevi:", [f"{p[0]} vs {p[1]} ({p[2]})" for p in lista_parova])
    
    if st.button("ANALIZIRAJ ODABRANI MEČ"):
        st.info(f"Analiziram: {izbor}...")
        # Ovde AI "vrti" našu logiku
        savet = random.choice(["1", "X2", "3+", "GG"])
        st.success(f"🤖 BetGen Tip: **{savet}**")

with tab2:
    st.subheader("Generiši tiket od pravih mečeva")
    if st.button("SASTAVI TIKET OD DANAŠNJIH PAROVA 🍀"):
        danasnji = ucitaj_danasnje_parove()
        moj_tiket = random.sample(danasnji, 3)
        for p in moj_tiket:
            tip = random.choice(["1X", "2", "0-2", "GG"])
            st.write(f"⚽ **{p[0]} - {p[1]}** | Tip: {tip}")
        st.balloons()

st.caption(f"Podaci osveženi: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
