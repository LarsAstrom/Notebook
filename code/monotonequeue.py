'''
Keeps a monotone queue (always increasing or decreasing).
This is good for solving "What is the smallest (largest) 
element in the window of size L in an array. This is done
by in each step calling add and remove on the monotone queue
and also looking at the smallest (largest) element which
is at position 0.

Time-Complexity: O(n), n is the size of the array.
Space-Complexity: O(n).
'''
from collections import deque
def minadd(mminque,x):
    while mminque and x < mminque[-1]:
        mminque.pop()
    mminque.append(x)

def minremove(mminque,x):
    if mminque[0] == x:
        mminque.popleft()

def maxadd(mmaxque,x):
    while mmaxque and x > mmaxque[-1]:
        mmaxque.pop()
    mmaxque.append(x)

def maxremove(mmaxque,x):
    if mmaxque[0] == x:
        mmaxque.popleft()
