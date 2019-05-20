# FizzBuzz 문제 pre- self-implementation

# 규칙
    # 1에서 100까지 출력
    # 3의 배수는 Fizz 출력
    # 5의 배수는 Buzz 출력
    # 3과 5의 공배수는 FizzBuzz 출력

for i in range(1,101):
    # print(i)
    if i%15 == 0:
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0: 
        print('Buzz')
    else:
        print(i)


# for i in range(1, 16):
#     if i%15 == 0:
#         print('FizzBuzz') 