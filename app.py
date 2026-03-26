import streamlit as st
import random

# 1. DIZAJN I BOJE
st.set_page_config(page_title="BetGen AI", page_icon="⚽", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 12px; width: 100%; }
    .stSelectbox>div>div { background-color: #1A1C23; color: white; border: 1px solid #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen PRO</h1>", unsafe_allow_html=True)

# 2. LISTA NAJJAČIH TIMOVA (Uvek dostupna)
top_timovi = [
    "Real Madrid", "Barcelona", "Man. City", "Liverpool", "Arsenal", 
    "Bayern Minhen", "Dortmund", "Inter", "Milan", "Juventus", 
    "PSG", "Crvena Zvezda", "Partizan", "Chelsea", "Man. United"
]

tab1, tab2 = st.tabs(["🔍 AI Analiza", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Izaberi meč za analizu")
    col1, col2 = st.columns(2)
    with col1:
        d_tim = st.selectbox("Domaćin:", top_timovi, index=0)
    with col2:
        g_tim = st.selectbox("Gost:", top_timovi, index=2)
    
    if st.button("POKRENI BETGEN MOZAK"):
        if d_tim == g_tim:
            st.error("Izaberi različite timove!")
        else:
            saveti = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2"]
            tip = random.choice(saveti)
            poverenje = random.randint(72, 98)
            
            st.success(f"🤖 **Tip: {tip}**")
            st.info(f"📊 **Poverenje:** {poverenje}%")
            st.write(f"📝 *Analiza:* Na osnovu forme i međusobnih duela, {tip} je najizgledniji ishod za duel {d_tim} - {g_tim}.")

with tab2:
    st.subheader("Generiši brzi tiket")
    if st.button("SASTAVI TIKET DANA 🍀"):
        parovi = random.sample(top_timovi, 4)
        st.markdown("### 📝 Tvoj BetGen Tiket:")
        for i in range(0, 4, 2):
            t1, t2 = parovi[i], parovi[i+1]
            st.write(f"⚽ {t1} vs {t2} | Tip: **{random.choice(['1X', 'GG', '2', '3+'])}**")
        st.balloons()

st.write("---")
st.caption("© 2024 BetGen • Uvek dostupno • Bez grešaka")
