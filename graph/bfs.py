"""
This is a solution for problem Labyrinth on cses

https://cses.fi/problemset/result/15584780/
"""

from collections import deque
n, m = map(int, input().split())

graph = []
dist = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
parent = [[(-1, -1) for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

hashmap = {
    (-1, 0): "U",
    (0, 1): "R",
    (1, 0): "D",
    (0, -1): "L"
}

for _ in range(n):
    graph.append(input())
    
def find_path(src, dest):
    x, y = dest
    path = [dest]
    
    while (x, y) != src:
        path.append(parent[x][y])
        x, y = parent[x][y]
    
    path.reverse()
    
    for i in range(1, len(path)):
        print(hashmap[(path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])], end="")
        
    
def find():
    found_src = found_dest = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "A":
                src = (i, j)
                found_src = True
            if graph[i][j] == "B":
                dest = (i, j)
                found_dest = True
                
            if found_src and found_dest:
                return src, dest
    
def inbound(new_x, new_y):
    return 0 <= new_x < n and 0 <= new_y < m

def bfs(src, dest):
    queue = deque([src])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == dest:
            return True
        
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            
            if inbound(new_x, new_y) and graph[new_x][new_y] != "#":
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
                    dist[new_x][new_y] = dist[x][y] + 1
                    parent[new_x][new_y] = (x, y)
    
    return False

def solve():
    src, dest = find()
    x, y = src 
    visited[x][y] = True
    ans = bfs(src, dest)
    print("YES") if ans else print("NO")
    if ans:
        print(dist[dest[0]][dest[1]])
        find_path(src, dest)
    
solve()