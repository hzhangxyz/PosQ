#!/usr/bin/python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def position():
	if "j1" in request.args:
		m=request.args
		arg=["./run.m"]+map(lambda x:str(m[x]),["j1","w1","d1","j2","w2","d2"])
		print arg
		return subprocess.check_output(arg).replace("{","").replace("}","").replace(",","")
	else:
		return app.send_static_file("index.html")

if __name__ == "__main__":
	app.run("0.0.0.0",80,debug=True)
