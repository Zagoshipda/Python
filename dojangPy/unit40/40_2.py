#40.2 generator 만들기 


#range(n) 처럼 동작하는 generator 만들기 

def num_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in num_generator(5):
    print(i, end = ' ')     #0 1 2 3 4
print()

a = [1, 2, 3, 4, 5]
g = num_generator(5)
for i in a:
    print(next(g), end = ' ')   #0 1 2 3 4 
print()



#yield에서 함수 호출하기 : yield에서 function/method를 호출하면 해당 함수의 반환값을 바깥으로 전달한다
    #yield에 무엇을 지정하든 그 결과만 바깥으로 전달한다(함수의 반환값, 식의 결과값)

def upper_generator(x):
    for i in x:
        yield i.upper()     #argument로 전달된 값을 대문자로 바꾼 것(함수의 반환값)을 바깥으로 전달 

fruits = ['apple', 'pear', 'grape']
for i in upper_generator(fruits):
    print(i, end = ' ')     #APPLE PEAR GRAPE 
print()

