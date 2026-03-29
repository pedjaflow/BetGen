import streamlit as st
import requests
import hashlib

st.set_page_config(page_title="BetGen AI Live", page_icon="⚽", layout="centered")
st.title("⚡ BetGen AI - Live analiza mečeva")

# -------------------------
# 1. Funkcija za povlačenje live mečeva (Football-Data API)
# -------------------------
API_KEY = st.secrets.get("API_KEY")  # dodaj u Streamlit Secrets

def get_live_matches():
    url = "https://api.football-data.org/v4/matches"  # besplatni plan
    headers = {"X-Auth-Token": API_KEY}
    try:
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            st.warning(f"API greška: {r.status_code}. Učitavamo simulirane mečeve.")
            return []
        data = r.json()
        matches = data.get("matches", [])
        return matches[:20]  # uzmi prvih 20 mečeva
    except:
        st.warning("Ne mogu da povučem podatke, učitavamo simulirane mečeve.")
        return [{"home": f"Team {i}", "away": f"Team {i+10}"} for i in range(1,11)]

# -------------------------
# 2. Funkcija za fiksnu analizu
# -------------------------
def analyze_match(match):
    # uzimamo ime tima
    home = match.get("homeTeam", {}).get("name") or match.get("home")
    away = match.get("awayTeam", {}).get("name") or match.get("away")
    
    # generišemo hash po meču da analiza bude ista svaki put
    hash_input = f"{home}-{away}".encode()
    h = int(hashlib.md5(hash_input).hexdigest(), 16)
    
    # simulacija prosečnih golova (fiksno po hash-u)
    avg_home = 1 + (h % 4) + (h % 10)/10
    avg_away = 1 + ((h//3) % 4) + ((h//7) % 10)/10
    
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
        analysis = f"Izjednačeni timovi (pros. golovi: {avg_home:.1f} vs {avg_away:.1f})"

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
# 3. Interfejs
# -------------------------
matches = get_live_matches()
match_options = []

for m in matches:
    home = m.get("homeTeam", {}).get("name") or m.get("home")
    away = m.get("awayTeam", {}).get("name") or m.get("away")
    match_options.append(f"{home} - {away}")

selected_match = st.selectbox("Izaberi meč za analizu:", match_options)

if st.button("Analiziraj meč 🚀"):
    # pronađi originalni match dict po imenu
    match_dict = None
    for m in matches:
        home = m.get("homeTeam", {}).get("name") or m.get("home")
        away = m.get("awayTeam", {}).get("name") or m.get("away")
        if f"{home} - {away}" == selected_match:
            match_dict = m
            break
    
    if match_dict:
        data = analyze_match(match_dict)
        st.markdown(f"### 🏟️ {selected_match}")
        st.markdown(f"**Predviđeni tip:** {data['tip']}")
        st.markdown(f"**Verovatnoće:** 1 → {data['1']}% | X → {data['X']}% | 2 → {data['2']}%")
        st.info(f"💡 Analiza: {data['analysis']}")
    else:
        st.error("Ne mogu da pronađem podatke za izabrani meč.")
