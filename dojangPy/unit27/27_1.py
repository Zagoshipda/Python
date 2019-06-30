#unit 27. 파일 사용하기 
    # 문자열 string 을 파일에 읽고 쓰는 방법
    # ***파이썬 객체 object***를 파일에 읽고 쓰는 방법


# 파일에 문자열을 쓰고 읽기

#1) 파일에 문자열 쓰기 (write)
    # 파일객체 = open(파일이름, 파일모드)
    # 파일객체.write('문자열')
    # 파일객체.close()

f = open('./unit27/hello.txt', 'w')     #파일 객체 반환 (write mode)
f.write('hello world')                  #파일에 문자열 쓰기 
f.close()                               #파일 객체 닫기 




#2) 파일에서 문자열 읽기 (read)
    # 변수 = 파일객체.read()

f = open('./unit27/hello.txt', 'r')     #파일 객체 반환 (read mode)
s = f.read()                            #파일에서 문자열 읽기
print(s)    #hello world
f.close()                               #파일 객체 닫기 

#존재하지 않는 파일을 읽는 경우 
# f = open('./unit27/hi.txt', 'r')        #FileNotFoundError: [Errno 2] No such file or directory: './unit27/hi.txt'




#자동으로 파일 객체 닫기 : with as 를 사용하면 파일 객체를 자동으로 닫아준다 
    # with open(파일이름, 파일모드) as 파일객체:
    #     statement

with open('./unit27/hello.txt', 'r') as file:
    s = file.read()
    print(s)    #hello world



