# Errors and Exceptions


# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)


# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print("its error")


# try:
#     a = 5 / 0
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)


# try:
#     a = 5 / 0
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('everything is fine')
# finally:
#     print('cleaning up...')

# -------------------------------------------
# make our own exceptions error 
# -------------------------------------------

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, massage, value):
        self.massage = massage
        self.value = value

def test_value(x):
    if x >100:
        raise ValueTooHighError('value too high')
    if x < 5:
        raise ValueTooSmallError('value too small', x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)