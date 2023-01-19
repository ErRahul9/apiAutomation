import requests
import os.path
import json
# = \ /

class getMethods():

	def __init__(self,reqUrl,payload):
		self.reqUrl  = reqUrl
		self.payload = payload
		self.header = {'Authorization':self.getToken(),'Content-Type':'application/json'}

	def getRequest(self):
		response = requests.get(self.reqUrl,headers = self.header)
		return (response.json(),response.status_code)

	def postRequest(self):
		response = requests.post(self.reqUrl,data =json.dumps(self.payload),headers =self.header)
		return (response.json(),response.status_code)


	def putRequest(self):
		response = requests.put(self.reqUrl,data =json.dumps(self.payload),headers =self.header)
		return (response.json(),response.status_code)







		




		