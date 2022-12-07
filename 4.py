import pymssql

import pandas as pd
import numpy as np


# INSERT DATA INTO LOCAL SQL SERVER
conn = pymssql.connect(
    host=r'127.0.0.1',
    user=r'sa',
    password=r'12345678',
    database='test'
)
cursor = conn.cursor(as_dict=True)
cursor.execute("Insert into Employees values ('14', 'Tuan', 'Nguyen', '6')")
conn.commit()
conn.close()

