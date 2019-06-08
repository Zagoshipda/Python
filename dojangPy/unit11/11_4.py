# 11.4 슬라이스 Slice 사용하기
# sequence slice - sequence object의 일부분을 잘라냄



# arr[i:j] takes element arr[i...j-1], list의 일부분을 잘라내어 새로운 list를 만든다 (index는 0부터 시작, 마지막 index는 포함하지 않음)
a = [0, 1, 2, 3, 4, 5, 6, 7]
b = a[0:4]          #a = a[0...3]
print(b, len(b))    #[0, 1, 2, 3] 4
print(b[0:0], b[1:2])   #[] [1]

#음수 index 사용하기 
print(a[3:-2])      #[3, 4, 5]


# index 증가폭 지정 (값이 아닌 index에 해당하는 위치의 element를 가져옴에 착각하지 않기)
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[2:7:2], a[2:9:3])   #[2, 4, 6] [2, 5, 8]


# index 생략 하기: 
    #시작 index를 생략하면 리스트의 처음index 부터 마지막index-1 까지를 가져올 수 있음
    #마찬가지로 끝 index를 생략하면 시작index 부터 마지막index 까지를 가져옴
    #둘 다 생략하면 전체를 가져옴

print(a[:6], a[3:])     #[0, 1, 2, 3, 4, 5] [3, 4, 5, 6, 7, 8, 9]
print(a, a[:])          #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#index 생략 + 증가폭 동시에 사용하기 
print(a[4::2], a[:8:3], a[::3]) #[4, 6, 8] [0, 3, 6] [0, 3, 6, 9]

# a, a[:], a[::] 3가지는 모두 list 전체를 나타냄 (시작index, 끝index, index증가폭 모두 생략하는 경우)
print(a[::])            #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



#slice의 index 증가폭을 음수로 지정하기 : index 증가폭을 음수로 지정하면 element를 뒤에서부터 가져옴
# -> index가 감소하므로 끝 index 보다 시작 index를 더 크게 지정해야 함
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[8:2:-1], a[8:2:-2])    #[8, 7, 6, 5, 4, 3] [8, 6, 4], 마찬가지로 마지막 index인 2는 포함하지 않다는 것에 주의 
print(a[::-1])      #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], index의 범위를 지정하지 않고 증가폭만 -1로 지정하면 리스트를 반대로 뒤집는 것과 같음 




#len 응용하기 - list 전체 가져오기 
print('using len() -----')
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[0:len(a)], a[:len(a)])  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



#tuple, range, 문자열string에 slice 사용하기 
# tuple[시작인덱스:끝인덱스:인덱스증가폭]
b = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9    #()를 붙이지 않아도 tuple로 인식함 
print(b[3:7], b[6:], b[:4], b[3:10:2])         #(3, 4, 5, 6) (6, 7, 8, 9) (0, 1, 2, 3) (3, 5, 7) 


#range에 슬라이스를 사용하면 지정된 범위의 숫자를 생성하는 ***range 객체를 새로 만든다
#바로 list를 생성하는 것이 아닌 range객체를 만든다는 것에 주의 
r = range(10)
print(r, r[4:8], r[6:], r[:8:2])    #range(0, 10) range(4, 8) range(6, 10) range(0, 8, 2)

#list를 만드려면 range객체를 list의 argument로 전달해야 함
l1 = list(r[:8:2])
l2 = tuple(r[:8:2])
print(l1, l2)    #[0, 2, 4, 6] (0, 2, 4, 6)


#문자열은 문자 하나가 요소이므로 문자 단위로 잘라서 새 문자열을 만든다
hello = 'Hello world!'
print(len(hello), hello[2:7], hello[::2])   #12 llo w Hlowrd


#slice 객체 사용하기 
#slice 객체를 사용하여 sequence object(시퀀스 자료형으로 만든 변수)를 잘라낼 수도 있음
    # 슬라이스객체 = slice(시작인덱스, 끝인덱스, 인덱스증가폭)
    # 시퀀스객체[슬라이스객체]
    # 시퀀스객체.__getitem__(슬라이스객체)
    # 시퀀스 객체의 [ ] 또는 __getitem__ 메서드에 slice 객체를 넣어주면 지정된 범위만큼 잘라내서 새 객체를 만들 수 있다
seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sl = slice(3, 9, 2)
print(seq[sl])              #[3, 5, 7], 새로운 list객체 생성
print(seq.__getitem__(sl))  #[3, 5, 7]
print(range(10)[sl], range(10).__getitem__(sl)) #range(3, 9, 2) range(3, 9, 2), 새로운 range객체 생성



print('assign values using slice =====')
#slice에 element 할당하기 : sequence 객체는 slice로 범위를 지정하여 여러 요소에 값을 할당할 수 있음 
#단, tuple, range, 문자열은 slice 범위를 지정하더라도 element를 할당할 수 없음 (TypeError: 'tuple' /'range' / 'str' object does not support item assignment)

    # 시퀀스객체[시작인덱스:끝인덱스] = sequence 객체
    # 범위를 지정해서 element를 할당하는 경우 기존의 list가 변경되는 것으로, 새로운 list가 생성되지 않음
    # element의 개수를 정확하게 맞추지 않아도 알아서 할당된다: 할당할 element 개수가 더 많으면 그만큼 list의 element가 늘어나고, 반대로 개수가 적으면 list의 element 개수도 줄어든다
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5] = ['a', 'b', 'c']
print(a, len(a))    #[0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9] 10
a[2:4] = ['d', 'e', 'f', 'g']
print(a, len(a))    #[0, 1, 'd', 'e', 'f', 'g', 'c', 5, 6, 7, 8, 9] 12
a[2:6] = ['ZZZ']
print(a, len(a))    #[0, 1, 'ZZZ', 'c', 5, 6, 7, 8, 9] 9 

#증가폭을 지정하여 index를 건너뛰면서 할당하기 -> ***index증가폭을 지정했을 때는 슬라이스 범위의 element 개수와 할당할 element 개수가 정확히 일치해야 한다
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[2:9:2] = ['a', 'a', 'a']  # ValueError: attempt to assign sequence of size 3 to extended slice of size 4
a[5:10:2] = ['a', 'a', 'a']
print(a, len(a))    #[0, 1, 2, 3, 4, 'a', 6, 'a', 8, 'a'] 10




#del로 슬라이스slice 삭제하기 
    # del 시퀀스객체[시작인덱스:끝인덱스]
    # del로 element를 삭제하면 원래 있던 리스트가 변경되며 새 리스트는 생성되지 않음 
    # tuple, range, 문자열은 del로 slice를 삭제할 수 없음 (TypeError: 'tuple'/ 'range'/ 'str' object does not support item deletion)
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[3:6]
print(a)    #[0, 1, 2, 6, 7, 8, 9]
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[2:9:2]    #증가폭 지정해서 element 삭제하기 
print(a)    #[0, 1, 3, 5, 7, 9]
