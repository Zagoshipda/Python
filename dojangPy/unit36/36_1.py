# unit 36. 클래스 상속 inheritance : base class - derived class

    # parent/super class - child/sub class : base 클래스의 능력을 그대로 활용하면서 새로운 클래스를 만들 때 사용
    #새로운 기능이 필요할 때마다 계속 클래스를 만든다면 중복되는 부분을 반복해서 만들어야 함. 이럴 때 상속을 사용하면 중복되는 기능을 만들지 않아도 되므로, 상속은 기존에 존재하는 class의 기능을 재사용할 수 있어서 효율적


    #class derivedclass(baseclass):
        #statement


#class inheritance : 클래스 상속은 base 클래스의 기능을 그대로 가져오면서 새로운 기능까지 추가할 수 있다
class Person:
    def greeting(self):
        print('hello')

class Student(Person):
    def study(self):
        print('study')


lee = Student()
lee.greeting()  #hello -> base class Person의 greeting method 호출 
lee.study()     #study -> derived class Student의 study method 호출 



#상속 관계 확인하기 : issubclass 함수 사용하기 -> 어떤 class가 특정 base class의 derived class인지 확인. derived class 이면 True, 아니면 False
    #issubclass(derivedclass, baseclass)

class Person:
    pass
class Student(Person):
    pass
class Teacher:
    pass

print(issubclass(Student, Person))  #True
print(issubclass(Person, Student))  #False
print(issubclass(Teacher, Person))  #False
