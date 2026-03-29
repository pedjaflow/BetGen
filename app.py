import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

st.set_page_config(page_title="BetGen AI Google Scraper", page_icon="⚽", layout="centered")

st.title("⚡ BetGen AI - Analiza utakmica sa Google-a")

# -------------------------
# 1. Funkcija za scraping utakmica
# -------------------------
def get_google_fixtures():
    url = "https://www.google.com/search?q=football+fixtures"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        matches = []

        # Google prikazuje utakmice u divovima sa class="VwiC3b" ili span tagovima, ovo je primer
        for div in soup.find_all("div"):
            text = div.get_text().strip()
            if " - " in text and len(text.split(" - ")) == 2:
                matches.append(text)
        # ukloni duplikate i vrati prvih 20
        return list(dict.fromkeys(matches))[:20]
    except:
        st.warning("Ne mogu da povučem listu sa Google-a, koristićemo simulirane mečeve.")
        return [f"Team {i} - Team {i+1}" for i in range(1,11)]

# -------------------------
# 2. Funkcija za analizu meča
# -------------------------
def analyze_match(match):
    home, away = match.split(" - ")

    # simulacija forme
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
        "tip": tip,
        "1": prob_home,
        "X": prob_draw,
        "2": prob_away,
        "analysis": analysis
    }

# -------------------------
# 3. Glavni interfejs
# -------------------------
st.subheader("📋 Lista mečeva")
matches = get_google_fixtures()

selected_match = st.selectbox("Izaberi meč za analizu:", matches)

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
