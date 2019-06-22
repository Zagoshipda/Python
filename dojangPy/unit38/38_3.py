#38.3 exception 발생시키기 - raise

#python에서 미리 정하고 있는 예외가 아닌, 사용자가 직접 예외를 만들어서 발생시키는 것이 가능 : raise exception('exception message')

try:
    # x = 3
    x = 2
    if x % 3 != 0:
        raise Exception('not a multiple of 3')
    print(x)    #raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고 바로 except로 넘어간다 -> x 가 3의 배수일 경우는 x를 출력하고, 아닌 경우는 아래의 예외 처리로 넘어가서 exception msg가 출력된다 
except Exception as e:
    print('exception occurred: ', e)    #not a multiple of 3




#raise의 처리 과정 
    # three_multiple 함수는 안에 try except가 없는 상태에서 raise로 예외를 발생시켰다. 이렇게 되면 함수 바깥에 있는 except에서 예외가 처리된다. 즉, 예외가 발생하더라도 현재 code block에서 처리해줄 except가 없다면 except가 나올 때까지 계속 상위 code block으로 올라가서 처리하게 된다. 만약 함수 바깥에도 처리해줄 except가 없다면 코드 실행은 중지되고 에러가 표시된다

def three_multiple():
    x = int(input('multiple of 3 : '))
    if x % 3 != 0:
        raise Exception('it is not a multiple of 3')
    print(x)

try:
    three_multiple()
except Exception as e:
    print('exception occurred', e)  #it is not a multiple of 3





print('error again ===== ')
#try except에서 처리한 현재 예외를 다시 발생시키기 : except 안에서 raise를 사용하면 현재 예외를 다시 발생시킨다 
    #multiple 함수 안에서 발생한 예외를 함수 안의 except에서 한 번 처리하고, raise로 예외를 다시 발생시켜서 상위 code block으로 넘겨준다. 그 다음에 함수 바깥의 except에서 다시 한 번 예외를 처리하였다. 이런 방식으로 같은 예외를 상위 code block으로 계속해서 넘겨주면서 처리해줄 수 있다.

def multiple():
    try:
        x = int(input('multiple of 3 : '))
        if x % 3 != 0:
            raise Exception('not a multiple of 3')  #함수 안에서 예외 발생
        print(x)
    except Exception as e:  #함수 안에서 예외 처리 
        print('exception occured', e)   #not a multiple of 3
        raise   # raise로 현재 예외를 다시 발생시켜서 상위 code block으로 넘김

try:
    multiple()
except Exception as e:
    print('error occured in function multiple()', e)    #not a multiple of 3




#raise ExceptionType('error msg') : raise만 사용하면 **같은 예외**를 상위 code block으로 넘기지만, raise에 다른 예외를 지정하고 error msg를 설정할 수도 있다
def multiple2():
    try:
        x = int(input('multiple of 3 : '))
        if x % 3 != 0:
            raise Exception('NOT a multiple of 3')  #함수 안에서 예외 발생
        print(x)
    except Exception as e:  #함수 안에서 예외 처리 
        print('exception occured', e)   #NOT a multiple of 3
        raise RuntimeError('ERROR')   # raise로 현재 예외를 다시 발생시켜서 상위 code block으로 넘김

try:
    multiple2()
except Exception as e:
    print('ERROR in multiple2()', e)    #ERROR




print('assert ===== ')
#assert로 예외 발생시키기 : assert는 지정된 조건식이 거짓일 때 AssertionError 예외를 발생시키며 조건식이 참이면 그냥 넘어간다. 
# ***보통 assert는 나와서는 안 되는 조건(corner case, special case)을 검사할 때 사용***한다 (간편하게 error를 확인하거나, 주어진 문제의 제약 조건을 검사하는 용도로 사용 가능)
    #assert는 디버깅 모드에서만 실행된다 : python은 기본적으로 debugging mode이며(__debug__의 값이 True) assert가 실행되지 않게 하려면 python에 -O(영문 대문자) 옵션을 붙여야 한다
    #python .\unit38\38_3.py -> assert 실행되어 에러가 발생하면 print(x)가 출력되지 않고 error msg가 출력됨 
    #python -O .\unit38\38_3.py -> assert 실행되지 않아서 에러가 발생하지 않고 항상 print(x)가 출력됨

x = int(input('multiple of 4 : '))
assert x % 4 == 0, 'NOT a multiple of 4'    #AssertionError: NOT a multiple of 4 -> 4의 배수가 아니면 예외 발생, 4의 배수이면 그냥 넘어감
print(x)


