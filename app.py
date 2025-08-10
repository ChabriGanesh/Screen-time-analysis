import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# Get the directory of the current file (app.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Build the file path relative to app.py
FILE_PATH = os.path.join(BASE_DIR, "Indian_Kids_Screen_Time.csv")
@st.cache_data
def load_data():
    df = pd.read_csv(FILE_PATH)
    return df

df = load_data()
st.title("Indian Kids' Screen Time Analysis")
st.markdown("""
Explore and analyze screen time patterns of Indian children aged 8 to 18 years.
Use the filters below to refine the data.
""")
# Sidebar filters
st.sidebar.header("Filter Data")
age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
age_range = st.sidebar.slider("Select Age Range", age_min, age_max, (age_min, age_max))

genders = df['Gender'].unique().tolist()
selected_genders = st.sidebar.multiselect("Select Gender", options=genders, default=genders)

localities = df['Urban_or_Rural'].unique().tolist()
selected_localities = st.sidebar.multiselect("Select Locality", options=localities, default=localities)

filtered_df = df[
    (df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1]) &
    (df['Gender'].isin(selected_genders)) &
    (df['Urban_or_Rural'].isin(selected_localities))
]

st.write(f"Showing {len(filtered_df)} records matching filters")

# Display filtered data table
st.dataframe(filtered_df)

# Visualization 1: Average Screen Time by Age
st.subheader("Average Screen Time by Age")
avg_screen_time_by_age = filtered_df.groupby('Age')['Avg_Daily_Screen_Time_hr'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8,4))
sns.barplot(data=avg_screen_time_by_age, x='Age', y='Avg_Daily_Screen_Time_hr', palette='viridis', ax=ax1)
ax1.set_ylabel('Avg Screen Time (hours/day)')
ax1.set_xlabel('Age')
st.pyplot(fig1)

# Visualization 2: Screen Time Distribution by Gender (Plotly for interactivity)
st.subheader("Screen Time Distribution by Gender")
fig2 = px.box(filtered_df, x='Gender', y='Avg_Daily_Screen_Time_hr', color='Gender', points="all",
              labels={"Avg_Daily_Screen_Time_hr": "Screen Time (hours/day)"}, title="Screen Time by Gender")
st.plotly_chart(fig2)

# Visualization 3: Screen Time by Locality
st.subheader("Average Screen Time by Locality")
avg_screen_time_by_locality = filtered_df.groupby('Urban_or_Rural')['Avg_Daily_Screen_Time_hr'].mean().reset_index()
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.barplot(data=avg_screen_time_by_locality, x='Urban_or_Rural', y='Avg_Daily_Screen_Time_hr', palette='magma', ax=ax3)
ax3.set_ylabel('Avg Screen Time (hours/day)')
ax3.set_xlabel('Locality')
st.pyplot(fig3)

# Visualization 4: Primary Device Usage
st.subheader("Primary Device Usage Counts")
device_counts = filtered_df['Primary_Device'].value_counts().reset_index()
device_counts.columns = ['Primary_Device', 'Count']

fig4 = px.bar(device_counts, x='Primary_Device', y='Count', color='Primary_Device',
              labels={'Count': 'Number of Children', 'Primary_Device': 'Device'}, title="Device Usage")
st.plotly_chart(fig4)

# Visualization 5: Health Impact Counts
st.subheader("Reported Health Impacts")
health_impact_counts = filtered_df['Health_Impacts'].value_counts().reset_index()
health_impact_counts.columns = ['Health_Impacts', 'Count']

fig5 = px.bar(health_impact_counts, x='Count', y='Health_Impacts', color='Health_Impacts',
              orientation='h', title="Health Impacts Reported", labels={'Count':'Count', 'Health_Impacts':'Health Issue'})
st.plotly_chart(fig5)
