import streamlit as st
import hashlib

st.set_page_config(page_title="BetGen AI Multi Match", page_icon="⚽", layout="centered")
st.title("⚡ BetGen AI - Analiza više mečeva")

# -------------------------
# 1. Simulirana lista mečeva (za test)
# -------------------------
matches = [f"Team {i} - Team {i+10}" for i in range(1, 21)]  # 20 mečeva
st.subheader("📋 Lista mečeva")
selected_match = st.selectbox("Izaberi meč za analizu:", matches)

# -------------------------
# 2. Fiksna analiza po meču
# -------------------------
def analyze_match(match):
    # hash za fiksnu analizu
    h = int(hashlib.md5(match.encode()).hexdigest(), 16)
    
    # generiši prosečne golove fiksno po hash-u
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
# 3. Dugme za analizu
# -------------------------
if st.button("Analiziraj meč 🚀"):
    data = analyze_match(selected_match)
    st.markdown(f"### 🏟️ {selected_match}")
    st.markdown(f"**Predviđeni tip:** {data['tip']}")
    st.markdown(f"**Verovatnoće:** 1 → {data['1']}% | X → {data['X']}% | 2 → {data['2']}%")
    st.info(f"💡 Analiza: {data['analysis']}")
