#35.2 정적static method 
    #instance를 이용하지 않고 클래스에서 바로 호출할 수 있는 static method, class method


# ***정적 메서드는 self를 argument로 받지 않으므로*** 인스턴스 속성에는 접근할 수 없다. 그래서 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용
# 그렇다면 무엇을 정적 메서드로 만들어야 하는가...? -> 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수(pure function)를 만들 때 사용한다. 순수 함수는 side effect가 없고 입력 값이 같으면 언제나 같은 출력 값을 반환한다. 즉, 정적 메서드는 ***instance의 상태를 변화시키지 않는 method를 만들 때 사용***한다


#static method : parameter에 self를 지정하지 않는다
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

#class에서 바로 method 호출하기 
Calc.add(1, 2)  #3
Calc.mul(2, 3)  #6




#python 자료형도 instance method, static method, class method 로 나뉘어져 있다 

#ex. set에 element를 더할 때는 instance method를 사용/ 합집합을 구할 때에는 static method를 사용한다 

a = {1, 2, 3}
a.update({5})
print(a)    #{1, 2, 3, 5}

b = set.union(a, {3, 4, 6})
print(a, b)     #{1, 2, 3, 5} {1, 2, 3, 4, 5, 6} -> 원본 set a는 바뀌지 않으므로 결과를 출력하고 싶다면 새로운 변수에 할당한 후 출력하거나, 아래와 같이 union한 결과 자체를 print해야 한다 

print(set.union({1, 2, 3, 5}, {3, 4, 6}))   #{1, 2, 3, 4, 5, 6}