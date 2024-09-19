# Description:
# Print values for 'Team', 'Yellow Cards', and 'Red Cards' columns.
 
# Imports
import pandas as pd
 
# Variables
excel_file = 'C:/Users/Angelo Ponniah/Downloads/Euro_2012_stats_TEAM.xlsx'
 
# Logic
df = pd.read_excel(excel_file)
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
 
# Output
print(selected_columns)  # Print the selected columns