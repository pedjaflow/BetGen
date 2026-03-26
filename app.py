import streamlit as st

# 1. PODEŠAVANJE DIZAJNA
st.set_page_config(page_title="BetGen AI", page_icon="⚽")
st.markdown("<h1 style='text-align: center; color: #00FF41;'>⚡ BetGen PRO Analiza</h1>", unsafe_allow_html=True)

# 2. TVOJA BAZA ANALIZA (Ovde unosiš parove i tekstove koje ti ja dam)
# Možeš sam dodavati nove redove ovde!
baza_analiza = {
    "Italija - Severna Irska": {
        "tip": "1 & 2-4",
        "analiza": "Italija igra kod kuće u play-off polufinalu. Severna Irska će se braniti, ali kvalitet Azura presuđuje.",
        "poverenje": "92%"
    },
    "Brazil - Francuska": {
        "tip": "GG (Oba tima daju gol)",
        "analiza": "Spektakl u prijateljskom tonu. Obe ekipe testiraju najjače sastave, očekuje se otvoren fudbal.",
        "poverenje": "85%"
    },
    "Vels - Bosna i Hercegovina": {
        "tip": "0-2 gola",
        "analiza": "Veoma tvrd meč u Kardifu. Tradicija kaže da u duelima ovih timova retko pada mnogo golova.",
        "poverenje": "78%"
    },
    "Španija - Argentina": {
        "tip": "X2 & GG",
        "analiza": "Finalissima 2026! Šampion Evrope protiv šampiona J. Amerike. Borba za prestiž i trofej.",
        "poverenje": "80%"
    }
}

# 3. INTERFEJS ZA KORISNIKA
st.subheader("Izaberi meč za detaljnu prognozu:")

# Korisnik bira par sa spiska (ključi iz naše baze)
izabrani_par = st.selectbox("Dostupni mečevi danas:", list(baza_analiza.keys()))

if st.button("PRIKAŽI BETGEN PROGNOZU"):
    podaci = baza_analiza[izabrani_par]
    
    st.markdown(f"### 🏟️ {izabrani_par}")
    st.success(f"🤖 **Preporučeni Tip:** {podaci['tip']}")
    st.info(f"📝 **Analiza:** {podaci['analiza']}")
    st.warning(f"📊 **Poverenje modela:** {podaci['poverenje']}")

st.write("---")
st.caption("© 2024 BetGen Expert Mode")
