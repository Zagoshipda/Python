#29.3 함수의 결과를 반환하기 

# return : 함수를 호출해준 바깥에 결과를 알려주기 위해 사용
# return 에 값을 지정하지 않으면 None을 반환 

# return 의 2가지 기능 (1)값을 반환 (2)함수 중간에서 빠져나오기 (if와 조합해서 특정 조건일 때 함수 중간에서 빠져나오는 용도로 사용)


def noreturn(a, b):
    return

def isreturn(a, b):
    return a+b

print(noreturn(1,2))    #None
print(isreturn(3,4))    #7

x = isreturn(5,6)
print(x)                #11


# 매개변수는 없고 반환값만 있는 함수 
def one():
    return 1
x = one()
print(x)                #1

# return 으로 함수 중간에서 빠져나오기 
def not_ten(a):
    if a == 10:
        return
    print('the number is: ', a, sep='')

not_ten(5)              #the number is 5
print(not_ten(10))      #None

