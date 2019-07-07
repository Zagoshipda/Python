#class method vs static method 


# https://suwoni-codelab.com/python%20%EA%B8%B0%EB%B3%B8/2018/03/11/Python-Basic-class-staticmethod/



class Lang:
    default_lang = 'english'

    def __init__(self):
        self.show = 'my lang is ' + self.default_lang

    @classmethod
    def class_my_lang(cls):
        return cls()

    @staticmethod
    def static_my_lang():
        return Lang()
    
    def print_lang(self):
        print(self.show)

class KoreanLang(Lang):
    default_lang = 'korean'


a = KoreanLang.static_my_lang()
b = KoreanLang.class_my_lang()

a.print_lang()  #my lang is english
b.print_lang()  #my lang is korean


