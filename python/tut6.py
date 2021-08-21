# TRY & EXCEPT
# try - test a block of code for errors
# except - handle errors
# finally - execute code regardless the result of try & except

# without try-except 
# program will stop asa it found some error(or exception)
# print(x)  # NameError: x is not defined

# with try-except
# program will execute except block asa it encounter an exception(or error)
from typing import cast


try:
    print(x)
except:
    handle_exception = "code for handling error"
# exception handling - handle exceptions(using try-except)
# and execute rest of the code
# generally used while accessing something from an database/api
x = "code after exception handling"

# Multiple Exception handling
# use multiple except
try:
    print(y)
except NameError:  # run if error == NameError
    error = "it's a NameError" 
except :   # run if error != NameError
    error = "it's not a NameError"

# else
# run else if no error raised
try:
    print("Hello")
except:
    error = "some error"
else:
    error = "No error found"

# finally
# execute regardless if try: raises any error
try:
    print(z)
except:
    error = "something went wrong"
finally:
    msg = "try & except are over"


# raise exception
# syntax - raise Exception(<msg>) | <default_error>(msg)
try:
    x = -1
    if x < 0:
        raise Exception("-ve no. not supported") # terminal output -- Exception: no. is -ve
except: 
    error = "custom exception"

try:
    x = "hello"
    if type(x) != int:
        raise NameError("only int values are allowed")
except:
    error = "my NameError"



#User input
# input()
# user_inp = input("your input : ")



# format()
# format selected (placeholder {}) parts of a string

price = 49
txt = "the price is ${}"
frmt_str = txt.format(price) # params - comma-sep vals, comma-sep key=val or both

# named {} 
txt = "{name} is {age} years old"
frmt_str = txt.format(name="Naman", age=19)

# indexed {}
# use a param val at multiple {}
txt = "{name} is a {0}, a {0} writes code"
frmt_str = txt.format( "programmer", name="Naman") 
# note: positional args always comes before kwargs e.g. "programmer" before name="Naman"

# refer formatting types on w3schools for more fun

print(frmt_str)
