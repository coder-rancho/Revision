# class

from typing import Iterable


class MyClass:
    x = "data member" 
obj = MyClass() # object/instance of class
access_val = obj.x

class person:
    x = 'class member (static prop)' # Can be accessed only by class( person.x ) as it belongs to the class (not obj)
    def __init__(self, name, age): # Constructor
        self.name = name 
        self.age = age
    def intro(self):  # obj method
        return "my name is " + self.name

# self parameter is a reference to the current instance/obj of class,
# use to access class/obj variables
# you can call it(self) whatever you like, but it has to be the first parameter of any function in the class:
me = person("naman", 20)
my_age = me.age        # access prop
me.name = "Naman Vyas" # modify obj prop
intro = me.intro()     # call method
del person.x           # delete class prop 
del me.age             # delete obj prop
del me                 # delete obj

# inheritance 
# child class inherit all prop & meth from parent class

class person:   # parent/base class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def intro(self):
        return ("Hi this is " + self.fname + " " + self.lname)

class student(person): # child/derived class
    pass

parent_obj = person('Naman', 'Vyas')
get_intro = parent_obj.intro()

child_obj = student('Radha', 'singh')
get_intro = child_obj.intro()


# __init__() && child class
# __init__() of child class will override __init__() of parent class.
# hence we hv to call parent.__init__ inside child's __init__
# to do that we hv two methods

# method 1 - parent.__init__
class teacher(person):
    def __init__(self, fname, lname, subject):
        person.__init__(self, fname, lname)
        self.subject = subject

# method 2 - using super().__init__
# super() inferits all method and properties from parent class
class author(person):
    def __init__(self, fname, lname, book):
        super().__init__(fname, lname)
        self.book = book


meth1_obj = teacher('alakh', 'pandey', 'physics')
get_intro = meth1_obj.intro()

meth2_obj = author('HC', 'Verma', 'concepts of physics')
get_intro = meth2_obj.intro()



# iterator
# it's an obj containing countable no. of values
# technically, an obj that contain __iter__() & __next__() (iterator protocol)

# iterable vs iterator
# set, dict etc. are all iterable obj which contains iter() method
# iter() is used to get an iterator

iterable_obj = ('1st', '2nd', '3rd')
itr = iter(iterable_obj) #iterator object
type_itr = type(itr) # tuple_iterator

# access 
# using next()
elem1 = next(itr)
elem2 = next(itr)
#using loop
for i in iterable_obj:
    pass
# for loop actually creates an iterator obj and execute next() method on each loop

# create iterator obj
# must include __iter__() & __next__()
# __iter__() -- Do operations( like initialization) and return self
# __next__() -- Do oprations and return next item in the seq

class my_itr:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        self.count = 1
        return self
    def __next__(self):
        if self.count <= self.stop:
            x = self.count
            self.count += 1
            return x
        else:
            raise StopIteration

iterable_obj = my_itr(10)
# since my_itr class has both iter() & next() methods,
# hence its obj are itrable obj
itr = iter(iterable_obj)
for i in itr:
    # print(i)
    pass





print(itr)