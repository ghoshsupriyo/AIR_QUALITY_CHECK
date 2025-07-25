import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("city_day.csv")  # Adjust filename if needed
    return df

df = load_data()

st.title("🌫️ Air Quality Index Analysis")

# Sidebar Filter
city = st.sidebar.selectbox("Select City", sorted(df['City'].dropna().unique()))
pollutant = st.sidebar.selectbox("Select Pollutant", ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3'])

# Filtered data
filtered_df = df[df['City'] == city].copy()
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
filtered_df.sort_values("Date", inplace=True)

st.subheader(f"{pollutant} levels in {city} over time")
st.line_chart(filtered_df.set_index('Date')[pollutant])

# Display AQI Stats
st.subheader(f"AQI Stats for {city}")
st.write(filtered_df[['AQI', 'AQI_Bucket']].describe())

# AQI Distribution
st.subheader("AQI Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['AQI'].dropna(), kde=True, ax=ax, color='skyblue')
st.pyplot(fig)
