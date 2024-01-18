import json


def verilog_code_for_module(module_name: str, inputs: list, output: list, wireorreg: str, wireorregname: str) -> str:
    
    verilog_code = f"module {module_name}(\n"
    
    # Add input ports
    for inp in inputs:
        verilog_code += f"  input wire {inp},\n"

    # Add output ports
    for out in output:
        verilog_code += f"  output reg {out},\n"

    # Remove the trailing comma and newline from the last port
    verilog_code = verilog_code.rstrip(",\n")

    # Add semicolon for the module declaration
    verilog_code += "\n);\n\n"

    # Add internal signals declaration
    verilog_code += f"//internal_signals\n  {wireorreg} {wireorregname};\n\n"

    # Add any additional logic here

    # Close the module
    verilog_code += "endmodule\n"

    return verilog_code


def verilog_code_for_moduleTB(module_name: str, inputs: list, output: list, wireorreg: str, wireorregname: str) -> str:
    
    verilog_code = f"module {module_name}_TB();\n"
    
    # Add input ports
    for inp in inputs:
        verilog_code += f"reg {inp}_TB,\n"

    # Add output ports
    for out in output:
        verilog_code += f" wire {out}_TB,\n"

    # Remove the trailing comma and newline from the last port
    verilog_code = verilog_code.rstrip(",\n")

    # Add semicolon for the module declaration
    verilog_code += "\n\n\n"

    # Add internal signals declaration
    if wireorreg == "wire":
        verilog_code += f"//internal_signals\n  reg {wireorregname}_TB;\n\n"
    elif wireorreg == "reg":
        verilog_code += f"//internal_signals\n  wire {wireorregname}_TB;\n\n"
    else:
        raise ValueError("wireorreg must be either wire or reg")

    #create instantiate design module
    verilog_code += f"{module_name} {module_name}_inst(\n"
    for inp in inputs:
        verilog_code += f".{inp}({inp}_TB),\n"
    for out in output:
        verilog_code += f".{out}({out}_TB),\n"
    verilog_code = verilog_code.rstrip(",\n")
    verilog_code += "\n);\n\n"

    verilog_code += "endmodule\n"

    return verilog_code

def json_to_verilog(json_data:dict,verilog_code_function) -> str:
    module_name = json_data["module_name"][0]
    inputs = json_data["inputs"]
    output = json_data["output"]
    wireorreg = json_data["wireorreg"][0]
    wireorregname = json_data["wireorregname"][0]
    verilog_code = verilog_code_function(module_name, inputs, output, wireorreg, wireorregname)

    return verilog_code

#  JSON data from output.json



