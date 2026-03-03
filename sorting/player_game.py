"""
Achieve target Sum
1. Problem
There are N cards with scores Ai and Bi written on them, representing scores for players PA and PB, respectively.
Two players, PA and PB, take turns picking cards, adding the value on the card to their total score.
The goal is to maximize the difference between the total scores of the two players (SA - SB), where SA and SB represent the total scores of players PA and PB, respectively.

"""

from functools import cmp_to_key

n = int(input())
nums = []

def compare(a, b):
	if a[0] + a[1] > b[0] + b[1]:
		return -1
	elif b[0] + b[1] > a[0] + a[1]:
		return 1
	else:
		return 0

for _ in range(n):
	nums.append(list(map(int, input().split())))

nums.sort(key=cmp_to_key(compare))
pa = 0
pb = 0
for i in range(n):
	if i % 2 == 1:
		pa += nums[i][0]
	else:
		pb += nums[i][1]
		
print(pa - pb)


"""
Explanation:

Initial State:

Initially, all cards are with player PB (Player B).
Total score of player PA (Player A), SA = 0.
Total score of player PB, SB = sum of scores of all cards held by player PB.
Calculation of SA - SB:

SA - SB represents the difference between the total scores of player PA and player PB.
In the initial state, SA - SB = - sum of scores of all cards held by player PB. This is because SA is 0 initially, and SB is the sum of scores of all cards.
Transition from Player B to Player A:

If we choose to transfer the jth card from player PB to player PA:
SA becomes Aj (score of the jth card).
SB becomes the sum of scores of all cards - the score of the jth card (sum of Bi - Bj).
The change in SA - SB due to this transition becomes Aj + Bj - sum of scores of all cards.
Maximizing SA - SB:

The goal is to maximize the difference SA - SB, as this represents the advantage of player A over player B.
To achieve this, we sort the cards based on the sum of their scores (Aj + Bj) in non-increasing order.
By doing so, we ensure that the cards that contribute the most to increasing SA - SB (i.e., Aj + Bj - sum of scores of all cards held by player PB) are picked first.
Picking Cards:

After sorting the cards, we pick them one by one, transferring them from player PB to player PA in the order determined by the sorting.
Each card transferred contributes to increasing the difference SA - SB by its score difference (Aj + Bj - sum of scores of all cards held by player PB).
By picking cards in this manner, we maximize the advantage of player A over player B.

"""
