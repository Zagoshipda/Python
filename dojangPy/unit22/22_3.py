# 22.3 반복문으로 list의 모든 element 출력하기 


# for loop 
a = [1, 2, 3, 4, 5]
for i in a:
    print(i, end=' ')   
print()     #1 2 3 4 5 


#element와 index 함께 출력하기 : enumerate(list) 
for index, val in enumerate(a):
    print(index, 'th:', val)
    # print(index+1, 'th:', val, end=' ')
# 0 th: 1 
# 1 th: 2 
# 2 th: 3 
# 3 th: 4 
# 4 th: 5 

#python다운 방법으로 출력하기 -> start 값을 지정해서 시작 index를 설정할 수 있음 
# for idx, val in enumerate(a, start=1):    
for idx, val in enumerate(a, 1):
    print(idx, val)
# 1 1
# 2 2
# 3 3
# 4 4
# 5 5


#element에 바로 접근하는 것이 아닌 index로 접근하기 -> i에 element값이 아닌 0 ~ (len(a)-1)까지의 index가 들어간다
a = [9, 8, 7, 6, 5]
for i in range(len(a)):
    print(a[i], end=' ')
print()     #9 8 7 6 5 


print("while loop =====")
#while loop -> index를 이용해서 출력, for loop에서 range(len(a))로 i에 index값을 넣어서 반복하는 것과 같음

a = [5, 7, 9, 3, 1]
i = 0
while i < len(a):
    print(a[i], end = ' ')
    i += 1
print()     #5 7 9 3 1 

