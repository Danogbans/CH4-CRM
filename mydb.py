import mysql.connector 


dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'DDD444ccc'

	)


# Prepare a cursor object
cursorObject = dataBase.cursor()


#Create a database
cursorObject.execute('CREATE DATABASE crm')

print('All Done!')
