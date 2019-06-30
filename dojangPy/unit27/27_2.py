#27.2 문자열 여러 줄을 파일에 쓰기write, 읽기read


#1) 쓰기

#반복문으로 문자열 여러 줄을 파일에 쓰기 
with open('./unit27/hello2.txt', 'w') as file:
    for i in range(3):
        file.write('hello world {0} \n'.format(i))  #개행 문자 \n를 지정해주어야 줄바꿈. \n을 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장됨


#list에 들어 있는 string을 파일에 쓰기 
    # 파일객체.writelines(string list)

lines = ['hello \n', 'world \n', 'bye \n']  #writelines를 사용할 때에도 마찬가지로 \n을 붙여주어야 개행된다 -> hello2.txt 파일을 보면 bye다음 마지막 줄이 공백으로 남아있게 됨
# lines = ['hello \n', 'world \n', 'bye ']     #마지막 글자에 \n을 빼는 경우 ---> hello2.txt 파일에서 가장 마지막 공백 줄이 없도록 하기  
with open('./unit27/hello2.txt', 'at') as file:
    file.writelines(lines)




#2) 읽기

#파일의 내용을 1줄씩 list로 가져오기 : read는 파일의 내용을 읽어서 문자열로 가져오지만 readlines는 파일의 내용을 1줄씩 list 형태로 가져온다
with open('./unit27/hello2.txt', 'r') as file:
    lines = file.readlines()
    print(lines)    #['hello world 0 \n', 'hello world 1 \n', 'hello world 2 \n', 'hello \n', 'world \n', 'bye \n']


#파일의 내용을 1줄씩 읽기 
    #var = 파일객체.readline()

# while은 특정 조건이 만족할 때 계속 반복하므로 파일의 크기에 상관없이 문자열을 읽어올 수 있다
with open('./unit27/hello2.txt', 'r') as file:
    line = None     #None으로 초기화 
    # line = '' #이렇게 하면 안된다...? ---> 당연하지 아래 while 조건문이 line != '' 인데 여기서 걸리잖누... '' == '' 이니까 False 가 되어 조건을 만족하지 않아 while문을 바로 건너띄게 된다.... / line을 None이 아닌 ''로 초기화하면 처음부터 line != ''는 거짓이 되므로 반복을 하지 않고 코드가 그냥 끝나버린다
    while line != '':
        line = file.readline()
        # print(line, 'here', end = ' ')
        print(line.strip('\n'), 'striped')     #파일에서 읽어온 string에는 \n이 이미 들어있기 때문에 \n을 삭제하여 출력 -> print는 자동으로 개행을 하므로 (string자체를 조작하고 print의 기능은 default기능을 그대로 사용한 것)
        # print(line)     # -> 이렇게 string에서 \n을 삭제하지 않으면 2칸씩 띄워서 출력된다 
        # print(line, end = '')   #아니면 이렇게 print의 개항을 삭제하는 방법도 가능 (string자체는 그대로 둔 상태에서 print의 기능을 조작한 것) 
    
# hello world 0  striped
# hello world 1  striped
# hello world 2  striped
# hello  striped
# world  striped
# bye  striped
#  striped 

print('using None.... ')
with open('./unit27/hello2.txt', 'r') as file:
    line = None
    while line is not '':
        line = file.readline()
        print(line.strip('\n'), 'striped')

# hello world 0  striped
# hello world 1  striped
# hello world 2  striped
# hello  striped
# world  striped
# bye  striped
#  striped


print('using read() ===== ')
f = open('./unit27/hello2.txt', 'r') 
s = f.read()
print(s)
# hello world 0 
# hello world 1 
# hello world 2 
# hello 
# world 
# bye 
# (공백)


print('using for loop =====')
#for 반복문으로 파일의 내용을 줄 단위로 읽기 

with open('./unit27/hello2.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

# hello world 0 
# hello world 1 
# hello world 2 
# hello 
# world 
# bye 

print('end === ')



#파일 객체는 iterator이다 -> unpacking 가능 
file = open('./unit27/hello2.txt', 'r')
a, b, c, d, e, f = file
print(a, b, c, d, e, f, sep = '')

# hello world 0 
# hello world 1 
# hello world 2 
# hello 
# world 
# bye 
# (공백)

print('end ... ')
