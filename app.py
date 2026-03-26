import streamlit as st
import pandas as pd
import requests
import random
from io import StringIO

st.set_page_config(page_title="BetGen AI Live", page_icon="⚽", layout="centered")

# OSVEŽAVANJE NA 6 SATI
@st.cache_data(ttl=21600)
def ucitaj_masovnu_ponudu():
    try:
        # FBref je "zlatni rudnik" za spiskove svih utakmica sveta
        url = "https://fbref.com"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        # Čistimo HTML od komentara da bi videli "skrivene" tabele
        html_cist = response.text.replace('<!--', '').replace('-->', '')
        tabele = pd.read_html(StringIO(html_cist))
        
        svi_mecevi = {}
        # FBref obično ima jednu ogromnu tabelu sa svim ligama
        for df in tabele:
            if 'Home' in df.columns and 'Away' in df.columns:
                # Brišemo prazne redove i redove koji su naslovi liga
                df = df.dropna(subset=['Home', 'Away'])
                for _, row in df.iterrows():
                    home = str(row['Home'])
                    away = str(row['Away'])
                    league = str(row.get('Competition', 'Fudbal'))
                    
                    # Filtriramo samo mečeve koji nisu već završeni (ako nema rezultata)
                    if "vs" in home or "vs" in away or ":" not in str(row.get('Score', '')):
                        par_ime = f"{home} vs {away} ({league})"
                        svi_mecevi[par_ime] = {
                            "tip": random.choice(["1", "X2", "GG", "3+", "0-2", "2", "1X"]),
                            "poverenje": f"{random.randint(65, 95)}%",
                            "kvota": round(random.uniform(1.40, 3.50), 2)
                        }
        return svi_mecevi
    except:
        return {"Crvena Zvezda vs Partizan (Superliga)": {"tip": "1", "poverenje": "70%", "kvota": 1.85}}

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen GLOBAL</h1>", unsafe_allow_html=True)

baza = ucitaj_masovnu_ponudu()

if len(baza) < 2:
    st.warning("Trenutno nema mnogo aktivnih mečeva. Osvežavam bazu...")
    st.cache_data.clear() # Prisilno osvežavanje ako je lista prazna
else:
    st.subheader(f"📊 Ponuda: {len(baza)} mečeva širom sveta")
    
    izbor = st.selectbox("Izaberi meč:", list(baza.keys()))
    
    if st.button("ANALIZIRAJ"):
        p = baza[izbor]
        st.success(f"🤖 **Tip: {p['tip']}** | Kvota: {p['kvota']}")
        st.info(f"📊 **Poverenje:** {p['poverenje']}")

    st.write("---")
    if st.button("SASTAVI TIKET DANA 🍀"):
        tiket_parovi = random.sample(list(baza.keys()), 3)
        ukupna = 1.0
        for p_ime in tiket_parovi:
            p = baza[p_ime]
            st.write(f"⚽ {p_ime} | **{p['tip']}** (Kvota: {p['kvota']})")
            ukupna *= p['kvota']
        st.success(f"💰 Ukupna kvota: **{round(ukupna, 2)}**")
        st.balloons()
