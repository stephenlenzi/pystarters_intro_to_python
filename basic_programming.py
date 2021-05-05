"""
Programming is essentially a list of commands that are executed in order to produce some output
To keep track of the data, and to make it human-readable, we give names to the outputs at various points. These named
data are called variables.

There are lots of different kinds of variables types that you will encounter. We will cover some simple ones.

A variable is something you declare, just a name you give to some value/computation so that you can read your code
"""


"""Assigning variables"""

a = 5
b = 10

print(b)

"We can define new variables using existing ones"

c = a * b
print(c)

a = b = 5
a, b = 5, 10
a, b = b, a

print(a)


"""try printing the sum of two variables"""


"""coding is more than just integers"""

print(type(5))
print(type(5.6))
print(type('text'))


"""- Data types
    basic types (integers, floats, strings)
    data types behave differently and do different things

    https://docs.python.org/3/library/stdtypes.html

    """

my_first_name = 'Stephen'
my_last_name = 'Lenzi'

my_full_name = my_first_name + ' ' + my_last_name

print(my_first_name)
print(type(my_first_name))
print(my_full_name)

"""what happens if you try to add two different types together?"""


"""some data types allow you to deal with many things (e.g. lists, tuples)"""
my_empty_list = []
my_randomly_organised_stuff = [1, 55, 218, 'cheese', 14, my_full_name, 55, 1]

my_number_list = [1, 55, 218, 555, 222, 2123, 55, 1]

"""indexing - i.e. getting stuff out of lists/arrays/etc"""

my_randomly_organised_stuff[0]

"""get the 3rd element of the list"""

my_randomly_organised_stuff[-1]

"""get the 3rd element from the end of the list by indexing"""

"""adding things to a list"""
my_empty_list.append('cheese')

"""tuples"""
my_randomly_organised_tuple = (1, 55, 218, 'cheese', 14, my_full_name, 55, 1)
my_randomly_organised_tuple[3]


"""- mutability: sometimes you want to change the data"""
my_randomly_organised_stuff[3] = 'gouda'

"""- print the list, see that is has changed
   - what happens if you do the same thing for my_randomly_organised_tuple?
   - what happens if you try to append to a tuple?
"""

my_randomly_organised_tuple[3] = 'gouda'

""""unpacking"""
my_tuple = (1, 5, 6, 60, 200, 20)
a, b, c, d, e, f = my_tuple
a, *b, c = my_tuple

"""what are the types of a, b and c?"""

"""try to split the tuple such that the first three elements go into a single variable"""

"""Dictionaries, Arrays and Sets"""

my_set_of_randomly_organised_stuff = set(my_randomly_organised_stuff)  # casting from a list to a set
my_number_set = set(my_number_list)
my_set_of_randomly_organised_stuff.intersection(my_number_set)

my_dictionary_of_stuff = {'stringy_things': ['cheese', my_full_name],
                          'numerical_things': [1, 55, 218, 14],
                          'the number one': 1}

my_dictionary_of_stuff.keys()
my_dictionary_of_stuff.values()
my_dictionary_of_stuff.items()


"""Indexing: can you access cheese from the dictionary?"""

"""Make a dictionary of your own that uses numbers as keys and strings as values"""


""" Loops
    - sometimes you want to run snippets of code many times
    - e.g. what if we have 100 numbers to add together, it would be tiresome to write 100 lines of code
    - loop through each element in a list
    - for each vs for i in
"""

for i in range(10):
    print(i)

for number in my_number_list:
    print(number)

for x in my_number_list:
    print(number)

"""maybe this does not work as expected. what result do you get? can you figure out what is happening?"""


"""getting (and using) the loop iteration"""

for item in my_dictionary_of_stuff.items():
    print(item)

for i, item in enumerate(my_dictionary_of_stuff.items()):
    print(i, item)

""""Write a loop that iterates through my_number_list and adds the values to a variable called running_total"""

"""Conditional statements
    
    What if we only want to add numbers that fulfil some specific criteria?"""

running_total = 0
for x in my_number_list:
    if x > 200:
        print(x)
        running_total += x
    elif x < 200:
        print('this number is too small to print')
    elif x == 200:
        print('200')
    else:
        print('if you are seeing this something has gone wrong')

"""
What if instead of my_number_list you do this with my_randomly_organised_stuff
    - does it work the same way? If not, why not?
    - can you modify this code so that it runs to completion without triggering an error?
    - can you modify the code such that 50 is subtracted from the total if x is a string?
"""


"""Installing packages with pip
install numpy, matplotlib and pandas
    add some lines to the script that use numpy as matplotlib
    run the script."""


import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(np.zeros(500))
y = np.random.normal(np.zeros(500))

plt.figure()
plt.scatter(x, y, color='k')

plt.show()


"""using what we have learned about loops, and conditional statements, replot each quadrant in a different color

Bonus: try to achieve the same using np.logical_and()
"""

"""Python can be executed in different ways. Integrated Development Environments (IDEs) allow you do to this in a user
friendly way (think Pycharm, or MATLAB). However, the simplest thing we can do is run python ourselves from the
command line.

make a script (called my_first_script.py)

the data is a track (x,y positions) of a mouse running around a box
    - load using numpy or pandas
    - plot the data
    - cut the data down to the first 1000 frames and plot that on top in a different color
    - find the points where the mouse crosses the 200 line in x
    - and the corresponding points in y(hint: try using numpy.where())
    - plot a red dot at these x, y locations (use plt.scatter)
    - print the estimated x_speed at these locations to the console (hint the x speed is in the csv) 
    - save the figure

    - try to do this again for the last 500 frames, with a crossing value of 400 (is it easy for you to change?)
"""


