a = 123456789.123456789
b = 123456789.123456789
print(a == b)  # True
print(a is b)  # True id(a) == id(b)
print(hex(id(a)), hex(id(b)))
print(id(a), id(b))

a, b = 5, 5
print(a, b, a == b, a is b) 

'''
object with no references - deleted object
'''
