import re
def validate_data(data):
#It can be composed of letters, digits, dollar sign ($), and underscore characters (_) only
#It must start with a letter or underscore
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_$]*$', data))


c= bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_$]*$', "s"))
print(c)