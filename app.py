import streamlit as st

st.set_page_config(page_title="MHI O/U Analyzer", layout="wide")
st.title("🏀 Elite Basketball O/U Predictor")

# Sidebar for Inputs
st.sidebar.header("Matchup Stats")
h_pace = st.sidebar.number_input("Home Team Pace", value=100.2)
h_off = st.sidebar.number_input("Home Off. Efficiency", value=114.5)
h_def = st.sidebar.number_input("Home Def. Efficiency", value=112.0)

a_pace = st.sidebar.number_input("Away Team Pace", value=99.8)
a_off = st.sidebar.number_input("Away Off. Efficiency", value=110.4)
a_def = st.sidebar.number_input("Away Def. Efficiency", value=115.2)

# The Math
est_pace = (h_pace + a_pace) / 2
predicted_total = (est_pace * ((h_off + a_def + a_off + h_def) / 2)) / 100

st.metric("📊 Predicted Game Total", round(predicted_total, 2))

st.info("💡 MHI Strategy: Compare this to the sportsbook line. If the gap is >4 points, you have an edge.")
