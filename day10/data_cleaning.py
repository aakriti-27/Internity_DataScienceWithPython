#Data cleaning means fixing bad data in your data set.

import pandas as pd

#Cleaning empty cells
df = pd.read_csv('data.csv')
df1 = pd.read_csv('data1.csv')

df2 = df.dropna()   #removing rows that contain empty cells using dropna()
print(df2)

df.dropna(inplace = True)   #to change the original DataFrame  #returns nothing
df1.fillna(0, inplace = True)  #replacing empty value with 0
df2=df["High"].fillna(45)    #replacing only empty value of column High with 45
print(df2)
x = df["High"].median()
df2=df["High"].fillna(x)    #replacing only empty value of column High with median
print(df2)

x = df["High"].mean()
df2=df["High"].fillna(x)    #replacing only empty value of column High with mean
print(df2)

x = df["Low"].mode()[0]
df2=df["Low"].fillna(x)    #replacing only empty value of column High with mode(the value that appears most frequently)
print(df2)

#Cleaning data with wrong format

df1['Date'] = pd.to_datetime(df1['Date'])   #to correct the format of date in 'Date' column
print(df1['Date'])

df2=df.dropna(subset=['Date'])      #Remove rows with a NULL value in the 'Date' column
print(df2)

#Wrong data

df1.loc[2, 'Pulse'] = 112     #replacing values

for x in df1.index:
  if df1.loc[x, "Duration"] > 60:
    df1.loc[x, "Duration"] = 60   #replacing 'duration' if value is more than 60

for x in df1.index:
  if df1.loc[x, "Duration"] > 60:
    df1.drop(x, inplace = True)    #removing rows with wrong data

df1.drop_duplicates(inplace = True)   #to remove duplicates




