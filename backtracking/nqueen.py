n = int(input())
	
queens = []

def check(level, col):
	for row in range(level):
		c = queens[row]
		if c == col or abs(row - level) == abs(col - c): 
			return False
	
	return True

def solve(level):
	# when all rows are explored or I reached past the last row. 
	# record the ans return from there.
	if level == n:
		ans += 1
		return
	
	# this code try to place a queen, when it find the a valid spot. It will 
	# place a queen and move to the next column. until it reaches beyond the 
	# last row. then it will unplace the last placed queen and try to place
	# it in some other next columns. If it can, else it will return and go back
	# and unplace the last queen and try to place in some other column in the same 
	# row if it can.
	for col in range(n):
		if check(level, col):
			queens.append(col)
			solve(level + 1)
			queens.pop()
	
solve(0)
