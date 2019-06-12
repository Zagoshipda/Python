#unit 26. set 사용하기 - 집합 

#복습...
#list: []
#tuple: ()
#dictionary: {key:value, ...}


# set 만들기 
    # set = {val1, val2, val3, ...} -> dictionary와의 차이를 비교하자면, dictionary는 하나의 element가 key:value pair를 이루고 있음. 중괄호를 사용한는 점에서 수학에서의 set과 개념적으로, 외형적으로도 일치

fruits = {'berry', 'apple', 'grape', 'cherry', 'banana'}
print(fruits, len(fruits), type(fruits))    #{'banana', 'grape', 'berry', 'apple', 'cherry'} 5 <class 'set'> 

nums = {1, 2, 3, 4, 5}
print(nums, len(nums), type(nums))  #{1, 2, 3, 4, 5} 5 <class 'set'>


# 특징 1) set은 element의 순서가 정해져 있지 않음 (unordered) : 위 2개의 set의 출력결과를 확인해보면 fruits set의 출력결과는 항상 순서가 바뀌는데, nums는 순서가 1 2 3 4 5 로 고정임을 알 수 있다... 이유는..??? 숫자라서 섞이지 않는 것인가....? 

# 특징 2) set에 들어가는 element는 중복될 수 없음 

a = {'orange', 'orange', 'cherry'}
print(a, len(a), type(a))   #{'orange', 'cherry'} 2 <class 'set'>

# 특징 3) set은 [] 로 특정 element 만 출력하는 것이 불가능
# print(a['orange'])  
# print(a[0])         #TypeError: 'set' object is not subscriptable




#set에 특정 값이 있는지 확인하기 : in 
fruits = {'berry', 'apple', 'grape', 'cherry', 'banana'}
print('berry' in fruits, 'berry' not in fruits)    #True False
print('choco' in fruits)    #False
print('choco' not in fruits)    #True





#set(반복 가능한 객체iterable) 로 set 만들기 - 문자열과 range()로 set 만들기 
a = set('apple')
print(a, len(a))    #{'p', 'e', 'a', 'l'} 4 -> 중복된 문자인 p는 1번만 들어감 

b = set(range(5))
print(b, len(b))    #{0, 1, 2, 3, 4} 5 -> 여기서도 역시나 a의 출력순서는 랜덤하게 바뀌는 반면, b의 출력순서는 그대로 유지됨... 

#빈 set 만들기 
c = set()
print(c, len(c), type(c))   #set() 0 <class 'set'>

# cf) {} 는 빈 dictionary이다...
d = {}
print(d, len(d), type(d))   #{} 0 <class 'dict'>


#set 안에 set 넣기... -> 불가능 ... unhashable type 이란...? (예상: 아무래도 특정한 값으로 지정되지 않는 자료형이란 뜻 같다... set은 unordered이므로 그런 것 같기도...?)
# a = {{1,2}, {1,2}}
# print(a, len(a))    #TypeError: unhashable type: 'set'



print('frozenset ===== ')
#내용을 변경할 수 없는 set : frozenset(iterable) -> (집합 연산, method에서 element를 추가하거나 삭제하는 연산, method 사용) 불가 / frozenset는 중첩이 가능, frozenset 끼리만 중첩이 가능하고, frozenset 안에 일반 set은 넣을 수 없다
a = frozenset(range(10))
print(a, len(a), type(a))   #frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}) 10 <class 'frozenset'>

# a = frozenset(1, 2)     #TypeError: frozenset expected at most 1 arguments, got 2
a = frozenset({1, 2})
print(a)    #frozenset({1, 2})

a = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(a, len(a), type(a))   #frozenset({frozenset({3, 4}), frozenset({1, 2})}) 2 <class 'frozenset'>

b = frozenset({frozenset({3, 4}), frozenset({1, 2})})
print(b)    #frozenset({frozenset({3, 4}), frozenset({1, 2})}) ... -> 이건 또 왜 {3, 4}부터 출력되는것....? 대체 어떤 순서가 있는 것인지...? ㅡㅡ;;

# frozenset안에 set 넣기 -> unhashable type error 
# a = frozenset({1, {2, 3}})  #TypeError: unhashable type: 'set'
# print(a)

