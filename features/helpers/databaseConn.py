import MYSQLdb
import os
import dattime
import time
from jsonReader import jsonReader
# = \ /

class DatabaseConnection:

	def setDatabaseConn(self,USER,HOST,PASS,DBNAME):
		self.dbconnection  = MYSQLdb.connect(HOST,USER,PASS,DBNAME)
		self.cursor  self.dbconnection.cursor(MYSQLdb.cursors.DictCursor)


 	def querySample(self,query):
 		self.cursor = self.dbconnection.cursor(MYSQLdb.cursors.DictCursor)
 		self.cursor.execute(query)
 		data = self.cursor.fetchall()
 		return data

 	 def closeConn(self):
 	 	self.dbconnection.close()
