"""
Given n, m board your task is to find in how many ways you can place k queens on the board
"""

n, m, k = map(int, input().split())
queens = [0] * n 


ans = 0

def check(row, col):
	if col == -1:
		return True
		
	for r in range(row):
		c = queens[r]
		if c == -1:
			continue
		
		if c == col or abs(r - row) == abs(c - col):
			return False
		
	return True


	
def generate():
	valid = []
	for i in range(n):
		v = []
		for j in range(m):
			if j == queens[i]:
				v.append("Q")
			else:
				v.append(".")
		valid.append(v)
	for item in valid:
		print("".join(item))

def solve(level):
	global ans
	if level == n:
		l = 0
		for q in queens:
			if q != -1:
				l += 1
		
		if l == k:
			ans += 1
			generate()
			return
		else:
			return
			
	for col in range(-1, m): # we can always place no queen on the board so check will always return True
		if check(level, col):
			queens[level] = col
			solve(level + 1)
			queens[level] = 0
	
solve(0)
print(ans)
