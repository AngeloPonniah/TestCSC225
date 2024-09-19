# Description:
# Find and print rows for teams that scored more than 6 goals and at least 4000 passes.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'
 
# Logic
df = pd.read_excel(excel_file)
teams_with_criteria = df[(df['Goals'] > 6) & (df['Passes'] >= 4000)]
 
# Output
print(teams_with_criteria)  # Print rows that meet the goals and passes criteria