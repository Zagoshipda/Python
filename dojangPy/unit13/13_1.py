# unit 13. if 조건문으로 특정 조건일 때 코드 실행하기 

# 13.1 if 조건문 사용하기 

# 조건문은 다양한 상황에 대처할 때 사용 -> 조건문을 사용하면 조건에 따라 다른 코드를 실행

x = 10
if x == 10:
    print('x is 10')    # 들여쓰기 4칸, if body 

y = 20
if y == 10:
    print('y is 10')
if y == 20:
    print('y is 20')

z = 30
if z == 30:
    pass    #코드 생략하기, 파이썬에서는 if 다음 줄에 아무 코드도 넣지 않으면 에러가 발생하므로 ***if 조건문의 형태를 유지하기 위해 pass를 사용. 나중에 작성해야 할 코드를 표시할 때 사용할 수 있음. ex. pass만 넣고 나중에 할 일은 주석으로 남겨놓는 방식으로 사용. TODO: ...

print('bye world')  #TODO: todo test...


# for comments: TODO, FIXME, BUG, NOTE, ... 



