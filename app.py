from flask import Flask, render_template, jsonify, request
from JSONEncoder import JSONEncoder
from server import *

app = Flask(__name__)


db = server.get_db()


@app.route("/")
def home():
	return "Hello world"

@app.route("/logData",methods=['POST'])
def logout():
	db.userdata.insert(request.get_json())


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
