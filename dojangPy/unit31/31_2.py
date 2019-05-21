# 31.2 make a factorial using recursive call

# recursive call -> 계산 결과가 즉시 구해지는 것이 아니라 재귀호출로 n-1을 계속 전달하다가 n==1일 때 비로소 1을 반환하면서 n과 곱하고 다시 결괏값을 반환. 그 뒤 n과 반환된 결괏값을 곱하여 다시 반환하는 과정을 반복해서 최종적으로 전체 문제에 대한 답을 구함 -> function stack 

def fact(n):
    if n == 1:      #종료조건 termination 
        return 1
    return n * fact(n-1)

print(fact(5))  #120
print(fact(6))  #720
print(fact(7))  #5040