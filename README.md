# <ins>Screen-time-analysis</ins>
Indian Kids' Daily Screen Time analysis through various platform's usage and their localities. Their screen time were analysed and their health impacts are considered.
## <ins>Dataset</ins>
The dataset are inputted through Kaggle (indian-kids-screentime-2025). 
## <ins>JupyterLab</ins>
The model is created in JupyterLab by using Python coding language.

## <ins>Process of analysis</ins>
1. The dataset should be downloaded to local network in which we code (PC, ocal server, or development machine) to ensure fast, offline access.
2. Specify the directory for the dataset to apply in the analysis.
3. Create a notebook in JupyterLab for the analysis with the extension .jpynb (if it is Jupyter only).
4. Install the accurate packages which are needed for analysis.
5. After installing, import the necessary libraries.
6. Save the datas as dataframes through 'pandas' library by this:
   ```
   df = pd.read_csv(r"C:\Users\Chabri Ganesh\Indian_Kids_Screen_Time.csv")
   print("📊 Data Preview:")
   print(df.head())
   print("\n📈 Summary Stats:")
   print(df.describe())
8. Using 'matplotlib' library, create a bar graph for 'Average Screen Time By Age':
   ```
   plt.figure(figsize=(8,5))
   sns.barplot(
    x=age_group_mean.index,
    y=age_group_mean.values,
    hue=age_group_mean.index,  # Needed for palette
    palette="viridis",
    legend=False
    )
9. Using 'matplotlib' library, create a boxplot for 'Screen Time Distribution by Gender':
    ```
    plt.figure(figsize=(6,4))
    sns.boxplot(
    x="Gender",
    y="Avg_Daily_Screen_Time_hr",
    hue="Gender",           # For palette colors per category
    data=df,
    palette="pastel",
    legend=False
   )
10. Using 'matplotlib' library, create a distribution plot for 'Distribution of Screen Time (Hours)':
    ```
    plt.figure(figsize=(6,4))
    sns.histplot(df["Avg_Daily_Screen_Time_hr"], bins=10, kde=True, color="skyblue")
11.  Using 'matplotlib' library, create a distribution plot for 'Primary Screen Device Usage Count':
     ```
    plt.figure(figsize=(8,5))
    sns.countplot(
    data=df,
    x="Primary_Device",
    hue="Primary_Device",
    palette="Set2",
    order=df["Primary_Device"].value_counts().index,
    legend=False
    )
12.  Using 'matplotlib' library, create a distribution plot for 'Health Impacts Report':
     ```
    plt.figure(figsize=(10,5))
    sns.countplot(
    data=df,
    y="Health_Impacts",
    hue="Health_Impacts",
    order=df["Health_Impacts"].value_counts().index,
    palette="coolwarm",
    legend=False
    )
13. Using 'matplotlib' library, create a distribution plot for 'Children Exceed Recommended Screen Time Limits':
     ```
    plt.figure(figsize=(5,4))
    sns.countplot(
    data=df,
    x="Exceeded_Recommended_Limit",
    hue="Exceeded_Recommended_Limit",
    palette="Set1",
    legend=False
    )
14. Create a folder as 'Screen-Time-app' for creating a web application for the model.
15. Create a python file inside the folder as 'app.py'.
16. Using Streamlit, make a web application with necessary codes:
     ```
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    FILE_PATH = r"C:\Users\Chabri Ganesh\Indian_Kids_Screen_Time.csv"
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
   Add the necessary model code and 'plt.' codes.
17. Save it and open Prompt.
18. Mention the path directory and paste the code.
   
      streamlit run app.py
19. The web app would run.

## Creating Repository
1. Install GitHub Desktop.
2. Shift all the files to the folder of Github.
3. Push the files.
4. All the fiels would be loaded in GitHub.
5. In Streamlit Cloud Community, Click -> 'Create App', mention the repo and the app file.
6. Deploy, The app is ready for public view.

The project ends here.
