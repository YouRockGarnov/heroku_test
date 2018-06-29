from flask import Flask, request, json



@app.route('/', methods=['POST'])
def processing():
	return 'HI'