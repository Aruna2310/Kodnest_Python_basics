#To connect python program with mysql database
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="root123",database="classroom")
sql="insert into class values(1,'Deepak'),(2,'Rahul')"
c=con.cursor()
c.execute(sql)
con.commit()



