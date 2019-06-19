#36.4 method overriding 
#derived class 에서 base class의 method를 새로 정의하기 

class Person:
    def greeting(self):
        print('hello')

class Student(Person):
    def greeting(self):
        print('bye')

kim = Student()
kim.greeting()      #bye


#왜 사용하는가? : 비슷한 기능을 하는 메서드를 같은 이름으로 계속 사용할 때 method overriding을 활용 -> base class의 method를 재활용하면서 중복을 줄일 수 있음, 중복되는 기능은 base class의 기능을 그대로 사용, 원래 기능을 유지하면서 새로운 기능을 덧붙일 수 있음 

class Student(Person):
    def greeting(self):
        super().greeting()
        print('hi')

kim = Student()
kim.greeting()  
#hello
#hi


