# 7.2 줄바꿈(개행) 활용하기
# print의 sep, end 속성에 제어 문자(escape sequence), 공백 문자 등을 조합하면 다양한 형태로 값을 출력할 수 있음
# sep -> 출력 사이에 들어갈 값 설정 
# end -> 출력 마지막에 들어갈 값 설정

# \n : 제어문자, escape sequence, \t: tab

print(1, 2, 3)              # 1 2 3, 한 줄에 모두 출력하기 
print(1, 2, 3, sep = '\n')  # 1\n2\n3, 한 줄에 하나씩 출력하기
print('1\n2\n3')            # 한 줄에 하나씩 출력, 위와 같은 결과를 얻을 수 있음 
print('1 \n 2 \n3')        # \n 양옆으로 간격 넣어보기 


print('-----')
# end 사용하기 

# print는 기본적으로 출력하는 값 끝에 \n을 붙인다. 즉, 자동 개행한다 
print(1)
print(2)
print(3)

# print를 여러 번 사용해서 print(val1, val2, val3, ... )처럼 한 줄에 여러 개의 값을 출력하는 방법은...? -> print의 end속성으로 빈 문자열을 지정하면 된다. 기본적으로 print의 end에 \n이 지정된 상태인데 빈 문자열을 지정하면 강제로 \n을 지워주기 때문.

# end는 현재 print가 끝난 뒤 그 다음에 오는 print 함수에 영향을 준다
print(1, end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)            # 123

print(1, 2, 3)      # 1 2 3 
print(1, end=' ')   # end에 공백 한 칸 지정하기, 위와 같은 결과를 얻을 수 있음  
print(2, end=' ')
print(3)            # 1 2 3 

