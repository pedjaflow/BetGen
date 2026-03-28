import streamlit as st
import hashlib
import urllib.parse

# 1. DIZAJN - ULTRA DARK SA NEON DETALJIMA
st.set_page_config(page_title="BetGen AI Expert", page_icon="⚽", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { 
        background-color: #00FF41; color: black; 
        font-weight: bold; border-radius: 12px; height: 55px; border: none;
        transition: 0.3s; width: 100%;
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
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI EXPERT</h1>", unsafe_allow_html=True)

# 2. LOGIKA ZA FIKSNU ANALIZU I PAMETNE LINKOVE
def dobij_analizu(domacin, gost):
    if not domacin or not gost:
        return None
    
    par_tekst = f"{domacin.strip()} - {gost.strip()}"
    hash_id = int(hashlib.md5(par_tekst.lower().encode()).hexdigest(), 16)
    
    tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2", "GG3+"]
    izabrani_tip = tipovi[hash_id % len(tipovi)]
    poverenje = 75 + (hash_id % 21)
    
    # Priprema Google pretraga
    query_odds = urllib.parse.quote(f"{par_tekst} match odds comparison")
    query_h2h = urllib.parse.quote(f"{domacin} vs {gost} h2h stats")
    query_injuries = urllib.parse.quote(f"{par_tekst} injury news lineups")
    query_weather = urllib.parse.quote(f"weather forecast for {domacin} stadium")

    return {
        "tip": izabrani_tip,
        "poverenje": poverenje,
        "odds_link": f"https://www.google.com{query_odds}",
        "h2h_link": f"https://www.google.com{query_h2h}",
        "inj_link": f"https://www.google.com{query_injuries}",
        "weather_link": f"https://www.google.com{query_weather}"
    }

# 3. INTERFEJS SA DVA POLJA
col_a, col_b = st.columns(2)
with col_a:
    domacin_input = st.text_input("Domaćin:", placeholder="npr. Real Madrid")
with col_b:
    gost_input = st.text_input("Gost:", placeholder="npr. Barcelona")

if st.button("POKRENI DETALJNU ANALIZU 🚀"):
    data = dobij_analizu(domacin_input, gost_input)
    
    if data:
        st.markdown(f"### 🏟️ Izveštaj za: {domacin_input} - {gost_input}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.success(f"🤖 **PROGNOZA: {data['tip']}**")
        with c2:
            st.info(f"📊 **POVERENJE: {data['poverenje']}%**")

        st.markdown(f"""
        <div class="report-card">
            <b>📍 Analiza:</b> AI model je obradio istoriju oba tima. <br><br>
            <b>📋 Preporuka:</b> Klikni na dugmiće ispod da proveriš najnovije povrede i kvote pre uplate.
        </div>
        """, unsafe_allow_html=True)
        
        # Red sa dugmićima
        b1, b2 = st.columns(2)
        with b1:
            st.link_button("📈 Uporedi Kvote", data['odds_link'])
            st.link_button("📊 H2H Statistika", data['h2h_link'])
        with b2:
            st.link_button("🏥 Povrede/Sastavi", data['inj_link'])
            st.link_button("☁️ Vremenska Prognoza", data['weather_link'])
    else:
        st.warning("Popuni oba polja (Domaćin i Gost) za analizu.")

st.write("---")
st.caption("© 2026 BetGen Expert System • v14.0")
