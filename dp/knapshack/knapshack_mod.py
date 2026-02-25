import sys
input = sys.stdin.readline

n , m, k = map(int, input().split())
weights = list(map(int, input().split()))
values = list(map(int, input().split()))
memo = {}
ans = []

def func(i, w, lasttaken, k):
	# pruning
	# base check
	if i == n and k == 0: # k is the num of items we are allowed to take
		return 0
	# cache check
	if (i , w, lasttaken, k) in memo:
		return memo[(i , w, lasttaken, k)]
	
	# transition
	skip = func(i + 1, w, 0, k)
	
	take = 0
	if weights[i] <= w and not lasttaken: # lasttaken to keep track of previous item was taken or not.
		take = values[i] + func(i + 1, w - weights[i], 1, k - 1)
	# save and return
	ans = max(skip, take)
	memo[(i , w, lasttaken, k)] = ans
	return ans
	
	
def solve():
	print(func(0, m, 0, k))
	print(ans)
	
solve()
