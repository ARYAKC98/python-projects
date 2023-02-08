# import pymysql
# db=pymysql.connect(host='localhost',user='root',password='mysql123456',database='jan_test')
# con=db.cursor()
# sqlquery="insert into t2 values(%s,%s,%s)"
# val = (3,'megha',21)
# con.execute(sqlquery,val)
# db.commit()
# print('inserted')





import pymysql
id = int(input("enter the id:"))
na = input("enter the name:")
ag = int(input("enter the age:"))
db = pymysql.connect(host='localhost',user='root',password='mysql123456',database='jan_test')
mycursor = db.cursor()
sql = "insert into t2 values(%S,%s,%s)"
val = (id,na,ag)
mycursor.execut(sql,val)
db.commit()
print('inserted successfully')