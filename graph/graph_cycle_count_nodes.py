n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

col = [1 for i in range(n + 1)]
parent = [-1 for i in range(n + 1)]

is_cycle = False
any_cycle = []
count_cycle = [0 for i in range(n + 1)] # partial sum for the nodes
prefix_order = [] # prefix sum of the nodes

for i in range(m):
	u, v = map(int, input().split())
	graph[u].append(v)

def dfs(node):
	col[node] = 2
	
	for neigh in graph[node]:
		if col[neigh] == 1: # forward edge
			parent[neigh] = node
			dfs(neigh)
		elif col[neigh] == 2: # back edge, we found a cycle
			# To find the cycle we need the links to previous node explored
			# So we created parent array
			
			if not is_cycle: # here when the neighbour see the node again, we found the cycle, tbh is_cycle flag is not required here
				# node to neigh is a back edge node --> neigh
				temp = node # we need to find the neigh from node
				while temp != neigh:
					any_cycle.append(temp)
					temp = parent[temp]
				any_cycle.append(temp)
				any_cycle.reverse()
			
			count_cycle[node] += 1 # increase count of node
			count_cycle[parent[neigh]] -= 1 # decrease count of parent of neigh
			
		elif col[neigh] == 3: # doesn't matter
			pass
			
	col[node] = 3
	prefix_order.append(node) # the order the node get visited, is the order we do the prefix sum part
							  # why? cuz we want to process the node, before we process the neigh for prefix sum
							  # as node will get the final value and neigh value depends on the node value 
	

for node in range(1, n + 1):
	if col[node] == 1: 
		dfs(node)

print(*any_cycle)

for v in prefix_order:
	count_cycle[parent[v]] += count_cycle[v] # propagate the +1 from the node 

nodes_in_a_cycle = 0
for i in range(1, n + 1):
	if count_cycle[i] > 0: # that means that node is a part of a cycle
		nodes_in_a_cycle += 1

print(nodes_in_a_cycle)
