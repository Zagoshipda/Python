#unit 39. 반복자Iterator : 값을 차례대로 꺼낼 수 있는 객체object 

#ex. for i in range(100):은 0부터 99까지 모든 숫자를 만들어내는 것이 아니라, 0부터 99까지 값을 차례대로 꺼낼 수 있는 iterator를 하나만 만들고 이후 반복할 때마다 iterator에서 숫자를 하나씩 꺼내서 반복하는 것.
# 이렇게 iterator를 사용하는 이유는...? -> 연속된 숫자를 미리 만들면 숫자가 적을 때는 상관없지만 숫자가 아주 많을 때는 메모리를 많이 사용하게 되므로 성능에도 불리. 그래서 파이썬에서는 iterator만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용 ---> 지연 평가(lazy evaluation) : 데이터 생성을 뒤로 미루는 방식


    #iterable은 __iter__ method로 iterator를 얻고, iterator의 __next__ method로 element를 하나씩 나아가면서 반복을 진행한다
    # -> iterable은 element를 한 번에 하나씩 가져올 수 있는 ***객체object이고, iterator는 __next__ method를 사용해서 차례대로 값을 꺼낼 수 있는 ***객체object 이다. iterable과 iterator는 서로 다른 별개의 객체이다. (iterable에서 __iter__ method로 iterator를 얻고 iterator에서 __next__ method로 반복할 수 있다)



#반복 가능한 객체Iterable : element가 여러 개 들어있고, 하나씩 꺼낼 수 있는 객체 
#객체가 iterable인지 확인하는 방법은...? 객체 안에 __iter__ method가 있는지 확인하면 된다
# -> 객체의 method확인하기 : dir(object)
print(dir([1, 2, 3]))   # -> object가 가지는 여러 method들 중에서 __iter__ 를 확인할 수 있고, 그 외에도 list에서 사용가능한 insert, pop, sort등의 method들을 확인할 수 있음 
print([1, 2, 3].__len__())  #3


x = [1, 2, 3]
#list에서 __iter__ method를 호출하면 iterator가 나온다 
print(x.__iter__)   #<method-wrapper '__iter__' of list object at 0x01C305D0>
print(x.__iter__()) #<list_iterator object at 0x01C322D0>

#iterator의 method 확인하기 
it = x.__iter__()
print(dir(it))  # -> __next__ method가 들어있음을 확인할 수 있다

#iterator의 __next__ method를 호출하면 element들을 차례로 꺼낼 수 있다
print(it.__next__)      #<method-wrapper '__next__' of list_iterator object at 0x008522B0> ---> method-wrapper...?
print(it.__next__())    #1
print(it.__next__())    #2
print(it.__next__())    #3
# print(it.__next__())    #StopIteration 예외 발생, 반복 종료 



#range() 에서 __iter__로 iterator를 얻어낸 뒤 __next__ method 호출해보기 
    #list, string, dictionary, set -> element가 직접적으로 존재하는 iterable 
    #range(n) -> element를 확인할 수는 없으나, 마찬가지로 지정된 숫자 n만큼 element를 꺼내서 반복할 수 있음 
it = range(3).__iter__()
print(it.__next__())    #0
print(it.__next__())    #1
print(it.__next__())    #2
# print(it.__next__())    #StopIteration





#for와 iterable object : for loop에 iterable object를 사용했을 때의 동작 과정은...? 
    #range(n)을 사용한다고 가정하자
    #1) 우선 range에서 __iter__로 iterator를 얻는다
    #2) for loop을 반복할 때마다 iterator에서 __next__ method로 element(숫자)를 하나씩 꺼내서 loop 변수에 저장한다
    #3) 계속해서 반복하다가 마지막이 되어 __next__ method를 호출하면 StopIteration 에러가 발생하면서 반복을 종료한다 


    #range()와 같은 경우 iterable과 iterator가 분리되어 있지만 클래스에 __iter__와 __next__ 메서드를 모두 구현하면 직접 iterator를 만들 수 있다.
    #특히 __iter__, __next__ method를 가진 객체를 iterator protocol 을 지원한다고 말한다.




#sequence 객체와 iterable 객체 비교
    #iterable > sequence : iterable 은 sequence 를 포함한다
    #element의 순서가 정해져 있고 연속적으로 이어져 있으면 sequence 객체, element의 순서와는 상관없이 element를 한 번에 하나씩 꺼낼 수 있기만 하면 sequence는 아니지만 iterable 은 된다

    #list, tuple, range, string -> sequence object 
    #dictionary, set -> iterable, NOT a sequence object ---> sequence 객체는 element의 순서가 정해져 있고 연속적(sequence)으로 이어져 있어야 하는데, dictionary와 set는 element/key의 순서가 정해져 있지 않기 때문


