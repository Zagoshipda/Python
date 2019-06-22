#38.4 exception 만들기 

# 예외 처리는 에러가 발생하더라도 스크립트의 실행을 중단하지 않고 계속해서 실행하고자 할 때 사용

#python 내장 예외가 아닌, 사용자 정의 exception을 만들어서 예외 발생시키기 -> Exception class를 상속받아서 새로운 class를 만들고, __init__ method에서 base class의 __init__ method 를 호출하면서 error message를 넣어주면 된다

    # class ExceptionName(Exception):   #inheritance 
    #     def __init__(self):           #error msg를 지정하여 initialization
    #         super().__init__('error msg') 



#입력되는 숫자가 3의 배수가 아닐 때 발생시킬 예외 만들기 
class NotThreeError(Exception):
    def __init__(self): 
        super().__init__('not a mul of 3')

class NotThreeError2(Exception):
    pass

def multiple():
    try:
        x = int(input('multiple of 3: '))
        if x % 3 != 0:
            # raise NotThreeError #사용자 정의 예외 - NotThreeError 발생
            raise NotThreeError2('NOT a mul of 3')  # -> 사용자 정의 exception class를 상속만 받고 error msg를 구현하지 않으면 exception을 raise할 때 exception msg를 넣어주면 된다 ... -> 이게 오히려 error msg를 바로 확인할 수 있어서 더 간단하고 직관적인 듯...?
        print(x)
    except Exception as e:
        print('Exception occurred:', e)

multiple()  #not a mul of 3 / NOT a mul of 3

