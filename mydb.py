import mysql.connector       


dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'DDD44'

	)


# Prepare a cursor object
cursorObject = dataBase.cursor()


#Create a database
cursorObject.execute('CREATE DATABASE crm')

print('All Done!')
