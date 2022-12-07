import pyodbc

import pandas as pd
import numpy as np

# GET DATA FROM LOCAL SQL SERVER
server = 'VN-PF2T7JW7'
database = 'test'
username = 'sa'
password = '12345678'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

tsql = "SELECT * FROM Employees;"
data = pd.read_sql(tsql, cnxn)
print(data.values)
print(data['EmployeeID'].values)


