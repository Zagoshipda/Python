# 30.2 키워드 인수argument 사용하기 

# 파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공 : 키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 (키워드=값) 형식으로 사용
# 키워드 인수를 사용하면 인수의 순서를 맞추지 않아도 키워드에 해당하는 값이 들어간다. 키워드 인수를 사용해서 순서를 지키지 않고 값을 넣을 수 있는 것. 

# syntax : function(keyword = value)


def personal_info(name, age, address):
    print('name: ', name, '/age: ', age, '/address: ', address)
    # print('age: ', age)
    # print('address: ', address)


personal_info('first', 1, 'korea')      #name:  first /age:  1 /address:  korea
personal_info(name = 'second', address = 'north', age = 2)  #name:  second /age:  2 /address:  north


# example of keyword argument : sep, end , 위 personal_info 함수의 호출과 비교해서 확인하기
print(10, 20, 30, sep = ':', end = '')  #10:20:30
