#42.3 매개변수가 있는 decorator 만들기
    #이전까지는 decorator를 호출해서 사용하는 원본 함수가 parameter와 return value를 가지는 경우들을 다루었다. 하지만 지금의 경우는 decorator 자체가 매개변수를 가지는 경우를 뜻하므로 서로 완전히 다른 경우임에 주의하자



#매개변수가 있는 decorator -> 값을 지정해서 동작을 바꿀 수 있다

#함수의 반환값이 특정 수의 배수인지를 확인하는 decorator
def is_multiple(x):
    def dec(func):
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0}'s return value is multiple of {1}".format(func.__name__, x))
            else:
                print("{0}'s return value is NOT multiple of {1}".format(func.__name__, x))
            return r
        return wrapper
    return dec

# @is_multiple
@is_multiple(3)
def add(a, b):
    return a + b

print('name :', add.__name__)   # wrapper
print(add(1, 2))    #dec() takes 1 positional argument but 2 were given
print(add(2, 3))
print(add(5, 7))

# add's return value is multiple of 3
# 3
# add's return value is NOT multiple of 3
# 5
# add's return value is multiple of 3
# 12

print('\nwrapper test --- ')
#매개변수가 있는 decorator의 실행순서는...? ---> why & How...????? by debugging, 위 is_multiple 함수를 분석해보자 ---> @is_multiple(3)을 만나면 is_multiple()실행 -> return dec -> --Call-- : dec()실행 -> return wrapper -> --Return-- : 여기서는 call하는 것이 아닌 함수 실행을 종료하고 다음 줄로 넘어감....
#이후 add(1, 2)를 실행하면 바로 wrapper()함수부터 실행된다 (이미 위에서 wrapper를 return하였으므로)

#확인할 사항 : wrapper함수의 이름은 꼭 wrapper이어야만 하는가...? -> 함수 이름 바꾸어보기
#함수의 이름을 바꾸어도 똑같이 작동한다면 python의 decorator 문법 자체가 위와 같이 1단계의 wrapper까지만 실행하고 그 내부의 다음 단계의 return function은 실행하지 않고 종료하고 다음 줄로 넘어가게끔 design되었다고 생각할 수 있다

def mul_test(x):
    def dec(func):
        def wrap(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0} : return val is mul of {1}".format(func.__name__, x))
            else:
                print("{0} : return val is NOT mul of {1}".format(func.__name__, x))
            return r
        return wrap
    return dec

@mul_test(2)
def add_test(a, b):
    return a + b

print(add_test(1, 2))
# add_test : return val is NOT mul of 2
# 3

#mul_test() 함수의 실행순서 : @mul_test(2)를 만나면 mul_test(2)실행 -> return dec -> --Return--, 그리고 다시 --Call-- : dec()실행 -> return wrap : 여기서도 마찬가지로 call을 계속하는 것이 아닌 함수 실행을 종료하고 다음 줄로 넘어감....
#이후 add_test(1, 2)를 실행하면 이미 return한 wrap()함수부터 실행
#wrapper함수의 이름은 꼭 wrapper이어야만 하는가...? -> X , 이름은 상관없음 (당연), 결국 decorator가 매개변수를 가지는 경우 wrapper function을 1단계더 설정해준다는 것만 기억하기



# @를 사용하지 않았다 가정하고 원래 코드의 동작은 어떤 모습일지를 분석해보자.
def add_test(a, b):
    return a + b

ret = mul_test(2)(add_test)
print(ret(1, 2))
# add_test : return val is NOT mul of 2
# 3





print()
#매개변수가 있는 decorator를 여러 개 지정하기

@is_multiple(3)
@is_multiple(4)
def add(a, b):      # (A)
    return a + b

print(add(1, 2))
print(add(2, 3))
print(add(3, 5))

# add's return value is NOT multiple of 4
# wrapper's return value is multiple of 3
# 3
# add's return value is NOT multiple of 4
# wrapper's return value is NOT multiple of 3
# 5
# add's return value is multiple of 4
# wrapper's return value is NOT multiple of 3
# 8




print('\nnot using @')
#@를 사용하지 않았을 때는 다음 코드와 동작이 같다: ... !? -> 코드 리뷰 더 필요...

dec_add = (is_multiple(3))(is_multiple(4)(add))     # (B)
print(dec_add(1, 2))

# add's return value is NOT multiple of 4
# wrapper's return value is multiple of 3
# wrapper's return value is NOT multiple of 4
# wrapper's return value is multiple of 3
# 3 .... -> 왜 결과가 2번씩 겹쳐서 나오는지.... ? -> 위와 같이 하면 위에서 이미 정의한 (A)의 add를 호출하는데 (A)의 add는 decorator가 이미 적용된 function이므로 --- (1) (A)실행 : decorator가 적용된 add를 호출  + (2) (B)실행 --- 으로 총 2번 add가 실행되므로 결과가 2번 출력되는 것

print('solve calling 2 times --- ')
#따라서 이를 해결하기 위해서는 다음과 같이 그냥 add 함수를 다시 정의해주면 된다 (바로 함수를 반영하도록)
def add(a, b):
    return a + b

dec_add = is_multiple(3)(is_multiple(4)(add))
print(dec_add(1, 2))
# add's return value is NOT multiple of 4
# wrapper's return value is multiple of 3 ---> 안쪽 decorator 함수인 is_multiple(4)에서 반환한 wrapper 함수가 is_multiple(3)의 argument로 들어가므로 원래 함수인 add가 아닌 wrapper함수의 이름이 출력되는 것을 확인할 수 있음
# 3




print('\nfunctools ===== ')
#decorator를 여러 개 사용하면 안쪽decorator에서 반환된 wrapper함수가 바깥쪽 decorator의 argument로 들어가므로 func.__name__을 출력하면 wrapper가 나온다
#***함수의 원래 이름을 출려하고 싶다면 (위에서 wrapper가 아닌 add 함수의 이름이 원래대로 그대로 나오게 하기 위한 방법)...? -> functools module의 wraps decorator를 사용 : @functools.wraps는 원래 함수의 정보를 유지시켜준다. 따라서 디버깅을 할 때 유용하므로 decorator를 만들 때는 @functools.wraps를 사용하는 것이 좋다 (이것도 근데 또 decorator임... ㅡㅅㅡ decorator를 위한 decorator...)

import functools

def is_multiple(x):
    def dec(func):
        @functools.wraps(func)  #@functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정 ---> 이 역시나 매개변수가 있는 decorator이므로 wrapping이 1단계 더 진행되는 것으로 이해할 수 있음
        #functols.wraps()에 대해서는 : https://docs.python.org/3/library/functools.html 
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print("{0}'s return value is multiple of {1}".format(func.__name__, x))
            else:
                print("{0}'s return value is NOT multiple of {1}".format(func.__name__, x))
            return r
        return wrapper
    return dec


@is_multiple(3)
@is_multiple(4)
def add(a, b):
    return a + b

print('name :', add.__name__)   # add / wrapper (when not using functools.wraps)

print(add(1, 2))
print(add(2, 3))
print(add(3, 5))

# 그러면 wrapper가 출력되는 것이 아닌 원래 함수의 이름인 add가 잘 출력되는 것을 확인할 수 있다
# add's return value is NOT multiple of 4
# add's return value is multiple of 3
# 3
# add's return value is NOT multiple of 4
# add's return value is NOT multiple of 3
# 5
# add's return value is multiple of 4
# add's return value is NOT multiple of 3
# 8
