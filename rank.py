'''
Created on 25 Apr 2013

@author: Nikhil
'''

#===============================================================================
# from index_dict import add_page_to_index
# from index_dict import add_to_index
# from index_dict import get_all_links
# from index_dict import get_next_target
# from index_dict import union
# from index_dict import get_page
#===============================================================================

from index_dict import *

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl,outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8     #damping factor 
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0/ npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))            
            newranks[page] = newrank
        ranks = newranks
    return ranks
        
index, graph = crawl_web('http://cs101.udacity.com/urank/index.html')
ranks = compute_ranks(graph)

print ranks