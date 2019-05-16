# 5.2 실수 계산하기 

print(3.5 + 1.3)    # 4.8
print(4.3 - 2.7)    # 1.5999999999999996, 실수 표현에 따른 오차 발생 
print(1.5 * 3.1)    # 4.65
print(5.5 / 3.1)    # 1.7741935483870968

print(4.1 + 3)  # 7.1, 실수, 정수의 계산 결과는 실수로 표현

#값을 실수로 만들기     
print(float(5))         # 5.0
print(float('5.3'))     # 5.3
print(float(1 + 2 * 3)) # 7.0

print(type(3.14))   # <class 'float'>

# complex number
print(1.2 + 1.3j)           # (1.2+1.3j)
print(complex(1.2, 1.3))    # (1.2+1.3j)

