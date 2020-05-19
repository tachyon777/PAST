#第一回 アルゴリズム実技検定
#G
"""
3**10が容易に間に合うので貪欲
"""
import sys
import itertools
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n-1):
    lst1.append(list(map(int,readline().split())))
ans = -10**18
for i in itertools.product([0,1,2],repeat=n):
    cost = 0
    for j in range(n-1):
        now = i[j]
        for k in range(n-j-1):
            if now == i[j+k+1]:
                cost += lst1[j][k]

    ans = max(ans,cost)

print(ans)
