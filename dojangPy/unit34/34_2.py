#34.2 속성attribute 사용하기 


# 1. 속성(attribute)을 만들 때 : __init__ 메서드 안에서 self.속성에 값을 할당 (1) __init__ 메서드에서 만든다 (2) self에 .(점)을 붙인 뒤 값을 할당 
# 2. 클래스 안에서 속성을 사용할 때 : self.(var)처럼 self 뒤에 점을 붙여서 사용

# __init__ method : 클래스에 ( )를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화

# 앞 뒤로 __(밑줄 두 개)가 붙은 method는 파이썬이 자동으로 호출한다: 이를 스페셜 메서드(special method) 또는 매직 메서드(magic method)라고 한다.


# ***self의 의미 : self는 instance 자기 자신을 의미 
class Person:
    def __init__(self):
        self.hello = 'hello...!'

    def greeting(self):
        print(self.hello)

lee = Person()
lee.greeting()  #hello...!




# 인스턴스를 만들 때 값argument 전달받아 생성하기 
class P2: 
    def __init__(self, name, age, address):
        self.hello = 'hello'
        self.name = name
        self.age = age
        self.address = address
    def greeting(self):
        print('{0} my name is {1}'.format(self.hello, self.name))   #string formatting

paul = P2('paul', 20, 'Seoul')
paul.greeting()                     #hello my name is paul

# instance attribute 접근하기 
print('name: ', paul.name)          #name:  paul
print('age: ', paul.age)            #age:  20
print('address: ', paul.address)    #address:  Seoul



# 클래스, positional argument, keyword argument 
# 클래스로 인스턴스를 만들 때 positional argument와 keyword argument를 사용할 수 있다

#(1)위치 인수positional argument와 list unpacking 사용하기: *args
class PosArg:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

    #단순히 출력하는 일만 하는 method이더라도 무조건 self parameter를 정의해주어야함
    def showInfo(self): 
        print(self.name, self.age, self.address)    

x = ['john', 25, 'SNU']
john = PosArg(*x)
john.showInfo()     #john 25 SNU

#(2)키워드 인수keyword argument와 dictionary unpacking 사용하기: **kwargs
class KeyArg:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address= kwargs['address']
    def showInfo(self):
        print(self.name, self.age, self.address)

y = {'name': 'good1', 'age': 20, 'address': 'Incheon'}
good1 = KeyArg(**y)
good2 = KeyArg(address = 'china', age = 20, name = 'good2')
good1.showInfo()    #good1 20 Incheon
good2.showInfo()    #good2 20 china


# instance를 생성한 뒤에 attribute 추가하기, 특정 attribute만 허용하기 
# 클래스로 instance를 만든 뒤에도 (instance.attribute = value) 형식으로 속성을 계속해서 추가할 수 있다

class AttrPlus:
    pass

lee = AttrPlus()
# print(lee.name)     #AttributeError: 'AttrPlus' object has no attribute 'name' -> name변수를 생성한 뒤에 출력해야 에러가 뜨지 않음
lee.name = "my name is lee"
print(lee.name)     #my name is lee 


#***이렇게 추가한 속성은 해당 instance에만 추가되는 것으로, 다른 instance에게는 영향을 미치지 않음

kim = AttrPlus()  
# print(kim.name)     #AttributeError: 'AttrPlus' object has no attribute 'name' -> lee instance에는 name 속성을 추가했지만 kim instance에는 name 속성이 없음, 즉 instance 속성은 서로 공유하는 것이 아닌 개별적인 속성임을 알 수 있다
kim.name = "my name is kim"
print(kim.name)     #my name is kim -> kim 인스턴스에도 name 속성을 추가하면 다른 인스턴스와는 다른, kim 인스턴스만의 name 속성을 가지게 된다


#인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있음. 단, 이때는 메서드를 호출해야 속성이 생성됨
class MethodAttr:
    def greeting(self):
        self.hello = 'hello'    # greeting 메서드에서 hello 속성 추가

mark = MethodAttr()
# print(mark.hello)   #AttributeError: 'MethodAttr' object has no attribute 'hello' -> 위에서 이미 살펴본 이유와 같이, 아직 mark 인스턴스에는 hello 속성이 없는 상태
mark.greeting()     #mark 인스턴스에 hello 속성 추가
print(mark.hello)   #hello


#인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고 다른 속성은 제한할 수 있음 -> 이때는 클래스에서 __slots__ = [(attribute name), ...] 으로 허용할 속성 이름을 리스트로 지정한다, 속성의 이름은 반드시 문자열이어야 함

class Slot:
    __slots__ = ['name', 'age'] #name, age 속성만 허용(다른 속성은 생성 제한)
    def showInfo(self):
        print(self.name, self.age)

test = Slot()
test.name = 'pass'
test.age = 1
# test.address = 'fail'   #AttributeError: 'Slot' object has no attribute 'address'
test.showInfo()     #pass 1
