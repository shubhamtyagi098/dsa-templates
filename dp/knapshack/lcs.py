import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

n = int(input())

def recur(l1, l2, l3):
	# base cases
	if  l1 < 0 or l2 < 0 or l3 < 0: # if string is empty can't have LCS with other strings s1 = "abc", s2 = "", s3 = "def"
		return 0
		
	if (l1, l2, l3) in memo:
		return memo[(l1, l2, l3)]
	
	if s1[l1] == s2[l2] == s3[l3]: # if last char mach lcs will be 1 + lcs with remaining strings
		return 1 + recur(l1 - 1, l2 -1, l3 - 1)
	
	ans = max(recur(l1, l2, l3 - 1), recur(l1 - 1, l2, l3), recur(l1, l2 - 1, l3))
	# if last char doesn't match we will check with all strings by 1 less index
	
	memo[(l1, l2, l3)] = ans
	
	return ans

for _ in range(n):
	s1, s2, s3 = input().split()

	l1, l2, l3 = len(s1), len(s2), len(s3)
	
	memo = {}
		
	print(recur(l1 - 1, l2 - 1, l3 - 1))
