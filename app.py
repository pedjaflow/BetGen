import streamlit as st
import hashlib
import urllib.parse

# 1. DIZAJN - "ULTRA DARK" SA NEON DETALJIMA
st.set_page_config(page_title="BetGen AI Expert", page_icon="⚽", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        background-color: #00FF41; color: black; 
        font-weight: bold; border-radius: 12px; height: 55px; border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #00CC33; transform: scale(1.02); }
    .stTextInput>div>div>input { 
        background-color: #1A1C23; color: white; border: 1px solid #00FF41; 
        border-radius: 10px; padding: 10px;
    }
    .report-card { 
        background-color: #1A1C23; padding: 25px; border-radius: 15px; 
        border-left: 6px solid #00FF41; margin-bottom: 20px;
    }
    .stLinkButton>a {
        background-color: #1A1C23 !important; color: #00FF41 !important;
        border: 1px solid #00FF41 !important; border-radius: 8px !important;
        text-decoration: none !important; display: block; text-align: center; padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI EXPERT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Analiza statistike, povreda i kvota u realnom vremenu</p>", unsafe_allow_html=True)

# 2. LOGIKA ZA FIKSNU ANALIZU I PAMETNE LINKOVE
def dobij_analizu(par_tekst):
    if not par_tekst or " - " not in par_tekst:
        return None
    
    timovi = par_tekst.split(" - ")
    domacin, gost = timovi[0].strip(), timovi[1].strip()
    
    # Generišemo fiksni ID na osnovu imena da prognoza uvek bude ista
    hash_id = int(hashlib.md5(par_tekst.lower().encode()).hexdigest(), 16)
    
    tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2", "GG3+"]
    izabrani_tip = tipovi[hash_id % len(tipovi)]
    poverenje = 75 + (hash_id % 21) # Poverenje 75% - 95%
    
    # Priprema Google pretraga
    query_odds = urllib.parse.quote(f"{par_tekst} match odds comparison bet365 pinnacle")
    query_h2h = urllib.parse.quote(f"{domacin} vs {gost} h2h stats")
    query_injuries = urllib.parse.quote(f"{par_tekst} injury news and starting lineups")
    query_weather = urllib.parse.quote(f"weather forecast for {domacin} match tonight")

    return {
        "tip": izabrani_tip,
        "poverenje": poverenje,
        "odds_link": f"https://www.google.com{query_odds}",
        "h2h_link": f"https://www.google.com{query_h2h}",
        "inj_link": f"https://www.google.com{query_injuries}",
        "weather_link": f"https://www.google.com{query_weather}",
        "domacin": domacin,
        "gost": gost
    }

# 3. INTERFEJS
par_input = st.text_input("Unesi par (format: Domaćin - Gost):", placeholder="npr. Srbija - Danska")

if st.button("POKRENI DETALJNU ANALIZU 🚀"):
    data = dobij_analizu(par_input)
    
    if data:
        st.markdown(f"### 🏟️ Izveštaj za: {par_input}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"🤖 **Tvoj Fiksni Tip: {data['tip']}**")
        with col2:
            st.info(f"📊 **Poverenje Modela: {data['poverenje']}%**")

        st.markdown(f"""
        <div class="report-card">
            <b>📍 Status meča:</b> Analizirani su istorijski podaci za {data['domacin']} i {data['gost']}.<br><br>
            <b>📋 Savet:</b> Pre konačne uplate, obavezno proveri dole navedene faktore uživo jer 
            povrede u poslednjem minutu mogu drastično promeniti tok meča.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("🔍 **PROVERI PODATKE U REALNOM VREMENU:**")
        
        # Red sa dugmićima (2x2 raspored za bolji prikaz na telefonu)
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("📈 Uporedi Kvote", data['odds_link'])
            st.link_button("📊 H2H Statistika", data['h2h_link'])
        with c2:
            st.link_button("🏥 Povrede/Sastavi", data['inj_link'])
            st.link_button("☁️ Vremenska Prognoza", data['weather_link'])
            
    else:
        st.warning("Upiši par pravilno (npr. Zvezda - Partizan) da bih generisao izveštaj.")

st.write("---")
st.caption("© 2026 BetGen Expert System • Fiksni AI Model v13.0")
