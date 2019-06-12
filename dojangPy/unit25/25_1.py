# unit25. dictionary 응용하기 

# dictionary의 key-value pair를 조작하는 method
# dictionary 정보(key, value)를 조회하는 method
# for loop를 사용하여 key, value에 접근하는 방법
# 딕셔너리 표현식 dictionary comprehension
# 중첩 딕셔너리 nested dictionary



# 25.1 dictionary 조작하기 

# dictionary에 key-value 쌍 추가하기 

    # setdefault: key-value 쌍 추가
    # update: 키의 값 수정, 키가 없으면 키-값 쌍 추가


#dictionary에 key와 기본값 저장하기 : setdefault(key, value) -> 딕셔너리에 key-value 쌍을 추가. setdefault(key)처럼 argument로 value값을 주지 않으면 value에 None을 저장(default 값이 아무 것도 없는 None)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)        #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}
x.setdefault('f', 100)
print(x)        #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None, 'f': 100}



# key의 value 수정하기 

# 1) key가 문자열인 경우 : update(key = value) 로 수정 가능
x.update(e = 50)
print(x)        #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 100}

# 만약 dictionary에 수정할려는 key가 없으면 key-value 쌍을 추가한다... -> 그럼 그냥 element를 추가하는 경우 보통은 update() 하는 게 좋은 방법일듯...?
x.update(g = 5)
print(x)        #{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 100, 'g': 5}

#여러 쌍을 한꺼번에 수정하기 -> 마찬가지로 key가 없으면 key-value쌍을 추가, 이 경우는 아래와 같이 value를 생략할 수 없음 
# x.update(a=1, b=2, c=3, h=9, i) #SyntaxError: positional argument follows keyword argument
# x.update(i, a=1, b=2, c=3, h=9) #NameError: name 'i' is not defined
x.update(a=1, b=2, c=3, h=9)
print(x)        #{'a': 1, 'b': 2, 'c': 3, 'd': 40, 'e': 50, 'f': 100, 'g': 5, 'h': 9}


# 2) key가 숫자인 경우 : update( {dictionary} ) 로 수정
y = {1:'one', 2:'two'}
# y.update(3 = 'three')   #SyntaxError: keyword can't be an expression
y.update({3:'three', 1:'ONE'})  
print(y)        #{1: 'ONE', 2: 'two', 3: 'three'}

#list와 tuple로 값 수정하기 : update(list / tuple)
y.update([[2, 'TWO'], [4, 'four']])
print(y)        #{1: 'ONE', 2: 'TWO', 3: 'three', 4: 'four'}
y.update(((4, 'FOUR'), (5, 'five')))
print(y)        #{1: 'ONE', 2: 'TWO', 3: 'three', 4: 'FOUR', 5: 'five'}



# update(반복 가능한 객체) -> key-value 쌍으로 된 반복 가능한 객체로 값을 수정
# key 리스트와 value 리스트를 묶은 zip 객체로 값을 수정하기
y.update(zip([1, 2, 3], ['one', 'two']))
print(y)        #{1: 'one', 2: 'two', 3: 'three', 4: 'FOUR', 5: 'five'} -> 3에 해당하는 value를 지정하지 않았더니 값이 수정되지 않음ㅇ을 알 수 있음

#파이썬 내장함수 - zip(반복 가능한 객체, ...) : 반복 가능한 객체 여러 개를 넣으면 각각의 객체들의 element들을 순서대로 tuple로 묶어서 zip 객체를 반환
a = list(zip([1, 2, 3], [97, 98, 99], [1, 2, 3]))
print(type(a), a, len(a))    #<class 'list'> [(1, 97, 1), (2, 98, 2), (3, 99, 3)] 3



#setdefulat() 와 update()의 차이는...? -> setdefault()는 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없음, 하지만 update()는 키-값 쌍 추가와 값 수정이 모두 가능.
x = {'a':1, 'b':2}
x.setdefault('a', 3)
print(x)    #{'a': 1, 'b': 2} -> 수정 불가
x.update(a = 3)
print(x)    #{'a': 3, 'b': 2} -> 수정 가능 



print('deletion ===== ')
#dictionary에서 key-value 쌍 삭제하기 : pop(), del
x = {'a': 1, 'b': 2, 'c': 3}
out = x.pop('a')        #pop()의 반환값을 저장
print(x, len(x), out)   #{'b': 2, 'c': 3} 2 1 

#pop(key, defaultvalue) -> default value를 지정하면 dictionary에 해당 key가 있을 경우에는 삭제한 value값을 반환, key가 없을 때는 미리 지정해던 default value를 반환 -> keyerror가 나도 프로그램을 실행시킬 수 있도록 하는 방법 (에러 사전 방지) 
# out = x.pop('z')    #KeyError: 'z'
out = x.pop('z', 0)
print(x, out)           #{'b': 2, 'c': 3} 0

# out = del x['b']    #SyntaxError: invalid syntax
del x['b']
print(x)                #{'c': 3}



# dictionary에서 (임의의) 가장 마지막 key-value 쌍 삭제하기 : popitem()  
# 파이썬 3.6 이상에서는 마지막 키-값 쌍을 삭제하며 3.5 이하에서는 임의의 키-값 쌍을 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = x.popitem()
z = x.popitem()
print(y, z, x, len(x))  #('d', 40) ('c', 30) {'a': 10, 'b': 20} 2


#dictionary의 모든 key-value 쌍 삭제하기 : clear()
x.clear()
print(x, len(x))    #{} 0 -> 빈 dictionary가 되었음 



#dictionary에서 특정 key의 값value 가져오기 : get(key), get(key, default value)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = x.get('c')
print(y, x)     #30 {'a': 10, 'b': 20, 'c': 30, 'd': 40} -> 원본이 되는 dictionary는 바뀌지 않음 
y = x.get('z', 0)   #get(key, default value) - default value를 지정하면 dictionary에 key가 없는 경우 에러를 발생시키지 않고 default value를 반환한다     
print(y, x)     #0 {'a': 10, 'b': 20, 'c': 30, 'd': 40}



print('dictionary methods ===== ')
#dictionary에서 key-value 쌍을 모두 가져오기 -> for 반목문과 조합해서 사용

    # items(): 키-값 쌍을 모두 가져옴
    # keys(): 키를 모두 가져옴
    # values(): 값을 모두 가져옴


x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items(), type(x.items()))    #dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)]) <class 'dict_items'>
print(x.keys(), type(x.keys()))     #dict_keys(['a', 'b', 'c', 'd']) <class 'dict_keys'>
print(x.values(), type(x.values()))   #dict_values([10, 20, 30, 40]) <class 'dict_values'>






print('dictionary from list and tuple ===== ')
#list와 tuple로 dictionary 만들기 : dict.fromkeys(key list/tuple, value) -> fromkeys expected at most 2 arguments
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)    #{'a': None, 'b': None, 'c': None, 'd': None}, key list로 dictionary 생성, value는 모두 None으로 초기화 

y = dict.fromkeys(keys, (1, 2))
print(y)    #{'a': (1, 2), 'b': (1, 2), 'c': (1, 2), 'd': (1, 2)}


keys = ('a', 'b', 'c')
z = dict.fromkeys(zip(keys, ('one', 'two')))
print(z)    #{('a', 'one'): None, ('b', 'two'): None}
z = dict.fromkeys(keys, 1)
print(z)    #{'a': 1, 'b': 1, 'c': 1} ... -> 각 key마다 서로 다른 value를 지정할 수는 없나...?



#없는 key에 접근했을 때 에러가 발생하지 않도록 하기 -> defaultdict는 없는 key에 접근하더라도 에러가 발생하지 않고 기본값을 반환한다 ... why? defaultdict(기본값 생성 함수) : argument로 기본값 생성 함수를 전달하여 default value를 미리 만들어주기 때문, 기본값 생성 함수로는 ***특정 값을 반환하는 함수***를 넣어주면 된다

from collections import defaultdict 
x = defaultdict(int)    #int로 기본값 생성, 기본값이 0인 default dictionary 생성  
print(x, len(x))        #defaultdict(<class 'int'>, {}) 0
x.setdefault('a', 1)
print(x, type(x))       #defaultdict(<class 'int'>, {'a': 1}) <class 'collections.defaultdict'>
print(x['a'], x['z'])   #1 0

#기본값이 0 인 이유는...? 
print(int())    # 0 -> int()는 ***실수나 문자열을 정수로 변환***하지만, 다음과 같이 int()의 argument로 아무것도 넣지 않고 호출하면 0을 반환한다



print('using lambda expression ===== ')
#0이 아닌 다른 값을 기본값으로 설정하기 : 기본값 생성 함수를 만들어서 argument로 넣어주기
    #람다 표현식 lambda expression 사용 (anonymous function)

y = defaultdict(lambda : 'python')  #문자열 'python'을 반환하는 함수를 defaultdict의 argument로 넣어 'python'문자열이 dictionary의 기본값이 되도록 설정하였다 
print(y, len(y), type(y))   #defaultdict(<function <lambda> at 0x03BE8660>, {}) 0 <class 'collections.defaultdict'>
print(y['a'], y[0])     #python python
print(y)    #defaultdict(<function <lambda> at 0x03978660>, {'a': 'python', 0: 'python'}) -> 위에서 호출한 key값들이 생성되었다

# y.setdefault('a', 1, 'b', 2)    #setdefault expected at most 2 arguments
y.setdefault('a', 1)
y.setdefault('b', 2)
print(y)    #defaultdict(<function <lambda> at 0x03978660>, {'a': 'python', 0: 'python', 'b': 2}) -> setdefault()는 이미 존재하는 key의 값value 을 변경할 수 없음 
print(y['a'], y['b'], y['c'], y[3], len(y))     #python 2 python python 5
print(y)    #defaultdict(<function <lambda> at 0x00AB8660>, {'a': 'python', 0: 'python', 'b': 2, 'c': 'python', 3: 'python'}) -> 'c' 와 3이 새로운 key로 추가되었음
y.update(a = 1, c = 3) 
print(y)    #defaultdict(<function <lambda> at 0x00B08660>, {'a': 1, 0: 'python', 'b': 2, 'c': 3, 3: 'python'}) -> update()는 기존에 존재하는 key의 value를 변경할 수 있음 



#참고 ===== 
#dictionary의 key가 tuple인 경우... -> 이런 경우 역시 가능은 하다...! 
a = {('a', 'b'):1, 'c':2}
print(a, len(a))    #{('a', 'b'): 1, 'c': 2} 2
print(a.get('c'), a.get('a', 'b'), a.get(('a', 'b')))   #2 b 1...? -> 'b'가 default value의 역할을 한 것, key값을 tuple로 설정하면 get으로 value를 가져올 때에도 key를 tuple로 넣어주어야 한다


