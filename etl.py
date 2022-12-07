import pymssql
import sqlalchemy

import pandas as pd
import numpy as np

# GET DATA FROM REMOTE SQL SERVER
conn = pymssql.connect(
    host=r'10.0.11.174',
    user=r'int-reader',
    password=r'vm1dta12#'+'$',
    database='INT77DB_R212FT'
)
cursor = conn.cursor(as_dict=True)
cursor.execute('select * from chdrpf')
data = cursor.fetchall()
data_df = pd.DataFrame(data)
conn.close()

# INSERT DATA INTO LOCAL SQL SERVER
engine = sqlalchemy.create_engine("mssql+pyodbc://sa:12345678@VN-PF2T7JW7:1433/test?driver=ODBC+Driver+17+for+SQL+Server")
data_df.to_sql("chdrpf", engine)