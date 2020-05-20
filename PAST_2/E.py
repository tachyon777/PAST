#第二回 アルゴリズム実技検定
#E
"""
数列の配置場所を参照する回数が答え
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))
ans = [0]*n

for i in range(n):
    res = 1
    now = i
    while True:
        if lst1[now]-1 == i:
            ans[i] = res
            break
        now = lst1[now] -1
        res += 1

print(*ans)