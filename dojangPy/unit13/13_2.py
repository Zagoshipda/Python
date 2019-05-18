# 13.2 if 조건문과 들여쓰기 


# unexpected indent error, if 다음에 오는 코드들은 반드시 들여쓰기indent의 깊이가 같아야 함
# 들여쓰기 칸 수 자체는 문법으로 정해져 있지 않으며 오직 들여쓰기 깊이로만 판단. 파이썬 코딩 스타일 가이드(PEP 8)에서는 공백 4칸으로 규정

x = 10
if x == 10:
    print('x is...')
        # print('ten...(1)')  #IndentationError: unexpected indent
    print('ten...(2)')

if x == 5:
    print('x is...')    

print('five...')    #의도하는 코드의 동작과 코드의 들여쓰기가 일치하는지 항상 확인하기 : 들여쓰기에 따라 코드가 에러를 발생하지 않고 실행이 되는 경우도 있는데, 이러한 경우에는 잘못된 부분을 찾기가 쉽지 않기 떄문



