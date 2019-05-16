# 34.1 클래스와 메서드 만들기 

#메서드의 첫 번째 매개변수는 반드시 self를 지정
#파이썬에서는 자료형도 클래스 


class Person:
    def greeting(self):
        print('hello')

lee = Person()  #lee-instance of Person class 
lee.greeting()  #hello

# int, list, dict도 class임을 확인해보자
a = int(10)
b = list(range(10))     #list syntax: []
c = dict(x=10, y=20)    #dict syntax: {}
# a, b, c는 모두 instance 이다. 다만 자주 사용되는 자료형/class의 경우 별도의 생성방법/문법을 제공하는 것이라 할 수 있다.  

print(a)    #10
print(b)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c)    #{'x': 10, 'y': 20}

b.append(20)
print(b)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

print(type(a), type(b), type(c), type(lee)) #<class 'int'> <class 'list'> <class 'dict'> <class '__main__.Person'>

#빈 클래스 만들기 
class Person2:
    pass

# class 내부 method에서 class내부의 또다른 method 호출하기 
class Person3:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()     # self.없이 메서드 이름만 사용하면 다른 의미->클래스 바깥쪽에 있는 함수를 호출한다는 뜻

james = Person3()
james.hello()       #Hello
james.greeting()    #Hello


#현재 instance가 특정 클래스class의 인스턴스instance인지 확인하기 -> 객체의 자료형을 판단할 때 사용
class Animal:
    pass
cat = Animal()
print(isinstance(cat, Animal))  #True
print(isinstance(cat, Person))  #False

# isinstance 사용예시 
def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))     #120

