n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [0] * len(stair)

for i in range(n):
    if i == 0:
        dp[0] = stair[0]
    elif i == 1:
        dp[i] = max(stair[i-1] + stair[i], stair[i])
    elif i == 2:
        dp[i] = max(stair[i-1] + stair[i], dp[i-2] + stair[i])
    else:
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[-1])