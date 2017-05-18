import hashlib
import os,csv,sys
import blueServer as obj1
from werkzeug import secure_filename
import swiftclient
import keystoneclient

from flask import Flask,render_template,request,url_for,redirect, session

app = Flask(__name__)

		   
@app.route("/")
def mainpage():
	return render_template('index.html')

@app.route("/loadfile",methods=['GET','POST'])
def loadfile():
	if request.method == 'POST':
		param1 = request.files['infile']
		#filename = secure_filename(file.infile)
		#file.save(os.path.join(app.config['FOLDER'], infile))
		#df = pd.read_csv(os.path.join(app.config['FOLDER'], infile)
		obj1.main(param1)
	return render_template('listfiles.html')
	
	
@app.route("/listfiles")
def listfile():
	auth_url = "https://identity.open.softlayer.com"+'/v3' #add "/v3" at the ending of URL
	password = ""
	project_id = ""
	user_id = ""
	region_name = ""
	conn = swiftclient.Connection(key=password, 
		authurl=auth_url,  
		auth_version='3', 
		os_options={"project_id": project_id, 
					"user_id": user_id, 
					"region_name": region_name})
	cont_name = "container1"
	conn.put_container(cont_name)
	print "List of files present in bluemix\n"
	
	fileList=[]
	fileByte=[]
	for cont_name in conn.get_account()[1]:
		for data in conn.get_container(cont_name['name'])[1]:
			#print '{0}\t size: {1}\t date: {2}'.format(data['name'], data['bytes'], data['last_modified'])
			fileList.append(data['name'])
			fileByte.append(data['bytes']) #added line
	session['my_file_list']=fileList
	session['my_file_byte']=fileByte #added line
	return render_template('listfiles.html')
	
# uncomment following 3 lines the following when pushing to bluemixServer
#port = os.getenv('VCAP_APP_PORT', '5000')  #https://github.com/michaljemala/hello-python/blob/master/hello.py
#if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=int(port))

#comment following 3 lines when using flask locally 
if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.debug=True
	app.run()