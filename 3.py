import pymssql

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
query = '''SELECT COLUMN_NAME, *
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA='vm1dta' 
    AND TABLE_NAME='chdrpf' and column_name = 'CHDRNUM';
'''

cursor.execute(query)
data = cursor.fetchall()
data_df = pd.DataFrame(data)
print(data_df)

cursor.close()



