
import sqlalchemy
import os
import psycopg2

from sqlalchemy import create_engine
from dotenv import load_dotenv

# 
# dbname = os.getenv("DB_NAME")
# user = os.getenv("DB_USER")
# password = os.getenv("DB_PASSWORD")
# host = os.getenv("DB_HOST")
# port = os.getenv("DB_PORT")

# conn = psycopg2.connect(
#     dbname=dbname,
#     user=user,
#     password=password,
#     host=host,
#     port=port
# )

load_dotenv()
# 1) Connect to the database here using the SQLAlchemy's create_engine function

connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
try:
    connection = engine.connect()
    print("Connected to the database!")
except Exception as e:
    print(f"Error: {e}")
    # createdb -h localhost -U gitpod estadisticasNBA
# psql -h 127.0.0.1 -p 5432 -U gitpod -W -d estadisticasNBA
#psql -h 127.0.0.1 -p 5432 -U gitpod -W postgres -d estadisticasNBA
