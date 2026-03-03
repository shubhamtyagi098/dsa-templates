from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque([])

ans = []

def add(i):
	while queue and nums[queue[-1]] > nums[i]:
		queue.pop()
	queue.append(i)
	
def remove(i):
	if queue[0] == i:
		queue.popleft()

for i in range(k):
	add(i) # Note here the minimum of the window is not just one element i.e. the minimum element
			# When window moves. second element can be the minimum as well. And we will lose that
			# if we add only the minimum on the queue. so store all the minimum and get the ans for
			# the first window.

ans.append(nums[queue[0]])

for r in range(k, n):
	add(r)
	remove(r - k)
	ans.append(nums[queue[0]])

print(ans)
