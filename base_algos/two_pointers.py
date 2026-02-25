"""
Given an array of 𝑛
 integers 𝑎𝑖
. Let's say that the segment of this array 𝑎[𝑙..𝑟]
 (1≤𝑙≤𝑟≤𝑛) is good if the sum of elements on this segment is at most 𝑠.
Your task is to find the longest good segment.
"""

n, s = map(int, input().split())
nums = list(map(int, input().split()))

curr = l = 0

ans = 0 # keep two pointers one at right border which will add an element
		# one at left which will remove an element
for r in range(n):
	curr += nums[r] # Add initially an element
	
	while curr > s: # remove the element until the array is turned good
		curr -= nums[l]
		l += 1
	
	ans = max(ans, r - l + 1) # update the ans

print(ans)


"""
Given an array of 𝑛
integers 𝑎𝑖. Let's say that the segment of this array 𝑎[𝑙..𝑟]
(1≤𝑙≤𝑟≤𝑛) is good if the sum of elements on this segment is at least 𝑠. 
Your task is to find the shortest good segment.
"""

n, s = map(int, input().split())
nums = list(map(int, input().split()))

curr = l = 0

ans = float("inf")

for r in range(n):
	curr += nums[r] # Add initially an element
	
	while curr - nums[l] >= s: # even after removing the element if 
								# segment is good, we can reduce the size
		curr -= nums[l]
		l += 1
	
	if curr >= s: # initailly the curr can be less than s, but after the first good segment
				# we will not let the segement to not good
		ans = min(ans, r - l + 1)

print(ans if ans != float("inf") else -1)


"""
Given an array of 𝑛
integers 𝑎𝑖. Let's say that the segment of this array 𝑎[𝑙..𝑟]
(1≤𝑙≤𝑟≤𝑛) is good if the sum of elements on this segment is at most 𝑠. 
Your task is to find the number of good segments.
"""

n, s = map(int, input().split())
nums = list(map(int, input().split()))
 
curr = l = 0
 
ans = 0
 
for r in range(n):
	curr += nums[r]
	
	while curr > s:
		curr -= nums[l]
		l += 1
	
	ans += r - l + 1
 
print(ans)


"""
Given an array of 𝑛
integers 𝑎𝑖. Let's say that the segment of this array 𝑎[𝑙..𝑟]
(1≤𝑙≤𝑟≤𝑛) is good if the sum of elements on this segment is at least 𝑠. 
Your task is to find the number of good segments.
"""

n, s = map(int, input().split())
nums = list(map(int, input().split()))

curr = l = 0

ans = 0

for r in range(n):
	curr += nums[r]
	while curr - nums[l] >= s:
		curr -= nums[l]
		l += 1
	
	if curr >= s:
		ans += l + 1

print(ans)


"""
Given an array of 𝑛integers 𝑎𝑖. 
Let's say that a segment of this array 𝑎[𝑙..𝑟](1≤𝑙≤𝑟≤𝑛) is good 
if the difference between the maximum and minimum elements on this segment is at most 𝑘. 
Your task is to find the number of different good segments.

Input
The first line contains integers 𝑛 and 𝑘
 (1≤𝑛≤105, 0≤𝑘≤1018). 
 The second line contains integers 𝑎𝑖
 (1≤𝑎𝑖≤1018).
"""

from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

l = ans = 0

q_min, q_max = deque([]), deque([]) # queue which will maintain index of min and max elements of a segment


def add(r):
	while q_min and nums[q_min[-1]] >= nums[r]: q_min.pop() # pop until the last element in segment is less than nums[r]
	q_min.append(r) # append the new element
	
	while q_max and nums[q_max[-1]] <= nums[r]: q_max.pop() # pop until the last element in segment is greater than nums[r]
	q_max.append(r) # append the new element

def remove(l):
	while q_min and q_min[0] < l: q_min.popleft()
	while q_max and q_max[0] < l: q_max.popleft()

def good():
	return nums[q_max[0]] - nums[q_min[0]] <= k

for r in range(n):
	add(r)
	
	while not good():
		l += 1
		remove(l)

	ans += r - l + 1

print(ans)