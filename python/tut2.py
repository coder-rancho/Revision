

# conditional extression
expression = "executed" if True else ("else's expression")

# logical opertors ==   and    or

# pass 
# if/for/func/class statements can't be empty use 'pass' to avoid error
if True or False : 
    pass

# range(start, stop, step) 
# returns a list of numbers
# default start=0 and step=1


# for-else
for x in range(5) :
    loop_body = "iterable code"
else :
    else_body = "execute when loop finish" # do not execute in case of break

# function
def myfunc(params) :
    return "function definition"
myfunc("fucn calling args")

def indefinite_args(*tup_args) : # when you don't know the no. of args to be passed
    return tup_args
tup_args = indefinite_args("par1", "par2", "par3")

def keyword_args_func(par1, par2, par3) : # note: kwargs = keyword args
    return {"par1": par1, "par2": par2, "par3": par3}
par_dict = keyword_args_func(par2="doesn't", par1="order", par3="matter")

def indefinite_kwargs(**dict_kwargs) :
    return dict_kwargs
dict_kwargs = indefinite_kwargs(name = "naman", age = 20)

def default_params(par = "default value") :
    return par
val1 = default_params()
val2 = default_params("myVal")

# note: list are passed as ref => change in local scope is reflected in global scope

#lambda func
# syntax my_func = lambda any_args : return_exp
sum_func = lambda a, b, c : a+b+c
received = sum_func(2, 5, 2)

def use_lambda_as_anonym(n) :
    return lambda a : a*n   # entire statement is returned
doubler = use_lambda_as_anonym(2)

doubled = doubler(22)

# List used as array
# import NumPy to work with actual array in python
array = ["list", "as", "array"]
array.append("at the end")
array.pop() # pop last item
array.pop(1) # pop(index)
array.remove("list") # remove specified item


print(array)