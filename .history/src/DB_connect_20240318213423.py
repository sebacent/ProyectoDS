import sqlite3

# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")
con.execute("DROP TABLE IF EXISTS ESTADISTICAS;")
            
con.execute("""CREATE TABLE IF NOT EXISTS ESTADISTICAS
    (SEASON_YEAR CHAR(7) NOT NULL,
     PLAYER_ID BIGINT NOT NULL,
     PLAYER_NAME TEXT,
     NICKNAME VARCHAR(30),
     TEAM_ID INT NOT NULL,
     TEAM_ABBREVIATION CHAR(5),
     TEAM_NAME TEXT,
     GAME_ID CHAR(10) NOT NULL,
     GAME_DATE CHAR(10),
     MATCHUP CHAR(12),
     WL CHAR(1),
     MIN REAL,
     FGM INT,
     FGA INT,
     FG_PCT REAL,
     FG3M INT,
     FG3A INT,
     FG3_PCT REAL,
     FTM INT,
     FTA INT,
     FT_PCT REAL,
     OREB INT,
     DREB INT,
     REB INT,
     AST INT,
     TOV INT,
     STL INT,
     BLK INT,
     BLKA INT,
     PF INT,
     PFD INT,
     PTS INT,
     PLUS_MINUS INT,
     AVAILABLE_FLAG INT,
     PTSRTeam INT,
     PTSTeam INT,
     W_PCTTeam REAL,
     HOME_AWAY CHAR(1),
     MIN_PROM REAL,
     FGM_PROM REAL,
     FGA_PROM REAL,
     FG_PCT_PROM REAL,
     FG3M_PROM REAL,
     FG3A_PROM REAL,
     FG3_PCT_PROM REAL,
     FTM_PROM REAL,
     FTA_PROM REAL,
     FT_PCT_PROM REAL,
     OREB_PROM REAL,
     DREB_PROM REAL,
     REB_PROM REAL,
     AST_PROM REAL,
     TOV_PROM REAL,
     STL_PROM REAL,
     BLK_PROM REAL,
     BLKA_PROM REAL,
     PF_PROM REAL,
     PFD_PROM REAL,
     PTS_PROM REAL,
     PLUS_MINUS_PROM REAL,
     PTSRTeam_PROM REAL,
     PTSTeam_PROM REAL,
     W_PCTTeam_PROM REAL,
     PRIMARY KEY (SEASON_YEAR, PLAYER_ID, TEAM_ID, GAME_ID)
     );""")

con.close()
