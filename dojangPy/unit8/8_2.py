# 8.2 논리 연산자 사용하기 
# and, or, not 

print(True and True)    #T
print(True and False)   #F
print(False and True)   #F
print(False and False)  #F

print(True or True)     #T
print(True or False)    #T
print(False or True)    #T
print(False or False)   #F

print(not True)         #F
print(not False)        #T

print('number examples: ')
# 숫자로 대신하기 -> 0/0.0이면 false (주로 1 사용)나머지는 모두 true
print(bool(1))          #true
print(bool(0))          #false
print(bool(0.0))        #false
print(bool(2))          #true
print(bool(-1))         #true

# 문자열로 대신하기 -> 문자열의 내용 자체는 판단하지 않으며 값이 있으면 true 아니면(빈 문자열이면) false
print(bool(''))         #false
print(bool('True'))     #true
print(bool('False'))    #true
print(bool(False))      #false

# short-circuit evaluation 단락평가 : 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인/평가하지 않는 것 
# ex. and일 경우 첫 번째 값이 false이면 두 번째 값은 확인하지 않고 바로 false로 결과를 확정. or일 경우 첫 번째 값이 true이면 두 번째 값을 확인하지 않고 바로 true로 결정 

print(False and True)   #False  
print(True or False)    #True

# 문자열 'Python'도 불로 따지면 True라서 True and True가 되어 True가 나올 것 같지만 'Python'이 출력. 왜냐하면 파이썬에서 ***논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환하기 때문. 즉, 논리 연산자는 무조건 불을 반환하는 것이 아니다.
print(True and 'python')    #python 
print(True or 'python')     #true

# and 인 경우 문자열 'Python'을 True로 쳐서 and 연산자가 두 번째 값까지 확인하므로 두 번째 값이 반환. or 인 경우 처음 문자열이 True이므로 (첫 번째 값만으로 결과가 결정되므로) 첫 번째 값인 문자열이 그대로 반환
print('python' and True)    #True 
print('python' and False)   #False
print('python' or True)     #python
print('Java' or False)      #Java

# and 연산자 앞에 False나 False로 치는 값이 와서 첫 번째 값 만으로 결과가 결정나는 경우에는 첫 번째 값이 반환
print(False and 'python')   # False
print(0 and 'python')       # 0
print(0.0 and 'python')     # 0.0

# or 연산에서 두 번째 값까지 판단해야 한다면 두 번째 값이 반환됨
print(False or 'python')    # python
print(False or 'React')     # React
print(0 or False)           # False
print(0 or True)            # True
