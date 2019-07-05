#42.5 Class 로 Decorator 만들기
    #1) 클래스로 매개변수와 반환값이 있는 함수를 처리하는 decorator 만들기
    #2) 클래스로 매개변수를 가지는 decorator 만들기





#1) 매개변수를 가진 함수의 return value를 출력하는 decorator 만들기 : positional / keyword argument 를 모두 처리할 수 있는 가변 인수 함수로 만들기
    #__call__()에 매개변수를 지정하고, self.func()에 매개변수를 넣어서 호출한 뒤에 반환값을 반환해준다(value를 return할 지는 원래 함수가 값을 return하는지 안하는지에 따라 결정됨)

class Trace:
    def __init__(self, func):   #호출할 함수를 instance의 초깃값으로 받음
        self.func = func        #호출할 함수를 속성 func에 저장
    def __call__(self, *args, **kwargs):    #__call__()에 매개변수를 지정
        r = self.func(*args, **kwargs)  #매개변수를 *args, **kwargs로 지정했으므로 self.func에 넣을 때는 unpacking하여 넣어준다
        print('{0} : (args = {1}, kwargs = {2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
        return r    #add 함수가 return 하므로 __call__()도 마찬가지로 return


@Trace
def add(a, b):
    return a + b

print(add(1, 2))
print(add(a = 4, b = 5))
# add : (args = (1, 2), kwargs = {}) -> 3
# 3
# add : (args = (), kwargs = {'a': 4, 'b': 5}) -> 9
# 9




print('\nClass decorator with parameter --- ')
#2) 클래스로 매개변수를 가지는 decorator 만들기


#함수의 반환값이 특정 수의 배수인지 확인하는 decorator
import functools

class IsMultiple:
    def __init__(self, x):  #이전까지는 호출할 함수func를 매개변수로 받았는데 여기서는 데코레이터가 사용할 매개변수를 받는다
        self.x = x

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(a, b):
            r = func(a, b)
            if r % self.x == 0:
                print("{0}'s return val is mul of {1}".format(func.__name__, self.x))
            else:
                print("{0}'s return val is NOT mul of {1}".format(func.__name__, self.x))
            return r
        return wrapper

@IsMultiple(3)
@IsMultiple(2)
def add(a, b):
    return a + b

print(add(1, 2))
print(add(2, 3))
# add's return val is NOT mul of 2
# add's return val is mul of 3 / wrapper's return val is mul of 3
# 3
# add's return val is NOT mul of 2
# add's return val is NOT mul of 3 / wrapper's return val is NOT mul of 3
# 5



print('\nDec with multiple param + func with param and ret val')

class IsMultiple2:
    def __init__(self, x, y):  #__init__ 에 func를 받아야하는지 decorator의 parameter를 받아야 하는지...?
        self.x = x
        self.y = y

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)

            if r % self.x == 0:
                print("{0}'s return val is mul of {1}".format(func.__name__, self.x))
            else:
                print("{0}'s return val is NOT mul of {1}".format(func.__name__, self.x))

            if r % self.y == 0:
                print("{0}'s return val is mul of {1}".format(func.__name__, self.y))
            else:
                print("{0}'s return val is NOT mul of {1}".format(func.__name__, self.y))

            return r
        return wrapper

@IsMultiple2(1, 2)
@IsMultiple2(2, 3)
def add2(a, b):
    return a + b

print(add2(a = 1, b = 2))
# add2's return val is NOT mul of 2
# add2's return val is mul of 3
# add2's return val is mul of 1 / wrapper's return val is mul of 1
# add2's return val is NOT mul of 2 / wrapper's return val is NOT mul of 2
# 3


print('\nTest 2 --- ')

class plusVal():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)


@plusVal(1, 2)
@plusVal(2, 3)
def findMin(*args, **kwargs):
    return min(min(args), min(kwargs.values()))

print(findMin(a = 1, b = 2, c = 3))



a = [1, 2, 3]
print('list sum:', sum(a))  #list sum: 6

b = {'a' : 1, 'b' : 2, 'c' : 3}
print('dict sum:', sum(b.values())) #dict sum: 6


c = [2, 3, 4]
print(max(a, b))
