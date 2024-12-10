# two.py
print('two.py')

import __main__

if __name__ == '__main__':
    print('two.py is __main__ operation')
else:
    print('two.py imported')
    print('two.py is NOT __main__ OPERATION')

print('------------------------------')

print(__name__)
print(__main__)

print('------------------------------')

def Fun():
    print('fun() from two.py')

print('Top level in two.py')

print('______________________________')