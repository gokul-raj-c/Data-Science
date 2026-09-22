#PS D:\Data Science> pip install mysql-connector-python

import mysql.connector
#print(mysql.connector.__version__)

connection=mysql.connector.connect(host="localhost",user="root",password="goookul8393#",database="company_db")
print(connection.is_connected())

#cursor=connection.cursor()

cursor=connection.cursor(dictionary=True)    #to get data with column name

cursor.execute("select * from employees;")
#data=cursor.fetchall()   #list of tuple
# data=cursor.fetchone()
# print(data)

# for i in data:
#     print(i)
    
# cursor.close()

#value is returned as list of tuples
#each tuple indicate a row


# data=cursor.fetchone()
# print(data)
# data1=cursor.fetchone()
# print(data1)

# data3=cursor.fetchmany(5)
# print(data3)

# c=cursor.rowcount   #no of rows fetched
# print(c)


data=cursor.fetchall()
for i in data:
    print(i['name'])
