# flask app
from flask import Flask, request
import os


app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def call_back():
	
	content = request.json

	try:
		#get info
		user = int(content["payer"]["telegram"])
		plan = content["reference"]["link"]
	except:
		return


	os.system(f"python3 callback.py {user} {plan}")
	return "Thanks for your paying" 



		


	

