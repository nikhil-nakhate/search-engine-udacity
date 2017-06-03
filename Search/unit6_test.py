'''
Created on 24 Apr 2013

@author: Nikhil
'''

def is_palindrome(word):
    if word =='':
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
    
    
def fibo(n):                                                        #recursive = costly dynamic trial
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        if fibo[n] ==None:
            fibo[n] = fibo(n-1) + fibo(n-2)
            return fibo[n]
        else: 
            return fibo[n]
        
def fibonacci(n):                                               #iterative def less costly
    curr = 0
    nextfib = 1
    for unused in range(0, n):
        curr, nextfib = nextfib, (curr+nextfib)
    return curr
            
            
print(fibonacci(3))