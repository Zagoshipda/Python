# unit35. 클래스 속성, 정적 method(instance를 만들지 않고 클래스로 호출), class method 

    #attribute의 2가지 종류: class attribute, instance attribute
    # class 속성: 모든 인스턴스가 공유. 인스턴스 전체가 동일하게 사용해야 하는 값을 저장할 때 사용
    # instance 속성: 인스턴스별로 독립. 각 인스턴스가 서로 각각의 값을 따로 저장해야 할 때 사용


#1) class 속성 사용하기 : 클래스 속성은 클래스에 속해 있으며 모든 instance가 공유한다
    #class 속성을 만드는 경우 class에 바로 속성을 지정하면 된다 
    #class (class name):
    #   attribute = value

class Person:
    bag = []
    def put_bag(self, possession):
        # self.bag.append(possession)     #self는 현재 instance를 뜻하므로 instance와는 독립적으로, 클래스 그 자체에 존재하는 클래스 속성에 사용하기에 적절하지 않다 (물론 정상적으로 동작하기는 함)
        Person.bag.append(possession)   #클래스 이름으로 클래스 속성에 접근 : 클래스 속성에 접근할 때는 이와 같이 클래스 속성이 속해 있는 클래스 그 자체의 이름으로 접근하면 클래스 속성이 가지는 의미를 조금 더 드러내면서 사용할 수 있다. 즉, 현재 사용하는 이 속성(bag)은 instance 속성이 아닌 class 속성임을 보다 명시적으로 밝힐 수 있다 (Person.bag -> Person class에 속한 bag 속성이라는 것을 바로 알 수 있음)

print(Person.bag)   #[] -> class 바깥에서도 class 이름으로 class attribute에 접근하기

john = Person()
john.put_bag('book')
print(Person.bag)   #['book']

jack = Person()
jack.put_bag('key')

print(john.bag)     #['book', 'key']
print(jack.bag)     #['book', 'key']    -> 위에서 bag에 넣었던 물건들이 모두 출력되는 것을 확인할 수 있다. 즉, class 속성은 모든 instance들이 공유하게 된다. 
print(Person.bag)   #['book', 'key']




print()
#python에서 attribute, method 이름을 찾는 순서 : instance -> class 순서대로 찾는다 
#instance 속성이 없으면 class 속성을 찾게 되므로 위 코드에서 Person.bag 대신 james.bag, maria.bag 이라고 해도 문제 없이 동작하게 된다 -> 코드만 보면 ***겉으로는 instance 속성을 사용하는 것처럼 보이지만 실제로는 class 속성을 사용***하는 것으로 동작한다

#인스턴스와 클래스에서 __dict__ 속성을 출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있습니다.
print(john.__dict__)    #{}
print(Person.__dict__)  #{'__module__': '__main__', 'bag': ['book', 'key'], 'put_bag': <function Person.put_bag at 0x02D886A8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}




#2) instance 속성 사용하기 : 인스턴스 속성은 instance별로 독립되어 있으며 서로 영향을 주지 않는다

class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, possession):
        self.bag.append(possession)

apple = Person()
apple.put_bag('apple')

baby = Person()
baby.put_bag('baby')

print(apple.bag)    #['apple']
print(baby.bag)     #['baby']




#비공개 class 속성 사용하기 :  __(밑줄 두 개)로 시작하면 클래스 속성도 비공개 속성으로 만들 수 있다 -> 클래스 안에서만 접근가능, 클래스 바깥에서는 접근 불가능 -> 클래스에서 공개하고 싶지 않은 속성이 있다면 비공개 클래스를 사용




#클래스, metod에서 docstring 사용하기 

