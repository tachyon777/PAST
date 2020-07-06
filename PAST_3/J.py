#第三回 アルゴリズム実技検定
#J
"""
子供の取った寿司は左から見て、必ず単調減少となる。
よって、どの子供が寿司を取るかは二分探索で求めることが可能
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
lst1 = list(map(int,readline().split()))
children = [0]*(n+1)
def func(mid,cost): #ここが関数部分
    return True if children[mid] < cost else False

def binary_search(cost): #2分探索
    ok = n
    ng = -1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if func(mid,cost):
            ok = mid
        else:
            ng = mid
    if ok ==n:
        return -1
    else:
        children[ok] = cost
        return ok+1


for i in range(m):
    print(binary_search(lst1[i]))