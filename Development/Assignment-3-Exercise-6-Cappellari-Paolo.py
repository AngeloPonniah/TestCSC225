# Description:
# Print values for 'Team' and 'Shooting Accuracy' for England, Italy, and Spain.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'
teams_to_select = ['England', 'Italy', 'Spain']
 
# Logic
df = pd.read_excel(excel_file)
selected_teams = df[df['Team'].isin(teams_to_select)][['Team', 'Shooting Accuracy']]
 
# Output
print(selected_teams)  # Print 'Team' and 'Shooting Accuracy' for the selected teams