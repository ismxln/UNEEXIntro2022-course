a = 123456789.123456789
b = 123456789.123456789
print(a == b)  # True
print(a is b)  # True, id(a) == id(b)
print(hex(id(a)), hex(id(b)))
print(id(a), id(b))

a, b = 5, 5
print(f'a = {a}',f'b = {b}', a == b, a is b) 

'''
object with no references - deleted object
int, str, tuple, etc. - constant objects
only - new object/delete old object.
'''

a=b=c=1234
print('a = {a}, b = {b}, c = {c}')
print('a is b: {a is b}')
print('a is b is c: {a is b is c}')

a, b, *c, d, e = 'QWERTYUIOP'  # c = ['E', 'R', 'T', 'Y', 'U', 'I']
print(a, b, c, d, e)  # Q W ['E', 'R', 'T', 'Y', 'U', 'I'] O P
