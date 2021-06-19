#Reading and writing Excel files
#install - pip install openpyxl xlsxwriter xlrd

import pandas as pd

df = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6,7],
   'Name': ['Rita', 'Vinit', 'Naman', 'Sarika', 'Mayank','Dev','Gauri'],
   'Subject':['CS','Physics','Chemistry','Geology','Maths','English','Economics']})

df.to_excel('./student.xlsx', sheet_name='student1', index=False)   #to_excel() function to write the contents to a file
print(df)

df1 = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6],
   'Name': ['Samar', 'Preeti', 'Tushar', 'Harshita', 'Deeksha','Dev'],
   'Subject':['Maths','Chemistry','Physics','Geology','CS','English']})

sheets = {'Student1': df, 'Student2': df1}
writer = pd.ExcelWriter('./s1.xlsx', engine='xlsxwriter')

for sheet_name in sheets.keys():     #writing multiple dataframe
    sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

writer.save()

student2 = pd.read_excel('./s1.xlsx')
print(student2.head())    #reading first 5 rows

student2 = pd.read_excel('./s1.xlsx', sheet_name='Student2', index_col='roll_no') #reading from a particular sheet
print(student2.head())    #reading first 5 rows

cols = [0, 2]
st = pd.read_excel('./s1.xlsx', usecols=cols)   #reading specific column
print(st.head())

#Reading and writing CSV file

file = pd.read_csv('data1.csv')   #reading csv file
print(file.head())

col_names = ['Pulse','Calories']
file1 = pd.read_csv('data1.csv', usecols=col_names)   #reading specific columns of csv file
print(file1.head())

file1 = pd.read_csv('data1.csv', names=col_names, skiprows=[0,2])   #skip rows while reading from csv file
print(file1.head())

df = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6,7],
   'Name': ['Rita', 'Vinit', 'Naman', 'Sarika', 'Mayank','Dev','Gauri'],
   'Subject':['CS','Physics','Chemistry','Geology','Maths','English','Economics']})
df.to_csv('student.csv')               #writing a dataframe to csv file

df = pd.DataFrame({
   'roll_no':[1,2,3,4,5,6,7],
   'Name': ['Rita', 'Vinit', 'Naman', 'Sarika', 'Mayank','Dev','Gauri'],
   'Subject':['CS','Physics','Chemistry','Geology','Maths','English','Economics']}, columns=['roll_no','Name','Subject'])
new_column_names = ['college_roll_no','Name','Subject']
df.to_csv('student.csv', index=False, header=new_column_names)   #customising headers

#Reading and writing a JSON file

patients = {
         "Name":{"0":"John","1":"Nick","2":"Ali","3":"Joseph"},
         "Gender":{"0":"Male","1":"Male","2":"Female","3":"Male"},
         "Nationality":{"0":"UK","1":"French","2":"USA","3":"Brazil"},
         "Age" :{"0":10,"1":25,"2":35,"3":29}   #
}
import json
with open('patients.json', 'w') as f:  
    json.dump(patients, f)      #writing a JSON file

df = pd.read_json('patients.json')    #reading JSON file
print(df.head())

import seaborn as sns
dataset = sns.load_dataset('tips')   #creating a JSON file from the tips dataset, which is included in the Seaborn library for data visualization
print(dataset.head())
dataset.to_json('tips.json')    #saving its content into JSON file


