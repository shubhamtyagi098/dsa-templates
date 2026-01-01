import sys
input = sys.stdin.readline

n , m = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
memo = {}

def func(i, w):
	# pruning
	# base check
	if i == n:
		return 0
	# cache check
	if (i , w) in memo:
		return memo[(i , w)]
	
	# transition
	skip = func(i + 1, w)
	
	take = 0
	if weights[i] <= w:
		take = values[i] + func(i + 1, w - weights[i])
	# save and return
	
	ans = max(skip, take)
	memo[(i , w)] = ans
	return ans 
	
def solve():
	print(func(0, m))
	
solve()
