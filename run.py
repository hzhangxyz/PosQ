#!/usr/bin/python
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def position():
	if "j1" in request.args:
		m=request.args
		arg=map(lambda x:str(m[x]),["j1","w1","d1","j2","w2","d2"])
		test=''.join(arg)
		for i in test:
			if ("a"<=i<="z") or ("A"<=i<="Z"):
				return "Error"
		arg=["./run.m"]+arg
		ans=subprocess.check_output(arg)
		print ans
		ans=ans.replace("{","").replace("}","").replace(",","")
		ans=ans.replace("\n"," ").split(" ")
		ret="1. <a href='http://cn.bing.com/ditu/default.aspx?cp=%s~%s' target='_blank'>%sN, %sE</a><br/>2. <a href='http://cn.bing.com/ditu/default.aspx?cp=%s~%s' target='_blank'>%sN, %sE</a>"%(ans[1],ans[0],ans[1],ans[0],ans[3],ans[2],ans[3],ans[2])
		return ret
	else:
		return app.send_static_file("index.html")

if __name__ == "__main__":
	app.run("0.0.0.0",80,debug=False)
