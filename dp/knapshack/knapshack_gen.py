import sys
input = sys.stdin.readline

n , m = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
memo = {}
ans = []

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
	
def generate(i, w):
	if i == n:
		return
	
	else:
		donttake = func(i + 1, w)
		if w >= weights[i]:
			take = func(i + 1, w - weights[i]) + values[i]
			if take < donttake:
				generate(i + 1, w) # If don't take is lead to better ans don't take this object and move further
			else:
				ans.append(i)
				generate(i + 1, w - weights[i]) # else go to the next state
		else:
			generate(i + 1, w)
	
def solve():
	print(func(0, m))
	generate(0, m)
	print(ans)
	
solve()
