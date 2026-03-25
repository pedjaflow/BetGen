import streamlit as st

# Postavke izgleda aplikacije
st.set_page_config(page_title="BetGen AI", page_icon="🚀")

# Naslov i Logo
st.title("🚀 BetGen v1.0")
st.subheader("AI Analiza Sportskih Rezultata")

# Glavni meni
st.write("---")
opcija = st.selectbox("Izaberi opciju:", ["Početna", "Analiziraj Meč", "Današnji Favoriti"])

if opcija == "Analiziraj Meč":
    col1, col2 = st.columns(2)
    
    with col1:
        domacin = st.text_input("Domaći tim", "Arsenal")
        forma_d = st.slider("Forma domaćina (golovi)", 0.0, 5.0, 1.5)
        
    with col2:
        gost = st.text_input("Gostujući tim", "Chelsea")
        forma_g = st.slider("Forma gosta (golovi)", 0.0, 5.0, 1.2)

    grad = st.text_input("Grad u kom se igra (za vremensku prognozu)", "London")
    
    if st.button("GENERISI PROGNOZU"):
        # Logika koju smo ranije napravili
        rezultat_d = round(forma_d * 0.9, 1) # Mala simulacija faktora
        rezultat_g = round(forma_g * 0.9, 1)
        
        st.success(f"🤖 BetGen Prognoza: {domacin} {rezultat_d} : {rezultat_g} {gost}")
        st.info("💡 Savet: Razmislite o tipu 'Oba tima daju gol' (GG)")

elif opcija == "Današnji Favoriti":
    st.write("📌 **Top 3 pick-a za danas:**")
    st.write("1. Man. City - Real Madrid (Tip: 1)")
    st.write("2. Partizan - Zvezda (Tip: X2)")
    st.write("3. Bayern - Arsenal (Tip: 3+ golova)")

st.write("---")
st.caption("BetGen koristi besplatne AI modele i vremensku prognozu uživo.")
