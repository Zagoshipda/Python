# 13.3 중첩 if 조건문 사용하기 


x = 15
if x > 10:
    print('x is above 10')

    if x == 15:
        print('x is 15')    #안쪽의 if에 속한 print는 들여쓰기의 깊이를 한 번 더한다. (recursive하게 적용)
    if x == 20:
        print('x is 20')