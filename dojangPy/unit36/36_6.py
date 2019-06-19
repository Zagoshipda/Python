#36.6 추상 클래스 abstract class 

#method의 목록만 가진 클래스 -> 상속받는 클래스에서 method implementation을 강제하기 위해 사용 

    #abc(Abstract Base Class) module을 import 해야 함 
    #클래스의 ( ) 안에 metaclass=ABCMeta를 지정하고, method를 만들 때 위에 @abstractmethod를 붙여서 abstract method로 지정해주어야 함 
    #abstract class는 derived class가 반드시 구현해야 하는 method를 정해주는 용도로 사용
    #abstract class의 abstract method를 모두 구현했는지 확인하는 시점은 이를 상속한 derived class를 사용해서 instance를 만들 때. 만약 구현하지 않은 abstract method가 있다면 TypeError 발생.
    #abstract class는 instantiate이 불가능, 오로지 상속의 용도로만 사용 -> abstract method는 empty method로 선언 



from abc import *
class StudentBase(metaclass = ABCMeta):
    @abstractmethod
    def study(self):
        pass        #abstract method는 호출할 일이 없으므로 empty method로 생성

    @abstractmethod
    def school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('study')

# john = Student()    #TypeError: Can't instantiate abstract class Student with abstract methods school -> abstract class를 상속했다면 @abstractmethod가 붙은 abstract method를 모두 구현해야 한다


class Student(StudentBase):
    def study(self):
        print('study')

    def school(self):
        print('school')

lee = Student()
lee.study()     #study
lee.school()    #school




#abstract method를 empty method로 만드는 이유는...? -> abstract class로는 instance를 만들 수 없다 (instantiate 불가능), 때문에 abstract method를 호출할 일이 없기 때문에 abstract method를 만들 때에도 empty method로 만든 것 

# kim = StudentBase()     #TypeError: Can't instantiate abstract class StudentBase with abstract methods school, study

