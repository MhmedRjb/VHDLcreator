import re
import random
def fix_data(data: str) -> str:
    # Remove invalid characters
    fixed_data = re.sub(r'^\d+|[^a-zA-Z0-9_$]', '', data)
    message = "Invalid input but it got fixed from " + data + " to " + fixed_data
    #soultion if data is empty raise error
    if fixed_data == "":
        fixed_data = "temp" + str(random.randint(1, 1000))
        message = "the input is empty so random data will genrated  " + fixed_data
    return fixed_data,message

