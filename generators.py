def myGenerator():
    yield 3
    yield 2
    yield 1

g = myGenerator()
# print(type(g))

'''
value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


# for i in g:
#     print(i)

'''

# print(sum(g))

# print(sorted(g))

'''
def Countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num +=1

cd = Countdown(4)

value = next(cd)
print(value)

print(next(cd))

'''

'''
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# print(sum(firstn(10)))
# print(sum(firstn_generator(10)))

# print(sys.getsizeof(firstn(1000000)))
# print(sys.getsizeof(firstn_generator(1000000)))

'''

'''
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

'''
import sys
mygenerator = (i for i in range(10) if i  % 2 == 0)
# for i in mygenerator:
#     print(i)

print(list(mygenerator))
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10) if i  % 2 == 0]
print(mylist)
print(sys.getsizeof(mylist))