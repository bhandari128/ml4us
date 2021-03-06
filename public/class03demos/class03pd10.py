# class03pd10.py

# This script should mimic the SQL listed below:

# SELECT COUNT(cdate) FROM prices;
# SELECT COUNT(lowp)  FROM prices;
# SELECT COUNT(*)     FROM prices;
# SELECT MIN(cdate),MIN(closep),MIN(volume) FROM prices;
# SELECT MAX(closep),MAX(volume), AVG(closep),AVG(volume) FROM prices;

# SQL lacks the ability to get data from the web.
# Pandas can get data from the web:

import pandas as pd

prices_df = pd.read_csv('http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC')
prices_df.columns = ['cdate','openp','highp','lowp','closep','volume','adjp']

# Mimic
# SELECT COUNT(cdate) FROM prices;
print(len(prices_df.cdate))

# Mimic
# SELECT COUNT(lowp) FROM prices;
print(len(prices_df.lowp))

# Mimic
# SELECT COUNT(*) FROM prices;
print(len(prices_df))

# Mimic
# SELECT MIN(cdate),MIN(closep),MIN(volume) FROM prices;
print(prices_df.cdate.min(), prices_df.closep.min(), prices_df.volume.min())

# Mimic
# SELECT MAX(closep),MAX(volume), AVG(closep),AVG(volume) FROM prices;
print(prices_df.closep.max(),prices_df.volume.max(),prices_df.closep.mean(),prices_df.volume.mean())

'bye'

