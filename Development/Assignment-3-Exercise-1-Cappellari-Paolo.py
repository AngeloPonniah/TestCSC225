# Description:
# Load data from the CSV file about Euro 2012 competition.
# This program loads the dataset and prints the first 5 rows to verify successful loading.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'  # CSV file path
 
# Logics
df = pd.read_excel(excel_file)
 
# Output
print(df.head())  # Display the first 5 rows of the DataFrame