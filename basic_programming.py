
"""
Programming is essentially a list of commands that are executed in order to produce some output
To keep track of the data, and to make it human-readable, we give names to the outputs at various points. These named
data are called variables.

There are lots of different kinds of variables types that you will encounter. We will cover some simple ones.

- Variables
A variable is something you declare, just a name you give to some value/computation so that you can read your code
"""
a = 5
b = 10
c = a * b
a = b = 5
a, b = 5, 10
a, b = b, a

"""
do something with the variables:"""

print(a)
print(a+b)

"""coding is more than just integers"""

print(type(5))

"""- Data types
    basic types (integers, floats, strings)
    data types behave differently and do different things
    
    https://docs.python.org/3/library/stdtypes.html
    
    """

my_string_variable = 'heyyyyyyyyya'
print(my_string_variable)
print(type(my_string_variable))
print(my_string_variable + ' playyya')


"""what happens if you try to add two different types?"""

"""dealing with many things (lists, tuples)"""

my_randomly_organised_stuff = [1, 55, 218, 'cheese', 14, my_string_variable, 55, 1]
my_number_list = [1, 55, 218, 555, 222, 2123, 55, 1]

"""indexing """
my_randomly_organised_stuff[0]
my_randomly_organised_stuff[3]
my_randomly_organised_stuff[-1]
my_randomly_organised_stuff[-5]

my_randomly_organised_tuple = (1, 55, 218, 'cheese', 14, my_string_variable, 55, 1)
my_randomly_organised_tuple[3]


"""- mutability"""
my_randomly_organised_stuff[3] = 'gouda'

"""- print the list, see that is has changed
   - what happens if you do the same thing for my_randomly_organised_tuple?"""

my_randomly_organised_tuple[3] = 'gouda'

""""- tuple unpacking"""
my_tuple = (1, 5, 6, 60, 200, 20)
a, b, c, d, e, f = my_tuple
a, *b, c = my_tuple
""" try to split the tuple such that the first three elements go into a single variable"""

"""- dictionaries, arrays and sets"""

my_set_of_randomly_organised_stuff = set(my_randomly_organised_stuff)  # casting from a list to a set
my_number_set = set(my_randomly_organised_stuff)
my_set_of_randomly_organised_stuff.intersection(my_number_set)


my_dictionary_of_stuff = {'stringy_things': ['cheese', my_string_variable], 'numerical_things': [1, 55, 218, 14], 'the number one': 1}

"""keys dont have to be strings"""

my_dictionary_of_stuff = {'stringy_things': ['cheese', my_string_variable], 'numerical_things': [1, 55, 218, 14], 'the number one': 1}
my_dictionary_of_stuff.keys()
my_dictionary_of_stuff.values()
my_dictionary_of_stuff.items()

my_dictionary_of_stuff['stringy_things']
my_dictionary_of_stuff['stringy_things'][0]

""" make a dictionary of your own that uses numbers as keys and strings as values"""


"""- Loops
    - what if we have lots of numbers to add together
    - loop through each element in a list
    - for each vs for i in
"""

for number in my_number_list:
    print(number)

for x in my_number_list:
    print(number)
"""maybe this does not work as expected. what result do you get? can you figure out what is happening?"""


"""getting the loop iteration"""

for item in my_dictionary_of_stuff.items():
    print(item)

for i, item in enumerate(my_dictionary_of_stuff.items()):
    print(i, item)


"""Conditional statements
    - what if we only want to add numbers that fulfil some specific criteria?"""

total = 0
for x in my_number_list:
    if x > 200:
        print(x)
        total += x
    elif x < 200:
        print('this number is too small to print')
    elif x == 200:
        print('200')
    else:
        print('if you are seeing this something has gone wrong')

"""what if instead of the number list you do this with my_randomly_organised_stuff
    - can you modify this code so that it still works?
    - can you make it subtract 50 from the total if the value is a string?
    """


"""Installing packages with pip
install numpy, matplotlib and pandas
    add some lines to the script that use numpy as matplotlib
    run the script."""


import numpy as np
import matplotlib.pyplot as plt


x = np.random.normal(np.ones(5000))
y = np.random.normal(np.ones(5000))

plt.figure()
plt.scatter(x, y, color='k')
plt.show()


"""replot the data, but plot making sure the top left quadrant is red and the bottom left quadrant black"""

"""Python can be executed in different ways. Integrated Development Environments (IDEs) allow you do to this in a user
friendly way (think Pycharm, or MATLAB). However, the simplest thing we can do is run python ourselves from the
command line.


make a script
the data is a track (x,y positions) of a mouse running around a box
    - load using numpy
    - plot the data
    - cut the data down to the first minute and plot that on top in a different color
    - find the points where the mouse crosses the 200 line in x
    - plot a red dot at these x, y locations 
    - print the estimated x_speed to the console (hint the x speed is in the csv) 
    - save the figure

"""

