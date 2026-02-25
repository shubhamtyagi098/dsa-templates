import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, qu = map(int, input().split())

nums = list(map(int, input().split()))

queries = list(map(int, input().split()))
memo = {}
sol = []

def func(level, target):
	if target == 0:
		return 1
	
	if target < 0 or level == n:
		return 0
	
	if (level, target) in memo:
		return memo[(level, target)]
	
	ans = 0
	
	donttake = func(level + 1, target)
	
	take = func(level + 1, target - nums[level])
	
	ans = max(donttake, take)
	
	memo[(level, target)] = ans
	
	return ans


def compute(level, target):
	if level == n or target == 0:
		return
	
	donttake = func(level + 1, target)
	if donttake:
		compute(level + 1, target)
		return
	
	take = func(level + 1, target - nums[level])
	if take:
		sol.append(nums[level])
		compute(level + 1, target - nums[level])

def solve(target):
	return func(0, target)

for q in queries:
	sol = []
	res = solve(q)
	print(1 if res else -1)
	if res:
		compute(0, q)
	if res:
		print(sol)
