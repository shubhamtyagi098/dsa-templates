"""
This is solution to multi-source bfs problem, where we have to find the solution to the question below

Given multiple sources find the closet distance from any source to any destination.

5 8
########
#.A#A..#
#.##.#B#
#.B....#
########
"""

from collections import deque
n, m = map(int, input().split())

graph = []
dist = [[0 for _ in range(m)] for _ in range(n)]  # If questions ask you for distance, create a distance array
visited = [[False for _ in range(m)] for _ in range(n)]
parent = [[(-1, -1) for _ in range(m)] for _ in range(n)] # If question ask you for path, create a parent array and path array
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
src = []
dest = []

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
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "A":
                src.append((i, j))
            if graph[i][j] == "B":
                dest.append((i, j))
    
def inbound(new_x, new_y):
    return 0 <= new_x < n and 0 <= new_y < m

def bfs(src, dest):
    queue = deque(src)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            
            if inbound(new_x, new_y) and graph[new_x][new_y] != "#":
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
                    dist[new_x][new_y] = dist[x][y] + 1
                    parent[new_x][new_y] = (x, y)

def solve():
    find()
    for node in src:
        x, y = node 
        visited[x][y] = True
    bfs(src, dest)
    
    for it in dist:
        print(it)

    best = dest[0]
    for state in dest:
        if dist[state[0]][state[1]] < dist[best[0]][best[1]]:
            best = state 
    
    print(best)
    
solve()