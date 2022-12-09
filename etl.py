import pymssql
import sqlalchemy

import pandas as pd
import numpy as np
import time

start = time.time()
## GET DATA FROM REMOTE SQL SERVER
# conn = pymssql.connect(
#     host=r'10.0.11.174',
#     user=r'int-reader',
#     password=r'vm1dta12#'+'$',
#     database='INT77DB_R212FT'
# )
# cursor = conn.cursor(as_dict=True)
# cursor.execute('select * from covrpf')
# data = cursor.fetchall()
# data_df = pd.DataFrame(data)
# conn.close()

## INSERT DATA INTO LOCAL SQL SERVER
# engine = sqlalchemy.create_engine("mssql+pyodbc://sa:12345678@VN-PF2T7JW7:1433/test?driver=ODBC+Driver+17+for+SQL+Server")
# data_df.to_sql("covrpf", engine)

## GET DATA FROM LOCAL SQL SERVER

# conn = pymssql.connect(
#     host=r'VN-PF2T7JW7',
#     user=r'sa',
#     password=r'12345678',
#     database='test'
# )
# cursor = conn.cursor(as_dict=True)
# cursor.execute('select * from chdrpf')
# data = cursor.fetchall()
# chdrpf_df = pd.DataFrame(data)
# cursor.execute('select * from covrpf')
# data = cursor.fetchall()
# covrpf_df = pd.DataFrame(data)

# merge_df = chdrpf_df.merge(covrpf_df, how='in', on='chdrnum')
# print(chdrpf_df.head())
# print(covrpf_df.head())

# conn.close()

## GET DATA WITH TRANSFORM FROM LOCAL SQL SERVER
conn = pymssql.connect(
    host=r'VN-PF2T7JW7',
    user=r'sa',
    password=r'12345678',
    database='test'
)
cursor = conn.cursor(as_dict=True)
query = ''' select count(*) count
from chdrpf ch inner join covrpf co
on ch.chdrnum = co.chdrnum'''
cursor.execute(query)
data = cursor.fetchall()
df = pd.DataFrame(data)

print(df)

conn.close()

end = time.time()
line = f'Whole process takes {end - start}'
print(line)