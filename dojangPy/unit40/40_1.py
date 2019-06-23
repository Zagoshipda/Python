#unit 40. Generator - yield

#generator 발생자 : iterator를 생성해주는 ***함수*** -> generator는 함수이다 
  
    #iterator는 클래스에 __iter__, __next__ 또는 __getitem__ method를 구현해야 하지만 generator는 함수 안에서 yield라는 키워드만 사용하면 되므로 훨씬 간단하다

    #generator의 단어 의미는...? -> generator객체에서 __next__ method를 호출할 때마다 함수 안의 yield까지 코드를 실행하며 yield에서 값을 발생generate시키기 때문
 
    # iterator : __next__ 메서드 안에서 직접 return으로 값을 반환, raise로 StopIteration 예외를 직접 발생시킨다
    # generator : yield에 지정한 값이 __next__ 메서드(next 함수)의 반환값으로 나옴, 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생


#yield 와 return의 차이점  
    #generator는 함수를 끝내지 않은 상태에서 yield를 사용하여 값을 바깥으로 전달할 수 있다
    #return : 반환 즉시 함수 종료
    #yield : 잠시 함수 바깥의 코드가 실행되도록 양보하여 yield 값을 가져가게 한 뒤 다음 번 함수 호출 때에도 generator 안의 코드를 계속해서 실행하는 방식




#함수 안에서 yield를 사용하면 함수는 generator가 되고, yield에는 값value을 지정한다 
    #yield value

def num_generator():
    yield 0
    yield 1
    yield 2

for i in num_generator():
    print(i, end = ' ')     #0 1 2 -> iterator를 사용할 떄와 같은 결과가 나온다 
print()



#generator객체가 iterator인지 확인하기 : dir 함수로 method목록을 확인하면 __iter__, __next__ method를 모두 확인할 수 있음
print(dir(num_generator()))     #num_generator 함수를 호출허면 generator객체가 반환된다.


#generator 객체의 __next__ method 호출하기 
# a = [1, 2, 3, 4]  #StopIteration -> iterator와 동일한 에러 처리 
a = [1, 2, 3]
g = num_generator()
for i in a:
    print(g.__next__(), end = ' ')  #0 1 2 
print()
    
#for 반복문과 generator : for 반복문은 반복할 때마다 __next__를 호출하므로 yield에서 발생시킨 값을 가져온다. 그리고 마지막에 StopIteration 예외가 발생하면 반복을 끝낸다
    #generator 객체에서 __iter__ method를 호출하면 self를 반환하므로 같은 객체(자기 자신)가 나온다  
    #yield를 사용하면 ***값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보****한다. 즉, ***yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행***되도록 하는 것


print('return ===== ')
#generator와 return : generator는 함수 끝까지 도달하면 StopIteration 예외가 발생한다. return도 함수를 끝내므로 return을 사용해서 함수 중간에 빠져나오면 StopIteration 예외가 발생한다 
    #generator안에서 return 에 반환값을 지정하면 StopIteration 예이의 error message로 들어간다 

#case1) generator 함수에 return이 있는 경우
def ex_generator():
    yield 1
    return 'example'

try:
    g = ex_generator()
    print(next(g))
    print(next(g))     #next(g)를 1번만 하면 yield 1을 전달하고 끝나지만 2번째에는 return 'example'을 하기 때문에 error msg로 'example'이 들어간다 
except StopIteration as e:
    print(e)    #example


#case2) generator 함수에 return이 없는 경우 
def ex_generator():
    yield 1
    # return 'example'

try:
    g = ex_generator()
    print(next(g))
    print(next(g))     #generator에 return이 없는 경우 next(g)를 1번만 하면 yield 1값을 전달하고 끝나고, 그 이후는 함수의 끝이므로 StopIteration 예외 발생 
except StopIteration as e:
    print(e)    #(공백)
    print('finished...')


