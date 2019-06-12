# 25.3 dictionary 표현식comprehension 사용하기 


# for 반복문과 if 조건문을 사용하여 dictionary 생성하기 -> dictionary 안에 key와 value, for 반복문을 지정하면 된다

    # { key:val for key, val in {dictionary} }
    # dict({ key:val for key, val in {dictionary} })

keys = ['a', 'b', 'c', 'd']
x = {key:value for key, value in dict.fromkeys(keys).items()}
y = {key:value for key, value in dict.fromkeys(keys, 1).items()}
print(x)    #{'a': None, 'b': None, 'c': None, 'd': None}
print(y)    #{'a': 1, 'b': 1, 'c': 1, 'd': 1} -> dictionary를 생성할 때 default value를 설정하는 경우 


#keys()로 key값만 가져오고 value는 0으로 초기화하기
x = {key:0 for key in dict.fromkeys(keys).keys()} 
print(x)    #{'a': 0, 'b': 0, 'c': 0, 'd': 0}


# values()로 값을 가져온 뒤 해당 값들을 새로운 dictionary의 key로 사용하기
sample = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {value:'good' for value in sample.values()}
print(x)    #{10: 'good', 20: 'good', 30: 'good', 40: 'good'}


#key-value 위치 바꾸기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y = {value:key for key, value in x.items()}
print(y)    #{10: 'a', 20: 'b', 30: 'c', 40: 'd'}





# -> 지금까지의 dictionary 표현식의 결과(dictionary를 생성하는 것)에서는 dict.fromkeys() 함수만을 사용한 결과와 큰 차이가 없음. 그렇다면 효용성은....? -> dictionary 표현식은 dictionary에서 특정 값을 찾아서 삭제할 때 유용하게 사용할 수 있다


#dictionary comprehension표현식 에서 if조건문 사용하기 
#특정 값을 찾아서 key-value 쌍을 삭제하려면...? pop(key, defaultvalue)은 특정 key를 찾아서 삭제하고 popitem()은 가장 마지막 key-value 쌍을 삭제함 
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.popitem()
# print(x)

# for 반복문으로 조건 검사해서 key-value 쌍 삭제하기 시도 : (실패)
# for key, value in x.items():
#     if value == 20 or value == 30:
#         del x[key]
# print(x)    # RuntimeError: dictionary changed size during iteration 


# ***dictionary는 for 반복문으로 반복하면서 키-값 쌍을 삭제하면 안됨...
# 해결방법은...? -> dictionary 표현식에서 if 조건문으로 삭제할 값을 제외시킨다 -> 이 방법은 직접적으로 key-value pair를 삭제하는 것이 아닌, 삭제할 key-value 쌍을 제외한 나머지 key-value pair들로 새로운 dictionary를 만드는 간접적인 삭제 방법이라고 할 수 있음

y = {key:value for key, value in x.items() if value != 20}
print(x, y)    #{'a': 10, 'b': 20, 'c': 30, 'd': 40} {'a': 10, 'c': 30, 'd': 40} -> 원본 dictionary는 그대로 유지한 채 새로운 dictionary가 생성되는 것을 확인할 수 있음 

