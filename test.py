import pandas as pd 
from ConnectionToDB.Connect import ConnectionToMSSQL


connect = ConnectionToMSSQL('apartments')
data = pd.read_sql(f"SELECT id, name FROM district", connect.engine).set_index('id')
data.to_csv('district.csv')
data = pd.read_sql(f"SELECT * FROM ViewAllInfoKeysAndData", connect.engine)
data.to_csv('data.csv')
data = pd.read_sql(f"SELECT id, name FROM numRoom", connect.engine).set_index('id')
data.to_csv('numRoom.csv')