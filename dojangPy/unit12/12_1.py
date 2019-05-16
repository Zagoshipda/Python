# 12.1 딕셔너리dictionary 만들기 

#연관되는 값들을 묶어서 저장하기 ~~~ 구조체structure
#딕셔너리 = {키1: 값1, 키2: 값2}, key-value pair 

marin = {'health': 400, 'mana': 300, 'armor': 20.2}
print(marin)        #{'health': 400, 'mana': 300, 'armor': 20.2}
print(type(marin))  #<class 'dict'>


#key가 중복되는 경우 -> 가장 마지막 key값을 사용 
lux = {'health': 500, 'health': 800, 'mana': 300, 'armor': 7.7}
print(lux['health'])    #800
print(lux['mana'])      #300
print(lux['armor'])     #7.7

#dictionary의 key로는 문자열, 정수, 실수, boolean을 섞어서 사용할 수 있음. key로 list와 dictionary를 사용할 수는 없음. value로는 list, dictionary 까지를 포함한 모든 자료형을 사용할 수 있음.
x = {100:'hundred', 'hundred':100, False:0, True:1, 3.3: [1, 2.4]}
print(x)    #{100: 'hundred', 'hundred': 100, False: 0, True: 1, 3.3: [1, 2.4]}
print(x[100])       #hundred
print(x['hundred']) #100
print(x[False])     #0
print(x[True])      #1
print(x[3.3])       #[1, 2.4]

# 빈 dictionary 만들기 
a = {}
print(a)    #{}
a = dict()
print(a)    #{}


#dict로 dictionary를 만드는 방법들 

a = dict(a=1, b=2, c=3, d=4)
b = dict(zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))   # zip함수로 key list와 value list를 묶어주는 것
c = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
d = dict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

print(a)    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(b)    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(c)    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)    #{'a': 1, 'b': 2, 'c': 3, 'd': 4}