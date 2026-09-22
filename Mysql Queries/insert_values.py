#PS D:\Data Science> pip install mysql-connector-python

import mysql.connector
#print(mysql.connector.__version__)

connection=mysql.connector.connect(host="localhost",user="root",password="goookul8393#",database="company_db")
print(connection.is_connected())

#cursor=connection.cursor()

cursor=connection.cursor(dictionary=True)    #to get data with column name

# cursor.execute("insert into employees (name, department, designation, salary, join_date, city, email , experience_years, is_active) values ('gokul raj c', 'development', 'developer', 25000, '2022-06-18','Kochi', 'gokul@tech.com', 0, 1);")

# connection.commit()   # to insert,update,delete values use commit()



# insert data with user input
# name=input("enter user name: ")
# depmt=input("enter department: ")
# desig=input("enter designation ")
# salary=int(input("enter salary: "))
# join_date=input("enter join date: ")
# city=input("enter city: ")
# email=input("enter email: ")
# exp=int(input("enter no of experience years: "))

# cursor.execute(f"insert into employees (name, department, designation, salary, join_date, city, email , experience_years, is_active) values ('{name}','{depmt}','{desig}',{salary},'{join_date}','{city}','{email}',{exp},1);")


emp_id=int(input("enter user id: "))
#cursor.execute(f"update employees set is_active=1 where emp_id={emp_id}")

cursor.execute(f"delete from employees where emp_id={emp_id}")

connection.commit()