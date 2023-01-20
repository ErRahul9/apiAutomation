This is the code structure for the Python Behave usage for REST API automation. The code is structured in following sections

1.	Fixtures: - This section includes the payload that you want to pass to the API’s to test the expected results
2.	Helpers: - This folder has helper classes which can be executed while making API calls
3.	Steps: - Actual code which runs behind the scenes to get the expected results and match expected results
4.	. Fixture files: - these are the files which have the actual test cases written in GHERKIN format to execute the test cases.

Here are details of each section
Fixtures: - 
1.	 JSON file which ahs the payload that is being send over the network to the API.
2.	Please make sure JSON structure which corresponds following structure(you can change it based on how you want to implement the automation)


Helpers:-
1. Following helpers are available which can be used independent of the code
a. getMethods.py:- this method is at the center of autoamtion it can be used to make the calls to API and pass the payload and get the expected results here is sample example of running this
getMehtods("www.url.com",{"test "}).postrequest() will return the response in JSON and Status Code for the response 
b. jsonReader.py:- Reading the JSON in file return the collection which we can manipulate. 
c. databaseConn.py:- if the API data is stored in database this method can be used, I am using MYSQL as an example. 




### Contributing
1. Fork it !
2. Create your own branch
3. Commit your changes
4. push to the branch
5. Submit pull request.

 
