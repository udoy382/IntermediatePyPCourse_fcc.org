# Tuple: ordered, immutable, allows duplicate elements

# mytuple = ("Max", 28, "Boston")
# mytuple2 = ("Max",)
mytuple3 = tuple(["Max", 27, "Boston"])
# print(mytuple3)
# print(type(mytuple3))

# -----------
# item = mytuple3[-2]
# print(item)

# -----------
#       tuple does not change it is a immutable

# mytuple3[0] = "Tim"

# -----------
# for x in mytuple3:
#     print(x)

# -----------
# if "Boston" in mytuple3:
#     print("yes")
# else:
#     print("no")


# -----------
# my_tuple = ('a', 'p', 'p', 'l', 'e')
# # print(len(my_tuple))
# # print(my_tuple.count('p'))
# # print(my_tuple.index('j'))

# my_list = list(my_tuple)
# print(my_list)

# tuple2 = tuple(my_list)
# print(tuple2)

# ------------
# a = (1, 2, 3, 4, 5, 6, 7, 8)

# b = a[::-2]

# print(b)

#-------------
# my_tuple1 = "Max", 28, "Boston"

# name, age, city = my_tuple1
# print(name)
# print(age)
# print(city)

#-----------
# my_tuple2 = (0, 1, 2, 3, 4)

# i1, *i2, i3 = my_tuple2
# print(i1)
# print(i3)
# print(i2)

#-------------
#       comphare to list and tuple

import sys
my_list = [0, 1, 2, "helo", True]
my_tuple = (0, 1, 2, "helo", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))