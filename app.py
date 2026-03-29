import streamlit as st
import requests
import os
import random
import pandas as pd

# -------------------------
# 1. Konfiguracija stranice i stil
# -------------------------
st.set_page_config(page_title="BetGen AI Pro", page_icon="⚽", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0E1117; color: white; }
.stButton>button { 
    background-color: #00FF41; color: black; 
    font-weight: bold; border-radius: 12px; height: 50px;
    width: 100%;
}
.report-card { 
    background-color: #1A1C23; padding: 20px; border-radius: 15px; 
    border-left: 6px solid #00FF41; margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ BetGen AI Pro - Više mečeva + Analiza")

# -------------------------
# 2. API ključ iz Secrets
# -------------------------
API_KEY = os.getenv("API_KEY")

# -------------------------
# 3. Funkcija za povlačenje mečeva
# -------------------------
def get_matches():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            st.warning(f"API greška: {response.status_code}. Učitavamo simulirane mečeve.")
            return []
        data = response.json()
        return data.get("matches", [])
    except:
        st.warning("Ne mogu da povučem podatke. Učitavamo simulirane mečeve.")
        return []

# -------------------------
# 4. Napredna analiza meča
# -------------------------
def analyze_match(match):
    # Ako API ne daje timove, koristimo simulaciju
    home = match.get("homeTeam", {}).get("name") or match.get("home") or f"Team {random.randint(1,50)}"
    away = match.get("awayTeam", {}).get("name") or match.get("away") or f"Team {random.randint(51,100)}"

    # Simulacija forme (poslednjih 5 mečeva)
    form_home = [random.randint(0,3) for _ in range(5)]  # golovi
    form_away = [random.randint(0,3) for _ in range(5)]

    avg_home = sum(form_home)/5 + random.randint(0,1)  # malo random boost
    avg_away = sum(form_away)/5 + random.randint(0,1)

    total = avg_home + avg_away
    prob_home = int((avg_home / total) * 100)
    prob_away = int((avg_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    if prob_home > prob_away:
        tip = "1"
        analysis = f"{home} su favoriti (pros. golovi: {avg_home:.1f} vs {avg_away:.1f})"
    elif prob_away > prob_home:
        tip = "2"
        analysis = f"{away} su favoriti (pros. golovi: {avg_away:.1f} vs {avg_home:.1f})"
    else:
        tip = "X"
        analysis = "Meč je izjednačen, mogući nerešeni ishod."

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
# 5. Prikaz mečeva
# -------------------------
if st.button("Učitaj i analiziraj mečeve 🚀"):
    matches = get_matches()

    # Ako nema više mečeva, kreiraj simulirane 10
    if not matches:
        matches = [{"home": f"Team {i}", "away": f"Team {i+10}"} for i in range(1,11)]

    # Prikaz svakog meča
    for m in matches:
        data = analyze_match(m)
        st.markdown(f"""
        <div class="report-card">
            <h3>🏟️ {data['home']} - {data['away']}</h3>
            <p>🤖 Predviđeni tip: <b>{data['tip']}</b></p>
            <p>📊 Verovatnoće:</p>
        </div>
        """, unsafe_allow_html=True)

        # Bar chart za procente
        df = pd.DataFrame({
            "Tip": ["1","X","2"],
            "Verovatnoća": [data['1'], data['X'], data['2']]
        })
        st.bar_chart(df.set_index("Tip"))

        # Analiza
        st.info(f"💡 Analiza: {data['analysis']}")
        st.write("---")
