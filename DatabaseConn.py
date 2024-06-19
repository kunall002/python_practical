import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kunal')
print(mydb.connection_id)

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kunal')
cur=mydb.cursor()
cur.execute("create database kunal")

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kunal',database='kunal')
cur=mydb.cursor()
s="create table book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='kunal',database='kunal')
cur=mydb.cursor()
s="insert into book(bookid,title,price)values(%s,%s,%s)"
b1=(2,'java',345)
cur.execute(s,b1)
mydb.commit()