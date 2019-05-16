# 12.2 Dictionary의 key에 접근하고 value 할당하기

# dictionary는 hash기법으로 data를 저장, 보통 dictionary와 같은 key-value 형태의 자료형을 해시hash, 해시 맵hash map, 해시 테이블hash table 이라 한다
# dictionary를 생성할 때는 { }(중괄호)를 사용하고, 키와 값을 1:1 관계로 저장한다
# dictionary는 특정 주제에 대해 서로 연관된 값을 저장할 때 사용 -> list, tuple과 구분되는 특별한 차이점 

#dictionary의 특정 key에 value 할당하기 
dic = {'a':1, 'b':2, 'c':3, 'd':4}
print(dic)      #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic['a'] = 5
print(dic)      #{'a': 5, 'b': 2, 'c': 3, 'd': 4}
print(dic['a']) #5

# dictionary에 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당
dic['e'] = 9
print(dic)      #{'a': 5, 'b': 2, 'c': 3, 'd': 4, 'e': 9}

#dictionary에 key가 있는지/없는지 확인하기 
print('a' in dic)       #Ture
print('a' not in dic)   #False
print('f' in dic)       #False
print('f' not in dic)   #True

#dictionary의 key 개수 구하기 
print(len(dic))     #5
dic2 = {'a':1, 'b':2, 'c':3, 'd':4, 'a':5}
print(dic2['a'])    #5
print(len(dic2))    #4 -> 중복되는 key의 경우를 제외하고 서로 다른distinct한 key의 개수만을 count한다는 것을 알 수 있음 

