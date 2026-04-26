
import streamlit as st
import requests
import pandas as pd

# CONFIG - Put your API Key here!
API_KEY =  "939992da5d91dd0abd8b0206193845e6"

st.set_page_config(page_title="MHI Pro Scanner", layout="wide")
st.title("🏀 MHI Basketball Market Scanner")

# Function to fetch live odds
def get_live_odds():
    url = f"https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey={API_KEY}&regions=us&markets=totals&oddsFormat=american"
    response = requests.get(url)
    return response.json()

if st.button("🚀 Scan Live Markets for MHI Gaps"):
    data = get_live_odds()
    
    if not data:
        st.error("No games found or API key invalid.")
    else:
        results = []
        for game in data:
            home = game['home_team']
            away = game['away_team']
            
            # Find totals across different books
            for book in game['bookmakers']:
                market = book['markets'][0] # Totals market
                for outcome in market['outcomes']:
                    if outcome['name'] == 'Over':
                        results.append({
                            "Game": f"{away} @ {home}",
                            "Bookie": book['title'],
                            "Total Line": outcome['point']
                        })
        
        df = pd.DataFrame(results)
        
        # Display the Gaps
        st.subheader("📊 Live Totals Across Books")
        st.dataframe(df, use_container_width=True)
        
        # MHI Analysis Logic
        st.subheader("🔍 MHI Analysis")
        # Group by game to find the max and min lines
        for g in df['Game'].unique():
            game_data = df[df['Game'] == g]
            low_line = game_data['Total Line'].min()
            high_line = game_data['Total Line'].max()
            gap = high_line - low_line
            
            if gap >= 3:
                st.success(f"🔥 MHI ALERT: {g} has a {gap} point gap! (Low: {low_line} / High: {high_line})")
            else:
                st.write(f"✅ {g}: Stable market ({gap} pt gap)")

st.sidebar.info("MHI Strategy: Bet the OVER on the low line and the UNDER on the high line to 'Middle' the game.")
