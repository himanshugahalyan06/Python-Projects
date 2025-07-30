import mysql.connector as mc                        
databse= mc.connect (        ## ✅ All parameter names must be lowercase: host, user, password, database. always 
    host='localhost',
    user='Himanshu',        ## we only write string in single comma in mysql 
    password='Himanshu2006',
    database='employee',
    allow_local_infile=True   # ✅ Required for LOAD DATA LOCAL INFILE
)

cursor= databse.cursor()
cursor.execute("create database employee")
print("Database Created Successfuly !!")

cursor.execute(" use employee")
print("DataBase Selected !!")

cursor.execute("""
create table employee_data (Emp_ID int,Emp_Name varchar(500)
,Emp_Company varchar(500)
,Emp_Salary int
,Emp_Age int
,Emp_Country varchar(500)
)
""")

print("Table Created Successfully !!")

## Fastest way to load data in databse 

query="""
LOAD DATA LOCAL INFILE 'C:/Users/Himanshu/OneDrive/Desktop/Summer Internship 2025/Data Base (My SQL)/employee_data.csv'
INTO TABLE employee_data
FIELDS TERMINATED BY ','          
ENCLOSED BY '"'
LINES TERMINATED BY '\\n'
IGNORE 1 ROWS
(Emp_ID, Emp_Name, Emp_Company, Emp_Salary, Emp_Age, Emp_Country)
"""
try:
    cursor.execute(query)
    databse.commit()
    print("Data Entered Successfully !!")
except Exception as e:
    print("Error while executing query:", e)
finally:
    cursor.close()
    databse.close()
    print("Object is Closed and Database is alos Closed Successfully !!")

## 🔍 What is next() in Python?
##next() is a built-in Python function used to get the next item from an iterator
#  (like a file, a list, or a CSV reader).
