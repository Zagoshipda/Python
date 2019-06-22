#39.3 index로 접근할 수 있는 iterator 만들기 
    #지금까지는 __iter__, __next__ method 를 구현하는 방식으로 iterator를 만들었다면, 
    #index로 접근할 수 있는 iterator를 만드는 방법은...? -> __getitem__ method를 사용해서 구현하기 

    # class에서 __getitem__만 구현해도 iterator가 되며 __iter__, __next__는 생략 가능 (초깃값이 없다면 __init__도 생략 가능)

#index로 접근하는 Counter class design 

class Counter:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, idx):     #argument로 index를 받는다 
        if idx < self.n:
            # return idx      #input으로 들어온 index값을 그대로 return, index로 계산을 해서 다른 숫자로 return 하는 것도 가능 
            return idx * 10     #output: 0 10 20 -> 이렇게 기본 index값을 계산해서 다른 값으로 return하면 iterator가 반복하는 숫자들의 값을 다양하게 조작할 수 있음 
        else:
            raise IndexError

a = Counter(3)
print(a[0], a[1], a[2])     #0 1 2 ---> 0, 1, 2 값을 input으로 주어 output으로 0, 1, 2가 나온 것과 같음 

for i in a:
    print(i, end = ' ')     #0 1 2

