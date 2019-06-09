# unit 22. list와 tuple 응용하기 


#22.1 list 조작하기 
    #cf) database CRUD - Create, Read, Update, Delete 기능을 기본으로 함


# list에 element 추가하기 
    # append: element 하나를 list 끝에 추가
    # extend: list와 list를 연결
    # insert: 특정 index에 element 추가

# list에 element 1개 추가하기 : append()를 하면 항상 list의 길이가 1씩 증가. 하나의 덩어리 전체가 element로 추가되는 것
    # append(val)는 argument로 들어온 val을 리스트 끝에 element로 추가한다
    # method를 호출한 list가 직접 변경되며 ***새 리스트는 생성되지 않음***
a = [1, 2, 3]
print(a, len(a))    #[1, 2, 3] 3
b = a.append(4)
print(a, len(a), b)    #[1, 2, 3, 4] 4 None, b의 값이 None인 것으로부터 append() 메서드의 결과로 새로운 list가 생성되는 것이 아님을 알 수 있음 

# 빈 list에 새로운 값 추가하기 
b = []
print(b, len(b))    #[] 0
b.append(5)
print(b, len(b))    #[5] 1



# (중첩 list) list 안에 list 다시 추가하기 
a = [10, 20, 30]
a.append([40, 50])
print(a, len(a))    #[10, 20, 30, [40, 50]] 4, list의 길이가 (5가 아닌) 4임에 주의 
print(a[0], a[1], a[2], a[3])   #10 20 30 [40, 50], a[3]은 그 자체로 다시 list이다 



# list 확장하기 
# 추가해야 할 element가 여러 개인 경우 
    # extend(list): list 끝에 다른 list를 연결하여 list를 확장한다 (메서드를 호출한 리스트가 변경되며 새 리스트는 생성되지 않음) -> extend로 전달되는 list B의 element를 하나씩 반복하면서 기존의 list A에 추가하는 것, list - list 로 연결 (~ linked list)

a = [1, 2, 3]
a.extend([4,5])
print(a, len(a))    #[1, 2, 3, 4, 5] 5
print(a[0], a[1], a[2], a[3], a[4]) #1 2 3 4 5, 위와 다르게 이번에는 각 element를 각각 list에 추가한 것이므로 list a의 길이가 5이고 각 원소가 하나씩 출력할 수 있음을 확인할 수 있다 



# list의 특정 index에 element 추가하기 : insert(index, value) -> list[index] = value, element를 1개 추가하는 것으로, ***list의 길이가 1 늘어남***
    # insert(0, value): 리스트의 맨 처음에 value를 추가
    # insert(len(list), value): 리스트 끝에 value를 추가 -> append(value)와 같음

a = [1, 2, 3]
a.insert(2, 5)
print(a, len(a))    #[1, 2, 5, 3] 4, a[2] = 5를 추가하고 3은 a[3]으로 밀려남 
a.insert(0, 0)
a.insert(len(a), 9) #현재까지 list의 길이는 len(a)-1이므로 앞으로 추가할 element의 index는 len(a)와 같음 ~ a.append(9)  
print(a, len(a))    #[0, 1, 2, 5, 3, 9] 6

#중첩 list 만들기
a = [1, 2, 3]
a.insert(0, [7, 7])
print(a, len(a), a[0])    #[[7, 7], 1, 2, 3] 4 [7, 7]


#list 중간에 여러 개의 element 추가하는 방법은? -> slice 이용
a = [1, 2, 3]
a[1:2] = [7, 8]
print(a, len(a))    #[1, 7, 8, 3] 4 -> 2는 덮어씌워졌고 3은 뒤로 밀려남

#기존의 list의 element를 덮어쓰지 않고 element를 해당 위치에 추가하는 방법은? -> slice의 시작index와 끝index를 같게 지정하기
a = [0, 1, 2, 3]
a[2:2] = [9, 9, 9]
print(a, len(a))    #[0, 1, 9, 9, 9, 2, 3] 7




print('delete =====')
#list에서 element 삭제하기     
    # pop: 마지막 element 또는 특정 index의 element를 삭제한 뒤 해당 element의 값을 반환return
    # remove: 특정 값value을 찾아서 삭제

    # pop / del : index를 기준으로 삭제 
    # remove : value를 기준으로 삭제 

#특정 index의 element 삭제하기 
a = [0, 1, 2, 3]
print(a.pop(), a, len(a))   #3 [0, 1, 2] 3 

#원하는 index의 element를 삭제하려면...? -> pop(index), del 와 같은 비슷한 기능인데 del은 삭제기능만 있고 해당 값을 return 하지는 않는다
a = [0, 1, 2, 3]
val1 = a.pop(2)
print(val1, a, len(a))  #2 [0, 1, 3] 3
# val2 = del a[0] #SyntaxError: invalid syntax
del a[0]
print(a, len(a))    #[1, 3] 2

#list에서 특정 value를 찾아서 삭제하기 : remove(value), value가 해당 list에 있는 경우에만 가능 
a = [1, 2, 3]
b = a.remove(2)
# c = a.remove(5) #value값이 list에 없는 경우 - ValueError: list.remove(x): x not in list

    # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print(a, b)     #[1, 3] None, 재미있는 점은 remove를 하면서 새로운 변수에 이를 담도록 해도 에러가 발생하지 않는다는 점인데... 출력해보면 None, 즉 아무것도 담겨 있지 않다는 점이다...
# b = del a[0]    #간단히 비교해서 이건 안되잖아...? 사실 뭐 어떤 차이일지는 대충 예상이 된다...
# b = (del a[1])    #참고로 이렇게 괄호를 쳐도 SyntaxError 가 발생하는 것은 마찬가지로, 애초에 불가능한 syntax임을 알 수 있다
print(a.remove(1), a, len(a))   #None [3] 1
print(a.remove(3), a, len(a))   #None [] 0, 이로써 list a의 모든 원소를 삭제하였다


# 만약 같은 값이 여러 개인 경우 가장 처음의 값을 삭제한다
a = [1, 2, 3, 5, 3, 4, 3]
a.remove(3)
print(a, len(a))    #[1, 2, 5, 3, 4, 3] 6
a.remove(3)
print(a, len(a))    #[1, 2, 5, 4, 3] 5, 가장 앞의 3부터 차례대로 삭제됨을 확인



print('stack & queue =====')
#list로 stack / queue 만들기 
    #list의 메서드 중 append, pop을 사용하면 stack이 되고 append, pop(0)을 사용하면 queue로 사용할 수 있다
    #파이썬에서는 queue는 조금 더 효율적으로 사용할 수 있도록 덱DEQUE(Double Ended QUEue)라는 ***자료형을 제공한다 -> 덱은 양쪽 끝에서 data 추가/삭제 가 가능한 자료 구조 (~ doubly linked list)
    #deque(반복 가능한 객체)
    #appendleft, popleft ... (deque) ... append, pop 

from collections import deque   ## collections 모듈에서 deque를 가져옴
a = deque([1, 2, 3])
print(a, len(a))    #deque([1, 2, 3]) 3, 출력 자체가 deque라는 자료형으로 출력됨을 확인
b = a.append(5)
print(a, b)         #deque([1, 2, 3, 5]) None, 마찬가지로 append도 변수값에 저장할 수 있는데 아무 것도 없는 것으로... 결국 저장할 값이 아예 없어서 저장하지 않은 텅 빈 변수의 상태라고 할 수 있겠음 
c = a.popleft()
print(c, a)   #1 deque([2, 3, 5]) -> popleft()도 값을 return하고 이를 저장할 수 있음 




#list에서 특정 value의 index구하기 : index(value) - value가 위치한 index를 return 
#같은 값이 여러 개일 경우 가장 처음으로 위치한 index (가장 작은 index) return 
a = [0, 1, 2, 3, 2, 5, 3]
print(a.index(2), a.index(3), a.index(5))   #2 3 5

#특정 value의 개수 구하기 : count(value)
print(a.count(1), a.count(2), a.count(3), a.count(11))  #1 2 2 0

#list의 순서 뒤집기 : reverse()
print(a.reverse(), a, len(a))   #None [3, 5, 2, 3, 2, 1, 0] 7

#list 정렬하기 : sort() 
    # sort(), sort(reverse=False): list의 값을 작은 순서대로 정렬(오름차순)
    # sort(reverse=True): list의 값을 큰 순서대로 정렬(내림차순)
a = [0, 5, 3, 4, 2, 1]
a.sort()
print(a)    #[0, 1, 2, 3, 4, 5]
a.sort(reverse = True)
print(a)    #[5, 4, 3, 2, 1, 0]

#sort() vs sorted()
    #sort()는 list의 method이고 sorted()는 파이썬 전체의 내장함수이고, 둘 모두 정렬을 수행한다
    #차이점은? sort는 method를 사용한 해당 list를 변경, sorted는 정렬된 새로운 list를 생성
    #sort()는 원본 list를 변경해도 되고 space를 효율적으로 사용할 때, sorted()는 원본 list가 계속해서 필요한 경우 사용 (단, 새로운 변수를 하나 만들어 정렬된 list를 저장해야 함)

a = [3, 2, 5, 4, 1]
b = a.sort()
print(a, b)     #[1, 2, 3, 4, 5] None -> 원본 list a가 정렬되었고, sort() method가 아무 것도 return하지 않는 다는 것을 알 수 있음
c = [8, 10, 7, 9, 6]
d = sorted(c)
print(c , d)    #[8, 10, 7, 9, 6] [6, 7, 8, 9, 10], 원본 list c는 그대로이고, sorted() method가 return한 새로운 정렬된 list d가 생성된 것을 확인할 수 있음




print('clear() ====')
#list의 모든 element 삭제하기 : clear() / del list[:]
a = [1, 2, 3]
print(a, len(a))            #[1, 2, 3] 3
print(a, len(a), a.clear(), a, len(a)) #[] 3 None [] 0 ....????? 3이 나오는 이유는...?
    # clear()가 실행되는 것은 라인 단위로(파이썬의 특징이므로 당연...) 이루어지고 따라서 a의 모든 element들이 삭제될 것이라 예상할 수 있는데.... len(a)의 상태가...?
    # 일단은 clear()는 한 라인에서 독립적으로 수행하는 것으로....

# trivial check
b = [7, 7, 7]
b.clear()
print(b, len(b))    #[] 0, 일단 이것은 자명

# compare 2 different cases....
c2 = [9, 9, 9]
print(c2.clear(), c2, len(c2)) #None [] 0, 이것도 자명
c1 = [9, 9, 9]
print(c1, len(c1), c1.clear()) #[] 3 None, 그런데 이것은....?


#clear() 대신 del a[:] 와 같이 시작, 끝 index를 생략하여 list의 모든 element를 삭제할 수 있음
a = [1, 2, 3]
del a[:]
print(a)    #[]



#list를 slice로 조작하기 : list는 method를 사용하지 않고, slice로 조작할 수도 있다
a = [1, 2, 3]
a[len(a):] = [4, 5, 6]  #끝 index를 지정하지 않고(생략) element를 추가하면 해당 추가하는 개수만큼 알아서 들어간다. 이 경우에는 특별히 ***list의 범위를 벗어난 index도 사용할 수 있음*** 
print(a, len(a))        #[1, 2, 3, 4, 5, 6] 6

#위 작업은 a.extend([val1, val2, ...]) 와 동일, 값을 1개만 추가하는 경우는 a.append(value) 와 같음 (append는 무조건 원소의 개수가 1씩 증가하므로)
a.extend([7, 8])
print(a, len(a))    #[1, 2, 3, 4, 5, 6, 7, 8] 8



print('list empty check =====')
#list가 비어 있는지 확인하기 
    # 1) list의 길이로 확인하기
    # 2) list 객체 그 자체로 확인하기 -> 파이썬에서는 sequence 객체를 바로 조건문으로 판단하는 방법을 권장(PEP 8, Python Enhance Proposal)

# 1) length condition
seq = [1, 2, 3]
if not len(seq):
    print('seq is empty')
if len(seq):
    print('seq is not empty')   #seq is not empty

# 2) list object condition
seq = []
if not seq:
    print('seq is empty')   #seq is empty
if seq:
    print('seq is not empty')

#(에러가 발생하는 것을 막기 위해)조건문으로 list가 비어있는지 확인한 후 list의 마지막 element를 가져오기
seq = [1, 2, 3]
if seq:
    print(seq[-1])  #3
seq = []
if not seq:
    print('seq is empty')   #seq is empty
