#22.2 list의 할당과 복사 

#할당과 복사의 공통점과 차이점은...?


#1) 할당
a = [1, 2, 3, 4, 5]
b = a
print(a is b)   #True -> list a 와 b 는 서로 같은 객체object
b[2] = 9
print(a, b, a is b)     #[1, 2, 9, 4, 5] [1, 2, 9, 4, 5] True

#2) 복사
c = a.copy()
print(a, c, a is c)     #[1, 2, 9, 4, 5] [1, 2, 9, 4, 5] False -> list a 와 c 는 서로 다른 object



# == 와 != 는 값 자체를 비교하고 is, is not 은 객체object를 비교함
# is 비교를 통해 a와 b는 같은 객체이지만 c는 a, b 와는 다른 객체 라는 것을 알 수 있다
print(a is b, a is c, a == b, a == c, b == c)   #True False True True True -> c의 값을 변경하기 전에는 복사된 element들의 값이 모두 같으므로 ==로 비교하면 true
c[0] = -1
print(a, b, c)  #[1, 2, 9, 4, 5] [1, 2, 9, 4, 5] [-1, 2, 9, 4, 5]
print(a is b, a is c, a == b, a == c, b == c)   #True False True False False -> c의 값을 변경한 후에는 ==로 비교하면 false

