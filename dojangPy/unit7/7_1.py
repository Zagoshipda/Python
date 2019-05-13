# 7.1 값을 여러 개 출력하기 


# print(val1, val2, val3, ...)
# print에 변수나 값을 콤마로 구분해서 넣으면 각 값이 (1)공백으로 띄워져서 (2)한 줄로 출력

print('Hello', 'Python')

# sep로 값 사이에 문자 넣기 -> 단, 값들 <사이> 에 들어가는 것이므로 마지막에는 추가되지 않음에 주의하자 
print(1, 2, 3, sep = ', ')      # 1, 2, 3
print(4, 5, 6, sep = ',')       # 4,5,6
print(7, 8, 9, sep = ' @-@ ')   # 7 @-@ 8 @-@ 9

print('Hello', 'Python', sep = '')  # HeelloPython, 빈 문자열을 지정하면 문자열이 서로 붙어서 출력되게 할 수 있음 
