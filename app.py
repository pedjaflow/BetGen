import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="BetGen AI", page_icon="⚽", layout="centered")
st.title("⚡ BetGen AI - Analiza utakmica")

# -------------------------
# 1. Simulirana lista mečeva
# -------------------------
matches = [f"Team {i} - Team {i+10}" for i in range(1, 11)]
st.subheader("📋 Lista mečeva")

selected_match = st.selectbox("Izaberi meč za analizu:", matches)

# -------------------------
# 2. Funkcija za sigurnu analizu
# -------------------------
def analyze_match(match):
    if not isinstance(match, str) or " - " not in match:
        match = f"Team {random.randint(1,50)} - Team {random.randint(51,100)}"
    
    home, away = match.split(" - ")

    # simulacija forme poslednjih 5 mečeva
    form_home = [random.randint(0,3) for _ in range(5)]
    form_away = [random.randint(0,3) for _ in range(5)]

    avg_home = sum(form_home)/5 + random.random()
    avg_away = sum(form_away)/5 + random.random()

    total = avg_home + avg_away
    prob_home = int((avg_home / total) * 100)
    prob_away = int((avg_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    if prob_home > prob_away:
        tip = "1"
        analysis = f"{home} favoriti (pros. golovi: {avg_home:.1f} vs {avg_away:.1f})"
    elif prob_away > prob_home:
        tip = "2"
        analysis = f"{away} favoriti (pros. golovi: {avg_away:.1f} vs {avg_home:.1f})"
    else:
        tip = "X"
        analysis = "Izjednačeni timovi, mogući nerešeni ishod."

    return {
        "home": home,
        "away": away,
        "tip": tip,
        "1": prob_home,
        "X": prob_draw,
        "2": prob_away,
        "analysis": analysis
    }

# -------------------------
# 3. Dugme za analizu
# -------------------------
if st.button("Analiziraj meč 🚀"):
    data = analyze_match(selected_match)
    st.markdown(f"### 🏟️ {selected_match}")
    st.markdown(f"**Predviđeni tip:** {data['tip']}")
    
    df = pd.DataFrame({
        "Tip": ["1","X","2"],
        "Verovatnoća": [data['1'], data['X'], data['2']]
    })
    st.bar_chart(df.set_index("Tip"))

    st.info(f"💡 Analiza: {data['analysis']}")
