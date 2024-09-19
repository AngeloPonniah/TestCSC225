# Description:
# Print the values of the 'Goal' column from the Euro 2012 dataset.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'  # CSV file path
 
# Logic
df = pd.read_excel(excel_file)
goals = df['Goals']
 
# Output
print(goals)  # Print all values in the 'Goals' column
