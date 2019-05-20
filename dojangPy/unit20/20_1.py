# unit 20. FizzBuzz 문제 

# 규칙
    # 1에서 100까지 출력
    # 3의 배수는 Fizz 출력
    # 5의 배수는 Buzz 출력
    # 3과 5의 공배수는 FizzBuzz 출력


for i in range(1, 101):
    # print(i)
    # if i%3 == 0 and i%5 == 0:   #공배수 검사를 먼저 수행해야 함에 주의 
    # 이렇게 3과 5의 LCM인 15를 직접 사용할 수도 있다. 하지만 주석에 적절한 설명이 없다면 코드를 읽는 사람이 15이 의미하는 것이 무엇인지, 그 속 뜻을 알아내야 한다. 문제가 간단하다면 별 문제가 없지만 복잡한 문제이거나 코드가 길어진다면 문맥적으로 파악하기가 어려울 수 있다. 따라서 실무에서는 i % 3 == 0 and i % 5 == 0처럼 의미를 명확하게 드러내는 코드를 작성하는 것이 좋다. 또한 요즘은 프로그래밍 언어의 성능도 좋아졌고, CPU도 매우 빨라졌으므로 사소한 부분에 신경쓰기 보다는 ***가독성을 높이는 쪽으로 코드를 작성하는 것이 추세. -> 다른 사람이 내 코드를 유지보수하기 쉽도록 코드를 작성해야 하고, 내가 만든 코드를 나중에 내가 봤을 때도 이해하기 쉽도록 작성
    if i%15 == 0:               
        print('FizzBuzz')
    elif i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print('Buzz')
    else:
        print(i)


# short-code implementation (code - golf)

#문자열에 True를 곱하면 문자열이 그대로 나오고, False를 곱하면 문자열이 출력되지 않음 (True는 1, False는 0으로 연산)
for i in range(1, 101):
    print('Fizz'*(i%3==0) + 'Buzz'*(i%5==0) or i)

# 3 또는 5의 배수가 아닐 때는 'Fizz' * False + 'Buzz' * False가 되고 결과는 빈 문자열 ''이 되는데, 이때는 or 연산자를 사용. 빈 문자열은 False로 취급하고, i는 항상 1 이상의 숫자이므로 or로 연산하면 i만 남게 되어(from the notion of short-circuit evaluation) 숫자가 그대로 출력됩니다.

#short-circuit evaluation -> or 일때 앞의 것이 True이면 앞쪽만 계산한것이 바로 결과값이 됨 
a = 'haha' or 'b'
print(a)    #haha