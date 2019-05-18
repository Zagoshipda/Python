#29.4 함수에서 값을 여러 개 반환하기 

def add_sub(a, b):
    return a+b, a-b     #실제로는 tuple이 반환됨 

x, y = add_sub(10, 20)  #unpacking : 튜플이 변수 여러 개에 할당되는 특성을 이용
print(x, y)             #30, -10
print(type(x), type(y)) #<class 'int'> <class 'int'>
z = add_sub(2,1)
print(z, type(z))       #(3, 1) <class 'tuple'>


# 값 여러 개를 직접 반환할 때 tuple로 return하면 된다. 그런데 파이썬에서는 괄호 없이 값을 콤마로 구분하면 튜플이 되므로 다음과 같이 그냥 , 로 구분해서 여러 개의 값을 return하면 된다. 
def multipleret():
    return 1,2,3
x = multipleret()
print(x)    #(1, 2, 3)

# 다른 방법으로는 list를 직접 반환하면 됨
def retlist():
    return [1,2,3,4,5]
x = retlist()
print(x)        #[1, 2, 3, 4, 5]

# x,y = retlist()
# print(x, y)   #ValueError: too many values to unpack (expected 2)

a1, a2, a3, a4, a5 = retlist()
print(a1, a2, a3, a4, a5)       #1 2 3 4 5