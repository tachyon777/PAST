#第三回 アルゴリズム実技検定
#H
"""
行動ごとに分けてdp
行動の途中でゴールすることを考慮しなければならない
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,l = map(int,readline().split())
lst1 = list(map(int,readline().split()))
x = [0]*(l+4)
for i in lst1:
    x[i] += 1
run,jump,hurdle = map(int,readline().split())
INF = 10**18
dp = [INF]*(l+4)
dp[0] = 0

for i in range(l):
    #1
    if x[i+1]:
        dp[i+1] = min(dp[i+1],dp[i]+run+hurdle)
    else:
        dp[i+1] = min(dp[i+1],dp[i]+run)

    #2
    if x[i+2]:
        dp[i+2] = min(dp[i+2],dp[i]+run+jump+hurdle)
    else:
        dp[i+2] = min(dp[i+2],dp[i]+run+jump)
    #3
    if x[i+4]:
        dp[i+4] = min(dp[i+4],dp[i]+run+3*jump+hurdle)
    else:
        dp[i+4] = min(dp[i+4],dp[i]+run+3*jump)

#行動の途中でゴール
#2
dp[l] = min(dp[l],dp[l-1]+run//2+jump//2)
#3
dp[l] = min(dp[l],dp[l-2]+run//2+jump+jump//2)
dp[l] = min(dp[l],dp[l-3]+run//2+jump*2+jump//2)

print(dp[l])