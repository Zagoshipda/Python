# 16.2 for 와 range 응용하기 


# 시작하는 숫자와 끝나는 숫자 지정하기
for i in range(3, 7):
    print('for with range: ', i)  # i = [3...6]


# 증가폭 사용하기 - 짝수만 출력하기 
for i in range(0, 8, 2):
    print('only even numbers: ', i) # i = [0...7]


# 숫자 감소시키기
# range는 숫자가 증가하는 기본 값이 양수 1이기 때문에 감소하는 양을 지정하지 않으면 다음과 같이 동작하지 않음
for i in range(5, 0):
    print('haha', i)    #아무것도 출력되지 않음

for i in range(5, 0, -1):
    print('range decrease: ', i)   #이렇게 증가폭을 음수로 지정하면 감소하는 숫자가 만들어진다 [5...1] 단, 여기서도 마지막 값인 0은 제외하고 1까지만 반복 수행



# reversed 사용하기 - 숫자의 순서를 반대로 뒤집기 
# for (var) in reversed(range(start, end, diff))
for i in reversed(range(3)):
    print('reversed: ', i)          #[0...2] -> [2...0]
for i in reversed(range(5, 10, 2)):
    print('reversed diff: ', i)     #[5...9] -> [9...5], 9, 7, 5



# input + for loop

cnt = int(input('num: '))
for i in range(cnt):
    print('iterate...', i)      #[0...cnt-1]
