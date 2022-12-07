import sqlalchemy

import pandas as pd
import numpy as np

# GET DATA FROM FLAT FILE AND INSERT INTO SQL SERVER
df = pd.read_excel('Book1.xlsx')
engine = sqlalchemy.create_engine("mssql+pyodbc://sa:12345678@VN-PF2T7JW7:1433/test?driver=ODBC+Driver+17+for+SQL+Server")

## write the DataFrame to a table in the sql database
df.to_sql("demo_compare_change", engine)

