# <ins>Screen-time-analysis</ins>
Indian Kids' Daily Screen Time analysis through various platform's usage and their localities. Their screen time were analysed and their health impacts are considered.
## <ins>Dataset</ins>
The dataset are inputted through Kaggle (indian-kids-screentime-2025). 
## <ins>JupyterLab</ins>
The model is created in JupyterLab by using Python coding language.

## <ins>Process of analysis</ins>
1. The dataset should be downloaded to local network in which we code (PC, Local server, or development machine) to ensure fast, offline access.
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
7. Using 'matplotlib' library, create a bar graph for 'Average Screen Time By Age':
   Hue: hue=age_group_mean.index
   Explanation:
   The hue here is set to the age group categories (e.g., age ranges like 8-10, 11-13, etc.), so each bar in the plot has a distinct color representing each age group.
   This enhances visual separation of age groups, making it easier to compare average screen time across different age categories through color coding.
   ```
   plt.figure(figsize=(8,5))
   sns.barplot(
    x=age_group_mean.index,
    y=age_group_mean.values,
    hue=age_group_mean.index,  # Needed for palette
    palette="viridis",
    legend=False
    )
8. Using 'matplotlib' library, create a boxplot for 'Screen Time Distribution by Gender':
   Hue: hue="Gender"
   Explanation:
   The hue is set to the gender of the children ("Gender" column), so the plot uses different colors for each gender category (e.g., Male, Female).
   This allows the boxplots to be color-coded by gender, highlighting differences in screen time distribution between genders clearly.
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
9. Using 'matplotlib' library, create a distribution plot for 'Distribution of Screen Time (Hours)':
   Hue: Not used (single continuous variable histogram)
   Explanation:
   There is no hue here since it’s a histogram of a single numeric variable.
   It shows the overall distribution of average daily screen time regardless of any category, hence no color grouping.
   ```
    plt.figure(figsize=(6,4))
    sns.histplot(df["Avg_Daily_Screen_Time_hr"], bins=10, kde=True, color="skyblue")
10. Using 'matplotlib' library, create a distribution plot for 'Primary Screen Device Usage Count':
    Hue: hue="Primary_Device"
    Explanation:
    Here hue is set to the device type used primarily by children (e.g., smartphone, tablet, etc.). Each device category gets its own color in the count bars.
    This makes it easy to visually differentiate device usage counts by color and see which devices are more popular.
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
11. Using 'matplotlib' library, create a distribution plot for 'Health Impacts Report':
    Hue: hue="Health_Impacts"
    Explanation:
    The hue corresponds to various health impact categories reported (e.g., eyesight issues, headaches, etc.). Each category is shown in a different color in the count bars tuned horizontally.
    Coloring by health impact helps quickly compare how many children report each type of health effect.
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
12. Using 'matplotlib' library, create a distribution plot for 'Children Exceed Recommended Screen Time Limits':
    Hue: hue="Exceeded_Recommended_Limit"
    Explanation:
    The hue uses the binary indicator showing whether children exceed recommended limits (0 = No, 1 = Yes).
    This visually separates the counts of children who do and do not exceed screen time limits, clarifying the proportion in each group by color.
    ```
    plt.figure(figsize=(5,4))
    sns.countplot(
    data=df,
    x="Exceeded_Recommended_Limit",
    hue="Exceeded_Recommended_Limit",
    palette="Set1",
    legend=False
    )
13. Create a folder as 'Screen-Time-app' for creating a web application for the model.
14. Create a python file inside the folder as 'app.py'.
15. Using Streamlit, make a web application with necessary codes:
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
   ---
   Add the necessary model code and 'plt.' codes.

16. Save it and open Prompt.
17. Mention the path directory and paste the code.
    ```
    streamlit run app.py
18. The web app would run.

## Creating Repository
1. Install GitHub Desktop.
2. Shift all the files to the folder of Github.
3. Push the files.
4. All the files would be loaded in GitHub.
5. In Streamlit Cloud Community, Click -> 'Create App', mention the repo and the app file.
6. Deploy, The app is ready for public view.

The project ends here.
