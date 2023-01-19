from helpers.jsonReader import jsonReader
from helpers.getMethods import getMethods


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



if __name__=="__main__":
    audienceTest().getRequest()