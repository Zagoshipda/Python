# 6.4 입력 값을 변수 2개에 저장하기 
# input과 split의 결과가 문자열string이라는 점을 주의하자
# split의 결과를 모두 int, float로 변환할 때는 map을 사용하면 편리


# 입력받은 값을 공백을 기준으로 분리
a, b = input('2 strings: ').split()
print(a)
print(b)

# 두 숫자의 합 구하기 
a, b = input('2 numbers: ').split()
print(a + b)
print(int(a) + int(b))
print(a + b)
a = int(a)
b = int(b)
print(a + b)


# map을 사용하여 정수로 변환하기 
# 변수1, 변수2 = map(int/float, input('문자열').split('기준문자열'))
a, b = map(int, input('2 numbers: ').split())
print(a + b)


# split에 기준 문자열을 지정하여 공백이 아닌 다른 문자로 분리하기

# 입력받은 값을 콤마(,) 를 기준으로 분리하기
a, b = map(int, input('2 numbers with , : ').split(','))
print(a + b)


# 정수 3 개를 입력받고 합계 출력하기
x, y, z = map(int, input('3 numbers: ').split())
print(x + y + z)