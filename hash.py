'''
Created on 23 Apr 2013

@author: Nikhil
'''

from index import *

def make_string(p):
    s = ""
    for e in p:
        s = s+e
    return s
        
def make_big_index(size):
    index = []
    letters =['a','a','a','a','a','a','a','a']
    while len(index) <size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i])+1)
                break
            else:
                letters[i] = 'a'
    return index
    
def bad_hash_string(keyword, buckets):
    return ord(keyword[0]) %buckets
    
def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results
    
def hash_string(keyword, buckets):
    h = 0
    for l in keyword:
        h = (h + ord(l)) % buckets
    return h 

def make_hash_table(n):
    table = []
    for unused in range(0, n):
        table.append([])
    return table

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key,value])
    
def hashtable_lookup(htable, key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
    
def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])
    



    
    
    
    
    
    
    
    