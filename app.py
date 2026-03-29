import streamlit as st
import requests
import os

# -------------------------
# 1. Konfiguracija stranice i stil
# -------------------------
st.set_page_config(page_title="BetGen AI", page_icon="⚽", layout="wide")

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

st.title("⚡ BetGen AI Expert - Multi Mečevi")

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
            st.error(f"Greška API-ja: {response.status_code}")
            return []
        data = response.json()
        return data.get("matches", [])[:20]  # uzimamo 20 mečeva
    except Exception as e:
        st.error(f"Ne mogu da povučem podatke: {e}")
        return []

# -------------------------
# 4. Analiza mečeva
# -------------------------
def analyze_match(match):
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]

    # jednostavan scoring
    score_home = len(home) % 10 + 1
    score_away = len(away) % 10 + 1
    total = score_home + score_away
    prob_home = int((score_home / total) * 100)
    prob_away = int((score_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    if prob_home > prob_away:
        tip = "1"
    elif prob_away > prob_home:
        tip = "2"
    else:
        tip = "X"

    return {
        "home": home,
        "away": away,
        "tip": tip,
        "1": prob_home,
        "X": prob_draw,
        "2": prob_away
    }

# -------------------------
# 5. Interfejs i dugme za analizu
# -------------------------
if st.button("Učitaj i analiziraj mečeve 🚀"):
    if not API_KEY:
        st.error("Dodaj API ključ u Streamlit Secrets i restartuj aplikaciju.")
    else:
        matches = get_matches()
        if not matches:
            st.warning("Nema mečeva trenutno.")
        else:
            # Prikaz svih mečeva
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
                    <p>💡 Analiza: Jednostavan model uzima ime tima kao osnovu za scoring. 
                    Može se kasnije unaprediti sa formom, golovima i domaćim/away prednostima.</p>
                </div>
                """, unsafe_allow_html=True)
