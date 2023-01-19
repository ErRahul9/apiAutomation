from helpers.jsonReader import jsonReader
from helpers.getMethods import getMethods
from helpers.databaseConn import DatabaseConnection

class audienceTest():



    def getRequest(self):
        jsonObject = jsonReader("../features/fixtures","job1.json").readJson()
        print(jsonObject)
        method = jsonObject.get("audience").get("GET_LOCATION").get("method")
        requrl = jsonObject.get("audience").get("GET_LOCATION").get("url")
        payload = jsonObject.get("audience").get("GET_LOCATION").get("payload")
        print(method)
        if "get" in method:
            runMethod = getMethods(requrl,payload).getRequest()
        print(runMethod)

    def runsql(self):
        jsonObject = jsonReader("../features/fixtures", "job1.json").readJson()
        sql = jsonObject.get("audience").get("GET_LOCATION").get("sql")
        result = DatabaseConnection(sql).connectToPostgres()
        print(result)

if __name__=="__main__":
    audienceTest().getRequest()
    audienceTest().runsql()