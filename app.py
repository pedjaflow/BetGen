import streamlit as st
import requests
import os
import random

# -------------------------
# 1. Konfiguracija stranice i stil
# -------------------------
st.set_page_config(page_title="BetGen AI Expert", page_icon="⚽", layout="wide")

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

st.title("⚡ BetGen AI Expert - Više mečeva")

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
# 4. Funkcija za analizu
# -------------------------
def analyze_match(match):
    home = match.get("homeTeam", {}).get("name") or match.get("home")
    away = match.get("awayTeam", {}).get("name") or match.get("away")

    # Jednostavna analiza + random faktor
    score_home = len(home) % 10 + random.randint(0,5)
    score_away = len(away) % 10 + random.randint(0,5)
    total = score_home + score_away
    prob_home = int((score_home / total) * 100)
    prob_away = int((score_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    if prob_home > prob_away:
        tip = "1"
        analysis = f"{home} su favoriti jer imaju bolju formu."
    elif prob_away > prob_home:
        tip = "2"
        analysis = f"{away} su favoriti zbog statistike poslednjih mečeva."
    else:
        tip = "X"
        analysis = "Moguć nerešeni ishod. Timovi su izjednačeni."

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
# 5. Dugme za učitavanje i prikaz mečeva
# -------------------------
if st.button("Učitaj i analiziraj mečeve 🚀"):

    matches = get_matches()

    # Ako nema više mečeva, kreiraj simulirane za test
    if not matches:
        matches = [{"home": f"Team {i}", "away": f"Team {i+10}"} for i in range(1,6)]

    # Prikaz svakog meča
    for m in matches:
        data = analyze_match(m)
        st.markdown(f"""
        <div class="report-card">
            <h3>🏟️ {data['home']} - {data['away']}</h3>
            <p>🤖 Predviđeni tip: <b>{data['tip']}</b></p>
            <p>📊 Verovatnoće:</p>
            <ul>
                <li>1 → {data['1']}%</li>
                <li>X → {data['X']}%</li>
                <li>2 → {data['2']}%</li>
            </ul>
            <p>💡 Analiza: {data['analysis']}</p>
        </div>
        """, unsafe_allow_html=True)
