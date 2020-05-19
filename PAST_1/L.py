#第一回 アルゴリズム実技検定
#L
"""
最小全域木
但し、達成すれば良いのは大きい塔のみ。
よって、各小さい塔を使う/使わないをbit全探索して、O(2**5)
全体のコストの最小値が答え。
各プリム法を用いた探索時間はO(ElogV)なので、
E=35**2,V=35として全体は
O(2**m*((n+m)**2)*log(n+m))となる
"""
import sys
import math
from copy import deepcopy
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())
xyc = []
for i in range(n+m):
    xyc.append(list(map(int,readline().split())))

#O(ElogV)
import heapq
def prim_heap(edge):
    used = [True] * len(edge) #True:不使用
    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist,e)
    used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,e)
        res += minedge[0]
    return res

edge = [[] for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        a = xyc[i]
        b = xyc[j]
        res = math.sqrt(((a[0]-b[0])**2+(a[1]-b[1])**2))
        if a[2] != b[2]:
            res *= 10
        edge[i].append([res,j])
        edge[j].append([res,i])
ans = 10**18
for i in range(1<<m):
    edge2 = deepcopy(edge)
    count = 0
    bit = []
    for j in range(m):
        if i>>j&1: #1ならば使う
            edge2.append([])
            for k in range(n):
                a = xyc[k]
                b = xyc[n+j]
                res = math.sqrt(((a[0]-b[0])**2+(a[1]-b[1])**2))
                if a[2] != b[2]:
                    res *= 10
                edge2[k].append([res,n+count])
                edge2[n+count].append([res,k])
            for k in range(count):
                a = bit[k]
                b = xyc[n+j]
                res = math.sqrt(((a[0]-b[0])**2+(a[1]-b[1])**2))
                if a[2] != b[2]:
                    res *= 10
                edge2[n+k].append([res,n+count])
                edge2[n+count].append([res,n+k])
            bit.append(b)
            count += 1
    ans = min(ans,prim_heap(edge2))

print(ans)
