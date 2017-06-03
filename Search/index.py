'''
Created on 21 Apr 2013

@author: Nikhil
'''

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    
def lookup(index,keyword):
    for entry in index:
        if entry[0] ==keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):    
    for word in content.split():
        add_to_index(index,word,url)
        

index = []
add_page_to_index(index, 'fake.test', "This is a test")
add_page_to_index(index, 'real.test', "This is not a test")
    
#print lookup(index,'is')        