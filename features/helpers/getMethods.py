import requests
import os.path
import json
# = \ /

class getMethods():

	def __init__(self,reqUrl,payload):
		self.reqUrl  = reqUrl
		self.payload = payload
		self.header = {'Host': 'audience-service-qa.coredev.west2.steelhouse.com'}

	def getRequest(self):
		response = requests.get(self.reqUrl,headers = self.header)
		return (response.json(),response.status_code)

	def postRequest(self):
		response = requests.post(self.reqUrl,data =json.dumps(self.payload),headers =self.header)
		return (response.json(),response.status_code)


	def putRequest(self):
		response = requests.put(self.reqUrl,data =json.dumps(self.payload),headers =self.header)
		return (response.json(),response.status_code)

	'''
	curl -v GET 'http://a4c827ba7542a11ea9f3502586e8d5fc-134438161.us-west-2.elb.amazonaws.com/audience?advertiser=35082&full=true' \
		--header 'Host: audience-service-qa.coredev.west2.steelhouse.com'
	
	
	'''





		




		