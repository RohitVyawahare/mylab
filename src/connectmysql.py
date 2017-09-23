#python program to connect to mysql
import pymysql.cursors
import pymysql

# Connect to the database
db = pymysql.connect(host='localhost',
                             user='root',
                             password='zimbra',
                             db='zippy',
                             charset='utf8mb4')



try:
	# you must create a Cursor object. It will let
  	#  you execute all the queries you need
 	cur = db.cursor()
 	
 	# Use all the SQL you like
	cur.execute("SELECT * FROM employee")

	# print all the first cell of all the rows
	for row in cur.fetchall():
    	print row[0]

finally:
    db.close()