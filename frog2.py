n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [float('inf') for _ in range(n)]
dp[-1] = 0
for i in range(n-1,0,-1):
    for j in range(i-1, max(i-k-1, -1),-1):
        dp[j] = min(dp[j], dp[i] + abs(stones[i]-stones[j]))
        # print(i,j, dp[j])
print(dp[0])
