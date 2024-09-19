""""
Write a python program that reads an excel file into a pandas dataframe
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # for plotting
# Replace 'your_file.xlsx' with the path to your Excel file
excel_file = 'C:/Users/Angelo Ponniah/Downloads/games.xlsx'

# Read the Excel file into a DataFrame
df_games = pd.read_excel(excel_file)

# Display the DataFrame
# print(df_games) #df.games.head() will display the first 5 rows of the DataFrame 
# you can use [['year','team']] to filter the columns
# you can use conditions as needed (df_games[df_games['year'] == 2019]) & (df_games[df_games['team'] == 'bears']) to filter the rows
df_team_avg = df_games.groupby('team') \
["wins"].agg(np.mean)
df_games.plot(x='year', y='team', kind='bar')

plt.show()