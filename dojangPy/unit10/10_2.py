# 10.2 튜플tuple 사용하기 

#  tuple은 list처럼 요소element를 일렬liear로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제를 할 수 없다. 간단하게 읽기 전용 리스트라고 할 수 있음 -> 이와 같은 특성 때문에 보통 ***튜플은 요소가 절대 변경되지 않고 유지되어야 할 때 사용/ 반면 요소를 자주 변경해야 할 때는 리스트를 사용. (상황에 맞게 적절한 자료형 선택하기) 
# 변수에 값을 저장할 때 ( )(괄호)로 묶어주면 tuple이 되며 각 값은 ,(콤마)로 구분. 괄호로 묶지 않고 (1개 이상의)값만 콤마로 구분해도 tuple이 만들어진다 
# tuple은 요소를 변경update, 추가add, 삭제delete할 수도 없는데 ***element가 1개 뿐인 tuple을 사용하는 이유는? -> 함수(클래스)를 사용하다 보면 (1개의 값value)이 아닌 (element가 1개인 tuple)을 넣어야만 하는 경우가 있는데, 이러한 경우 (val, )과 같은 형식을 사용해야 함. 즉, data를 tuple의 형태를 유지면서 처리하기 위한 문법.

# tuple 만들기 
a = 1,2,3,4,5
b = (1,2,3,4,5)
print(a)    #(1, 2, 3, 4, 5)
print(b)    #(1, 2, 3, 4, 5)

#여러 자료형을 섞어서 저장하는 것 또한 가능 
c = ('hello', 2, 2.78, False)
print(c)        #('hello', 2, 2.78, False)
print(type(c))  #<class 'tuple'>

#요소가 1개 있는 tuple 만들기 - 그냥 한 개의 값을 ()로 묶으면 그냥 그 값 자체로 아무런 변화가 없음
a = (3)
print(a)        #3
print(type(a))  #<class 'int'>, type이 그냥 int임을 확인 

#때문에 요소element가 1개인 tuple을 만들 때에는 (val, ) 이런 식으로 사용 혹은 val, 처럼 ()를 붙이지 않고 만드는 것도 가능 
b = (5, )
c = 6,
print(b)        #(5,)
print(type(b))  #<class 'tuple'>
print(c)        #(6,)
print(type(c))  #<class 'tuple'>, type이 tuple이 되었음을 확인 

print("using range ----- ")
#range를 사용하여 tuple만들기 
#(1) var = tuple(range(n)) : n개의 element를 가지는 tuple [0...n-1] 생성 
a  = tuple(range(5))    
print(a)        #(0, 1, 2, 3, 4)
#(2) var = tuple(range(start, end)) : tuple [start...end-1] 생성, end가 포함되지 않는다는 것에 주의(일반적인 array index와 같이 마지막은 포함하지 않는다고 생각하면 될 듯)
 
#(3) var = tuple(range(start, end, diff)) : tuple [start...end-1, 증가폭 diff만큼] 생성, end-1이하까지의 숫자만 포함한다는 것을 아래로부터 확인하기 
c1 = tuple(range(1, 9, 1))
c2 = tuple(range(1, 9, 2))
print(c1)           #(1, 2, 3, 4, 5, 6, 7, 8)
print(c2)           #(1, 3, 5, 7)

d1 = tuple(range(1, 10, 1))
d2 = tuple(range(1, 10, 2))
print(d1)           #(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(d2)           #(1, 3, 5, 7, 9)

e1 = tuple(range(1, 10, 3))     #e1[1...9]
e2 = tuple(range(1, 11, 3))     #e2[1...10]
print(e1)           #(1, 4, 7)
print(e2)           #(1, 4, 7, 10)


# tuple <-> list : tuple을 list로 만들고 list를 tuple로 만들기
# tuple/ list는 요소를 변경, 추가, 삭제할 수 있는지/ 없는지만 다를 뿐 기능과 형태는 같다. 따라서 튜플을 리스트로 바꾸거나 리스트를 튜플로 바꾸는 것이 가능하다.

a = [1,2,3]
print(a, type(a))    #[1, 2, 3] <class 'list'>
a = tuple(a)
print(a, type(a))    #(1, 2, 3) <class 'tuple'>
b = 1,2,3
print(b, type(b))    #(1, 2, 3) <class 'tuple'>
b = list(b)
print(b, type(b))    #[1, 2, 3] <class 'list'>

#list, tuple 안에 문자열 넣기 -> string list, string tuple :  문자 하나 하나가 list와 tuple의 element가 된다 
a = list('hello')
b = tuple('world')
print(a)    #['h', 'e', 'l', 'l', 'o']
print(b)    #('w', 'o', 'r', 'l', 'd')
print(a[0], a[1], a[2], a[3], a[4], sep='')     # hello

#list와 tuple로 변수 여러 개를 한 번에 만들기 -> 변수의 개수와 list/tuple의 element 개수는 같아야 함
a, b, c = [1, 2, 3]
d, e, f = (4, 5, 6)
print(a, b, c, d, e, f)     #1 2 3 4 5 6


# list packing and unpacking/ tuple packing and unpacking 
# packing : 변수에 list, tuple을 할당하는 것 (변수 -> list/tuple)
# unpacking : list와 tuple의 element를 변수들에 할당하는 것 make and assign variables at a time using list variable/ tuple variable (list/tuple -> 변수)

x = [3, 2, 1]   #list packing
y = (6, 5 ,4)   #tuple packing 
a, b, c = x     #list unpacking
d, e, f = y     #tuple unpacking 
print(a, b, c, d, e, f)     #3 2 1 6 5 4

# input().split() 은 list를 반환한다 
print(type(input('input().split() type check (press any key...)').split()))   #<class 'list'>
a, b, c = input('3 numbers: ').split()  #list unpacking, 입력 값을 변수 여러 개에 한번에 저장할 수 있음 
print(a, b, c)