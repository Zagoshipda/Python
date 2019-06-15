#unit 33 클로저closure 사용하기 


#변수의 사용 범위

x = 10
def foo():
    print(x)

foo()       #10
print(x)    #10


def foo2():
    y = 2   #local variable
    print(y)

foo2()      #2
# print(y)    #NameError: name 'y' is not defined



#함수 안에서 전역 변수 변경하기 : global (global variable)
def foo():
    x = 2   # -> x는 global variable이 아닌 또다른 local variable
    print(x)
foo()       #2 
print(x)    #10

def foo():
    # global x = 3    #SyntaxError: invalid syntax -> why...?
    global x
    x = 3
    print(x)

foo()       #3
print(x)    #3
    

#만약 global variable이 없을 때 함수 안에서 global을 사용하면 해당 변수는 전역 변수가 된다
def foo():
    global z 
    z = 9
    print(z)
foo()       #9
print(z)    #9 -> 근데 warning 이 잡히긴 함....





#namespace : 파이썬에서 변수는 이름공간namespace에 저장된다 : locals() 함수를 사용하면 현재 namespace를 dictionary형태로 출력할 수 있음 

x = 7
print(locals())

# global namespace 전역범위에서의 출력
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x01BCB050>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\JGB\\coding\\python\\dojangPy\\unit33\\33_1.py', '__cached__': None, 'x': 10, 'foo': <function foo at 0x01BF86F0>, 'foo2': <function foo2 at 0x01BF86A8>, 'z': 9}

def foo():
    x = 5
    print(locals())

foo()   #{'x': 5} -> local namesapce 지역 범위에서의 출력
