# 25.2 반복문으로 dictionary의 key-value 쌍을 모두 출력하기 


x = {'a': 1, 'b':2, 'c':3, 'd':4}
for i in x:
    print(i, end=' ')
print('\n')
# a b c d, key값만 출력됨을 알 수 있음 -> key 와 value 모두를 출력하기 위한 방법은? 


# x.items() 는 딕셔너리 x에서 키-값 쌍을 꺼내서 키는 key에 값은 value에 저장하고, 이를 반복한다
for key, val in x.items():
    print(key, val)
# print('\n')

# a 1
# b 2
# c 3
# d 4



# key, value 각각만 가져오는 것도 가능하다 
# items(): 키-값 쌍을 모두 가져옴
# keys(): 키를 모두 가져옴
# values(): 값을 모두 가져옴

# dictionary의 key만 출력하기 
for key in x.keys():
    print(key, end = ' ')
print()     # 줄바꿈 
# a b c d 

# dictionary의 value만 출력하기 
for val in x.values():
    print(val, end = ' ')
print()
#1 2 3 4 



######################################################

# print 줄바꿈 확실하기 알기... 
print(00000)    #0, 0은 그냥 0으로 출력 
print(10)
print()         #2줄 띄우기 
print(20)   
print('\n')     #3줄 띄우기 (print(20) 끝나고 1줄 + \n 출력 1줄 + print(\n)끝나고 1줄)
print(30)

# -> 기본적으로는 print로 구성한 코드의 줄과 출력되는 줄이 동일하다고 생각하면 된다: 다음과 같은 경우 5가 있고 한줄 공백이고, 그 다음 6이 출력되는 것으로, 코드의 줄바꿈과 출력의 줄바꿈이 완전히 일치한다
print(5)
print()
print(6)
