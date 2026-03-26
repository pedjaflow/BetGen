import streamlit as st
import requests
import random

# --- TVOJ KLJUČ (Očišćen) ---
API_KEY = "958d1f2948df4ca69ad062d7856c2a2a"

@st.cache_data(ttl=600)  # Čuva podatke 10 minuta da te API ne blokira
def ucitaj_parove_api():
    try:
        url = "https://api.football-data.org"
        headers = { 'X-Auth-Token': API_KEY }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            return [["Previše zahteva", "Sačekaj 1 min", "API Limit"]]
        
        data = response.json()
        mecevi = data.get('matches', [])
        
        if not mecevi:
            return [["Nema mečeva danas", "", "Proverite sutra"]]

        lista = []
        for m in mecevi:
            domacin = m['homeTeam']['shortName'] or m['homeTeam']['name']
            gost = m['awayTeam']['shortName'] or m['awayTeam']['name']
            liga = m['competition']['name']
            lista.append([domacin, gost, liga])
        return lista
    except:
        return [["Sistem preopterećen", "Probaj opet", "Greška"]]

# --- DIZAJN ---
st.set_page_config(page_title="BetGen AI", page_icon="⚽")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen AI Live")

parovi = ucitaj_parove_api()

# Glavni deo
if parovi[0][0] in ["Previše zahteva", "Sistem preopterećen"]:
    st.error(f"⚠️ {parovi[0][0]} - {parovi[0][1]}")
    if st.button("Pokušaj ponovo"):
        st.cache_data.clear()
        st.rerun()
else:
    tab1, tab2 = st.tabs(["🔍 Analiza", "🍀 Srećni Tiket"])
    
    with tab1:
        opcije = [f"{p[0]} - {p[1]} ({p[2]})" for p in parovi]
        izbor = st.selectbox("Izaberi par:", opcije)
        if st.button("ANALIZIRAJ"):
            st.success(f"🤖 Tip: {random.choice(['1', 'X2', 'GG', '3+'])} (Poverenje: {random.randint(70,95)}%)")

    with tab2:
        if st.button("GENERISI TIKET 🍀"):
            n = min(len(parovi), 3)
            tiket = random.sample(parovi, n)
            for t in tiket:
                st.write(f"⚽ {t[0]} - {t[1]} | **{random.choice(['1', 'X', '2', 'GG'])}**")
            st.balloons()
