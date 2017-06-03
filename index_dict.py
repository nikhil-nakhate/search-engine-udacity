'''
Created on 24 Apr 2013

@author: Nikhil
'''

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    
def union(l1, l2):
    for b in l2:
        if (b not in l1):
            l1.append(b)
        return l1,l2;            
            
            
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]  #end quote is the index but we end the url at index-1
    return url, end_quote
            
def get_all_links(page):
    i = 0
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            if i ==0:
                links = [url]
                i = i+1
                page = page[endpos:]
            else:
                links.append(url)
                page = page[endpos:]
        else:
            break
    return links


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
        
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else: 
        return None
    
def add_page_to_index(index, url, content):    
    for word in content.split():
        add_to_index(index,word,url)
        
    
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            index.add_page_to_index(index, page, content)
            union(tocrawl,get_all_links(content))
            crawled.append(page)
    return index