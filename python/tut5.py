# Datetime
# inbuilt module for date & time
import datetime as dt
cur_time = dt.datetime.now()  # yyyy-mm-dd hh-mm-ss-msmsms
year = cur_time.year

# date object
date_obj = dt.datetime(2021, 5, 17) # (yyyy, mm, dd) time & timezone params are optional

# strftime - date_obj to readable string
weekDay = date_obj.strftime('%A') 
# for all legal format codes (%A) refer https://www.w3schools.com/PYTHON/python_datetime.asp



# Math
# module related to maths func refer https://www.w3schools.com/PYTHON/module_math.asp


# JSON
# syntax ("key": "value") for store/share info
import json 

# json.loads()
# -- json-string to py-dictionary
json_str = '{ "name":"John", "age":30, "city":"New York"}'
py_dict = json.loads(json_str)

# json.dumps()
# -- python obj to json-string
# python obj -- dict, list, tuple, str, int, float, True, False, None
json_str = json.dumps(py_dict)




#RegEx
# regular expression - sequence of characters that forms a search pattern
# refer https://www.w3schools.com/PYTHON/python_regex.asp



# PIP
# python package manager
# package - directory with Python files(modules) & a file __init__.py

# download package
# terminal - pip install <package Name> (say camelcase)

# import the installed package
import camelcase
cc = camelcase.CamelCase()
txt = "hi, i'm naman. bye"
cc_txt = cc.hump(txt)

# pypi.org -- for more packages

# unistall
# terminal - pip uninstall camelcase

# list packages
# terminal - pip list

print(cc_txt)