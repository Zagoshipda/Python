#https://terzeron.com/wp/?p=771

import sys

def func():
    print(sys._getframe().f_code.co_name + "()")    #func()
    print(sys._getframe(0).f_code.co_name + "()")   #func()
    print(sys._getframe(1).f_code.co_name + "()")   #test()
    print(sys._getframe(2).f_code.co_name + "()")   #main()
    print(sys._getframe(3).f_code.co_name + "()")   #<module>()
    # print(sys._getframe(4).f_code.co_name + "()")   #ValueError: call stack is not deep enough
    # return

def test():
    func()

def main():
    test()

main()
