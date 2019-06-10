# 22.6 list에 map 사용하기

# map은 (리스트의 element를 특정 지정한 함수로 처리)해주는 함수이다
# map은 원본 리스트를 변경하지 않고 ***새 리스트를 생성***한다 (return)
# map에는 모든 반복 가능한 객체object를 넣을 수 있다  
    # (object)(map(function, object))
    # list(map(함수, list))
    # tuple(map(함수, tuple))

# a, b = map(int, input().split()) 정리
    # x = input().split()    # input().split()의 결과는 문자열 리스트
    # m = map(int, x)        # 리스트의 element를 int로 변환, 결과로 나온 map object를 변수에 저장
    # a, b = m               # 맵 객체는 변수 여러 개에 값을 저장할 수 있음


#실수가 저장된 list가 있을 때 이 list의 모든 element를 정수로 변환하기 

    # int, str 도 특정 함수...? -> 자료형을 바꾸어주는 함수와 같은 역할. 따라서 변수 앞에서 (int)var 처럼 casting 하는 것이 아닌, int(var) 처럼 변수를 argument로 넣어주는 식으로 사용하는 것

#1) for 반복문으로 하나씩 직접 변환하기
a = [1.1, 2.2, 3.3, 4.4]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)    #[1, 2, 3, 4]

#2) map() 함수를 사용해서 변환하기
a = [1.1, 2.2, 3.3, 4.4]
print(a)    #[1.1, 2.2, 3.3, 4.4]
b = list(map(int, a))   #list의 모든 element를 int를 사용해서 변환
print(a, len(a), b, len(b))    #[1.1, 2.2, 3.3, 4.4] 4 [1, 2, 3, 4] 4 -> 원본 list a는 그대로이고, 새로운 list b가 만들어진 것을 확인할 수 있다

a = list(map(str, range(10)))
print(a)    #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] -> 각 숫자를 문자열str으로 변환하여 list에 저장



#input().split() 과 map() -> input(), input().split()의 결과가 문자열 list이기 때문에 map()을 사용할 수 있는 것 
#실행은 python (filename)
a = input().split()
print(a)    #['10', '20']

a, b = map(int, input().split())    # map()은 iterator객체(map object)를 반환한다 -> 변수 여러 개에 값을 저장하는 unpacking이 가능 
print(a, b)     #10 20

a, b = list(map(int, input().split()))  #list unpacking
print(a, b)     #10 20




