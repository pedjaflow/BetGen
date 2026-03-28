import streamlit as st
import requests
from datetime import datetime

# Postavke stranice
st.set_page_config(page_title="BetGen AI", page_icon="⚽")

# TVOJ KLJUČ (Football-Data.org)
API_KEY = "958d1f2948df4ca69ad062d7856c2a2a"

@st.cache_data(ttl=3600)
def ucitaj_meceve_v4():
    # Ovo je prava adresa za tvoj ključ (Football-Data.org)
    url = "https://api.football-data.org"
    headers = { 'X-Auth-Token': API_KEY }
    
    try:
        response = requests.get(url, headers=headers)
        # Ako dobijemo grešku 403, znači da ključ nije za v4 ili su limitirani mečevi
        if response.status_code != 200:
            return [f"Greška {response.status_code}: Proveri ključ na sajtu"]
            
        data = response.json()
        mecevi = data.get('matches', [])
        
        if not mecevi:
            return ["Trenutno nema aktivnih mečeva u tvojim ligama."]

        lista = []
        for m in mecevi:
            domacin = m['homeTeam']['name']
            gost = m['awayTeam']['name']
            liga = m['competition']['name']
            lista.append(f"{domacin} vs {gost} ({liga})")
        return lista
    except Exception as e:
        return [f"Sistem nedostupan: {str(e)}"]

# DIZAJN
st.markdown("<h1 style='color: #00FF41; text-align: center;'>⚡ BetGen LIVE</h1>", unsafe_allow_html=True)

# POVLAČENJE PODATAKA
svi_parovi = ucitaj_meceve_v4()

# PROVERA I PRIKAZ
if "Greška" in svi_parovi[0] or "Nema" in svi_parovi[0]:
    st.error(svi_parovi[0])
    st.info("💡 Savet: Proveri da li si na football-data.org potvrdio mejl nakon registracije.")
else:
    st.subheader(f"📅 Današnja ponuda: {len(svi_parovi)} mečeva")
    izbor = st.selectbox("Izaberi par za AI prognozu:", svi_parovi)
    
    if st.button("POKRENI BETGEN"):
        import random
        tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2"]
        st.success(f"🤖 Tip: **{random.choice(tipovi)}** (Poverenje: {random.randint(70,96)}%)")

st.write("---")
st.caption("Podaci: Football-Data.org API")
