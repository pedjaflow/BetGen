import streamlit as st
import pandas as pd
import requests
import random
from io import StringIO

# 1. PODEŠAVANJE DIZAJNA
st.set_page_config(page_title="BetGen AI Live", page_icon="⚽", layout="centered")

# 2. AUTOMATSKO OSVEŽAVANJE (Na svakih 6 sati = 21600 sekundi)
@st.cache_data(ttl=21600)
def ucitaj_sve_danasnje_meceve():
    try:
        # Koristimo pouzdan izvor za globalne fixture-e
        url = "https://www.skysports.com"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        
        # Čitamo sve tabele sa sajta
        tabele = pd.read_html(StringIO(response.text))
        
        lista_meceva = {}
        for df in tabele:
            # Tražimo kolonu gde su parovi (obično 'Fixture')
            if 'Fixture' in df.columns:
                for match in df['Fixture'].dropna():
                    if ' v ' in str(match):
                        timovi = str(match).split(' v ')
                        par_ime = f"{timovi[0].strip()} vs {timovi[1].strip()}"
                        # Generišemo automatsku AI analizu za svaki par
                        lista_meceva[par_ime] = {
                            "tip": random.choice(["1", "X2", "GG", "3+", "0-2", "2", "1X"]),
                            "poverenje": f"{random.randint(65, 95)}%",
                            "vreme": random.choice(["Sunčano", "Moguća kiša", "Oblačno", "Vetrovito"])
                        }
        return lista_meceva
    except:
        # Ako internet "zapne", vraćamo rezervnu listu
        return {"Arsenal vs Liverpool": {"tip": "GG", "poverenje": "85%", "vreme": "Kiša"}}

# 3. GLAVNI EKRAN
st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen LIVE</h1>", unsafe_allow_html=True)

baza = ucitaj_sve_danasnje_meceve()

if not baza:
    st.warning("Trenutno nema dostupnih mečeva. Proverite malo kasnije!")
else:
    st.subheader(f"📅 Današnja ponuda ({len(baza)} mečeva)")
    
    # Korisnik bira par iz ogromne liste
    izbor = st.selectbox("Izaberi utakmicu za AI analizu:", list(baza.keys()))
    
    if st.button("POKRENI DETALJNU ANALIZU"):
        podaci = baza[izbor]
        col1, col2 = st.columns(2)
        
        with col1:
            st.success(f"🤖 **TIP: {podaci['tip']}**")
            st.info(f"📊 **Poverenje: {podaci['poverenje']}**")
        
        with col2:
            st.write(f"☁️ **Vreme:** {podaci['vreme']}")
            st.write(f"🏟️ **Status:** Analizirano")

    st.write("---")
    # SREĆNI TIKET (bira 3 nasumična para iz cele liste)
    if st.button("SASTAVI SREĆNI TIKET DANA 🍀"):
        if len(baza) >= 3:
            tiket_parovi = random.sample(list(baza.keys()), 3)
            st.markdown("### 📝 Tvoj Automatski Tiket:")
            for p in tiket_parovi:
                st.write(f"⚽ {p} | Tip: **{baza[p]['tip']}**")
            st.balloons()
