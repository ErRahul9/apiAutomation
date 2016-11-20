import json
import os
import ordereddict
# = \ /

class jsonReader():

	def __init__(self,path,filename):
		self.path  = path
		self.filename  = filename


	def readJson(self):
		returnJsonObjects  = {}
		jsonPath  = os.path.join(self.path,self.filename)
		readFile  json.load(open(jsonPath))
		for Key,values in readFile.iteritems():
			returnJsonObjects[Key]  = Values
	 	return returnJsonObjects