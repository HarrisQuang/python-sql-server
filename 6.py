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
cursor.execute('Select top 5 * from chdrpf')
data = cursor.fetchall()
data_df = pd.DataFrame(data)
conn.close()
print(data_df)

