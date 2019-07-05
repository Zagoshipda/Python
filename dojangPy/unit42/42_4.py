#42.4 클래스로 decorator 만들기
    #클래스로도 decorator를 만들 수 있다 : class로 decorator를 만들 때는 ***instance를 함수처럼 호출하게 해주는 __call__ method를 구현***해야 한다
    #이 경우 decorator를 사용하는 방법은 closure 형태의 decorator와 같다. 호출할 함수 위에 @을 붙이고 사용할 decorator를 지정한다


#함수의 시작과 끝을 출력하는 decorator design
class Trace:
    def __init__(self, func):   #호출할 함수를 instance의 initial value로 받음
        self.func = func        #호출할 함수를 class의 func속성에 저장

    def __call__(self):
        print(self.func.__name__, ': func start')
        self.func()
        print(self.func.__name__, ': func end')

@Trace
def hello():
    print('hello')

hello()

# hello : func start
# hello
# hello : func end


print('\nNOT using @ --- ')
#@를 사용하지 않고 decorator의 반환값return value을 호출하는 방식으로 사용하기
    #decorator에 호출할 함수를 넣어서 instance를 생성한 뒤 instance를 호출하여 사용 : class에 __call__() method를 정의했으므로 함수처럼 ()를 붙여서 호출할 수 있다
def hello():
    print('hello')

ret = Trace(hello)  #decorator에 호출할 함수를 넣어서 instance를 생성
ret()               #instance 호출 -> class 내부의 __call__() method 호출
# hello : func start
# hello
# hello : func end
