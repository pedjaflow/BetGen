 import streamlit as st
import random

# 1. DIZAJN I BOJE (Konfiguracija)
st.set_page_config(page_title="BetGen AI", page_icon="⚽", layout="centered")

# Custom CSS za Dark Mode i neon zelenu boju
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .stButton>button { 
        background-color: #00FF41; color: black; 
        font-weight: bold; border-radius: 10px; border: none;
        width: 100%; height: 50px;
    }
    .stTextInput>div>div>input { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    .stHeader { color: #00FF41; }
    </style>
    """, unsafe_allow_status=True)

# 2. LOGO I NASLOV
st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen AI</h1>", unsafe_allow_status=True)
st.markdown("<p style='text-align: center;'>Generacija pametnog klađenja</p>", unsafe_allow_status=True)

# 3. GLAVNE FUNKCIJE
tab1, tab2 = st.tabs(["🔍 Analiza Meča", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Analiziraj svoj par")
    col1, col2 = st.columns(2)
    with col1:
        domacin = st.text_input("Domaćin", "Crvena Zvezda")
    with col2:
        gost = st.text_input("Gost", "Partizan")
    
    grad = st.text_input("Grad (za vremensku prognozu)", "Beograd")
    
    if st.button("POKRENI AI ANALIZU"):
        # Simulacija naše logike
        prognoza = random.choice(["1", "X", "2", "GG", "0-2"])
        poverenje = random.randint(65, 95)
        st.success(f"🤖 Analiza završena! Tip: **{prognoza}** (Poverenje: {poverenje}%)")

with tab2:
    st.subheader("Generiši dobitni tiket")
    broj_parova = st.slider("Koliko parova želiš?", 2, 5, 3)
    
    if st.button("SASTAVI SREĆNI TIKET 🍀"):
        st.markdown("### 📝 Tvoj BetGen Tiket:")
        test_timovi = ["Arsenal", "Real Madrid", "Man. City", "Milan", "Bayern", "PSG", "Barcelona", "Liverpool"]
        
        ukupna_kvota = 1.0
        for _ in range(broj_parova):
            t1, t2 = random.sample(test_timovi, 2)
            tip = random.choice(["1", "X2", "GG", "3+", "1X"])
            kvota = round(random.uniform(1.4, 2.2), 2)
            ukupna_kvota *= kvota
            st.write(f"⚽ {t1} - {t2} | Tip: **{tip}** | Kvota: {kvota}")
        
        st.info(f"💰 Ukupna kvota: **{round(ukupna_kvota, 2)}**")

st.write("---")
st.caption("© 2024 BetGen - Powered by AI & Open-Meteo")
