#38.2 exception - else, finally

#else : 예외가 발생하지 않았을 때 실행할 코드, except바로 다음에 위치, except를 생략할 수 없음 
    #try:
        #(test statement)
    #except:
        #(exception handling code)
    #else:
        #(non-exception execution code)
    #finally:
        #(always execution code)


try:
    x = int(input('divisor : '))
    y = 10 / x
except ZeroDivisionError:
    print("can't divide by 0")
else:
    print(y)

#exception과는 상관없이 항상 코드 실행하기 : finally -> except와 else를 생략할 수 있음 
finally:
    print('execution finished...!')


#try, except, else, finally는 함수가 아니므로 stack frame을 만들지 않는다 -> try, except, else, finally 안에서 변수를 만들더라도 try, except, else, finally 바깥에서도 계속해서 사용할 수 있음

print("x, y : ", x, y)  # -> 위에서 생성한 변수 x, y를 scope 바깥에서도 출력할 수 있음 

