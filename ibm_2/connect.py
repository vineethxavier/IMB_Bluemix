import pymysql

def authenticate(username,password):
	#con = pymysql.connect('us-cdbr-iron-east-04.cleardb.net','bbbffad4fe31c5', '8316136d', 'ad_8a13ced370b5e57');
	con = pymysql.connect('','', '', '');
	with con:
		cursor = con.cursor()  #result of query
		query = ("SELECT username, password FROM user WHERE username = %s AND password = %s")
	try:
	# Execute the SQL command
		cursor.execute(query, (username, password))
   # Commit your changes in the database
		con.commit()
	except:
   # Rollback in case there is any error
		con.rollback()
    # check if user exists and login matches password
	flag=0
	for (username, password) in cursor:
		flag=1
	if(flag):
		return "true"
	else:
		return "false"
	cursor.close()


def insert(username,filename,filecontent,filesize):
	#con = pymysql.connect('us-cdbr-iron-east-04.cleardb.net','bbbffad4fe31c5', '8316136d', 'ad_8a13ced370b5e57');
	con = pymysql.connect('','', '', '');
	print "hiddd"
	with con:
		cursor = con.cursor()  #result of query
		query = ("INSERT into filestorage (username,filename,filecontent,filesize) values (%s,%s,%s,%s)")
		print "2222hidddssfsfsfs"
	try:
	# Execute the SQL command
		cursor.execute(query,(username,filename,filecontent,filesize))
		print "3333333"
   # Commit your changes in the database
		con.commit()
	except:
   # Rollback in case there is any error
		con.rollback()
    # check if user exists and login matches password
	
	cursor.close()
