from collections import deque
q = deque([0])      # initiates a queue
q.popleft()         # pops the first element
q.append(0)         # pushes a element to end of queue

import sys
sys.setrecursionlimit(1000000) # default is 1000.

from itertools import permutations, combinations, product
a = 'ABCD'
premutations(a,2) == ['AB','AC','AD','BA','BC','BD',
        'CA','CB','CD','DA','DB','DC']
combinations(a,2) == ['AB','AC','AD','BC','BD','CD']
combinations_with_replacement(a,2) == \
        ['AA','AB','AC','AD','BB','BC','BD','CC','CD','DD']
product(a,2) == ['AA','AB','AC','AD','BA','BB','BC','BD',
        'CA','CB','CC','CD','DA','DB','DC','DD']

#If a specified output, o, should be outputed with x decimals:
print '\%.xf' % o
#For example
print '\%.4f' % 2.05
print '\%.4f' % 3.1415926535
#gives us 2.0500, 3.1416
