'''
Created on 21 Apr 2013

@author: Nikhil
'''
def find_element(p, t):
    i = 0
    for e in p:
        if (e == t):
            print i
            return i
        i = i+1
    return -1

find_element([1,2,3], 3)

def find_element_in(p, t):
    if (t in p):
        print p.index(t)
        return p.index(t)
    else:
        print -1
        return -1

find_element_in([1,2,3,4,5,5],0)

def union(l1, l2):
    for b in l2:
        if (b not in l1):
            l1.append(b)
    
    return l1,l2;

print(union([1,2,3], [2,4,6]))
        