#create function take data from dictionary and create new file

from validate_data import validate_data
from fix_data import fix_data
#make dict data inputs and outputs



# make a function to take data from user to fill the dictionary with name of module and inputs and outputs 
dict = {}


def user_input(name: str, listname: str, askuser: str, multiple: bool = True) -> list:
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
            fixed_name, message = fix_data(name)
            print(message)
            listname.append(fixed_name[0])
        if not multiple:
            break

    return listname
    

def take_data():

    module_name= user_input("module_name",listname="module_name",askuser="module_name",multiple=False)
    dict["module_name"] = module_name
    inputs = user_input("inputs",listname="inputs",askuser="inputs",multiple=True)
    dict["inputs"] = inputs

    outputs = user_input("output",listname="outputs",askuser="outputs",multiple=True)
    dict["output"] = outputs

    print(dict)
    return dict


take_data()

# def create_file(data: dict = dict) -> None:
#     print("Creating file...")
#     print("Data: ", data)


# create_file()
    