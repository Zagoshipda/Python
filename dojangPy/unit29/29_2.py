# 29.2 덧셈 함수 만들기 


# 매개변수parameter/ 함수를 호출할 때 넣는 값 인수argument

def add(a, b):
    """this funciton adds a and b and prints it(a+b)"""
    print(a+b)
add(3,5)            #8

def add2(a, b):
    """this function returns the result of a+b"""
    return a+b
print(add2(3,5))    #8

# function documentation strings, docstrings : 함수의 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개)로 문자열을 입력하면 함수에 대한 설명을 넣을 수 있음. 독스트링의 윗줄에 다른 코드가 오면 안 됨
# ' '(작은따옴표), " "(큰따옴표), ''' '''(작은따옴표 세 개)로 만들어도 되지만, 파이썬 코딩 스타일 가이드(PEP 8)에서는 """ """(큰따옴표 세 개)를 권장
# docstring은 함수의 사용 방법만 기록할 뿐 해당 함수를 호출해도 출력되지 않는다. docstring을 출력하는 방법: print((func).__doc__)와 같이 함수 func의 __doc__을 출력
print(add.__doc__)      #this funciton adds a and b and prints it(a+b)
print(add2.__doc__)     #this function returns the result of a+b

#help 사용하기 - help(object) : help에 함수를 넣으면 함수의 이름, 매개변수, 독스트링을 도움말 형태로 출력print
help(add)
