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
6. Save the datas as dataframes through pandas library by this:
          ```python
          df = pd.read_csv(r"C:\Users\Chabri Ganesh\Indian_Kids_Screen_Time.csv")  
          print("📊 Data Preview:")
          print(df.head())
          print("\n📈 Summary Stats:")
          print(df.describe())
8.  
