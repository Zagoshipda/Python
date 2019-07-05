
def trace(func):
    def wrapper(a, b):
        print(func.__name__, 'func start')
        r = func(a, b)
        print(func.__name__, 'func end')
        return r
    return wrapper      #wrapper 함수 자체를 반환 -> 함수 안에서 함수를 만들고 반환하는 클로저

def is_multiple(x):
    def dec(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0}'s return value is multiple of {1}".format(func.__name__, x))
            else:
                print("{0}'s return value is NOT multiple of {1}".format(func.__name__, x))
            return r
        return wrapper
    return dec



@is_multiple(2)
@is_multiple(3)
def add(a, b):
    return a + b
print(add(1, 2))
# add's return value is multiple of 3
# wrapper's return value is NOT multiple of 2
# 3


print('\nnot using @ ===== ')
def add2(a, b):
    return a + b
# f = is_multiple(2)(trace(add))
f = is_multiple(3)(is_multiple(2)(add2))
print(f(2, 2))
# add2's return value is multiple of 2
# wrapper's return value is NOT multiple of 3
# 4


print('\ncombine 2 diff decorators')
@trace
@is_multiple(2)
def add3(a, b):
    return a + b

print(add3(1, 2))
# wrapper func start
# add3's return value is NOT multiple of 2
# wrapper func end
# 3


@is_multiple(2)
@trace
def add4(a, b):
    return a + b

print(add4(2, 4))
# add4 func start
# add4 func end
# wrapper's return value is multiple of 2
# 6



print('\nusing 2 parameters in decorator ----- ')

import functools

def is_multiple2(x, y):
    def dec(func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0} : return val is mul of {1}".format(func.__name__, x))
            else:
                print("{0} : return val is NOT mul of {1}".format(func.__name__, x))
            if r % y == 0:
                print("{0} : return val is mul of {1}".format(func.__name__, y))
            else:
                print("{0} : return val is NOT mul of {1}".format(func.__name__, y))
            return r
        return wrapper
    return dec

@is_multiple2(2, 3)
def add2(a, b):
    return a + b

print(add2(1, 2))
# add2 : return val is NOT mul of 2
# add2 : return val is mul of 3
# 3
