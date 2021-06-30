# itertools: product, permutations, accumulate, groupby, and infinite iterators

# from itertools import product
# from itertools import permutations
# from itertools import combinations
# from itertools import combinations, combinations_with_replacement

# from itertools import accumulate
# import operator

from itertools import groupby, count, cycle, repeat


a = [1, 2]
b = [3, 4]
# prod = product(a,b)
# prod = product(a,b, repeat=2)
# print(list(prod))

# ----------------

x = [1, 2, 3]
# perm = permutations(x)
# perm = permutations(x, 2)
# print(list(perm))

# ------------------

z = [1, 2, 3, 4]
# comb = combinations(z, 2)
# print(list(comb))

# comb_wr = combinations_with_replacement(z, 2)
# print(list(comb_wr))

# -------------------

m = [1, 2, 5, 3, 4]
# acc = accumulate(m)
# acc = accumulate(m, func=operator.mul)
# acc = accumulate(m, func=max)
# print(m)
# print(list(acc))

#--------------

def smaller_than_3(x):
    return x < 3

n = [1, 2, 3, 4]
# group_obj = groupby(n, key=smaller_than_3) # or 
# group_obj = groupby(n, key=lambda x: x<3)
# print(group_obj)
# for key, value in group_obj:
#     print(key, list(value))

#-----------------
#       Danger:- infinity loop

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

#---------------
#       Danger:- infinity loop

# g = [1, 2, 3]
# for i in cycle(g):
#     print(i)
#     if i == 20:
#         break

#------------------
        # Danger:- infinity loop

# g = [1, 2, 3]
# for i in repeat(1, 4):
#     print(i)