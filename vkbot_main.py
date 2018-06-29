from flask import Flask, request, json



@app.route('/', methods=['GET'])
def processing():
	print('hi')
	return 'HI'