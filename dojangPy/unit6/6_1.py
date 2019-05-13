# 6.1 변수variable 만들기 

x = 10
print(x)
y = 'Hello, world!'
print(y)
z = "bye, world!"
print(z)

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'str'>

# 여러 개 변수에 서로 다른 값 할당하고 출력하기 
x, y, z = 10, 20, 30
print(x, 
y, 
z)              # 10 20 30
x = 40  
print(x, y, z)  # 40 20 30

# 여러 개 변수에 같은 값 할당하기 
x = y = z = 10
print(x, y, z)  # 10 10 10 

# swap ... 이게 언어냐...
x, y = 10, 20
print(x, y)     # 10 20
x, y = y, x
print(x, y)     # 20 10 

# delete variable
a = 5
print(a)
del a
# print(a)    # NameError: name 'a' is not defined 

# making empty variable
b = None
print(b)    # None (아무것도 없는 상태를 나타내는 자료형 ~> NULL), terminal에서 스크립트에 그냥 b를 입력하면 (아무것도 출력되지 않는)다.

