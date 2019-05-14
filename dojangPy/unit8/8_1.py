# 8.1 불과 비교 연산자 사용하기 

print(3>1)  #true
print(3<1)  #false

print(10 == 10) #true
print(10 != 10) #false

# 문자열 비교 -> 대소문자를 구분한다
print('python' == 'python') #true
print('Python' != 'python') #true
print('Python' == 'python') #false

# 부등호의 비교 기준은 첫 번째 값
print(10 >= 10) #true
print(10 <= 10) #true
print(10 < 10)  #false

# 객체 비교하기 - is/ is not
# ==, != 는 값 자체를 비교하고, is, is not 은 객체(object)를 비교한다
# is, is not은 클래스로 객체를 만든 뒤에 객체가 서로 같은지 비교할 때 주로 사용
print(1 == 1.0)     #true, 값이 같다
print(1 is 1.0)     #false, 1은 정수 객체, 1.0은 실수 객체이므로 두 객체는 서로 다르다
print(1 is not 1.0) #true

# 정수 객체와 실수 객체가 서로 다른 것 확인하기 -> id 함수 사용 
# id 함수는 객체의 고유한 값(메모리 주소)을 구한다.(이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라진다) ...??
# id 값이 다르다면 서로 다른 객체라고 할 수 있음 

print(id(1))    # 다시 실행해도 변하지 않음
print(id(1.0))  # 프로그램을 실행할 때마다 바뀜....??? 

# 정수와 실수를 저장하는 메모리 영역에 차이가 있는 것...?


# 변수에 다른 값을 할당하면 메모리 주소가 달라진다. ....?? 그렇다면 변수의 값을 바꾼다기보다는 아예 새로운 메모리 공간을 할당하고 다른 값을 assign 하는 것인지?
a = 5
print(a is 5)   # true
print(a is 7)   # false
a = 7
print(a is 5)   # false
print(a is 7)   # true


# https://tech.songyunseop.com/post/2017/09/python-comparing/
# 의문해결: Python Interpreter에서 [-5, 256] 범위의 Integer를 미리 캐싱(?) 하고 있음 
# 아래처럼 함수로 만들어서 실행하거나 지금처럼 스크립트를  파일 내부에서 한번에 실행하는 경우에는 모두 true가 나온다. 하지만 한 줄씩 실행하면 [-5, 256] 범위에서만 true가 나오고 나머지는 false가 나온다 
def test():
    a = -5
    print(a is -5)     #true
    a = -6
    print(a is -6)     #true
    a = 257
    print(a is 257)    #true
test()

b = -5
print(b is -5)      #true
b = -6
print(b is -6)      #true

c = 256
print(c is 256)     #true
c = 257 
print(c is 257)     #true

print(id(2))
print(id(2))
a = 2
print(id(a))

# https://stackoverflow.com/questions/306313/is-operator-behaves-unexpectedly-with-integers
# 스크립트를 한 줄씩 실행해보면 256일 떄는 id값이 같지만 257일 때는 id값이 서로 다르다는 것을 알 수 있고, 이 때문에 is 연산의 결과가 true/false 로 다르게 나타나는 것임을 알 수 있다  
# operators is and is not test for object identity 
# a is b / id(a) == id(b) are equivalent 
# id returns the identity of an object. This is an integer (or long integer) which is guaranteed to be (1)unuique and constant for this object (2)during its lifetime. 2 objects with non-overlapping lifetimes may have the same id() vlaue.
# the id of an object in CPython (the reference implementation of Python) is the location in memory is an implementation detail...
# cf) comparisons to singletons like <None> should always be done with is or is not, never the equality operators 

a = 256
b = 256
print(id(a))    # get back a reference to the existing object
print(id(b))
a = 257
b = 257
print(id(a))
print(id(b))
print('literal compare:', 257 is 257)