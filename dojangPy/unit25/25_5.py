#25.5 dictionary의 할당과 복사 

x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
y = x
print(x == y, x is y, type(x), type(y))   #True True <class 'dict'> <class 'dict'>


# (A) 와 (B) 의 결과를 비교해보라...!

z = x.copy()
print(x == z, x is z, type(x), type(z)) #True False <class 'dict'> <class 'dict'> ---(A)

y['a'] = 9
print(x)    #{'a': 9, 'b': 2, 'c': 3, 'd': 4}
print(y)    #{'a': 9, 'b': 2, 'c': 3, 'd': 4}
print(z)    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(x == y, x is y, type(x), type(y)) #True True <class 'dict'> <class 'dict'>
print(x == z, x is z, type(x), type(z)) #False False <class 'dict'> <class 'dict'> ---(B)




print('nested dictionary ===== ')
#nested dictionary의 할당과 복사 
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x
z = x.copy()
print(y)    #{'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
print(z)    #{'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
print(x == y, x is y, x == z, x is z)   #True True True False

y['a']['python'] = 1
print(y)    #{'a': {'python': 1}, 'b': {'python': '3.6'}}
print(z)    #{'a': {'python': 1}, 'b': {'python': '3.6'}} -> (A) 여기서 변경되면 안됨... 변경된다는 것은 완전히 새로운 dictionary를 만들어낸 것이 아닌 원본 dictionary와 어떠한 부분을 공유하고 있다는 것을 의미... 
print(x == y, x is y, x == z, x is z)   #True True True False

y['a'] = 9
print(x)    #{'a': 9, 'b': {'python': '3.6'}}
print(y)    #{'a': 9, 'b': {'python': '3.6'}}
print(z)    #{'a': {'python': 1}, 'b': {'python': '3.6'}} -> (B) 변경되지 않음
print(x == z, x is z)   #False False

y['b']['python'] = 2
print(y)    #{'a': 9, 'b': {'python': 2}}
print(z)    #{'a': {'python': 1}, 'b': {'python': 2}}

# -> 여기까지의 결과 분석: z가 x와 완전히 같은 것은 아니지만, 또한 x가 우리가 예상하는대로의, 제대로 복사된 것(원본 dictionary의 값의 변경 여부와 상관없이, 독립적으로 존재하는 완전히 새로운 dictionary)도 역시나 아닌 것임을 알 수 있다... (B) 그냥 key값을 통한 변경에 대해서는 변경이 이루어지지 않고 dictionary가 그대로 유지되지만, (A) nested key값을 통한 값의 변경에 대해서는 수정사항이 반영되고 있다... 
# 추측: 가장 1차적인 key값에 대해서는 새로운 key값이 생성되지만 neseted key는 원본 dictionary와 새롭게 만든 dictionary가 서로 공유하고 있는 구조일 것이라 예상해볼 수 있음. (~ 일종의 얕은 복사라고 할 수 있겠다)
# -> nested dictionary에서의 copy()를 하면 key list가 복제되는것...? 정확한 내부 구조는?



print('deepcopy() ===== ')
#nested dictionary를 완전하게 복사하는 방법: copy 모듈의 deepcopy() 함수를 사용 -> nested dictionary에 들어있는 모든 dictionary를 복사하는 깊은 복사(deep copy)를 수행 

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy
y = copy.deepcopy(x)
print(x == y, x is y)   #True False
x['a']['python'] = 1
print(x)    #{'a': {'python': 1}, 'b': {'python': '3.6'}}
print(y)    #{'a': {'python': '2.7'}, 'b': {'python': '3.6'}} -> 변경되지 않음
print(x == y, x is y)   #False False

x['a'] = 1
print(x)    #{'a': 1, 'b': {'python': '3.6'}}
print(y)    #{'a': {'python': '2.7'}, 'b': {'python': '3.6'}} -> 변경되지 않음
print(x == y, x is y)   #False False 

# -> dictionary y의 값을 변경해도 dictionary x에는 영향을 미치지 않음
# 즉 원본 dictionary인 x의 값의 변경과 무관하게 새로 만든 dictionary y의 key-value가 변경되지 않는다는 것으로부터, 완전히 독립된 새로운 dictionary를 생성하였음을 알 수 있다 
