# unit31. 함수에서 재귀호출recursive call 사용하기 

#  파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1000으로 정해져 있음.

def hello(cnt):
    if cnt == 0:    #종료조건 base case
        return
    print('hello world:', cnt)
    cnt -= 1
    hello(cnt)

hello(5)    #hello function call 
            #hello world: 5...1


