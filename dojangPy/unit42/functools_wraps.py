# https://docs.python.org/3/library/functools.html

from functools import wraps
def my_decorator(f):
    # @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()
# Calling decorated function
# Called example function

print(example.__name__) #example    /   wrapper (when not using wraps)
print(example.__doc__)  #Docstring  /   None    (when not using wraps)


#what is __name__ ...?

def a():
    def b():
        pass
    return b
print(a.__name__)   #a
b = a()
print(b.__name__)   #b



def trace(func):
    def wrapper():
        print(func.__name__, 'func start')
        func()
        print(func.__name__, 'func end')
    return wrapper      #wrapper 함수 자체를 반환 -> 함수 안에서 함수를 만들고 반환하는 클로저

def hello():
    print('hello')

print(hello.__name__)   #hello



@trace
def hello():
    print('hello')

print(hello.__name__)   #wrapper ---> decorator로 wrapping하면 가려짐...!
