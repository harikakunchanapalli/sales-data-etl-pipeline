import pandas as pd 
df=pd.read_csv("sales.csv")
print("Raw data Loaded")
print(df.head())
#handle nulls
df['category']=df['category'].fillna("Unknown")
df['region']=df['region'].fillna("Unknown")
#convert data types
df['price']=df['price'].astype(int)
df['quantity']=df['quantity'].astype(int)
df['date']=pd.to_datetime(df['date'])
#add new column 
df['total_amount']=df['price']*df['quantity']
print("cleaned data:")
print(df.head())
df.to_csv("sales_cleaned.csv",index=False)
print("cleaned file saved as sales_cleaned.csv")

