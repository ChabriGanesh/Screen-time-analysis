import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
# This MUST be the first Streamlit command!
st.set_page_config(
    page_title="✨ Indian Kids' Screen Time Analysis 📱",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for fonts and backgrounds
st.markdown("""
    <style>
    .main {font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;}
    h1, h2, h3, .stMarkdown {color: #3e5cd6;}
    .css-18e3th9 {background: #f5f7fe !important;}
    .stSidebar {background-color: #4682B4;}
    .stDataFrame {background-color: #40E0D0;}
    </style>
    """, unsafe_allow_html=True)

# Decorative Banner Image
st.image("images/banner.png", use_column_width=True)

# Stylish Title & Description with Emojis
st.title("✨ Indian Kids' Screen Time Analysis 📱")
st.markdown("""
#### Welcome!  
Explore and analyze screen time patterns of Indian children aged 8 to 18 years.  
🎨 Use the filters in the sidebar to refine your data selection.
""")
st.markdown("---")
# Get the directory of the current file (app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Build the file path relative to app.py
FILE_PATH = os.path.join(BASE_DIR, "Indian_Kids_Screen_Time.csv")
@st.cache_data
def load_data():
    df = pd.read_csv(FILE_PATH)
    return df

df = load_data()
# Sidebar with emojis, tip, and instructions
with st.sidebar:
    st.header("🔖 Filter Data")
    st.info("⬅️ Use these controls to explore specific groups.")
    st.success("💡 Tip: Try adjusting all filters for deeper insights!")
    age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
    age_range = st.slider("🎚️ Select Age Range", age_min, age_max, (age_min, age_max))
    genders = df['Gender'].unique().tolist()
    selected_genders = st.multiselect("🧑‍🦱 Select Gender", options=genders, default=genders)
    localities = df['Urban_or_Rural'].unique().tolist()
    selected_localities = st.multiselect("🌏 Select Locality", options=localities, default=localities)

filtered_df = df[
    (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) &
    (df['Gender'].isin(selected_genders)) &
    (df['Urban_or_Rural'].isin(selected_localities))
]

st.write(f"🔎 Showing **{len(filtered_df)}** records matching filters")
# Pretty Data Table with emoji and divider
st.markdown("#### 📋 Filtered Data")
st.dataframe(filtered_df)
st.markdown("---")

# Visualization 1: Average Screen Time by Age
st.header("📊 Average Screen Time by Age ")
avg_screen_time_by_age = filtered_df.groupby('Age')['Avg_Daily_Screen_Time_hr'].mean().reset_index()
fig1, ax1 = plt.subplots(figsize=(8,4))
sns.barplot(data=avg_screen_time_by_age, x='Age', y='Avg_Daily_Screen_Time_hr', palette='viridis', ax=ax1)
ax1.set_ylabel('Avg Screen Time (hours/day)')
ax1.set_xlabel('Age')
st.pyplot(fig1)
st.markdown("---")

# Visualization 2: Screen Time Distribution by Gender (Plotly for interactivity)
st.header("👩‍🦰👦 Screen Time Distribution by Gender")
fig2 = px.box(filtered_df, x='Gender', y='Avg_Daily_Screen_Time_hr', color='Gender', points="all",
              labels={"Avg_Daily_Screen_Time_hr": "Screen Time (hours/day)"}, title="Screen Time by Gender")
st.plotly_chart(fig2)
st.markdown("---")

# Visualization 3: Screen Time by Locality
st.header("🗺️ Average Screen Time by Locality")
avg_screen_time_by_locality = filtered_df.groupby('Urban_or_Rural')['Avg_Daily_Screen_Time_hr'].mean().reset_index()
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(data=avg_screen_time_by_locality, x='Urban_or_Rural', y='Avg_Daily_Screen_Time_hr', palette='magma', ax=ax3)
ax3.set_ylabel('Avg Screen Time (hours/day)')
ax3.set_xlabel('Locality')
st.pyplot(fig3)
st.markdown("---")

# Visualization 4: Primary Device Usage
st.header("🔌 Primary Device Usage Counts")
device_counts = filtered_df['Primary_Device'].value_counts().reset_index()
device_counts.columns = ['Primary_Device', 'Count']
fig4 = px.bar(device_counts, x='Primary_Device', y='Count', color='Primary_Device',
              labels={'Count': 'Number of Children', 'Primary_Device': 'Device'}, title="Device Usage",
              color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig4)
st.markdown("---")

# Visualization 5: Health Impact Counts
st.header("🩺 Reported Health Impacts")
health_impact_counts = filtered_df['Health_Impacts'].value_counts().reset_index()
health_impact_counts.columns = ['Health_Impacts', 'Count']
fig5 = px.bar(health_impact_counts, x='Count', y='Health_Impacts', color='Health_Impacts',
              orientation='h', title="Health Impacts Reported", labels={'Count':'Count', 'Health_Impacts':'Health Issue'},
              color_discrete_sequence=px.colors.diverging.Tealrose)
st.plotly_chart(fig5)
st.markdown("---")

# Add a closing emoji footer
st.markdown("#### Thank you for exploring! 🚀")
st.markdown("##### Made with Streamlit | Powered by Python 🐍")
