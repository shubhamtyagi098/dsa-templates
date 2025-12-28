## The Problem
You have m dollars and n books. Each book has a price and gives you some pages. You want maximum pages within your budget.

## What DP Table Means
dp[i][j] = "Best pages I can get using first i books with j dollars"

## The Logic - Book by Book Decision

For each book, you have 2 choices:
1. Buy it (if you can afford it)
2. Skip it

```python
# For book i with budget j:
if j >= price[i]:  # Can I afford this book?
    # Option 1: Skip book i, keep previous best
    skip = dp[i-1][j]

    # Option 2: Buy book i, add its pages to previous best
    buy = dp[i-1][j - price[i]] + pages[i]

    # Pick the better option
    dp[i][j] = max(skip, buy)
else:
    # Can't afford it, must skip
    dp[i][j] = dp[i-1][j]
```

## Why the Else Case Matters

Without else case:
• Book costs $10, you have $5
• dp[i][j] stays 0 (loses all previous progress!)

With else case:
• Book costs $10, you have $5
• dp[i][j] = dp[i-1][j] (keeps previous best result)

## Simple Example
Books: [price=$3, pages=10], [price=$5, pages=20]
Budget: $6

dp[0][6] = 0  (no books = 0 pages)
dp[1][6] = 10 (buy book 1: $3 for 10 pages)
dp[2][6] = 20 (buy book 2: $5 for 20 pages, better than book 1)