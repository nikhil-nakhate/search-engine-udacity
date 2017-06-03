'''
Created on 23 Apr 2013

@author: Nikhil
'''
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time
    
def spin_loop(n):
    i = 0
    while(i < n):
        i = i+1