# Description:
# Find and print rows for teams that scored more than 6 goals.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'
 
# Logic
df = pd.read_excel(excel_file)
teams_more_than_6_goals = df[df['Goals'] > 6]
 
# Output
print(teams_more_than_6_goals)  # Print rows where teams scored more than 6 goals
