#create function take data from dictionary and create new file

from validate_data import validate_data
from fix_data import fix_data
import json

#make dict data inputs and outputs



# make a function to take data from user to fill the dictionary with name of module and inputs and outputs 
jsondict = {}
def user_input(name: str, listname: str, askuser: str, multiple: bool = True ) -> list:
    print("Enter " + askuser + ": ")
    listname = []

    while True:
        name = input()
        if name == "":
            if len(listname) == 0:
                print("Please enter at least one " + askuser + ":")
                continue
            break

        if validate_data(name):
            listname.append(name)
        else:
            fixed_data, message = fix_data(name)
            print(message)
            listname.append(fixed_data)
            
        if not multiple:
            break

    return listname
    

def take_data():

    module_name= user_input("module_name",listname="module_name",askuser="module_name",multiple=False)
    jsondict["module_name"] = module_name

    inputs = user_input("inputs",listname="inputs",askuser="inputs",multiple=True)
    jsondict["inputs"] = inputs

    outputs = user_input("output",listname="outputs",askuser="outputs",multiple=True)
    jsondict["output"] = outputs

    wireorreg = user_input("wireorreg",listname="wireorreg",askuser="wireorreg",multiple=False)
    jsondict["wireorreg"] = wireorreg

    wireorregname = user_input("wireorregname",listname="wireorregname",askuser="wireorregname",multiple=False)
    jsondict["wireorregname"] = wireorregname
    return jsondict



    