#from Crypto import Random
#from Crypto.Cipher import AES

import swiftclient
import keystoneclient

def main(file_name):
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
	print "Hello world"

	#file_name = "C:/fileuploadpysrb/Sample.txt"
	#newfile = "C:/fileuploadpysrb/Sampledecrypt.txt"

	#key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'

	#encrypt_file(file_name, key)

	#file_name = "C:/fileuploadpysrb/Sample.enc"
	#with open(file_name, 'r') as upload_file:
	conn.put_object(cont_name, file_name.filename, contents= file_name)
		

	#conn.get_object(cont_name, file_name+".enc")
	#with open(file_name+".enc", 'r') as f:
	#	file_contents = f.read()
		#print (file_contents)
	#	with open(file_name+"_d.enc", 'w') as f1:
	#		f1.write(file_contents)
	#decrypt_file(file_name+"_d.enc", key)