#unit 42. decorator

#42.1 decorator 만들기 

    #decorator : 함수를 감싸는 형태로 구성, 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용


#함수의 시작과 끝을 출력하는 decorator 만들기 
def trace(func):
    def wrapper():
        print(func.__name__, 'func start')
        func()
        print(func.__name__, 'func end')
    return wrapper      #wrapper 함수 자체를 반환 -> 함수 안에서 함수를 만들고 반환하는 클로저

def hello():
    print('hello')

def world():
    print('world')

trace_hello = trace(hello)
trace_hello()
trace_world = trace(world)
trace_world()


#@로 decorator 사용하기
    # @decorator
    # def 함수이름():
    #     statement

@trace
def hi():
    print('hi')

@trace
def good():
    print('good')

hi()
good()



#decorator를 여러 개 지정하기 : decorator는 위에서 아래의 순서로 실행된다
    # @decorator1
    # @decorator2
    # def 함수이름():
    #     statement

def dec1(func):
    def wrapper():
        print('dec 1')
        func()
    return wrapper

def dec2(func):
    def wrapper():
        print('dec 2')
        func()
    return wrapper

@dec1
@dec2
def hello():
    print('hello')

hello()
# dec 1
# dec 2
# hello


#이는 @를 사용하지 않았을 때 다음과 동작이 같다 - nested decorator 
def bye():
    print('bye')

decorated_bye = dec1(dec2(bye))
decorated_bye()
# dec 1
# dec 2
# bye


