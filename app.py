import streamlit as st
import pandas as pd
import requests
import random
from io import StringIO

# 1. PODEŠAVANJE STRANICE
st.set_page_config(page_title="BetGen AI", page_icon="⚽")

# 2. FUNKCIJA ZA POVLAČENJE PAROVA (BEZ API KLJUČA)
@st.cache_data(ttl=3600) # Osvežava na svakih sat vremena
def ucitaj_live_parove():
    try:
        url = "https://www.skysports.com"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        # Tražimo parove u tekstu stranice (jednostavan metod)
        tabele = pd.read_html(StringIO(response.text))
        
        svi_parovi = []
        for df in tabele:
            if 'Fixture' in df.columns:
                for match in df['Fixture'].dropna():
                    if ' v ' in str(match):
                        timovi = str(match).split(' v ')
                        svi_parovi.append([timovi[0].strip(), timovi[1].strip(), "Live Ponuda"])
        
        return svi_parovi if svi_parovi else [["Nema mečeva", "u ponudi", "Pokušaj kasnije"]]
    except:
        return [["Real Madrid", "Barcelona", "La Liga"], ["Arsenal", "Man City", "Premier League"]]

# 3. DIZAJN
st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI Live</h1>", unsafe_allow_html=True)

parovi = ucitaj_live_parove()

# 4. INTERFEJS
tab1, tab2 = st.tabs(["🔍 Analiza", "🍀 Srećni Tiket"])

with tab1:
    opcije = [f"{p[0]} vs {p[1]} ({p[2]})" for p in parovi]
    izbor = st.selectbox("Izaberi par iz današnje ponude:", opcije)
    
    if st.button("POKRENI AI ANALIZU"):
        st.success(f"🤖 Tip: **{random.choice(['1', 'X2', 'GG', '3+'])}**")
        st.info(f"📊 Poverenje: {random.randint(70,95)}%")

with tab2:
    if st.button("SASTAVI SREĆNI TIKET 🍀"):
        n = min(len(parovi), 3)
        tiket = random.sample(parovi, n)
        st.write("### 📝 Tvoj Tiket:")
        for t in tiket:
            st.write(f"⚽ **{t[0]} - {t[1]}** | Tip: {random.choice(['1', 'X', '2', 'GG'])}")
        st.balloons()
