import streamlit as st
import requests
import os

# -------------------------
# 1. Konfiguracija stranice
# -------------------------
st.set_page_config(page_title="BetGen AI", page_icon="⚽", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #0E1117; color: white; }
.stButton>button { 
    background-color: #00FF41; color: black; 
    font-weight: bold; border-radius: 12px; height: 50px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ BetGen AI (MVP)")

# -------------------------
# 2. Uzimanje API ključa iz Secrets
# -------------------------
API_KEY = os.getenv("API_KEY")  # ovde dodaješ ključ u Streamlit Secrets

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
        return data.get("matches", [])[:10]  # uzimamo prvih 10 mečeva
    except Exception as e:
        st.error(f"Ne mogu da povučem podatke: {e}")
        return []

# -------------------------
# 4. Analiza mečeva
# -------------------------
def analyze_match(match):
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]

    # jednostavan scoring (MVP) - kasnije možeš poboljšati
    score_home = len(home) % 10 + 1
    score_away = len(away) % 10 + 1

    total = score_home + score_away
    prob_home = int((score_home / total) * 100)
    prob_away = int((score_away / total) * 100)
    prob_draw = 100 - prob_home - prob_away

    # određivanje tipa
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
# 5. Interfejs
# -------------------------
if st.button("Učitaj mečeve i analiziraj 🚀"):
    if not API_KEY:
        st.error("Nema API ključa! Dodaj ga u Streamlit Secrets.")
    else:
        matches = get_matches()
        if not matches:
            st.warning("Nema mečeva ili API ne radi.")
        else:
            for m in matches:
                data = analyze_match(m)
                st.markdown(f"### 🏟️ {data['home']} - {data['away']}")
                st.success(f"Tip: {data['tip']}")
                st.write(f"1 → {data['1']}%\nX → {data['X']}%\n2 → {data['2']}%")
                st.write("---")
