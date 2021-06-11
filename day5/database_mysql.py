#Python needs a MySQL driver - "MySQL Connector" to access the MySQL database.
import mysql.connector

mydb = mysql.connector.connect(       #creating connection
  host="localhost",
  user="root",
  password="",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE student_details")       #creating database

mydb = mysql.connector.connect(       #connecting with database
  host="localhost",
  user="root",
  password="tiger",
  database="student_details"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students (name VARCHAR(255), course VARCHAR(255), rollno INT(4) )")  #creating the table
mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")        #altering the table

sql = "INSERT INTO students (name, course, rollno) VALUES (%s, %s, %s)"
val = [
  ('Anjali', 'Bsc(H) CS', 8176),
  ('Yash', 'Bsc(H) Physics', 8202),
  ('Vertika', 'Bsc(H) Chemistry', 7662),
  ('Manan', 'Bsc(H) CS', 8180),]

mycursor.executemany(sql, val)
mydb.commit()            #commit() required to make the changes, otherwise no changes are made to the table.
print(mycursor.rowcount, "was inserted.")
print("Last row inserted, ID:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM students")    #to select all the records of students table
myresult1 = mycursor.fetchone()
print(myresult1)

mycursor.execute("SELECT name, rollno FROM students")  #to select 2 columns name and rollno
myresult2 = mycursor.fetchall()
for x in myresult2:
  print(x)

sql = "SELECT * FROM students WHERE course ='Bsc(H) CS'"   #To select records where course='Bsc(H) CS'
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "SELECT name,course FROM students WHERE course LIKE '%CS%'"   #'%' represent wildcard characters
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#When query values are provided by the user, you should escape the values.
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
sql = "SELECT * FROM students WHERE course = %s"
c = ("Bsc(H) Physics",)
mycursor.execute(sql, c)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "SELECT * FROM students ORDER BY name"   #order acc. to name
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "SELECT * FROM students ORDER BY name DESC"   #order acc. to name in descending order 
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

sql = "DELETE FROM students WHERE course = %s"    #delete record
c = ("Bsc(H) Chemistry", )
mycursor.execute(sql, c)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

sql = "DROP TABLE IF EXISTS stu"          #to drop table
mycursor.execute(sql)

sql = "UPDATE students SET rollno = %s WHERE name = %s"       #update record
val = ("7415", "Yash")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

mycursor.execute("SELECT * FROM students LIMIT 2")     #limit the record sent by query
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor.execute("SELECT * FROM students LIMIT 2 OFFSET 1")   #Start from another position using OFFSET(index starts from 0)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE details (id_r INT(4), address VARCHAR(255))")
sql = "INSERT INTO details (id_r, address) VALUES (%s, %s)"
val = [
  (8176,'Bangalore'),
  (7662,'Delhi'),
  (8180,'Kanpur'),
  (8202,'Pune')]
mycursor.executemany(sql, val)
mydb.commit() 

#to join 2 tables
mycursor = mydb.cursor()
sql = "SELECT * FROM students INNER JOIN details ON students.rollno = details.id_r"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


