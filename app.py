import streamlit as st
import random

# 1. FORSIRANJE TAMNE TEME I BOJA
st.set_page_config(page_title="BetGen PRO", page_icon="⚽", layout="centered")

st.markdown("""
    <style>
    /* Pozadina cele aplikacije */
    .stApp { background-color: #0E1117 !important; }
    /* Svi tekstovi postaju beli */
    h1, h2, h3, p, span, label { color: #FFFFFF !important; }
    /* Naslov u neon zelenoj */
    .neon-title { color: #00FF41 !important; text-align: center; font-size: 40px; font-weight: bold; text-shadow: 0 0 10px #00FF41; }
    /* Dugmići */
    .stButton>button { 
        background-color: #00FF41 !important; color: black !important; 
        font-weight: bold !important; border-radius: 12px !important; 
        border: none !important; width: 100% !important; height: 55px !important;
    }
    /* Okviri za unos */
    .stSelectbox div[data-baseweb="select"] { background-color: #1A1C23 !important; border: 1px solid #00FF41 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. NASLOV
st.markdown("<div class='neon-title'>⚡ BetGen PRO AI</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888 !important;'>Ažurirano: Subota, 28. mart</p>", unsafe_allow_html=True)

# 3. AKTIVNI MEČEVI ZA DANAS (SUBOTA, 28. MART)
# Ovde menjaš listu kad god želiš nove parove
mecevi_danas = [
    "Srbija vs Mađarska (Prijateljska - UŽIVO)",
    "Hrvatska vs Norveška (Prijateljska)",
    "Španija vs Argentina (Finalissima 2026)",
    "Engleska vs Nemačka (Klasik)",
    "Francuska vs Brazil (Spektakl)",
    "Portugal vs Turska (Play-off)",
    "Poljska vs Švedska (Kvalifikacije)",
    "Austrija vs Bosna i Hercegovina",
    "Crna Gora vs Grčka"
]

tab1, tab2 = st.tabs(["🔍 ANALIZA", "🍀 TIKET"])

with tab1:
    st.subheader("Izaberi meč za AI prognozu:")
    izbor = st.selectbox("Današnja ponuda:", mecevi_danas)
    
    if st.button("POKRENI BETGEN MOZAK"):
        tipovi = ["1", "X2", "GG", "3+", "0-2", "2", "1X", "GG3+"]
        poverenje = random.randint(78, 97)
        st.success(f"🤖 **TIP: {random.choice(tipovi)}** (Poverenje: {poverenje}%)")
        st.info("📊 **Analiza:** Favorit ulazi u meč sa punim sastavom. Očekuje se visok intenzitet.")

with tab2:
    st.subheader("Sastavi dobitni tiket")
    if st.button("GENERISI SREĆNI TIKET 🍀"):
        parovi = random.sample(mecevi_danas, 3)
        st.write("### 📝 Tvoj BetGen Tiket:")
        for p in parovi:
            st.write(f"⚽ {p} | Tip: **{random.choice(['1', 'GG', 'X2', '3+'])}**")
        st.balloons()

st.write("---")
st.caption("© 2026 BetGen Expert Mode • Offline Database")
