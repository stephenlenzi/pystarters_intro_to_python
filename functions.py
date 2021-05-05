
"""functions - we have hopefully each written a python script to take an arbitrary section of this data,
get coordinates when a mouse is in a particular part of the coordinate space, and """


a = 27
b = 8


def add():
    a = 5
    b = 10
    return a + b

type(add)
add()



def add(a, b):
    return a + b

add()


def add(a, b):
    a + b

add(5, 29)


add(5)


def add(a, b=2):
    return a + b

"""rewrite your script but using three distinct functions

1) load the x,y positions using the file path as the only argument
2) get the coordinates of points that cross an arbitrary x threshold with a default set to 200
3) plot the tracks and the overlaid points

try to do it in as few lines as possible
"""


