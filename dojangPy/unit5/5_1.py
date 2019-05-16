# 5.1 정수 계산하기
# 파이썬에서는 숫자를 정수, 실수, 복소수...!!! 로 구분한다 -> 복소수는 공학에서 주로 사용 
 
# 파이썬에서는 숫자도 객체(object)이며, 객체는 클래스(class)로 표현한다

print(1+1)  # 2

# 기본적으로 나눗셈의 결과는 실수로
print(5/2)  # 2.5
print(4/2)  # 2.0

# floor division 버림 나눗셈 -> 결과를 정수로 
print(5//2) # 2
print(4//2) # 2

# floor division에 실수가 있다면 결과는 정수, 형태는 (x.0)과 같이 실수형태로 
print(5.0//2)   # 2.0
print(4/2.0)    # 2.0
print(4.1//2.1) # 1.0

# power
print(2**10)    # 1024
print(2**5)     # 32

# make it to integer
print(3.3)      # 3.3
print(int(3.3)) # 3.0, 정수로 변환하면 소숫점을 버림, 실수 3.3을 int 클래스 객체로 변환함 
# print('10'+3)   # TypeError: can only concatenate str (not "int") to str
print('10'+'3')       # 103
print(int('10')+3)    # 13

# 객체의 자료형type 알아내기, 파이썬에서는 숫자도 객체object, 객체는 class로 표현
print(type(10))     # <class 'int'>
print(type('10'))   # <class 'str'>

#몫과 나머지 함께 구하기 (개사기스킬...ㄷㄷ)
print(divmod(5,2))  # (2, 1), tuple 
quotient, remainder = divmod(7,4)
print(quotient, remainder)  # 1 3 


# 2진수, 8진수, 16진수
print(0b110)    # 6, <b>inary
print(0o10)     # 8, <o>ctal
print(0xf)      # 15, he<x>adecimal

