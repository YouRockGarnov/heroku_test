from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def processing():
	print('hi')
	return 'HI'

app.run()
