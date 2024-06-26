import pandas as pd

## Script para importar los diccionarios y utilizarlos en la app.

players = pd.read_csv(r'C:\Users\sebas\Documents\Repositorio_DS\ProyectoDS\data\raw\data_complete_raw.csv')



#Se crean diccionarios para el nombre de los equipos y su abreviación, y para el nombre de los jugadores

team_name_dict = players.groupby('TEAM_ID')['TEAM_NAME'].first().to_dict()
team_abbre_dict = players.groupby('TEAM_ID')['TEAM_ABBREVIATION'].first().to_dict()
players_dict = players.groupby('PLAYER_ID')['PLAYER_NAME'].first().to_dict()
