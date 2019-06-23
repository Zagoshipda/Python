#40.3 yield from으로 값을 여러 번 바깥으로 전달하기 


#case1) 반복문을 사용해서 매번 yield하기
def num_generator():
    x = [1, 2, 3]
    for i in x:
        yield i

for i in num_generator():
    print(i, end = ' ')     #1 2 3
print() 

#case2) yield from 사용하기 (python 3.3 이상부터 사용 가능)

    # yield from iterable
    # yield from iterator
    # yield from generator 

def num_generator():
    x = [1, 2, 3]
    yield from x

for i in num_generator():
    print(i, end = ' ')     #1 2 3 
print()



#yield from에 generator 객체 지정하기 
def num_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

def five_generator():
    yield from num_generator(5)     #generator 객체를 yield from

for i in five_generator():
    print(i, end = ' ')     #0 1 2 3 4 
print()



#generator 표현식 ~ list comprehension 
    #list comprehension : [] -> 처음부터 list의 모든 element를 만들어냄
    #generator comprehension : () -> 필요할 때 그때그때 element를 만들어내므로 메모리를 절약할 수 있다

a = [i for i in range(20) if i % 2 == 0]
print(a)    #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

b = (i for i in range(20) if i % 2 == 0)
print(b)    #<generator object <genexpr> at 0x039F4F30>

i = 0
while i < 10:
    print(next(b), end = ' ')   #0 2 4 6 8 10 12 14 16 18 
    i += 1
print()

