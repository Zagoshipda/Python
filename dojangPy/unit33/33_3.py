#33.3 closure 사용하기 

    #closure : 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수 
    #클로저를 사용하면 ***프로그램의 흐름을 변수에 저장***할 수 있다 -> 지역 변수와 코드를 묶어서 사용하고 싶을 때 클로저를 활용, 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용


#함수를 closure 형태로 만들기 
def calc():
    a = 1
    b = 2

    #함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산, 함수 ALU를 만든 뒤에는 이 함수를 바로 호출하지 않고 return으로 함수 자체를 반환 -> 함수를 반환할 때는 함수 이름만 반환해야 하며 ()를 붙이지 않는다 (함수를 호출하는 것이 아님)
    def ALU(x):
        return a * x + b    
    return ALU

c = calc()  #여기서는 calc() 함수를 호출한다
print(c(1), c(2), c(3), c(4), c(5), type(c))    #3 4 5 6 7 <class 'function'> -> 함수 calc가 끝났는데도 c는 calc의 ***지역 변수 a, b를 사용***해서 계산을 하고 있음, c에 저장된 함수 (ALU)가 클로저이다




#lambda로 closure 만들기 -> lambda를 사용하면 보통 클로저는 람다 표현식과 함께 사용하는 경우가 많음
    #lambda: 이름이 없는 익명 함수, closure: 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수
def calc():
    a = 1
    b = 2
    return lambda x : a * x + b     #람다 표현식을 만든 뒤 람다 표현식 자체를 반환
c = calc()
print(c(1), c(2), c(3), c(4), c(5), type(c))    #3 4 5 6 7 <class 'function'>




#클로저의 지역 변수 변경하기 : nonlocal 사용

print('change local variable ===== ')
# nonlocal을 사용하지 않는 경우는? 
def calc():
    a = 1
    b = 2
    total = 0
    def ALU(x):
        total = total + a * x + b   #UnboundLocalError: local variable 'total' referenced before assignment
        print(total)
    return ALU

c = calc()
# print(c(1), c(2), c(3), c(4), c(5), type(c))    # -> 여기서 error 발생...


# nonlocal으로 변수를 선언해서 클로저의 지역 변수의 값 변경하기 
print('nonlocal --- ')
def calc():
    a = 1
    b = 2
    total = 0
    def ALU(x):
        nonlocal total  #이렇게 nonlocal으로 변수를 선언해주어야 값을 변경하는 것이 가능해진다 
        total = total + a * x + b
        print(total)
    return ALU

c = calc()
print(c(1), c(2), c(3), c(4), c(5), type(c))    

# 3
# 7
# 12
# 18
# 25
# None None None None None <class 'function'>

