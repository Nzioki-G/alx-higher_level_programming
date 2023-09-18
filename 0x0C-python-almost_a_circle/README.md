# Python - Almost a circle

This project is a preparation for AirBnB clone<br>
* Unit testing is testing done to specific functions
* To implement unittesting in a large project, create the test functions during or before function implementation
* To serialize a class use it's ```py_obj = obj.__dict__``` property to get its object representation. Then use ```json.dump/s(py_obj)``` to json-ify the object
* To deserialize a class, use ```json.load/s(json_file/_string)``` to Pythonify a json string or file. Then use the object to recreate the class
* How to write and read a JSON file? Use ```json.dump(py_object)``` and ```json.load(json_file)``` respectively.
* ```*args``` is a variable-length list of arguments
  * To use it, handle it as an array
* ```**kwargs``` is a variable-length dictionary of keyword arguments
  * use kwargs as a normal dictionary with arg_name as keys
