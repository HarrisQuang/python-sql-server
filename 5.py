import pymssql

import pandas as pd
import numpy as np


# CREATE TABLE IN LOCAL SQL SERVER
create_tbl = "create table demo_compare_change (cate varchar, day int, month int, year int, value real)"
conn = pymssql._mssql.connect(
    server=r'127.0.0.1',
    user=r'sa',
    password=r'12345678',
    database='test')
conn.execute_non_query(create_tbl)
conn.close()

