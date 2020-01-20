n=int(input())
lst=list(map(int, input().split()))
dp=[0 for _ in range(1001)]
Max=0
for i in range(n):
    Min=0
    for j in range(i):
        if lst[i] > lst[j]:
            if Min < dp[j]:
                Min=dp[j]
    dp[i]=Min+1
    if Max < dp[i]:
        Max=dp[i]
print(Max)
