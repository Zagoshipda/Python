# 집합 연산 사용하기 

#집합 연산 -> 산술 연산자, 논리 연산자 


#합집합 : set.union(a, b) / a | b 
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
c = a | b
print(c, len(c), type(c))   #{1, 2, 3, 4, 5, 6, 7} 7 <class 'set'>, 4는 중복이므로 1개만 

d = set.union(a, b)
print(d, len(d), type(d))   #{1, 2, 3, 4, 5, 6, 7} 7 <class 'set'>

d = {1, 2, 3} | {2, 3, 4}
print(d, len(d), type(d))   #{1, 2, 3, 4} 4 <class 'set'>




#교집합 : set.intersection(a, b) / a & b
c = a & b
d = set.intersection(a, b)
print(c, d)     #{4} {4}

c = {1, 2, 3} & {2, 3, 4}
print(c, len(c))    #{2, 3} 2




#차집합 : set.difference(a, b) / a - b
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a - b
d = b - a
print(c, d)     #{1, 2} {5, 6}
c = set.difference(a, b)   
d = set.difference(b, a)
print(c, d)     #{1, 2} {5, 6}




#대칭차집합 : symmetric_difference(a, b) / a ^ b (= U - a & b)
c = a ^ b
d = b ^ a
print(c, d)     #{1, 2, 5, 6} {1, 2, 5, 6} -> 대칭차집합은 symmetric 

c = set.symmetric_difference(a, b)
print(c, len(c))    #{1, 2, 5, 6} 4





print('set operation & assignment ===== ')
#집합 연산 후 할당 연산자 사용하기 : set 자료형에 |, &, -, ^ 연산자와 할당 연산자 =을 함께 사용하면 집합 연산의 결과를 변수에 다시 저장(할당)한다 (~ 변수에서의 += -= *= /= 등의 연산과 비슷)

#현재 set에서 다른 set 더하기 : set1 |= set2 / set1.update(set2)
a = {1, 2, 3, 4}
a |= {5}
print(a, len(a))    #{1, 2, 3, 4, 5}
a.update({4, 5, 6})
print(a)    #{1, 2, 3, 4, 5, 6}


#현재 set에서 다른 set중 겹치는 element만 현재 set에 더하기 (나머지는 제외함) : set1 &= set2 / set1.intersection_update(set2)
a = {1, 2, 3, 4}
a &= {0, 1, 3, 4, 5}
print(a)    #{1, 3, 4}
a.intersection_update({2, 3, 4, 5, 6})
print(a)    #{3, 4}


#현재 set에서 다른 set 과 겹치는 element 빼기 : set1 -= set2 / set1.difference_update(set2)
a = {1, 2, 3, 4}
a -= {4, 5, 6}
print(a)    #{1, 2, 3}
a.difference_update({0, 1, 4, 5, 6})
print(a)    #{2, 3}


#현재 set와 다른 set를 포함한 전체 element들 중 겹치지 않는 요소만 현재 set에 저장 : set1 ^= set2 / set1.symmetric_difference_update(set2)
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)    #{1, 2, 5, 6}
a.symmetric_difference_update({2, 3, 4, 5, 6, 7})
print(a)    #{1, 3, 4, 7}




print('subset and superset ===== ')
#부분집합과 상위집합 -> 집합 사이의 포함관계 파악하기 

#부분집합 subset : set1 <= set2 / set1.issubset(set2)
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4, 5})     #True
print(a <= {1, 2, 3, 4})        #True
print(a.issubset({1, 2, 3}), a.issubset({1, 2, 3, 4, 5}))   #False True


#진부분집합 proper subset : set1 < set2 / method는 없음... ㅡㅅㅡ;;;
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5}, a < {1, 2, 3, 4})    #True False


#상위집합 superset : set1 >= set2 / set1.issuperset(set2)
a = {1, 2, 3, 4}
print(a >= {1, 2, 3}, a >= {1, 2, 3, 4})    #True True
print(a.issuperset({1}), a.issuperset({1, 2, 3, 4, 5})) #True False


#진상위집합 proper superset : set1 > set2 / 마찬가지로 method는 없음
a = {1, 2, 3, 4}
print(a > {1, 2, 3}, a > {1, 2, 3, 4}, a > {1, 2, 3, 4, 5}) #True False False




print('set comparison ===== ')
#두 set이 같은지 다른지 비교하기 : ==
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4}, a == {3, 2, 1, 4}, a == {1, 2, 4})    #True True False, set은 element의 순서가 정해져 있지 않으므로 element들 전체가 같기만 하면 True
print(a != {1, 2}, a != {2, 4, 3, 1})   #True False



#set가 겹치는지 확인하기 : set1.isdisjoint(set2) - 겹치는 element가 없으면(disjoint하면) True, 있으면(disjoint하지 않으면) False
a = {1, 2, 3, 4}
print(a.isdisjoint({2, 4, 5}), a.isdisjoint({5, 6, 7, 8}))  #False True
print(a.isdisjoint(set()))  #True, 공집합과는 disjoint함... 겹치는 것이 없는 것이 자명
b = set()
print(b, len(b), type(b))   #set() 0 <class 'set'>
print(b.isdisjoint({1}), b.isdisjoint(set()))   #True True ... 역시나 마찬가지로 공집합은 모든 set들과 disjoint하다... 공집합은 또한 공집합과도 disjoint하다... (자명) 겹치는 것이 있을 것이 없으므로 아무 것도 없는 상태 또한 겹치는 element가 없는 것이라 할 수 있다


