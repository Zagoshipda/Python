#22.7 tuple 응용하기 

#tuple -> immutable : element의 값을 변경하는 메서드(append, ...)는 사용할 수 없고, element의 정보를 구하는(값을 가져오는) 메서드만 사용할 수 있다


#특정 값의 index구하기 : index(value), 같은 값이 여러 개일 경우 가장 처음의(가장 작은) index를 구한다
a = (3, 4, 5, 7, 3, 4)
print(a.index(4), len(a))   #1 6


#특정 값의 개수 구하기 : count(value)
a = (1, 1, 2, 2, 2, 3, 3, 4)
print(a.count(1), a.count(2), a.count(4))   #2 3 1


#for 반복문으로 element 출력하기 
a = (1, 2, 3, 4, 5)
for i in a:
    print(i, end = ' ')
print()     #1 2 3 4 5




#tuple 표현식comprehension : 
    # tuple(식 for 변수 in 리스트 if 조건식)
    # for 반복문은 i가 가질 수 있는 값의 범위를, if조건문은 i가 만족해야 하는 특별한 성질을 명시하는 것

a = tuple(i for i in range(10) if i%2 == 0)     #0~9까지의 수 중 짝수
print(a)    #(0, 2, 4, 6, 8)
b = tuple(j for j in range(10) if j < 5)
print(b, len(b))    #(0, 1, 2, 3, 4) 5
c = tuple(k for k in [1, 2, 3, 4, 5, 6, 7, 8] if k>3 and k%2 == 0)     #여러 개의 조건을 설정하는 경우
print(c)    #(4, 6, 8)


#tuple에 map()사용하기
a = (1.1, 2.2, 3.3, 4.4)
b = tuple(map(int, a))
print(a, len(a), b, len(b))     #(1.1, 2.2, 3.3, 4.4) 4 (1, 2, 3, 4) 4 -> 역시나 map()의 결과로 새로운 tuple이 생성되며, 원본 tuple a는 변하지 않음을 확인할 수 있다


# min() max() sum() 사용하기
a = (3, 2, 1, 4, 5, 6)
print(min(a), max(a), sum(a))   #1 6 21

