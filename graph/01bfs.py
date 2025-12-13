"""
Find the shortest path in below grid from upper left to lower right 0/1 bfs
where cost of going to a matching dir is 0 and in another dir in 1
3 6
LDRRRD
RDULDU
LDULRD
"""
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(input())

visited = [[False for _ in range(m)] for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
parent = [[(-1, -1) for _ in range(m)] for _ in range(n)]
hashmap = {
    (-1, 0): "U",
    (0, 1): "R",
    (1, 0): "D",
    (0, -1): "L"
}
    
def find_path(src, dest):
    x, y = dest
    path = [dest]
    
    while (x, y) != src:
        path.append(parent[x][y])
        x, y = parent[x][y]
    
    path.reverse()
    
    for i in range(1, len(path)):
        print(hashmap[(path[i][0] - path[i - 1][0], path[i][1] - path[i - 1][1])], end="")

def inbound(new_x, new_y):
    return 0 <= new_x < n and 0 <= new_y < m

def bfs(src, dest):
    queue = deque([src])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == dest:
            return True
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if inbound(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if hashmap[(dx[i], dy[i])] == graph[x][y]:
                    queue.appendleft((new_x, new_y))
                    dist[new_x][new_y] = dist[x][y]
                else:
                    queue.append((new_x, new_y))
                    dist[new_x][new_y] = dist[x][y] + 1
                parent[new_x][new_y] = (x, y)
    return False

def solve():
    src = (0, 0)
    dest = (n - 1, m - 1)
    
    visited[0][0] = True
    
    print(bfs(src, dest))
    print(dist)
    
    print(dist[dest[0]][dest[1]])
    find_path(src, dest)
    
solve()