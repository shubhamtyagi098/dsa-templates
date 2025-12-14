"""
This is a solution to https://maang.in/problems/Easy-Graph-Queries-400
"""

import sys
input = sys.stdin.readline

n, m, qu = map(int, input().split())

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
    
def union(x, y):
    x_p, y_p = find(x), find(y)
    
    if x_p == y_p: return False
    
    if size[x_p] > size[y_p]:
        x_p, y_p = y_p, x_p
        
    size[y_p] += size[x_p]
    parent[x_p] = y_p
    return True
    
def component(x, y):
    return find(x) == find(y)
    
for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)
    
for q in range(qu):
    temp = input().split()
    if temp[0] == "1":
        print(size[find(int(temp[1]))])
        
    else:
        o, x, y = map(int, temp)
        print("YES") if component(x, y) else print("NO")