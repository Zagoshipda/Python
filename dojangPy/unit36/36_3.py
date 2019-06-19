#36.3 base class의 attribute 사용하기 



class Person:
    def __init__(self):
        print('Person __init__')    #(A)
        self.hello = 'hello'        #(B)
    
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = 'school'

lee = Student()     #Student __init__
print(lee.school)   #school

# print(lee.hello)    #AttributeError: 'Student' object has no attribute 'hello' -> base class의 attribute를 출력하려고 하면 error 발생 -> 이유는...? -> base class Person의 __init__ method가 호출되지 않았기 때문...! 이는 (A) 가 출력되지 않은 것으로부터 확인이 가능. 따라서 (B)역시 실행되지 않았기 때문에 self.hello attribute가 생성되지 않은 상태라서 error가 발생한 것이다


#해결 방법은...? : super()로 base class 초기화하기 -> super()를 사용해서 base class의 __init__(self) method를 호출하여 base class 초기화를 진행시킨다 

    #super().method()

print('super() --- ')
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()      #Person.__init__() 과 같음 
        self.school = 'school'

kim = Student()
# Student __init__
# Person __init__   -> derived class 먼저 호출 후 base class 호출 

print(kim.school)   #school
print(kim.hello)    #hello




#base class를 초기화하지 않아도 되는 경우 : 만약 derived class 에서 __init__() method를 생략하면 base class의 __init__() method가 자동으로 호출되어 super()를 이용해 호출하지 않아도 된다

    #derived class에 __init__() method 가 없다면 base class 의 __init__()이 자동으로 호출되므로 base class의 attribute를 사용할 수 있다

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    pass

james = Student()   #Person __init__
print(james.hello)  #hello



print('super === ')
#super(derivedclass, self).method() : 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법 -> self가 2번째 argument로 들어감에 주의하기 

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     #baseclass.__init__()
        self.school = 'school'

john = Student()
# Student __init__
# Person __init__

print(john.school)  #school
print(john.hello)   #hello

