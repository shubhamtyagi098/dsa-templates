"""
For given array of 0's and 1's find the first occurance of 1

python3 bin_s.py 
4                  
0 0 1 1
2

python3 bin_s.py

10
0 0 0 0 0 1 1 1 1 1
5
"""

n = int(input())
nums = list(map(int, input().split()))

l, r = -1, n

while l + 1 < r:
	m = (l + r) // 2
	
	if nums[m] == 1:
		r = m
	else:
		l = m

print(r)



"""
In array of of 1 and 0, find the index of 1 just before 0.

python3 bin_s.py
10 
1 1 1 1 1 0 0 0 0 0
4
"""


n = int(input())
nums = list(map(int, input().split()))

l, r = -1, n

while l + 1 < r:
	m = (l + r) // 2
	
	if nums[m] == 1:
		l = m
	else:
		r = m

print(l)




"""
Question find the first value greater than equals target.

This is just converting the array in 0's followed by 1. and finding that good value at first one

target 6 in below array

Array 1 2 3 5 7 11 14 15 
      0 0 0 0 1 1   1  1
"""
n = int(input())
nums = list(map(int, input().split()))
target = int(input())

l, r = -1, n

"""
equations:
l < a[i] <= r
"""

while l + 1 < r:
	m = (l + r) // 2
	if nums[m] >= target: # when this condition hold true it's like 1, 1, 1, 1.... 1 and we are just finding the first one
		r = m
	else: # and here it will just be 0, 0, 0, 0, ... 0
		l = m

print(r)


"""
find the first value which is greater than target

python3 bin_s.py
8     
1 2 3 5 7 11 14 15
11
6
"""

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

l, r = -1, n

"""
l <= a[i] < r
"""

while l + 1 < r:
	m = (l + r) // 2
	
	if nums[m] <= target: # if value is less than target i.e. 0 0 0 0...... we just move the left pointer
		l = m
	else:
		r = m # if it is 1 move right pointer

print(r) # return right point


"""
Given an rotated array determine how many times it was rotated

[4 5 6 1 2 3]

ans is 3

what if we don't see these as numbers as decimal numbers but as 0's and 1's, where I'm thinking element 
in first part of array as 0 and second part as 1. Than I just have to find the first occurence of 1

python3 bin_s.py
6
4 5 6 1 2 3
3
"""


n = int(input())
nums = list(map(int, input().split()))

l, r = -1, n

"""
l <= a[i] < r
"""

def good(x):
	return x <= nums[0] # we need to find the element smaller than first element

while l + 1 < r:
	m = (l + r) // 2
	
	if good(nums[m]):
		r = m
	else:
		l = m

print(r)


"""
In bitonic array find the peak

1 2 3 4 5 6 7 8 9 4 3 2 1

again if we see these as 0's and 1's, we have have two groups. 
where one group has relation a[i] < a[i + 1] and a[i] > a[i + 1]. 

We will make first group as 0 and second as 1
"""

n = int(input())
nums = list(map(int, input().split()))

l, r = -1, n

"""
l <= a[i] < r
"""

def good(m):
	if m + 1 >= n or nums[m + 1] <= nums[m]: # first boundary condition check if element is last element
		                                    # then second condition verify if it belongs to second group
		return True
	
	return False

while l + 1 < r:
	m = (l + r) // 2
	
	if good(m):
		r = m
	else:
		l = m

print(r)
