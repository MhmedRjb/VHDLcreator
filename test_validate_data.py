from validate_data import validate_data
from fix_data import fix_data
import random

def test_validate_data():
    assert validate_data("data") == True
    assert validate_data("data$") == True
    assert validate_data("data_") == True
    assert validate_data("_data") == True
    assert validate_data("da1ta") == True
    assert validate_data("data1") == True
    assert validate_data("data data") == False
    assert validate_data("data-data") == False
    assert validate_data("data.data") == False
    assert validate_data("data@data") == False
    assert validate_data("data#data") == False
    assert validate_data("1data") == False
    assert validate_data("1data1") == False
    assert validate_data("data1data") == True
    assert validate_data("data1_data") == True
    assert validate_data("12") == False

def test_fix_data():
    random.seed(1)
    assert fix_data("data")[0] == "data"
    assert fix_data("data$")[0] == "data$"
    assert fix_data("data_")[0] == "data_"
    assert fix_data("_data")[0] == "_data"
    assert fix_data("da1ta")[0] == "da1ta"
    assert fix_data("data data")[0] == "datadata"
    assert fix_data("data-data")[0] == "datadata"
    assert fix_data("data.data")[0] == "datadata"
    assert fix_data("data@data")[0] == "datadata"
    assert fix_data("data#data")[0] == "datadata"
    assert fix_data("data1")[0] == "data1"
    assert fix_data("1data")[0] == "data"
    assert fix_data("1223data")[0] == "data"
    assert fix_data("-data")[0] == "data"
    assert fix_data("--data")[0] == "data"
    assert fix_data("##data")[0] == "data"
    assert fix_data("1data1")[0] == "data1"
    assert fix_data("data1data")[0] == "data1data"
    assert fix_data("data1_data")[0] == "data1_data"
    assert fix_data("12")[0] == "temp138"
    assert fix_data("")[0] == "temp583"
    



