# 34.3 비공개 속성private attribute 사용하기 

#공개 속성public attribute : class 바깥에서도 접근 가능
#private attribute : class 안에서만 접근 가능

# private attribute : 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있음 -> class 내부의 method에서만 접근 가능  
    #비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용 -> 중요한 값인데 바깥에서 함부로 바꾸면 안될 때 비공개 속성을 주로 사용, 비공개 속성을 바꿀 수 있는 것은 클래스의 메서드로 한정
    #__(attribute) : private attribute는 __ 로 시작


#class 정리
    #클래스는 특정 개념을 표현(정의)만 할 뿐 실제로 사용하려면 instance로 만들어야 한다
    #속성attribute, method를 사용할 때는 self와 instance를 통해 사용해야 한다


class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  #private attribute

    def pay(self, amount):
        if amount > self.__wallet:
            print('not enough minerals...')
            return

        self.__wallet -= amount     #같은 class 내부의 method에서는 private attribute에 접근 가능 
        print('{0} won left'.format(self.__wallet))
        
    
kim = Person('kim', 20, 'seoul', 1000)
print(kim.name, kim.age, kim.address)   #kim 20 seoul
# print(kim.__wallet)     #AttributeError: 'Person' object has no attribute '__wallet' -> class 외부에서는 private attribute 접근 불가능 

kim.pay(500)    #500 won left
kim.pay(100)    #400 won left
kim.pay(200)    #200 won left
kim.pay(300)    #not enough minerals...


#private method : method도 마찬가지로 __ 로 시작하면 class 안에서만 호출할 수 있는 비공개 method가 된다 
    #method를 클래스 바깥으로 드러내고 싶지 않을 때 사용 -> 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 선언.

class Person:
    def __greeting(self):   #private method
        print('hello')
    def hello(self):
        self.__greeting()   #마찬가지로 class내부에서는 private method 호출 가능 


lee = Person()
lee.hello()         #hello
lee.__greeting()    #AttributeError: 'Person' object has no attribute '__greeting' -> class 바깥에서는 private method 호출 불가능 
