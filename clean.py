import pandas as pd
import sqlite3
df= pd.read_csv("upi_transactions_2024.csv")
df=df.dropna()
conn=sqlite3.connect("bank_data.db")
df.to_sql('transactions',conn,if_exists="replace",index=False)
print("Data saved to database!")
conn.close()

