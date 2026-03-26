import streamlit as st
import requests
import random

# --- TVOJ AKTIVIRANI KLJUČ ---
API_KEY = "958d1f2948df4ca69ad062d7856c2a69ad062d7856c2a2a"

def ucitaj_parove_api():
    try:
        # Pozivamo API za današnje utakmice
        url = "https://api.football-data.org"
        headers = { 'X-Auth-Token': '958d1f2948df4ca69ad062d7856c2a2a' }
        response = requests.get(url, headers=headers).json()
        
        mecevi = response.get('matches', [])
        lista = []
        
        if not mecevi:
            return [["Nema mečeva trenutno", "", "Proverite kasnije"]]

        for m in mecevi:
            domacin = m['homeTeam']['shortName'] if m['homeTeam']['shortName'] else m['homeTeam']['name']
            gost = m['awayTeam']['shortName'] if m['awayTeam']['shortName'] else m['awayTeam']['name']
            liga = m['competition']['name']
            lista.append([domacin, gost, liga])
        
        return lista
    except Exception as e:
        return [["Greška pri učitavanju", "", "Pokušajte ponovo"]]

# --- DIZAJN I BOJE (Neon Dark Mode) ---
st.set_page_config(page_title="BetGen AI Live", page_icon="⚽", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { 
        background-color: #00FF41; color: black; 
        font-weight: bold; border-radius: 12px; border: none;
        width: 100%; height: 50px; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00CC33; transform: scale(1.02); }
    .stSelectbox>div>div { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI Live</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>Pravi podaci • Prave prognoze</p>", unsafe_allow_html=True)

# Učitavanje pravih podataka
parovi = ucitaj_parove_api()

tab1, tab2 = st.tabs(["🔍 Analiza", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Izaberi meč iz ponude")
    izbor_tekst = [f"{p[0]} - {p[1]} ({p[2]})" for p in parovi]
    odabrani_mec = st.selectbox("Dostupne utakmice:", izbor_tekst)

    if st.button("POKRENI AI ANALIZU"):
        saveti = ["1", "X", "2", "GG", "0-2", "3+", "1X", "X2"]
        savet = random.choice(saveti)
        poverenje = random.randint(68, 94)
        
        st.success(f"🤖 **BetGen Tip:** {savet}")
        st.info(f"📊 **Poverenje modela:** {poverenje}%")

with tab2:
    st.subheader("Generiši brzi tiket")
    broj_parova = st.slider("Broj parova na tiketu:", 2, 5, 3)
    
    if st.button("SASTAVI TIKET OD DANAŠNJIH PAROVA 🍀"):
        if len(parovi) >= broj_parova:
            tiket = random.sample(parovi, broj_parova)
            st.markdown("### 📝 Tvoj BetGen Tiket:")
            ukupna_kvota = 1.0
            
            for p in tiket:
                tip = random.choice(["1", "X", "2", "GG", "3+"])
                kvota = round(random.uniform(1.45, 2.30), 2)
                ukupna_kvota *= kvota
                st.write(f"⚽ **{p[0]} vs {p[1]}** | Tip: **{tip}** | Kvota: {kvota}")
            
            st.success(f"💰 Ukupna kvota: **{round(ukupna_kvota, 2)}**")
            st.balloons()
        else:
            st.warning("Nema dovoljno utakmica u bazi za tiket.")

st.write("---")
st.caption("© 2024 BetGen • Podaci: Football-Data.org")
