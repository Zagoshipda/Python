# unit 29 함수 사용하기 
# 29.1 Hello, world 출력 함수 만들기 


# why use funciton...?
# 코드의 용도를 구분할 수 있다.
# 코드를 재사용할 수 있다.
# 실수를 줄일 수 있다.

# 들여쓰기 규칙: python에서 함수의 본문은 반드시 들여쓰기를 해야 함 

# function 만들기
def hello():
    print('Hello, world...!')   #Hello, world...!

hello()             #Hello, world...!
print(hello())      #Hello, world...!
                    #None   ....???? 2줄이 출력되는 이유와 None이 출력되는 이유는?

# https://www.codeit.kr/questions/1924
# 위에서 non이 출력되는 이유는 hello() function이 아무것도 return 하고 있지 않기 떄문. 아래와 같이 하면 된다.

def hello2():
    return print('Bye, world...?')  #return 하는 척을 하고는 있지만 실제로 return 하는 값이 없음
print(hello2())     #때문에 이 경우에도 역시나 None까지 포함하여 총 2줄로 출력이 이루어지는 것을 확인할 수 있다
print()             #(공백)

def hello3():
    return 'Again, world...'
print(hello3())     #'Again, world...', 이렇게 function으로부터 string을 return 받아서 출력하게 하면 None이 뜨지 않음 

# https://docs.python.org/ko/3/library/constants.html
# None: 내장 상수(-> True, False), NoneType 형의 유일한 값. None 은 기본 인자가 함수에 전달되지 않을 때처럼, 값의 부재를 나타내는 데 자주 사용됨
print(type(None))   # <class 'NoneType'>

# python은 interpreter방식으로 순차적으로 실행하므로 (함수 정의 -> 호출)의 순서를 지켜야 함. (함수를 만들기 전에 함수를 먼저 호출하면 안 됨)

# 내용이 없는 빈 함수 만들기 - pass는 아무 일을 하지 않아도 함수의 틀을 유지할 필요가 있을 때 사용
def hi():
    pass 

