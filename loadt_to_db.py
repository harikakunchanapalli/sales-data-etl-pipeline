import pandas as pd
import sqlite3

#load cleaned CSV
df=pd.read_csv("sales_cleaned.csv")
print("Cleaned data loaded")

#connect to SQLite DB
conn=sqlite3.connect("sales.db")
cursor=conn.cursor()

#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
order_id INTEGER,
product TEXT,
category TEXT,
price INTEGER,
quantity INTEGER,
date TEXT,
region TEXT,
total_amount INTEGER
)""")

#insert data into table
df.to_sql("sales",conn,if_exists='replace',index=False)

#close connection
conn.commit()
conn.close()
print("Data loaded into sales.db successfully")

