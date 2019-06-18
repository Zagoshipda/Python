# 36.2 상속 관계와 포함 관계 

#class 상속은 어떤 경우에 사용해야 하는가...? -> is-a relation 



#상속 관계 : is-a relation 
class Person:
    def greeting(self):
        print('Hello')

class Student(Person):
    def study(self):
        print('Study')



#포함 관계 : has-a relation

class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)

    def print_person(self):
        print(self.person_list)

kim = PersonList()
kim.append_person('john')
kim.print_person()      #['john']
kim.append_person('lee')
kim.append_person('park')
kim.print_person()      #['john', 'lee', 'park']
