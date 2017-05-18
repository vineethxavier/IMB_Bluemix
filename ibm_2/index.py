import hashlib
import os,csv,sys
import connect as obj1
import cgi
#from werkzeug import secure_filename

from flask import Flask,render_template,request,url_for,redirect, session

app = Flask(__name__)
app.secret_key = 'super secret key'
		   
@app.route("/")
def mainpage():
	return render_template('index.html')

@app.route("/loadfile",methods=['GET','POST'])
def loadfile():
	
	uploadedfile = request.files['infile'] #filr from html to python
	filecontent=uploadedfile.read()
	#print len(filecontent)
	username= session['username']   #username
	print filecontent
	#uploadedfile.filename  # toget the file name
	result=obj1.insert(username,uploadedfile.filename,filecontent,len(filecontent))

		#form_data = cgi.FieldStorage()   # getting file data
		#file_data = form_data['file'].value # getting file data
	return render_template('login.html')

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == 'POST':
		paramusername = request.form['username']
		parampassword = request.form['password']
		session['username']=paramusername
		#filename = secure_filename(file.infile)
		#file.save(os.path.join(app.config['FOLDER'], infile))
		#df = pd.read_csv(os.path.join(app.config['FOLDER'], infile)
		result=obj1.authenticate(paramusername,parampassword)  #true or false
		if(result=="true"):
			return render_template('login.html')
		else:
			return render_template('loginfailed.html')

	
# uncomment following 3 lines the following when pushing to bluemixServer
port = os.getenv('VCAP_APP_PORT', '5000')  #https://github.com/michaljemala/hello-python/blob/master/hello.py
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))

#uncomment following 3 lines when using flask locally 
#if __name__ == "__main__":
#	app.secret_key = 'super secret key'
#	app.config['SESSION_TYPE'] = 'filesystem'
#	app.debug=True
#	app.run()