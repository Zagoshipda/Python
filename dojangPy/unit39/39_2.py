#39.2 iterator 만들기 

#__iter__, __next method를 구현해서 직접 iterator 만들어보기 


#range(n) 처럼 동작하는 iterator class 만들기 : (0...n-1)까지를 반복할 수 있는 class를 설계해야 한다

class Counter:
    def __init__(self, n):
        self.cur = 0    #0부터
        self.n = n      #지정된 숫자 n-1까지 반복

    def __iter__(self):
        return self         #현재 instance를 반환... ??? -> 이 객체는 list, string, dictionary, set, range처럼 __iter__를 호출해줄 iterable가 없으므로 자기 자신(현재 인스턴스)를 반환하면 된다. 즉, 이 객체는 iterable이면서 iterator 이다. 

    def __next__(self):
        if self.cur < self.n:
            r = self.cur
            self.cur += 1
            return r
        else:
            raise StopIteration     #위 조건을 만족하지 않으면, 즉 반복의 끝에 도달하면(cur == n) 에러를 발생시키면서 종료 


for i in Counter(3):
    print(i, end = ' ')

#0 1 2 


print()
print('iterator unpacking === ')
#iterator unpacking : iterator가 반복하는 횟수와 변수의 개수는 같아야 함 
a, b, c = Counter(3)
print(a, b, c)  #0 1 2

#ex. map() 도 iterator이다 
a, b, c = map(int, input('three numbers : ').split())
print(a, b, c)


#반환값에 _ 이용하기 : 반환값을 unpacking했을 때 _에 할당하는 것은 특정 순서의 반환값을 사용하지 않고 무시하겠다는 관례적 표현, 사용하지 않더라도 _는 해당하는 반환값을 가지고 있어 이를 여전히 사용할 수는 있음 
_, b, _ = range(3)
print(_, b)     #2, 1 ---> 가장 마지막 _ 에 저장된 값이 2 가 출력되었다 

a, _, c, d = range(4)
print(a, c, d, _)   #0 2 3 1 


