# STRING
str = "this is my str"
mStr = ''' this is 
multiline str'''

# slicing
subStr = str[2:5] # [2,5) index

#modify
uppercase = str.upper() 
remWhiteSpace = str.strip
replace_subStr_to_newStr = str.replace('my', 'your')
split_into_list = str.split(" ") # white space is the separator

#concatenation
merged_str = str + mStr

#format() 
str_with_placeholder = "this is a format str with placeholder {}"
int_val = 18
formatted_str = str_with_placeholder.format(int_val) # replace {} with 18 (as a str value)
# no. of {} == args to format()
# specify {indx}, where indx is the index of arg to format()



# LIST

# datatypes in python list, set, dictionary and tuple
myList = ["Naman", "is", 20]
list_constr = list(("created", "using", "constructor")) # note: two round brackets
num_list = [100, 50, 65, 82, 23]

# access & modify
item_at = myList[0]
item_from_end = myList[-1]
subList = myList[0:2]  
myList[2] = 19
list_constr[0:] = ["modified", "using", "range", "subList"]

# insert
myList.insert(1, "Vyas")
myList.append("years")

# extend & join
tempList = ['.']
myList.extend(tempList)
Concatenated_list = myList + tempList
# can append any iterable object (tuple, sets, dictionary etc.)

# remove items
myList.remove('Vyas')
myList.pop(4) # pop() = pop last item
del myList[3]
# del myList # delete list completely
# myList.clear() # empty the list, python 3.3+

# type(list) 
list_datatype = type(myList) 

# in keyword
check = "naman" in myList

# loop through list
# for i in myList :
#     print(i)

# list comprehension
# syntax : newlist = [expression for item in iterable if condition == True]
# [print(x) for x in myList] # docs says python 2.0+ but my system run on 3.0+
subList = [x for x in myList if isinstance(x, type(str))]

#sort
num_list.sort()
num_list.sort(reverse = True) #descending
def get_key(n) :
    return n - 50
num_list.sort(key = get_key) # sort on the basis of n - 50
# ?????????????????????????????????????????????????????????????????
#sorted_list = sorted(["Hello", "mr", "naMan"], key = str.lower) # case insensitive sorting
# ???????????????????????????????????????????????????????????????
# sorted func is similar to sort but it gives new sorted list instead of modifying original

#copying list
list_ref = myList # list_ref is list with reference, any change in myList reflect in list_ref
new_list = myList[:] # note: list.copy() do not work

#          ordered  changable   duplicate  
# list      yes      yes        yes
# tuple     yes      no         yes
# set       no       no        no
# dictonary yes      yes        no




# TUPLES
my_tup = ("tuples", "are", "Immutable")
single_item_tuple = ("notice comma",)
tup_constr = tuple(my_tup) # arg is any iterable obj

#access, loop etc -- same as list

# change tuple values
tup_list = list(my_tup)
tup_list[2] = "Mutable"
my_tup = tuple(tup_list)
# tuples aren't mutable, but lists are.
# tuple -> list -> chages -> tuple

# concatination -- allowed

# delete tuple
del single_item_tuple

# unpacking tuple 
(sub, verb, obj) = my_tup # similar to object destructuring in JS
# (sub, *info) = my_tup # *info -- list of rest of items python3.0+



# SET
my_set = {"Set", "have", "unordered", "items"}
set_constr = set(my_tup) 
#note: set don't hv duplicates. even if u provide it'll merge them into one item

# add items
# can't change items but add new items using add() & update
my_set.add(".")
my_set.update(set_constr) # add items of set_constr(or any iterable obj) to my_set
union_set = my_set.union(set_constr)
intersection_set = union_set.intersection(my_set) # store the intersectn of two sets
union_set.intersection_update(my_set) # update set1 as intxn of set1 and set2
union_excluding_intersection = union_set.symmetric_difference(my_set)

# remove items
my_set.remove("tuples") # error if not found item
my_set.discard("are")   # NO error if not found
removed_item = my_set.pop() # remove last item (note: set is unordered so any item could be removed)
del set_constr # delete the entire set




#DICTIONARY
my_dict = {
    "name": "Naman",
    "age": 19,
    "languages": ("python", "javaScript", "C++")
}
# key:value pairs -- no duplicate keys are allowed
# python 3.7+ => ordered otherwise unordered

# access
item_val = my_dict["name"]
keys_list = my_dict.keys()  
values_list = my_dict.values() 
list_tup_items   = my_dict.items() # [(key, val), (key, val)]
# above three methods give a live reference to dict, i.e. their val change if dict is changed
check_key = "name" in my_dict

#modify 
my_dict["name"] = "Naman Vyas"
# update -- dict.update(dict or iterable) -- update or add values
my_dict.update({"name": "Naman", "age": 20}) # using dict
my_dict.update(name = "naman", hobby = "songs") # using iterable

#remove item
my_dict.pop("hobby")
my_dict.popitem() # 3.7+ -- last inserted item otherwise random item
# my_dict.clear() # empty the list
# del my_dict

#looping
# for key in my_dict :
# for val in my_dict.values() :
# for key, val in my_dict.items :

# copy
dict_ref = my_dict # dict (as reference to my_dict)



print(my_dict)