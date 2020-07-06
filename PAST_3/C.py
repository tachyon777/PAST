#第三回 アルゴリズム実技検定
#C
"""
公比1のとき、aでexit()
"""
import sys
sys.setrecursionlimit(10**7)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
a,r,n = map(int,readline().split())
if r == 1:
    print(a)
    exit()
def func(now,res):
    if res > 10**9:
        print("large")
        exit()
    if now == n:
        return res
    return func(now+1,res*r)

print(func(1,a))