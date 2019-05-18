# 9.1 문자열 사용하기 


# 문자열을 만드는 다양한 방법들 
print('Hello World')
print("Hello World")
print('''Hello World''')
print("""Hello World""")

# multiline string 
string = '''Hello World
    continue...
        Bye World'''
print(string)

string2 = """Hello World2
    continue...
        Bye World2"""
print(string2)

# using ' and " among string 작은따옴표나 큰따옴표가 포함된 문자열 사용하기
s = "Python isn't difficult"
print(s)
s = 'he said "Python is easy"'
print(s)

# 작은따옴표 안에 작은따옴표를 넣거나 큰따옴표 안에 큰따옴표를 넣을 수는 없음 (syntax error)
# s = 'python isn't difficult'
# s = "he said "Python is easy""

# 그러나 여러 줄로 된 문자열은 작은따옴표 안에 작은따옴표와 큰따옴표를 둘 다 넣을 수 있다. 또한, 큰따옴표 안에도 작은따옴표와 큰따옴표를 넣을 수 있다

s = """"Hello" 'hi'"""
print(s)
# s = '''"Hello" 'hi''''  #SyntaxError: EOL while scanning string literal
s = '''"Hello" 'hi' ''' # '가 연속적으로 너무 많이 나오면 syntax error가 뜨는 듯 
print(s)
s = ''' "Hello"
'hi'
'''
print(s)

# using escape(\) to express ' and "" in '...' and "..." 
t = 'python isn\'t difficult'
print(t)
t = "he said \"python is easy\""
print(t)

# 따옴표 3개로 묶지 않고 여러 줄로 된 문자열 사용하기 -> using \n
# cf) 원리 - 따옴표 3개로 묶어서 여러 줄로 된 문자열을 만들면, 줄바꿈이 되는 부분에 \n이 들어있는 것처럼 처리하는 것
print('Hello\nPython')
print('''Hello
Python''')
# 스크립트에서 print하지 않고 문자열 그대로 출력하면 
# >>> '''Hello
# Python'''
# 'Hello\nPython'   -> 이렇게 \n가 결과로 나오는 것을 확인할 수 있다 
