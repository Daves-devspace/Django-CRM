import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password@123'
)
#prepare cursor object
cursorObject=dataBase.cursor()

#create database
cursorObject.execute("  CREATE  DATABASE daudi")
print('All done')