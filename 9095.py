dp=[-1 for _ in range(15)]
def solve(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n]=solve(n-1)+solve(n-2)+solve(n-3)
    return dp[n]
a=int(input())
for _ in range(a):
    print(solve(int(input())))
