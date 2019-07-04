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

print(add(1, 2))    #dec() takes 1 positional argument but 2 were given
print(add(2, 3))
print(add(5, 7))

# add's return value is multiple of 3
# 3
# add's return value is NOT multiple of 3
# 5
# add's return value is multiple of 3
# 12





#매개변수가 있는 decorator의 실행순서는...? -> @is_multiple(3)을 만나면 is_multiple()실행 -> return dec -> 다시 dec()실행 -> return wrapper -> 여기까지 하고 다음 줄로 넘어감.... ---> why...?????

# decorator를 사용하지 않았다 가정하고 원래 코드는 어떤 모습일지를 분석해보자. 
# ret = is_multiple(3)
# pass 

#... 






print()
#매개변수가 있는 decorator를 여러 개 지정하기 

@is_multiple(3)
@is_multiple(4)
def add(a, b):
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
#@를 사용하지 않았을 때는 다음 코드와 동작이 같다: ... ? -> 코드 리뷰 더 필요...

dec_add = is_multiple(3)(is_multiple(4)(add))
print(dec_add(1, 2))

# add's return value is NOT multiple of 4
# wrapper's return value is multiple of 3
# wrapper's return value is NOT multiple of 4
# wrapper's return value is multiple of 3
# 3 .... -> 왜 결과가 2번씩 겹쳐서 나오는지.... ? 





print('\nfunctools ===== ')
#함수의 원래 이름을 출려하고 싶다면...? -> 위에서 wrapper가 아닌 add 함수의 이름이 원래대로 그대로 나오게 하기 위한 방법은...? -> functools module의 wraps decorator를 사용 : @functools.wraps는 원래 함수의 정보를 유지시켜준다. 따라서 디버깅을 할 때 유용하므로 decorator를 만들 때는 @functools.wraps를 사용하는 것이 좋다

import functools

def is_multiple(x):
    def dec(func):
        @functools.wraps(func)  #@functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
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

print(add(1, 2))
print(add(2, 3))
print(add(3, 5))

# add's return value is NOT multiple of 4
# add's return value is multiple of 3
# 3
# add's return value is NOT multiple of 4
# add's return value is NOT multiple of 3
# 5
# add's return value is multiple of 4
# add's return value is NOT multiple of 3
# 8
