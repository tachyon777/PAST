#第一回 アルゴリズム実技検定
#I
"""
典型bitdp
ABC142-E get everythingそのまんま
dp[i]: bit状態でi以上の部品を調達している時のコストの最小値
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
INF = 10**18
VW = []
for i in range(m):
    s,c = readline().rstrip().decode('utf-8').split()
    b = 0
    for i in range(n):
        if s[i] == "Y":
            b += 1<<i
    VW.append([b,int(c)])

dp = [INF for _ in range(1<<n)]
dp[0] = 0
for i in range(1<<n):
    for j in range(m):
        s = i|VW[j][0]
        dp[s] = min(dp[s],dp[i]+VW[j][1])

print(dp[-1] if dp[-1] != INF else -1)