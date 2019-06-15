#33.2 함수 안에서 함수 만들기 - 함수 중첩 에서 global/local변수 사용하기 



def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()   #Hello, world!

#지역 변수의 범위 : 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있다




#지역 변수 변경하기 : 바깥쪽 함수의 지역 변수를 안쪽 함수에서 변경한다면...?
def A():
    x = 10
    def B():
        x = 20
        print('function B():', x)    #function B(): 20
    B()
    print('function A():', x)    #function A(): 10
A()




#바깥쪽 함수의 지역 변수의 값을 변경하기 : nonlocal 키워드 사용하기 
def A():
    x = 10
    def B():
        nonlocal x
        x = 20
        print('function B():', x)   #function B(): 20
    B()
    print('function A():', x)   #function A(): 20
A() 


#nonlocal이 변수를 찾는 순서는...? nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운(상위 함수들 중 가장 낮은 순서의) 함수부터 먼저 찾는다
    #바깥에서 가장 가까운 함수부터 지역 변수를 찾고, 지역 변수가 없으면 한 단계씩 계속 바깥쪽으로 나가서 해당하는 지역변수를 찾는다
def A():
    x = 1
    y = 10
    def B():
        x = 2
        def C():
            nonlocal x
            nonlocal y  # -> nonlocal으로 선언했으므로 바깥쪽 가장 가까운 함수에서 지역변수 y를 찾아아하는데 함수 B()에는 지역변수 y가 없으므로 한 단계 더 바깥으로 나가고, 함수 A()에는 지역변수 y가 있으므로 현재 지역변수 y가 가지는 값은 10이 된다
            x = x + 5
            y = y + 10
            print('func C() x:', x)     #7
            print('func C() y:', y)     #20
        C()
        print('func B() x:', x)     #7
        print('func B() y:', y)     #20
    B()
    print('func A() x:', x)     #1
    print('func A() y:', y)     #20
A()



#global로 전역 변수 사용하기 : 함수가 몇 단계이든 상관 없이 ***global 키워드를 사용하면 무조건 전역 변수를 사용***하게 된다
    #파이썬에서 global을 제공하지만 함수끼리 값을 주고받을 때는 (매개변수parameter와 반환값return value)을 사용하는 것이 좋음 -> 전역 변수는 코드가 복잡해졌을 때 변수의 값을 어디서 바꾸는지를 파악하기가 힘들기 때문에, 전역 변수는 가급적이면 사용하지 않기

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            # x = 30
            # print('C:', x)  #30
            # nonlocal x
            # x = x + 30
            # print('C:', x)  #50
            global x
            x = x + 30
            print('C:', x)  #31
        C()
        print('B:', x)  #20 
    B()
    print('A:', x)  #10
A()

