# List: ordered, mutable, allows duplicate elements

# myList = ["banana", "cherry", "apple"]
# print(myList)

# myList2 = [5, True, "äpple", "apple"]

#----------
# item = myList[-2]
# print(item)

#---------
# for i in myList:
#     print(i)

#---------
# if "apple" in myList:
#     print("yes")
# else:
#     print("no")

# print(len(myList))

#----------
# myList.append("lemon")
# print(myList)

#----------
# myList.insert(1, "blueberry")
# print(myList)

#----------
# item = myList.pop()
# item = myList.remove("cherry")
# item = myList.clear()
# item = myList.reverse()
# item = myList.sort()
# print(item)
# print(myList)


# new_list = sorted(myList)
# print(myList)
# print(new_list)

#-----------

# my_list = [0] * 5
# print(my_list)

# my_list2 = [1,2, 3, 4, 5]
# new = my_list + my_list2
# print(new)

#-----------
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = list1[::-1]
# print(a)

#-----------
#       copy the list some methods
'''
list_org = ["banana", "cherry", "apple"]

# list_cpy = list_org.copy()
# list_cpy = list(list_org)
list_cpy = list_org[:]

list_cpy.append("lemon")

print(list_cpy)
print(list_org)
'''

#------------
#       one liner list

a = [1,2, 3, 4, 5, 6]
b = [x*x for x in a]
print(a)
print(b)