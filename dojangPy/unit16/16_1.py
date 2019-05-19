# for 와 range 사용하기 

# 반복문은 반복 횟수counter, 반복iterate 및 정지 조건condition을 자유자재로 제어할 수 있다

# for (var) in range(count):
#     statement...  #indentation necessary 


for i in range(3):  #range(n) : iterate (0...n-1)
    print('hi world', i)    # loop index i = 0 ... 2, range()의 결과로 나온 숫자들은 변수 i에 저장되고 이를 for문 안에서 사용할 수 있다


# range 복습 ----- 아래에서 range를 처음 만들면 'range' class이며, list로 바꾼 후에는 'list' class가 됨을 확인하기
print(range(5))     #range(0, 5)
a = range(5)
print(a, type(a))   #range(0, 5) <class 'range'>
print(a[0], a[1], a[2], a[3], a[4])     #0 1 2 3 4
# print(a[0], a[1], a[2], a[3], a[4], a[5])   #IndexError: range object index out of range

#파이썬 3에서는 range를 사용하면 range 객체(반복 가능한 객체...?)를 만들어낸다.
b = list(range(5))  #range 객체 -> list 로 만든다
print(b, type(b))   #[0, 1, 2, 3, 4] <class 'list'>
