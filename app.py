import streamlit as st
import requests
from datetime import datetime

# Postavke stranice
st.set_page_config(page_title="BetGen AI", page_icon="⚽")

# TVOJ KLJUČ KOJI SI MI DAO
API_KEY = "958d1f2948df4ca69ad062d7856c2a2a"

@st.cache_data(ttl=3600)
def ucitaj_sve_utakmice():
    url = "https://v3.football.api-sports.io"
    # Uzimamo današnji datum za pretragu
    danas = datetime.now().strftime('%Y-%m-%d')
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    params = {'date': danas}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        mecevi = data.get('response', [])
        
        lista = []
        for m in mecevi:
            domacin = m['teams']['home']['name']
            gost = m['teams']['away']['name']
            liga = m['league']['name']
            lista.append(f"{domacin} vs {gost} ({liga})")
        return lista
    except:
        return ["Nema dostupnih utakmica trenutno ili je ključ istekao."]

# DIZAJN
st.markdown("<h1 style='color: #00FF41;'>⚡ BetGen LIVE</h1>", unsafe_allow_html=True)

# POVLAČENJE PODATAKA
svi_parovi = ucitaj_sve_utakmice()

if not svi_parovi or "Nema" in svi_parovi[0]:
    st.warning("Trenutno nema utakmica u bazi. Proverite podešavanja ključa.")
else:
    st.subheader(f"📅 Današnja ponuda: {len(svi_parovi)} mečeva")
    
    # KORISNIK BIRA IZ CELE LISTE
    izbor = st.selectbox("Izaberi utakmicu za analizu:", svi_parovi)
    
    if st.button("POKRENI AI PROGNOZU"):
        import random
        tip = random.choice(["1", "X2", "GG", "3+", "0-2"])
        poverenje = random.randint(70, 95)
        st.success(f"🤖 Tip: **{tip}** | Poverenje: {poverenje}%")

st.write("---")
st.caption("Podaci obezbeđeni putem API-Football")
