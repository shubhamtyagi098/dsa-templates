"""
let suppose there are n intervals for n people in a room.
Find the sum of hours where more than k peoples are available in room.
"""

n, k = map(int, input().split())

events = [] # will contain [event time, +1/-1] 

for i in range(n):
	l, r = map(int, input().split())

	events.append([l, +1]) # person enter at this time so +1
	events.append([r, -1]) # person left at this time so -1

events.sort()


count = 0
ans = 0

n = len(events) # we have modified the num of event so redefining it will be 2 * n

for i in range(n):
	count += events[i][1] # whether person entered or left the room.
	if i + 1 < n and count >= k: # if there are more events and people are more than k. Record the ans
		ans += events[i + 1][0] - events[i][0]

print(ans)
