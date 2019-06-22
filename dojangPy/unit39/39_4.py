#39.4 python 내장 함수 iter, next 

    #iter : 객체의 __iter__ method 호출
    #next : 객체의 __next__ method 호출 
    #iter는 iterable에서 iterator를 반환하고, next는 iterator에서 값을 차례대로 꺼낸다


it = iter(range(3))
print(next(it))     #0
print(next(it))     #1
print(next(it))     #2
# print(next(it))     #StopIteration




#1) iter : 반복을 끝낼 값을 지정할 수 있고, 지정하면 해당하는 값이 나올 때 반복을 끝냄 -> iterable 대신 호출 가능한 객체 callable을 parameter로 넣어주어야 함 
    #sentinel : 반복을 끝낼 값 
    #iter(callable, sentinel)

import random
it = iter(lambda : random.randint(0, 5), 2)     #0...5까지 random 숫자를 생성하고, 2가 나오면 멈추도록 -> callable을 넣어야 하므로 매개변수parameter가 없는 함수 또는 람다 표현식을 넣어준다
# print(next(it))
# print(next(it))
# print(next(it))
for i in it:
    print(i, end = ' ')

#위는 다음과 동작이 같다 -> iter에서 sentinel을 활용하면 if 조건문으로 검사하는 과정을 간단하게 처리할 수 있음
print()
while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end = ' ')



print('\nnext ===== ')
#2) next : 기본값default value를 지정할 수 있음. 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 해당 기본값을 출력한다
    #반복의 범위 안에서는 해당 반복값을 출력하고, 반복이 끝났을 때는 (StopIteration error가 발생하지 않고) 미리 지정한 기본값을 출력
    #next(iterator, default value)

num = [1, 2, 3, 4, 5]   #총 5번을 반복할 것임 
it = iter(range(3))
for i in num:
    print(next(it, 10), end = ' ')      #0 1 2 10 10 

print()
it = iter(range(3))
print(next(it, 10))     #0
print(next(it, 10))     #1
print(next(it, 10))     #2
print(next(it, 10))     #10
print(next(it, 10))     #10 
# print(next(it, 10))     #StopIteration


