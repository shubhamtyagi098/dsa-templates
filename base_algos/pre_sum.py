import sys
input = sys.stdin.readline

n , k = map(int, input().split())
nums = list(map(int, input().split()))

pre = [0] * (n + 1)

for i in range(n):
	pre[i + 1] = nums[i] + pre[i]

for i in range(k):
	l, r = map(int, input().split())
	l, r = l - 1, r - 1
	print(pre[r + 1] - pre[l])
	
