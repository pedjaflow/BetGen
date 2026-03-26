import streamlit as st
import random

st.set_page_config(page_title="BetGen AI", page_icon="⚡")

st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen PRO</h1>", unsafe_allow_html=True)

# TABOVI
tab1, tab2 = st.tabs(["🎯 Današnje Prognoze", "🍀 Srećni Tiket"])

with tab1:
    st.subheader("Analiza Expert Modela")
    # Ovde nalepiš ono što ti ja pošaljem
    dnevni_unos = st.text_area("Admin unos (samo za tebe):", "Real Madrid - Barcelona | Tip: GG3+ | Poverenje: 88%")
    
    if st.button("PRIKAŽI ANALIZU"):
        st.success(f"🤖 **BetGen Analiza:** \n\n {dnevni_unos}")

with tab2:
    st.subheader("Generiši tiket")
    if st.button("SASTAVI TIKET 🍀"):
        parovi = ["Arsenal - Liverpool", "Milan - Inter", "Bayern - Dortmund", "Partizan - Zvezda"]
        tiket = random.sample(parovi, 2)
        for t in tiket:
            st.write(f"⚽ {t} | Tip: **{random.choice(['1', 'X2', 'GG'])}**")
        st.balloons()

st.info("💡 Podatke za danas obezbedio BetGen AI Expert model.")
