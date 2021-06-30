# Sets: unordered, mutable, no duplicates

# myset = {1, 2, 3, 1, 2, 3, 4}
# myset = set([1, 2, 3, 3])
# myset = set("Hello")

myset = set()
# print(myset)
# print(type(myset))


# myset.add(1)
# myset.add(2)
# myset.add(4)
# myset.add(88)

# myset.remove(4)
# myset.discard(44) # does not show error, when it not found number for remove
# myset.clear()
# print(myset.pop())
# print(myset)

# for i in myset:
#     print(i)

# if 44 in myset:
#     print("yes")
# else:
#     print("no")

#------------
#       calculate union

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = evens.intersection(primes)
# print(i)

#----------------

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1,2, 3, 10, 11, 12}

# diff = setB.difference(setA)
# print(diff)

#       print both of sets value are not same
# diff = setA.symmetric_difference(setB)
# print(diff)

# setA.update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

# setA.symmetric_difference_update(setB)
# print(setA)

# print(setB.issubset(setA))
# print(setB.issuperset(setA))
# print(setA.isdisjoint(setB))

#       there is two way to copy sets value

# setB = setA.copy()
# setB = set(setA)

# setB.add(79)
# print(setB)
# print(setA)

#       there is frozentset its cannot change or remove or more
# a = frozenset([1, 2, 3, 4])
# print(a)