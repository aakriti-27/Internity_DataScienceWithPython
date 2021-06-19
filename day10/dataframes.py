#Accessing , Indexing and Slicing dataframes  

import pandas as pd
  
marks_list = [['Kuldeep', 80, 75, 88], 
               ['Gauri', 88, 74, 75], 
               ['Naman', 78, 70, 68],
               ['Prakhar', 85, 80, 82], 
               ['Ritika', 95,100, 99],
               ['Sahil', 70, 72, 80],
               ['Harshit', 80, 85, 90]]       # Initializing the nested list with Data set

df = pd.DataFrame(marks_list, columns=['Name', 'Physics_Marks', 'Chemistry_Marks', 'Maths_Marks'])    #creating dataframe
print(df)

#Dataframe.iloc[] is used to retrieve rows from a Data frame.
#used when the index label of a data frame is something other than numeric series of 0, 1, 2, 3….n
df1 = df.iloc[0:4]
print(df1)
  
df1 = df.iloc[:,0:2]    #slicing column
print(df1)

#indexing dataframe
df = pd.DataFrame(marks_list, columns=['Name', 'Physics_Marks', 'Chemistry_Marks', 'Maths_Marks'],index=[8180,8181,8182,8183,8184,8185,8186]) 
print(df)

df1 = df.loc[:,['Name','Maths_Marks']]    #slicing column
print(df1)

df1 = df.loc[[8180,8183],:]
print(df1)
