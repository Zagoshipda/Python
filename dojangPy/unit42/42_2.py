#42.2 매개변수와 반환값을 처리하는 decorator 만들기 



def trace(func):            #호출할 함수를 argument로 받음
    def wrapper(a, b):      #안쪽 wrapper 함수의 매개변수를 호출할 함수 func의 매개변수와 똑같이 설정 
        r = func(a, b)      #func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0} : (a = {1}, b = {2}) -> {3}'.format(func.__name__, a, b, r))
        return r            #func의 반환값을 반환 -> func의 반환값을 반환하지 않으면 add 함수를 호출해도 반환값이 나오지 않는다. 원래 func함수의 동작과 동일한 동작을 할 수 있도록 wrapper 함수를 design해야 함 
    return wrapper          #wrapper 함수 반환 

                            #wrapper 함수에서 func의 반환값을 출력할 필요가 없으면 return func(a, b)처럼 func를 호출하면서 바로 반환해도 됩니다

@trace
def add(a, b):
    return a + b 

print(add(10, 20))  
#add : (a = 10, b = 20) -> 30   ---> decorator output   
#30                             ---> add function output





print()
# 가변 인수argument 함수의 decorator : 매개변수가 고정되지 않은 함수의 처리는...? -> wrapper 함수도 마찬가지로 가변 인수 함수로 만든다  
def trace(func):        #positional / keyword argument를 모두 처리할 수 있도록 design하기 
    def wrapper(*args, **kwargs):   #positional argument와 keyword argument를 모두 받을 수 있도록 *args와 **kwargs를 지정 -> wrapper function을 가변 인수 함수로 만들기 
        r = func(*args, **kwargs)   #func을 호출, args는 list이고 kwargs는 dictionary이므로 func에 넣을 때는 args, kwargs를 언패킹하여 넣어준다
        print('{0} : (args = {1}, kwargs = {2}) -> {3}'.format(func.__name__, args, kwargs, r))     #매개변수와 함수의 반환값을 출력해서 확인 
        return r        #func의 반환값을 반환
    return wrapper      #wrapper 함수 반환


@trace              
def get_max(*args):     #positional argument를 사용하는 가변 인수 함수 
    return max(args)

@trace
def get_min(**kwargs):  #keyword argument를 사용하는 가변 인수 함수 
    return min(kwargs.values())     #get_min : (args = (), kwargs = {'x': 1, 'y': 2, 'z': 3}) -> 1
    # return min(kwargs.keys())       #get_min : (args = (), kwargs = {'x': 1, 'y': 2, 'z': 3}) -> x
    # return min(kwargs.items())      #get_min : (args = (), kwargs = {'x': 1, 'y': 2, 'z': 3}) -> ('x', 1)

@trace 
def add(a, b):
    return a + b

print(get_max(1, 2, 3, 4, 5))
print(get_min(x = 1, y = 2, z = 3))
print(add(3, 5))

# get_max : (args = (1, 2, 3, 4, 5), kwargs = {}) -> 5
# 5
# get_min : (args = (), kwargs = {'x': 1, 'y': 2, 'z': 3}) -> 1
# 1
# add : (args = (3, 5), kwargs = {}) -> 8
# 8




print('class ===== ')
#method에 decorator 사용하기 
    #(instance) method는 항상 self를 첫 번째 argument로 받으므로 decorator를 만들 때도 wrapper 함수의 첫 번째 매개변수는 self로 지정해야 한다. (클래스 메서드는 cls) 마찬가지로 func를 호출할 때도 self와 매개변수를 그대로 넣어주어야 한다

def trace(func):
    def wrapper(self, a, b):
        r = func(self, a, b)
        print('{0} : (a = {1}, b = {2}) -> {3}'.format(func.__name__, a, b, r))
        return r
    return wrapper

class Calc:
    @trace
    def add(self, a, b):
        return a + b

c = Calc()
print(c.add(7, 8))

# add : (a = 7, b = 8) -> 15
# 15
