# 22.4 list의 가장 작은 수, 가장 큰 수, 합계 구하기

    # min(), max(), sum() 에는 list뿐만 아니라 모든 반복 가능한 객체(iterable - list, tuple, dictionary, set, range, ... )를 넣을 수 있음 


# 가장 작은 수/ 가장 큰 수 구하기 

#1) 모든 element를 비교해서 직접 구하기
a = [3, 2, 4, 5, 6, 8, 1]
smallest = a[0]
largest = a[0]
for i in a:
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print(smallest, largest)     #1 8

# 2) 정렬해서 구하기
a.sort()
print(a[0], a[len(a)-1])    #1 8

# 3) 파이썬에서 제공하는 min(), max() method 사용하기
print(min(a), max(a))   #1 8



#list element의 합 구하기 

#1) 직접 다 더하기 
a = [4, 3, 2, 1, 5]
totalsum = 0
for i in a:
    totalsum += i

print(totalsum)      #15


#2) 파이썬 sum() 함수 사용하기 ... 좋타...ㅎ
print(sum(a))   #15

