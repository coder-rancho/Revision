# Scope
# a variable can be accessed in its scope
# local - variable defined inside a func
#       - can also be accessed by func defined inside the func
# global - variable defined in main func
#        - available in whole program

# same variable in diff scope
def my_func():
    var = "local"
    # print(var)    # local -- local var overide global var
var = "global"
my_func()

# global keyword
# use to change value of a global variable inside a func
def change_in_func():
    global name
    name = "naman vyas"
name = "naman"
change_in_func()
# print(name)    # naman vyas



# Module
# .py file imported in another program to use its var, obj and func in the program
# 1. create module (say myModule.py)
# 2. import module
# 3. use func inside module
import myModule
name = myModule.myName
intro = myModule.intro()

# Built-in module
# modules comes with installed with python
# import platform
#    or
import platform as pf # importing using alias
os = pf.system()

# dir()
# list all func and var in a module
list = dir(myModule)  # list (including built-in func)

# from -- import
# used to import specified func or var only
from myModule import intro
# note : don't use module.func() now, instead use func()
x = intro()


print(x)