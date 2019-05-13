# 6.3 입력 값을 변수에 저장하기 
# python 스크립트파일.py 형식으로 실행

# input 함수 사용해서 입력값 받기 
x = input('input string...: ')
print(x)


# 두 숫자의 합 구하기 (정수)
a = input('first number: ')
b = input('second number: ')
print(a+b)  # input에서 입력받은 값은 항상 문자열 형태, 문자열의 덧셈 수행 

c = int(input('first number: '))
d = int(input('second number: '))
print(c+d)  # str을 int형으로 바꾸어서 저장한 후 숫자의 덧셈 수행

# 두 실수의 합 구하기 
e = float(input('first float: '))
f = float(input('second float: '))
print(e+f)
