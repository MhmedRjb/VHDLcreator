from collectdata import take_data, jsondict, user_input
from validate_data import validate_data
from fix_data import fix_data
from json_to_verilog import json_to_verilog, verilog_code_for_moduleTB, verilog_code_for_module
import json


with open('output.json', 'w') as f:
    json.dump(take_data(), f)

with open('output.json') as f:
    json_data = json.load(f)

# create v file
with open('output_tb.v', 'w') as f:
    f.write(json_to_verilog(json_data, verilog_code_for_moduleTB))

with open('output.v', 'w') as f:
    f.write(json_to_verilog(json_data, verilog_code_for_module))
