#!/usr/local/bin/python3
import cgi, os
import sys
import cgitb; cgitb.enable ()
import random
import argparse
import subprocess
print("content-type: text/html\n\n" )
print ("<html>")
print ("<head>")
print ("<link rel='stylesheet' href='../css/mysite.css'>")
print ("<link rel='stylesheet' href='../css/bootstrap.css'>")
print ("<script src='//ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>")
print ("<script src='../js/jquery.cookie.js'></script>")
print ("<script src='../js/bootstrap.js'></script>")
print ("<script src='../js/myscript.js'></script>")
rootServer='hi.py?'
print ("</head>")
print ("<body>")
print ('''<div id="loadingFon"></div> ''')
print ('''<div id="loading1"><div><img src="../img/spinner.gif" alt="loading">
		</div>
		</div> ''')
		
print ('''<div class='header'>
	<a href="'''+rootServer+'''post=home">
		<div class='logo'>logo</div>
	</a>''')
	
#GET Cookies
bool_cookie="false"
cookie_email=""
cookie_pass=""
import Cookie
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	cookie_email=c['email'].value
	cookie_pass=c['pass'].value
	#print ('''<br>sad'''+c['email'].value+'''<br>sdfsd'''+c['pass'].value)
	try:
		
		#GET Cookies
        #print ('''<br>'''+c['email'].value+'''<br>'''+c['pass'].value)
		
		print('''<a  class='loginButton1a' href="#">
					<div class='loginButton1'>Login out</div>
				</a>''')
		print('''<a  href="'''+rootServer+'''post=user_profile">
					<div class='loginButton1b'>User Profile</div>
				</a>''')
		bool_cookie="true"
	except KeyError:
		print('''Cookies not !!!''')
else:
	print('''<div class='loginForm metkaForm'><form action="'''+rootServer+'''post=login" method='POST' enctype='multipart/form-data'>
						<input class='loginTextInput email_input' type='text' name='username' placeholder='username'>
						<input class='loginTextInput pass_input' type='password' name='password' placeholder='password'>
						<p style="display:none;" class="messageServer1"></p>
						<input class='login_Sign' type='submit' value='log in'>
					</form>
					<a href="'''+rootServer+'''post=registration">Registration</a>
					<br><br>
				</div>
				<a href="'''+rootServer+'''post=login">
				<div class='loginButton metkaForm'>Login or Sign Up</div>
				</a>''')
	bool_cookie="false"
print('''<div class='HeaderMenu'> 
			<ul class='headerUlMenu'>
				<a href="'''+rootServer+'''post=home"><li>Home</li></a>
				<a href="'''+rootServer+'''post=classify_an_image"><li>Classify an Image</li></a>
				<a href="'''+rootServer+'''post=train_neural_network"><li>Train Neural Network</li></a>
				<a href="'''+rootServer+'''post=use_your_neural_network"><li>Use your Neural Network</li></a>
			</ul>
	</div>
    </div>''')
print ("<div class='content'><br>")
url = os.environ["QUERY_STRING"]
fullPath = os.environ["REQUEST_URI"]

if (url=="post=faq"):	
	print ("<h1>FAQ</h1>")
	print ('''
	<div class="row">
		<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
		<div class="col-sx-10 col-sm-10 col-md-10 col-lg-10">
					
					
					<div class="textClassify"> 
					<h2> Frequently Asked Questions:<br></h2>
					<h3> 1.Question</h3>
					<h3> Answer</h3><br>
					<h3> 2.Question</h3>
					<h3> Answer</h3><br>
					<h3> 3.Question</h3>
					<h3> Answer</h3><br>
			        </div><br><br><br><br>
		</div>
		<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
	</div> ''')
elif (url=="post=user_profile"):	
	#SELECT
	import pymysql.cursors
	import my_connect
	connection = my_connect.getConnection()
	import hashlib
	import os.path, time
	import datetime
	try:
		with connection.cursor() as cursor:
    
		# connection is not autocommit by default. So you must commit to save
		# your changes.
		# connection.commit()
			# SQL 
			sql = "SELECT `id`, `pass`, `email` FROM `users`"
         
			# Execute query.
			cursor.execute(sql)
			for row in cursor:
				email_sql=row["email"]
				password_sql=row["pass"]
				
				m = hashlib.md5()
				m.update(password_sql.encode('utf-8'))
				password_sql=m.hexdigest()
				
				m1 = hashlib.md5()
				m1.update(email_sql.encode('utf-8'))
				email_sql=m1.hexdigest()
				if(cookie_email==email_sql and cookie_pass==password_sql):
					#print(email_sql+" "+password_sql)
					#id_model="16575976"
					print ('''<br><br><br><br><h1>User Profile</h1>	
						<h3>'''+row["email"]+'''</h3>
					''')
					user_id_sql=str(row["id"])
					root_dir = os.path.abspath(os.curdir)
					puth="//Users//alexanderdubilet//Documents//oxd553//lightScripts//custom_models//"
					directory= os.listdir(root_dir+puth)
					list1=[]
					j = 0
					while j < len(directory):	
						list1.append(os.path.getctime(root_dir+puth+directory[j]))
						j = j + 1
					list2=[]
					#Sort Date-----
					list1.sort()
					list1.reverse()
					for i in range(len(directory)):
						for k in range(len(directory)):
							if(list1[i]==os.path.getctime(root_dir+puth+directory[k])):
								list2.append(str(directory[k]+" "+str(datetime.datetime.strptime(time.ctime(os.path.getctime(root_dir+puth+directory[k])),"%a %b %d %H:%M:%S %Y"))))
								mass_dir_name=str(directory[k]).split('_')
								id_model=mass_dir_name[1]
								id_user_dir=mass_dir_name[0]
								if(user_id_sql==id_user_dir):
									print('''<a style="color:gray;" href="'''+rootServer+'''post=use_your_neural_network&par='''+id_model+'''">'''+id_model+'''</a>&nbsp&nbsp<span>['''+str(datetime.datetime.strptime(time.ctime(os.path.getctime(root_dir+puth+directory[k])),"%a %b %d %H:%M:%S %Y"))+''']<br>''')
					#Sort Date-----End
					print("<br><br>")
	finally:
		# Close connection.
		connection.close()
	
elif (url=="post=out"):	
	print ('''<br><br><br><br><h1>Login Out</h1>
	<h3>You signed out of your account</h3>''')
	print('''<script type="text/javascript">document.cookie = "email =; expires=Thu, 01 Jan 1970 00:00:01 GMT;";document.cookie = "pass =; expires=Thu, 01 Jan 1970 00:00:01 GMT;";</script>''') 
elif (url=="post=login"):	
	import hashlib
	form = cgi.FieldStorage()
	email=form.getvalue("username");
	password=form.getvalue("password");
	m = hashlib.md5()
	m.update(email.encode('utf-8'))
	email=m.hexdigest()
	
	m1 = hashlib.md5()
	m1.update(password.encode('utf-8'))
	password=m1.hexdigest()
	
	
	#print (email+'''<h1>Your JavaScript Off !!!</h1>'''+password)
	import pymysql.cursors
	import my_connect
	#SELECT
	connection = my_connect.getConnection()
	try:
		with connection.cursor() as cursor:
    
		# connection is not autocommit by default. So you must commit to save
		# your changes.
		# connection.commit()
			# SQL 
			sql = "SELECT `id`, `pass`, `email` FROM `users`"
         
			# Execute query.
			cursor.execute(sql)
			for row in cursor:
				form_email=row["email"]
				form_pass=row["pass"]
				m3 = hashlib.md5()
				m3.update(form_email.encode('utf-8'))
				form_email=m3.hexdigest()
	
				m4 = hashlib.md5()
				m4.update(form_pass.encode('utf-8'))
				form_pass=m4.hexdigest()
				if(form_pass==password and form_email==email):
					print('''<br><br><br><br><h1>You have successfully logged in to the site</h1>
					<h2>Now you can train your models</h2><h3><a class="gray_link" href="#">Your Profile</a></h3>''')
					print('''
						<script type="text/javascript">
						var CookieDate = new Date;
						CookieDate.setFullYear(CookieDate.getFullYear( ) +1);
						document.cookie = "email='''+email+'''; expires=" + CookieDate.toGMTString( ) + ";";
						document.cookie = "pass='''+password+'''; expires=" + CookieDate.toGMTString( ) + ";";
						</script>''') 	
					
	finally:
		# Close connection.
		connection.close()
elif (url=="post=registration"):	
    print ('''<h1>Post Registration</h1>
	<form class='formFile' action="'''+rootServer+'''post=print_confirm_email" method='POST' '>
	<h2>If you don`t - please register</h2>
	<p>E-mail</p>
	  <div style="float:left; visibility: hidden; width:30px; height:10px;"></div>
	  <input class="NameInput email_Input" name="email" type="text" size="40">&nbsp;&nbsp;	 
	  <img style="display:none;" class="validation email_validate" width="23px" src="../img/validation.png">
	  <img style="display:none;"  class="validation email_invalidate" width="23px" src="../img/invalidation.png">
	   <img style="display:block; float: right;" class="validation email_none" width="23px" src="../img/none.png">
		<p>Password</p>
	    <div style="float:left; visibility: hidden; width:30px; height:10px;"></div>
		<input class="SurnameInput pass1" name="pass1" type="text" size="40">&nbsp;&nbsp;
		   <img style="display:none;" class="validation pass1_validate" width="23px" src="../img/validation.png">
	  <img style="display:none;"  class="validation pass1_invalidate" width="23px" src="../img/invalidation.png">
	   <img style="display:block; float: right;" class="validation pass1_none" width="23px" src="../img/none.png">
		<p>Confirm password</p>
	    <div style="float:left; visibility: hidden; width:30px; height:10px;"></div>
		<input class="SurnameInput pass2" name="pass2" type="text" size="40">&nbsp;&nbsp;
		    <img style="display:none;" class="validation pass2_validate" width="23px" src="../img/validation.png">
	  <img style="display:none;"  class="validation pass2_invalidate" width="23px" src="../img/invalidation.png">
	   <img style="display:block; float: right;" class="validation pass2_none" width="23px" src="../img/none.png">
		<p></p>
        <button id="clickme_reg"> Register </button>
		<p class="reg_error"></p>

	</form>
	''')
elif (url=="post=about"):	
	print ('''<h1>ABOUT</h1>
	<div class="row">
	<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
				<div class="textClassify">
				<h3> Image Classification problem<br></h3>
				<p>text description</p>
				</div><br><br><br><br>
		</div>
		<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div class="textClassify"> 
					<h3> Tensorflow solution<br></h3>
					<p>text description</p>
			        </div><br><br><br><br>
		</div>
		<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div class="textClassify"> 
					<h3> TensorCreator - a lightweight, user-friendly web application solution<br></h3>
					<p>text description</p>
			        </div><br><br><br><br>
			    
		</div>
	    </div> ''')
elif (url=="post=home"):	
    print ('''<h1>HOME</h1>
	<div class="row">
	<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
		<div class="col-sx-10 col-sm-10 col-md-10 col-lg-10">
					<div class="textClassify"> I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". 
			        </div><br><br><br><br>
		</div>
		<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
	    </div> ''')
elif (url=="post=classify_an_image"):	
	print ('''<div class="row">
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">

					<div class="textClassify"> I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". 
					</div>
				</div> 
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
				  <div class="ElementDinamic1"></div>
			<form class='formFile' action="'''+rootServer+'''post=classify_an_image_upload" method='POST' enctype='multipart/form-data'>
			<h1>Upload the image of the test</h1>
			<input class='inputfileCenter' type='file' id='file900' name='file'  accept='image/x-png,image/gif,image/jpeg' /><br>
			<img src='#' style='display:none;' class='img900 ImgClassify id='output'><br><br>
			<input class='button900' style='display:none;' name='submit' type='submit'>
			</form>
				  
				</div>
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div> <span id="output"></span></div>
					<div>
					
						<ul class="ResultAnaliz">
							<li>1. Empty</li>
							<li>2. Empty</li>
							<li>3. Empty</li>
						</ul>
					</div>
				</div>
	       </div>''')
elif (url=="post=classify_an_image_upload"):
	#Clone classify_an_image
	#import cgitb; cgitb.enable ()
	import cgitb; cgitb.enable ()
	try: # Windows needs stdio set for binary mode.
		import msvcrt
		msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
		msvcrt.setmode (1, os.O_BINARY) # stdout = 1
	except ImportError:
		pass

	form = cgi.FieldStorage()
	url = os.environ["QUERY_STRING"]
	fullpathPicture=''
	message=''
	
	fullPuth= os.path.abspath(__file__)
	num= fullPuth.rindex('/')
	root=  fullPuth[0:num]	
	#print(root)
	root = root.replace('\\', '/')
	fullpathPicture=""
	def FileUpload(name):
			# A nested FieldStorage instance holds the file
			
			fileitem = form[name]
			# Test if the file was uploaded
			if fileitem.filename:

				# strip leading path from file name
				# to avoid directory traversal attacks
				fn = os.path.basename(fileitem.filename)
				puth_img='/Users/alexanderdubilet/Pictures/'+ fn
				# fullpathPictureDir='/var/www/html/Users/alexanderdubilet/Pictures/' 
				fullpathPictureDir='/Applications/XAMPP/xamppfiles/cgi-bin/Users/alexanderdubilet/Pictures/' 
				fullpathPicture=fullpathPictureDir + fn
				open(fullpathPicture, 'wb').write(fileitem.file.read())
				message = 'File uploaded successfully'
			else:
				message = 'No file was uploaded'	
			
			return puth_img
		

	# Example usage:
	# python3 imageReciever.py 
	# --image_file=/Users/alexanderdubilet/Pictures/dog.jpg \
	# --model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model
			
	def main ():
		root='/var/www/html'	
		# print('python3.5 '+root+'/native_TF_scripts/classify_image.py --image_file=/var/www/html/'+fullpathPicture+' --model_dir='+root+'/Users/alexanderdubilet/Documents/oxd553/imagenet_model')
		# request = 'python3.5 '+root+'/native_TF_scripts/classify_image.py --image_file=/var/www/html/'+fullpathPicture+' --model_dir='+root+'/Users/alexanderdubilet/Documents/oxd553/imagenet_model'
		print('python3 native_TF_scripts/classify_image.py --image_file='+fullpathPicture+' --model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model')
		request = 'python3 native_TF_scripts/classify_image.py --image_file='+fullpathPicture+' --model_dir=/Users/alexanderdubilet/Documents/oxd553/imagenet_model'

		results =os.popen(request).readlines()
		return (results)

	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		
		parser.add_argument(
			'--image_file',
			required=False,
			type=str,
			#C:\xampp1\htdocs\Users\alexanderdubilet\Pictures
			help='C:/xampp1/htdocs/Users/alexanderdubilet/Pictures/pic (50).jpg')

		parser.add_argument(
			'--model_dir',
			required=False,
			type=str,
			help="""/Users/alexanderdubilet/Documents/oxd553/imagenet_model""")
		img_puth=FileUpload('file')
		fullpathPicture=img_puth
		output = main()
		print ('''<div class="row">
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">

					<div class="textClassify"> I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". 
					</div>
				</div> 
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
				  <div class="ElementDinamic1"></div>
			<form class='formFile' action="'''+rootServer+'''post=classify_an_image_upload" method='POST' enctype='multipart/form-data'>
			<input type='file' id='file900' name='file' accept='image/x-png,image/gif,image/jpeg' />
			<img src='#' style='display:none;' class='img900 ImgClassify id='output'><br><br>
			<input class='button900' style='display:none;' name='submit' type='submit'>
			<img class="ServerImage" src="'''+img_puth+'''" width="300px">
			</form>
				  
				</div>
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div> <span id="output"></span></div>
					<div>
					
						<ul class="ResultAnaliz">''')
		print ("<h2>These are our best guesses: </h2><br>")
		for guess in output:
			print ("<li>"+guess+"</li>")
		print('''
						</ul>
					</div>
				</div>
	       </div>''')
	

elif (url=="post=train_neural_network"):	
	if(bool_cookie=='true'):
		rand1=random.randint(10000000,99999999) 
		print ('''<div class="row">
		<form class='formMenyFiles' action="'''+rootServer+'''post=result_traning" method='POST' enctype='multipart/form-data'>
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div class="textClassify"> I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". 
					</div>
				</div> 
				
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
				
				  <div class="ElementDinamic">
				  </div>
				  <input id="prodId" name="prodId" type="hidden" value="null">
				   <input id="prodId1" name="prodId_id" type="hidden" value="'''+str(rand1)+'''">
				  <div class="addFileInput">Add Image</div><br><br>
				
				 
				</div>
				<div class="col-sx-4 col-sm-4 col-md-4 col-lg-4">
					<div> <span id="output"></span></div>
					<div>
					<h2>Your model ID is: <b>'''+str(rand1)+'''</b></h2>
					
					  <input class='buttonStartTraning' style='display:none;' name='submit' type='submit' value='Start Traning'><br><br>  
					   <h3 class='buttonStartTraningText' style='display:none;'>Before clicking, save the id of your model</h3>
						<ul class="ResultAnaliz">
							<li>1. 1st guess + confidence rate</li>
							<li>2. 2st guess + confidence rate</li>
							<li>3. 3st guess + confidence rate</li>
						</ul>
					</div>
				</div>
				 </form>
			
	       </div>''')
	else:
		print ('''<br><br><br><br><br><br><h1>To use this page you need to enter the account</h1>''')
#elif (url.substring(0,url.indexof("&s="))=="post=print_confirm_email"):
elif (url=="post=print_confirm_email"):
	import hashlib
	import pymysql.cursors
	import my_connect
	#form registration
	form = cgi.FieldStorage()
	email=form.getvalue("email");
	#print(email)
	password=form.getvalue("pass1");
	#print(password)
	#INSERT pass login-email
	connection = my_connect.getConnection()
	try :
		with connection.cursor() as cursor:
			sql = "INSERT INTO `users` (`email`, `pass`) VALUES (%s, %s)"
			cursor.execute(sql, (email, password))
		connection.commit()
	finally:
		# Close connection.
		connection.close()
	 
	import Cookie
	password_original=password
	m = hashlib.md5()
	m.update(password.encode('utf-8'))
	password=m.hexdigest()
	
	email_original=email
	m1 = hashlib.md5()
	m1.update(email.encode('utf-8'))
	email=m1.hexdigest()
	key='email'
	value=email
	key1='pass'
	value1=password
	#SET Cookies javascript
	print('''
			<script type="text/javascript">
			var CookieDate = new Date;
			CookieDate.setFullYear(CookieDate.getFullYear( ) +1);
			document.cookie = "'''+key+'''='''+value+'''; expires=" + CookieDate.toGMTString( ) + ";";
			document.cookie = "'''+key1+'''='''+value1+'''; expires=" + CookieDate.toGMTString( ) + ";";
			</script>''') 
	#Email send
	import smtplib
	sender = 'media-softs@mail.ru'
	receivers = ['vkuzyomko@gmail.com']

	message = '''From: From Person <from@fromdomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test
To: To Person <to@todomain.com>
Subject: SMTP e-mail localhost
<h1>Did you register on the site using this email?</h1>
<a href="http://localhost/'''+rootServer+'''post=user_profile&s='''+email+'''"><h3>Confirm that this is your email address<h3></a>
Our website: <a href="http://localhost/'''+rootServer+'''post=user_profile">http://localhost/</a> 
'''
	#Gmail email
	user='vkuzyomko@gmail.com'
	pwd='1207911212qwerty12'
	try:
		smtpObj  = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.ehlo()
		smtpObj.starttls()
		smtpObj.login(user, pwd)
		smtpObj.sendmail(sender, receivers, message)    
		smtpObj.close()   
		print ('''<br><br><br><br><br><br><h1>
		You have sent a letter to the email to confirm your email <b>'''+email_original+'''</b></h1>
		<h3>Go to your mail to complete registration</h3>
		''')
	
	except SMTPException:
		print ("Error: unable to send email")

elif (url=="post=user_profile"):
	print('''<h1>Num</h1>''')	
elif (url=="post=upload_image"):

	try: # Windows needs stdio set for binary mode.
		import msvcrt
		msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
		msvcrt.setmode (1, os.O_BINARY) # stdout = 1
	except ImportError:
		pass

	form = cgi.FieldStorage()
	id_model=str(form.getvalue("id"));
	print('''<h2>Model id: '''+id_model+'''</h2>''')

	def FileUpload(name):
			puthDir='Users/alexanderdubilet/Pictures/'
			# A nested FieldStorage instance holds the file
			fileitem = form[name]
			
			# Test if the file was uploaded
			if fileitem.filename:

				# strip leading path from file name
				# to avoid directory traversal attacks
				fn = os.path.basename(fileitem.filename)
				fn=fn.replace(' ','_')
				open(puthDir + fn, 'wb').write(fileitem.file.read())
				message = 'The file uploaded successfully'
				print('''<img src="'''+puthDir+fn+'''" width="300px"> \n ''')	
			else:
				message = 'No file was uploaded'	
			return fn

	
	def main (image, graph, labels, puth_script):
		request = "python " +puth_script, image, graph, labels
		request = ' '.join(request)
		results  = os.popen(request).readlines()
		return (results)

	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		
		parser.add_argument(
			'--image',
			required=False,
			type=str,
			help='Absolute path to image file.')

		parser.add_argument(
			'--graph',
			required=False,
			type=str,
			help='Absolute path to graph.pb file.')

		parser.add_argument(
			'--labels',
			required=False,
			type=str,
			help="Absolute path to labels.txt file")
			
		picture_name=FileUpload('file')	
		
		fullPuth= os.path.abspath(__file__)
		num= fullPuth.rindex('\\')
		root=  fullPuth[0:num+1]	
		root = root.replace('\\', '/')
		import hashlib
		import pymysql.cursors
		import my_connect
		connection = my_connect.getConnection()
		email_sql=''
		id_user_sql=''
		try:
			with connection.cursor() as cursor:
				sql = "SELECT `email`, `pass`, `id` FROM `users`"
				cursor.execute(sql)
				for row in cursor:
					email_sql=row["email"]
					password=row["pass"]
					id_sql=row["id"]
					m = hashlib.md5()
					m.update(password.encode('utf-8'))
					password=m.hexdigest()
					m1 = hashlib.md5()
					m1.update(email_sql.encode('utf-8'))
					email_sql=m1.hexdigest()
					if(email_sql==cookie_email):
						id_user_sql=id_sql
		finally:
			# Close connection.
			connection.close()
		model=str(id_user_sql)+"_"+id_model+'_model'
		puth_script=root+'/native_TF_scripts/label_image.py'
		graphRequest=' --graph='+root+'/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+model+'/output_graph.pb'
		labelsRequest=' --labels='+root+'/Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+model+'/output_labels.txt'
		imageFileRequest=' --image='+root+'/Users/alexanderdubilet/Pictures/'+picture_name
		
		#print(graphRequest)
		#print("<br>")
		#print(labelsRequest)
		#print("<br>")
		#print(imageFileRequest)
		#print("<br>")
		output = main(imageFileRequest, graphRequest, labelsRequest, puth_script)
		
		print ("<h2>These are our best guesses:</h2>")
		for guess in output:
			print ('<h3>'+guess+'</h3>')
		print("<br>")
		print("<br>")
elif (url.find("post=use_your_neural_network")!=-1):
	value_input=''
	style_file_input='''"display:none;"''';
	if (url.find("post=use_your_neural_network&par=")!=-1):
		id_model_user_profile=url[url.find("par=")+4:len(url)]
		value_input=id_model_user_profile
		style_file_input='''"display:block;"''';
	else:
		value_input=''
		style_file_input='''"display:none;"''';
	print ('''<div class="row">
				<div class="col-sx-6 col-sm-6 col-md-6 col-lg-6">
					<div class="textClassify"> I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate".I have the honour to forward herewith the Chinese and English texts of a document entitled "Draft decision on the establishment of an ad hoc committee on the prevention of an arms race in outer space and its mandate". 
					</div>
				</div> 
				<div class="col-sx-6 col-sm-6 col-md-6 col-lg-6">
				<h2>What do you want to do with those image?</h2>
				
				  	<form class='formFile' action="'''+rootServer+'''post=upload_image" method='POST' enctype='multipart/form-data'>
					<div style='display:none;'>
						<input type="radio" value="Sort and place in respective folders" name="radio"  checked="checked" id="radioButton1"> <span> Sort and place in respective folders</span><br>
						<span> Remove image of particular class</span><br>
						<input type="radio" value="Remove image of particular class:Class 1" name="radio" id="radioButton2"><span> Class 1</span> 
						<input type="radio" value="Remove image of particular class:Class 2" name="radio" id="radioButton3"><span> Class 2</span><br>
						<span> Remove all image expert...</span><br>
						<input type="radio"  name="radio" value="Remove all image expert:Class 1" id="radioButton4"><span> Class 1</span>
						<input type="radio"  name="radio" value="Remove all image expert:Class 2" id="radioButton5"><span> Class 2</span><br>
						<input type="radio"  name="radio" value="Download as one folder, but rename images after their class" id="radioButton6"> 
						<span> Download as one folder, but rename images after their class</span><br><br><br><br>
					</div>
					<span>Please enter your model ID&#160;&#160;</span>  
					<input class="NameInput inputId" name="id" type="text" value="'''+value_input+'''" size="8"><br><br>
					<input style='''+style_file_input+''' class='inputfileCenter' type='file' id='file900' name='file'  accept='image/x-png,image/gif,image/jpeg' />
					<img src='#' style='display:none;' class='img900 ImgClassify id='output'><br><br>
					<input class='button900 buttonFindIt' style='display:none;' name='submit' value='Upload Image' type='submit'>
					</form>
					<br><br>
				</div>
	       </div>''')
elif (url=="post=contact_us"):	
    print ('''<h1>CONTACT US</h1>
	<div class="row">
	<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
		<div class="col-sx-10 col-sm-10 col-md-10 col-lg-10">
					<div class="textClassify"> 
							<h3> Contact details<br></h3>
							<p>My email:</p>
					</div><br><br><br><br>
		</div>
		<div class="col-sx-1 col-sm-1 col-md-1 col-lg-1">
		</div>
	    </div> ''')
elif (url=="post=result_traning"):	
	id_user_sql=''
	try: # Windows needs stdio set for binary mode.
		import msvcrt
		msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
		msvcrt.setmode (1, os.O_BINARY) # stdout = 1
	except ImportError:
		pass
	import hashlib
	import pymysql.cursors
	import my_connect
	connection = my_connect.getConnection()
	email_sql=''
	try:
		with connection.cursor() as cursor:
			sql = "SELECT `email`, `pass`, `id` FROM `users`"
			cursor.execute(sql)
			for row in cursor:
				email_sql=row["email"]
				password=row["pass"]
				id_sql=row["id"]
				m = hashlib.md5()
				m.update(password.encode('utf-8'))
				password=m.hexdigest()
				m1 = hashlib.md5()
				m1.update(email_sql.encode('utf-8'))
				email_sql=m1.hexdigest()
				if(email_sql==cookie_email):
					id_user_sql=id_sql
	finally:
		# Close connection.
		 connection.close()
	form = cgi.FieldStorage()
	HidenInput = form.getvalue('prodId')
	user_id = form.getvalue('prodId_id')
	fullPuth= os.path.abspath(__file__)
	num= fullPuth.rindex('\\')
	curent_Puth=  fullPuth[0:num+1]
	dir_model_name=str(id_user_sql)+'_'+user_id+'_model'
	os.makedirs(curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name, exist_ok=True)
	os.makedirs(curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name+'\\labeled_training_images', exist_ok=True)
	i = 1
	PuthDir1=curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name+'\\labeled_training_images\\'
	#PuthDir1=curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name+'\\labeled_training_images\\Class_'
	val = int(HidenInput)+2
	name_input=""
	nameDirInput = []
	while i < val:
		Name_Dir_Input = form.getvalue("Class"+str(i))
		nameDirInput.append(Name_Dir_Input)
		os.makedirs(PuthDir1+Name_Dir_Input, exist_ok=True)
		#os.makedirs(PuthDir1+str(i), exist_ok=True)
		i = i + 1
	def FileUpload(name, puth):
			fileitem = form[name]
			puth=puth+"\\"
			if isinstance(fileitem, list):
				i = 0
				for element in fileitem:
					if fileitem[i].filename:
						fn = os.path.basename(fileitem[i].filename)
						open(puth + fn, 'wb').write(fileitem[i].file.read())
						message = 'File uploaded successfully'
					else:
						message = 'No file was uploaded'	
						
					i = i + 1
			else:			
				if fileitem.filename:
					fn = os.path.basename(fileitem.filename)
					fullpathPictureDir=puth 
					fullpathPicture=puth + fn
					open(fullpathPicture, 'wb').write(fileitem.file.read())
					message = 'File uploaded successfully'
				else:
					message = 'No file was uploaded'	
	i = 0
	PuthDir=curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name+'\\labeled_training_images\\'
	#PuthDir=curent_Puth+'Users\\alexanderdubilet\\Documents\\oxd553\\lightScripts\\custom_models\\'+dir_model_name+'\\labeled_training_images\\Class_'
	val = int(HidenInput)+1
	while i < val:
		FileUpload('file'+str(i),PuthDir+nameDirInput[i])
		#FileUpload('file'+str(i),PuthDir+str(i+1))
		
		i = i + 1
	root=curent_Puth
	root = root.replace('\\', '/')
	print('<br><br><br>')
	print('<h1>Files uploaded successfully</h1>')
	print ("<h2>Program Traning...</h2>")
	print ("<h4>Come back in 2 hours</h4>")
	print('''<input class="email" name="email" type="hidden" value="'''+email_sql+'''">''')
	print('''<input class="root" name="root" type="hidden" value="'''+root+'''">''')
	print('''<input class="model_name" name="model_name" type="hidden" value="'''+dir_model_name+'''">''')
	print ('''<h4><img src="../img/spinner.gif" alt="loading"></h4>''')

elif (url=="post=start_trening"):	
	import json
	fs = cgi.FieldStorage()
	sys.stdout.write("Content-Type: application/json")
	sys.stdout.write("\n")
	sys.stdout.write("\n")
	result = {}
	result['success'] = True
	result['message'] = "successfully"
	result['keys'] = ",".join(fs.keys())
	d = {}
	for k in fs.keys():
		d[k] = fs.getvalue(k)

	result['data'] = d
	email=fs.getvalue('email')
	root=fs.getvalue('root')
	dir_model_name=fs.getvalue('model_name')

	def mail ():
		#Email send
		import smtplib
		sender = 'media-softs@mail.ru'
		receivers = ['vkuzyomko@gmail.com']
		mass_dir_name=str(dir_model_name).split('_')
		id_model=mass_dir_name[1]
		message = '''From: From Person <from@fromdomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test
To: To Person <to@todomain.com>
Subject: SMTP e-mail localhost
<h1>The program has finished trimming, for its use click on the link</h1>
<a href="http://localhost/hi.py?post=use_your_neural_network&par='''+id_model+'''"><h3>
Thank you for using our service<h3></a>
Our website: <a href="http://localhost/'''+rootServer+'''post=user_profile">http://localhost/</a> 
'''
		#Gmail email
		user='vkuzyomko@gmail.com'
		pwd='1207911212qwerty12'
		try:
			smtpObj  = smtplib.SMTP("smtp.gmail.com", 587)
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login(user, pwd)
			smtpObj.sendmail(sender, receivers, message)    
			smtpObj.close()   
			print ('''<br><br><br><br><br><br><h1>
			You have sent a letter to the email to confirm your email <b></b></h1>
			<h3>Go to your mail to complete registration</h3>
			''')
		except SMTPException:
			print ("Error: unable to send email")
	def main ():	
		request = ('python '+root+'native_TF_scripts/retrain.py --image_dir='+root+'Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+dir_model_name+'/labeled_training_images/ --output_graph='+root+'Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+dir_model_name+'/output_graph.pb --output_labels='+root+'Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+dir_model_name+'/output_labels.txt --bottleneck_dir='+root+'Users/alexanderdubilet/Documents/oxd553/lightScripts/custom_models/'+dir_model_name+'/bottleneck_animals --how_many_training_steps=10 --model_dir='+root+'Users/alexanderdubilet/Documents/oxd553/imagenet_model') 
		results = subprocess.call(request, shell=True)
		if results==0:
			return True
		else:
			return False	
	if __name__ == '__main__':
		parser = argparse.ArgumentParser()
		
		parser.add_argument(
			'--image_dir',
			required=False,
			type=str,
			help='Absolute path to labeled training images.')

		parser.add_argument(
			'--output_graph',
			required=False,
			type=str,
			help='Save output graph to ... ')

		parser.add_argument(
			'--output_labels',
			required=False,
			type=str,
			help='Save output labels to ... ')

		 #parser.add_argument(
		 #	'print_misclassified_files',
		 #	defualt=""
		 #	help='Do we print images we are unsure about? ')

		parser.add_argument(
			'--bottleneck_dir',
			required=False,
			type=str,
			help='Save bottleneck to ... ')
		parser.add_argument(
			'--how_many_training_steps',
			required=False,
			type=int,
			default=4000,
			help='How many training steps we want to make. Default is 4000 ')
		parser.add_argument(
			'--model_dir',
			required=False,
			type=str,
			help="Path to imagenet folder")
		#run function
		output = main()
		mail ()
		sys.stdout.write(json.dumps(result,indent=1))
		sys.stdout.write("\n")
		sys.stdout.close()
		print ("Operations successful: ", output)
	
elif (url=="post=github_source"):	
    print ("<h1>Post Github Source</h1>")
#Send to Server ot email login=email	
elif(url.find('&s=')!=-1):
	import hashlib
	import pymysql.cursors
	import my_connect
	email=url[url.find('&s=')+3:len(url)]
	connection = my_connect.getConnection()
	try:
		with connection.cursor() as cursor:
			sql = "SELECT `email`, `pass` FROM `users`"
			cursor.execute(sql)
			for row in cursor:
				email_ORG=row["email"]
				password=row["pass"]
				password_original=password
				
				m = hashlib.md5()
				m.update(password.encode('utf-8'))
				password=m.hexdigest()
	
				email_sql=email_ORG
				m1 = hashlib.md5()
				m1.update(email_sql.encode('utf-8'))
				email_sql=m1.hexdigest()
				if(email_sql==email):
					print('''<br><br><br><br><br><h2>'''+email_ORG+'''</h2><h1>EMAIL APPROVED</h1>
					<h3><a href="#">Go to your Profile</a></h3>''')  
					cursor = connection.cursor()
					sql = "Update users set confirm_email = %s where email = %s" 
					# Execute sql, and pass 3 parameters.
					rowCount = cursor.execute(sql, ("true", email_ORG ) )
					connection.commit()
					print('''
							<script type="text/javascript">
							var CookieDate = new Date;
							CookieDate.setFullYear(CookieDate.getFullYear( ) +1);
							document.cookie = "email='''+email_sql+'''; expires=" + CookieDate.toGMTString( ) + ";";
							document.cookie = "pass='''+password+'''; expires=" + CookieDate.toGMTString( ) + ";";
							</script>''') 					
	finally:
		# Close connection.
		 connection.close()
else:
	print ("<h1>404 - Error</h1>")	
print ("</div>")	
print ('''<div class='footer'>
			<ul class='footerUlMenu'>
				<a href="'''+rootServer+'''post=about"><li>About</li></a>
				<a href="'''+rootServer+'''post=faq"><li>Faq</li></a>
				<a href='https://github.com/Aleksey1590/Tensorflow-web-classifier'><li>Github Source</li></a>
				<a href='https://www.tensorflow.org/'><li>TensorFlow by Google</li></a>
				<a href="'''+rootServer+'''post=contact_us"><li>Contact Us</li></a>
			</ul>
		</div>''')
print ("</body>")
print ("</html>")



