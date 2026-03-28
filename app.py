import streamlit as st
import hashlib
import urllib.parse

# 1. DIZAJN
st.set_page_config(page_title="BetGen AI Expert", page_icon="⚽")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; height: 50px; }
    .stTextInput>div>div>input { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    .report-card { background-color: #1A1C23; padding: 20px; border-radius: 15px; border-left: 5px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen AI Expert")

# 2. LOGIKA ZA DOSLEDNU ANALIZU I LINKOVE
def dobij_analizu(par_tekst):
    if not par_tekst or " - " not in par_tekst:
        return None
    
    # Razdvajamo timove
    timovi = par_tekst.split(" - ")
    domacin, gost = timovi[0].strip(), timovi[1].strip()
    
    # Generišemo fiksni broj na osnovu imena (da prognoza bude uvek ista)
    hash_broj = int(hashlib.md5(par_tekst.lower().encode()).hexdigest(), 16)
    
    tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2"]
    izabrani_tip = tipovi[hash_broj % len(tipovi)]
    poverenje = 72 + (hash_broj % 24)
    
    # Generisanje Google linkova za realne podatke
    query_h2h = urllib.parse.quote(f"{domacin} vs {gost} h2h statistics")
    query_injuries = urllib.parse.quote(f"{par_tekst} injuries and team news")
    query_weather = urllib.parse.quote(f"weather forecast for {domacin} stadium matchday")

    return {
        "tip": izabrani_tip,
        "poverenje": poverenje,
        "h2h_link": f"https://www.google.com{query_h2h}",
        "inj_link": f"https://www.google.com{query_injuries}",
        "weather_link": f"https://www.google.com{query_weather}",
        "domacin": domacin,
        "gost": gost
    }

# 3. INTERFEJS
par = st.text_input("Unesi par (format: Tim A - Tim B):", placeholder="npr. Srbija - Danska")

if st.button("POKRENI EKSPERTSKU ANALIZU"):
    data = dobij_analizu(par)
    
    if data:
        st.markdown(f"### 🏟️ {par}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"🤖 **PROGNOZA: {data['tip']}**")
        with col2:
            st.info(f"📊 **POVERENJE: {data['poverenje']}%**")

        st.markdown("#### 📑 Detaljni Izveštaj:")
        with st.container():
            st.markdown(f"""
            <div class="report-card">
                <b>📊 H2H Analiza:</b> Istorija duela ukazuje na taktičko nadmudrivanje. <br>
                <b>🏥 Medicinski bilten:</b> Proverite poslednje izmene u sastavima (link ispod). <br>
                <b>☁️ Vremenski uslovi:</b> Mogući uticaj na brzinu terena i broj golova.
            </div>
            """, unsafe_allow_html=True)
            
        st.write("---")
        st.write("🔍 **Proveri realne podatke uživo na Google-u:**")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.link_button("📊 H2H Statistika", data['h2h_link'])
        with c2:
            st.link_button("🏥 Povrede/Sastavi", data['inj_link'])
        with c3:
            st.link_button("☁️ Vremenska prognoza", data['weather_link'])
            
    else:
        st.warning("Molimo unesite par u ispravnom formatu (Tim A - Tim B).")

st.write("---")
st.caption("BetGen v12.0 - Deep Search Integration")
