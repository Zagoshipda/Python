#27.3 python 객체를 파일에 저장하기, 가져오기 

    #pickling : python 객체를 파일에 저장하는 과정 
    #unpickling : python 객체를 읽어오는 과정 



#python 객체를 파일에 저장하기 : pickling 
import pickle
name = 'john'
age = 23
address = 'korea'
scores = {'korean': 9, 'english': 5, 'chinese': 8}
with open('./unit27/john.p', 'wb') as file:     #write binary file mode
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


#파일에서 python 객체 읽기 : unpickling
with open('./unit27/john.p', 'rb') as file:     #read binary file mode 
    #name, age, address, scores 순서로 저장했으므로 data를 가져올 때에도 같은 순서로 가져오면 된다
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name, age, address, scores)   #john 23 korea {'korean': 9, 'english': 5, 'chinese': 8}

