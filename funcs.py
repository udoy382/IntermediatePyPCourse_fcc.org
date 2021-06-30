"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- Parameter passing (by value or by reference?)

"""

# def print_name(name):
#     print(name)

# print_name('Udoy')

#----------------------------
'''
def fool(a, b, c, d=4):
    print(a, b, c, d)

# fool(1, 2, 3)
# fool(a=1, b=2, c=3) # ordered key

fool(1, 2, 3, 7)
'''
#-------------------------------
'''
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5)
'''
#-----------------------------------
'''
def foo(a, b, c):
    print(a, b, c)

my_list = [0, 1, 2]
my_dict = {'a':1, 'b':2, 'c':3}
# print(my_list)

foo(*my_list)
foo(**my_dict)
'''
#-------------------------------------
'''
def foo():

    # global number
    # x = number

    global number
    number = 3

    # print('number inside function: ', x)

number = 0
foo()
print(number)
'''
#---------------------------------------
# mutable object - can change
# immutable object - cannot change

def foo(a_list): # add x for x=5
    # x = 5
    # a_list = [200, 300, 400] 
    a_list.append(4)
    a_list[0] = 100

# var = 10
my_list = [1, 2, 3]

# foo(var)
foo(my_list)

# print(var)
print(my_list)