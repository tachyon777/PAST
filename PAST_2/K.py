#第二回 アルゴリズム実技検定
#K
"""
dp[i][j]:i文字目まで見たときの"("の空いている個数をj個とした場合の
最小コスト
負の遷移")"を許さず、負になる場合は必ず削除・変更を行う。
"""
import sys
from copy import deepcopy
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
INF = 10**18
s = readline().rstrip().decode('utf-8')
C = list(map(int,readline().split()))
D = list(map(int,readline().split()))
dp = [[INF]*3010 for _ in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    go = s[i-1]
    for j in range(3005):
        if j == 0: #必ずdelか"("
            if go == "(":
                dp[i][j+1] = min(dp[i][j+1],dp[i-1][j])
                dp[i][j] = min(dp[i][j],dp[i-1][j] + D[i-1])
            else:
                dp[i][j] = min(dp[i][j],dp[i-1][j]+D[i-1])
                dp[i][j+1] = min(dp[i][j+1],dp[i-1][j]+C[i-1])
        else:
            if go == "(":
                dp[i][j-1] = min(dp[i][j-1],dp[i-1][j]+C[i-1])
                dp[i][j] = min(dp[i][j],dp[i-1][j]+D[i-1])
                dp[i][j+1] = min(dp[i][j+1],dp[i-1][j])
            else:
                dp[i][j-1] = min(dp[i][j-1],dp[i-1][j])
                dp[i][j] = min(dp[i][j],dp[i-1][j]+D[i-1])
                dp[i][j+1] = min(dp[i][j+1],dp[i-1][j]+C[i-1])


print(dp[-1][0])