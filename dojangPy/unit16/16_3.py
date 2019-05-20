# 16.3 시퀀스 객체로 반복하기 
# for loop는 sequence object로 반복할 수 있다

fruits = 'apple', 'orange', 'grape'

for fruit in fruits:
    print(fruit, end=' ')   # apple orange grape

print(' ')
for l in 'python':
    print(l, end=' ')       # p y t h o n, end 속성으로 줄바꿈 하지 않음

#reversed는 시퀀스 객체를 넣으면 시퀀스 객체를 뒤집는다. (원본 객체 자체는 바뀌지 않으며 뒤집어서 꺼내줌)
print(' ')
a = 'python'
for l in reversed(a):
    print(l, end= ' ')      # n o h t y p
print(' ')
print(a)    #python


