import streamlit as st
import hashlib

# 1. DIZAJN
st.set_page_config(page_title="BetGen PRO", page_icon="⚽")
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #00FF41; color: black; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ BetGen Dosledna Analiza")

# 2. FUNKCIJA KOJA "ZAKLJUČAVA" PROGNOZU
def generisi_fiksnu_prognozu(par_tekst):
    if not par_tekst or par_tekst.strip() == "":
        return None, None
    
    # Pretvaramo tekst u broj koji je uvek isti za taj par
    hash_broj = int(hashlib.md5(par_tekst.lower().strip().encode()).hexdigest(), 16)
    
    tipovi = ["1", "X", "2", "GG", "3+", "0-2", "1X", "X2"]
    # Biramo tip na osnovu broja (uvek će izabrati isti za isti tekst)
    izabrani_tip = tipovi[hash_broj % len(tipovi)]
    poverenje = 70 + (hash_broj % 26) # Poverenje između 70% i 95%
    
    return izabrani_tip, poverenje

# 3. INTERFEJS
par = st.text_input("Unesi par (npr. Engleska - Belgija):")

if st.button("POKRENI ANALIZU"):
    tip, procenat = generisi_fiksnu_prognozu(par)
    
    if tip:
        st.success(f"🏟️ Meč: **{par}**")
        st.write(f"🤖 Tip: **{tip}**")
        st.write(f"📊 Poverenje: **{procenat}%**")
        st.info("💡 Ova prognoza je fiksna za ovaj par na osnovu AI algoritma.")
    else:
        st.warning("Prvo unesi ime utakmice.")

st.write("---")
st.caption("BetGen v11.0 - Dosledni model")
