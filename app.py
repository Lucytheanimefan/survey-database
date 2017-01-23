import os
from flask import Flask, render_template, jsonify, request
from JSONEncoder import JSONEncoder
from server import *
import server

app = Flask(__name__)


db = server.get_db()


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/logData",methods=['POST'])
def logout():
	print("-----------LOG DATA---------")
	print request.get_json()
	if "IceCream" in request.get_json():
		db.data.insert(request.get_json())
	return "Success"


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
