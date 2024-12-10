# one.py
print('one.py')

import __main__
from two import Fun 

if __name__ == '__main__':
    print('one.py is __main__ operation')
else:
    print('one.py imported')
    print('one.py is NOT __main__ OPERATION')
    

print('------------------------------')

print(__name__)
print(__main__)

print('------------------------------')

def fun():
    print('fun() from one.py')

print('Top level in one.py')

print('------------------------------')

Fun()

print('------------------------------')

fun()

print('______________________________')