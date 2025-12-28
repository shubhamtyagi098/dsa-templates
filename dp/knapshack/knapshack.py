n, m = map(int, input().split())

prices = list(map(int, input().split()))

pages = list(map(int, input().split()))

"""
dp[i][j] --> maximum pages I can get while paying j 
"""

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= prices[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - prices[i - 1]] + pages[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][m])