'''
Write a Python program to convert JSON into Python object.
'''
import json 

if __name__=="__main__":
    json_obj = '{"name":"faisal","age":12,"course":"Python"}'
    print(json_obj)
    print(type(json_obj))

    print("After converting...")
    
    py_obj = json.loads(json_obj)
    print(py_obj)
    print(type(py_obj))