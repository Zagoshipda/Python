#36.5 다중 상속 multiple inheritance 

#여러 base class 들로부터 상속을 받아서 derived class 만들기 

    #class derivedclass(baseclass1, baseclass2, ...):
    #   statement


#Undergraduate class <- Person, University class 의 기능을 모두 상속받음 
class Person:
    def greeting(self):
        print('hello')

class University:
    def credit(self):
        print('credit')

class Undergraduate(Person, University):
    def study(self):
        print('study')

lee = Undergraduate()
lee.study()     #study
lee.credit()    #credit
lee.greeting()  #hello



#diamond inheritance ... aka 죽음의 diamond... 
class A:
    def greeting(self):
        print('A')

class B(A):
    def greeting(self):
        print('B')

class C(A):
    def greeting(self):
        print('C')

class D(B, C):
    pass

x = D()
x. greeting()   #B ...? -> MRO을 따른 것 


#diamond inheritance 문제 해결 : method 탐색 순서 (Method Resolution Order, MRO) -> 다중 상속의 경우 클래스 목록 왼쪽에서 오른쪽 순서로 method를 찾음, 여러 상속 관계에서는 classname.mro() method를 호출해서 resolution order 확인하기 

print(D.mro())  #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]




#object class : python에서 object class는 모든 클래스의 parent이다
print(int.mro())    #[<class 'int'>, <class 'object'>]
print(bool.mro())   #[<class 'bool'>, <class 'int'>, <class 'object'>] -> bool 의 parent가 int 인 것...?ㄷㄷ

#모든 class는 object class를 상속받기 때문에 기본적으로 object의 상속은 생략한다 -> python3부터는 object class의 상속 표시 여부를 구분하지 않고 모두 new-style class를 생성한다 (old-style class 는 삭제됨)
class X:
    pass

class X(object):
    pass 

