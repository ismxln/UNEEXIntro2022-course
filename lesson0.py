dfgdfghjk = 100500
print(dfgdfghjk)

dfgdfghjk = 'SDFSDFJO'
print(type(dfgdfghjk))

dfgdfghjk = 100500
print(type(dfgdfghjk))


def add(a, b):
    return a + b


x, y = 100, 500
# what methods does the object x have? dir(x)
print(dir(x))  # is there an add operation for an integer object
print(add(x, y))

x, y = '100', '500'
print(dir(x))  # is there an add operation for a string object
print(add(x, y))

"""
names are - references to objects, objects are - always strongly typed, the type is always known.
the operations that we can do - are just a set of methods that operations have, - duck typing.

default modules in python = https://docs.python.org/3/py-modindex.html
"""

