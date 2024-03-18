
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cur = con.cursor()

res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

PLAYER_NAME, PTS = res.fetchone()
print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
