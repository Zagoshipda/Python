#35.3 class method 


#class method는 언제 사용하는가...? 정적 메서드처럼 인스턴스 없이 호출할 수 있다는 점은 같다. 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용



#클래스 메서드는 첫 번째 매개변수에 cls를 지정 (cls <- class)

class Person:
    cnt = 0
    def __init__(self):
        Person.cnt += 1

    @classmethod
    def print_cnt(cls):
        print('{0}th person'.format(cls.cnt))

    @classmethod
    def create(cls):
        p = cls()   #method 안에서 현재 class의 instance 만들기 
        return p

james = Person()
marry = Person()
mike = Person()
Person.print_cnt()  #3th person

jake = Person()
sam = Person()
Person.print_cnt()  #5th person




#cls를 사용하면 method 안에서 현재 클래스의 instance를 만들 수도 있다. cls는 클래스이므로 cls()는 Person()과 같다. 

paul = Person.create()
print(paul.cnt)     #6
Person.print_cnt()  #6th person





#class method vs static method -> instance 없이도 호출할 수 있다는 공통점
    #class method는 method 안에서 class 속성, class method에 접근해야 할 경우 사용한다


