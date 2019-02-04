# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:19:48 2019

@author: Lenovo
"""
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            try:
                queue.extend(graph[vertex])
            except KeyError:
                continue
    return visited
    
import json
graph={}
classes = set()
data = input()
for line in json.loads(data):
    classes.add(line['name'])
    if line['parents'] != []:
        for parent in line['parents']:
            if parent in graph.keys():
                graph[parent].append(line['name'])
            else:
                graph[parent] = [line['name']]
for cl in sorted(classes):
    a = bfs(graph, cl)
    print('{} : {}'.format(cl,len(a)))