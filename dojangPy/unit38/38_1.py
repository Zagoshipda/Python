#unit 38. 예외Exception 처리 
    # 예외 처리 exception handling : 예외가 발생하더라도 스크립트의 실행을 중단하지 않고 프로그램을 계속해서 실행하기 위한 방법

#built-in exceptions : exception-hierarchy 예외 계층 구조 -> exception은 class들 끼리의 상속으로 구현되어 있다. 새로운 예외를 만들 때에는 Exception을 상속하여 구현한다.


#try - except
try:
    x = int(input('10 / x, x = ? '))
    y = 10 / x
    print(y)
except:
    print('exception occurred')


#특정 exception 처리하기 -> 여러 개의 exception 경우들을 exception name에 따라 동시에 처리할 수 있음 
#exception error message 가져오기 (e named after Error) 
    # -> 예외가 여러 개 발생하는 경우, 먼저 발생한 예외의 처리 코드만 실행된다. 또는, 예외 중에서 높은 계층의 예외부터 처리된다(base class -> derived class -> ... 순서) 
    # ex. 아래 예시에서 input으로 5 0 을 주면, index error와 zero division error에 모두 해당하는 input인데 error msg로는 index error만 출력된다. 단순히 코드의 순서상으로는 뒤에 있지만 index error가 더 상위 class의 예외이기 때문일 것.

y = [10, 20, 30]
try:
    idx, div = map(int, input('index, divisor = ? ').split())
    print(y[idx] / div)
except ZeroDivisionError as e:
    print("you can't divide by zero/", e)    #division by zero
except IndexError as e:
    print('wrong index (0, 1, 2 possible)/', e)  #list index out of range


#특정 예외만을 검사하는 것이 아닌 모든 예외를 검사해서 error message 출력하기 -> Exception (상위 계층 exception class) 이용 
try:
    idx, div = map(int, input('index, divisor = ? ').split())
    print(y[idx] / div)
except Exception as e:
    print("exception occurred : ", e)    #list index out of range
    

