n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

col = [1 for i in range(n + 1)]
parent = [-1 for i in range(n + 1)]

# Note: For undirected graphs, we don't even need 3 colors.
# visited/unvisited + parent tracking is sufficient since there are no cross edges.

is_cycle = False
any_cycle = []

for i in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)

def dfs(node):
	global is_cycle
	col[node] = 2
	
	for neigh in graph[node]:
		if is_cycle:
			return
		if neigh == parent[node]: # skip the edge back to parent, not a real cycle for A <--> B
			continue
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
