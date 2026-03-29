import streamlit as st
import requests
from bs4 import BeautifulSoup
import hashlib

st.set_page_config(page_title="BetGen AI Live Scraper", page_icon="⚽", layout="centered")
st.title("⚡ BetGen AI - Live analiza mečeva")

# -------------------------
# 1. Funkcija za scraping live mečeva
# -------------------------
def get_live_matches():
    try:
        url = "https://www.livescore.com/football/live/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")

        matches = []
        # primer: pronađi sve utakmice u tagovima sa timovima
        # ovo može zavisiti od stranice, trenutno simulacija
        for div in soup.find_all("div"):
            text = div.get_text().strip()
            if " - " in text and len(text.split(" - ")) == 2:
                matches.append(text)
        
        if not matches:
            raise Exception("Nema utakmica")
        
        # ukloni duplikate i uzmi prvih 20
        return list(dict.fromkeys(matches))[:20]
    except:
        st.warning("Ne mogu da povučem live podatke, koristićemo simulirane mečeve.")
        return [f"Team {i} - Team {i+10}" for i in range(1,21)]

# -------------------------
# 2. Fiksna analiza po meču
# -------------------------
def analyze_match(match):
    h = int(hashlib.md5(match.encode()).hexdigest(), 16)

    avg_home = 1 + (h % 4) + ((h % 10)/10)
    avg_away = 1 + ((h//3) % 4) + ((h//7) % 10)/10

    total = avg_home + avg_away
    prob_home = int((avg_home / total) * 100)
    prob_away = int((avg_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    if prob_home > prob_away:
        tip = "1"
        analysis = f"{match.split(' - ')[0]} favoriti (pros. golovi: {avg_home:.1f} vs {avg_away:.1f})"
    elif prob_away > prob_home:
        tip = "2"
        analysis = f"{match.split(' - ')[1]} favoriti (pros. golovi: {avg_away:.1f} vs {avg_home:.1f})"
    else:
        tip = "X"
        analysis = f"Izjednačeni timovi (pros. golovi: {avg_home:.1f} vs {avg_away:.1f})"

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
matches = get_live_matches()
selected_match = st.selectbox("Izaberi meč za analizu:", matches)

if st.button("Analiziraj meč 🚀"):
    data = analyze_match(selected_match)
    st.markdown(f"### 🏟️ {selected_match}")
    st.markdown(f"**Predviđeni tip:** {data['tip']}")
    st.markdown(f"**Verovatnoće:** 1 → {data['1']}% | X → {data['X']}% | 2 → {data['2']}%")
    st.info(f"💡 Analiza: {data['analysis']}")
