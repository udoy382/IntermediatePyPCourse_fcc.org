# Strings: ordered, immutable, text representation

from timeit import default_timer as timer

# my_string = "Hello world"
# my_string2 = 'I am udoy'

# my_string3 = """Hello
# world"""

# print(my_string3)

#--------------

x = "Hello world"
# y = x[0] = 'h'
# print(y)

# substring = x[::-1]
# print(substring)

greeting = "Hello"
# name = "Tom"
# sentence = greeting + " " + name
# print(sentence)

# for i in greeting:
#     print(i)

# if 'ell' in greeting:
#     print("Yes")
# else:
#     print("No")

z = '     Hello udoy     '
z = z.strip()
# print(z)

# print(z.upper())
# print(z.lower())
# print(z.startswith('Hello'))
# print(z.endswith('udoy'))
# print(z.find('o'))
# print(z.count('o'))
# print(z.replace('udoy', 'Universe'))

#-------------

# strings = 'how,are,you,doing'
# my_list = strings.split(",")
# print(my_list)
# new_string = ' '.join(my_list)
# print(new_string)

#--------------
'''
j = ['a'] * 666666
# print(j)

# bad
start = timer()
k = ''
for i in j:
    k += i
stop = timer()
print(stop-start)

# good
start = timer()
l = ''.join(j)
# print(l)
stop = timer()
print(stop-start)
'''

#-----------
# %, .formart(), f-string
# %s for string / %d for decimal value / %f for floting point

var = "Tom"
var2 = 4
var3 = 3.9
# my_string = "the variable is %f" %var3
my_string2 = "the variable is {:.2f}".format(var3)
# print(my_string2)

my_string3 = f"the variable is {var} and {var2} and {var3}"
print(my_string3)