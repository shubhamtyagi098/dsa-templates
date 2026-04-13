n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

col = [1 for i in range(n + 1)]
parent = [float('inf') for i in range(n + 1)]

is_cycle = False
any_cycle = []

for i in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)

def dfs(node):
	global is_cycle
	col[node] = 2
	
	for neigh in graph[node]:
		if is_cycle:
			return
		if col[neigh] == 1: # forward edge
			parent[neigh] = node
			dfs(neigh)
		elif col[neigh] == 2: # back edge, we found a cycle
			# To find the cycle we need the links to previous node explored
			# So we created parent array
			# node to neigh is a back edge node --> neigh
			temp = node # we need to find the neigh from node
			while temp != neigh:
				any_cycle.append(temp)
				temp = parent[temp]
			any_cycle.append(neigh)
			any_cycle.reverse()
			is_cycle = True
			return
			
	col[node] = 3
	

for node in range(1, n + 1):
	if col[node] == 1: 
		dfs(node)

print(*any_cycle)
