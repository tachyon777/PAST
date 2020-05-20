#第二回 アルゴリズム実技検定
#F
"""
選べるものの中で最も報酬が大きいものを選び続ける
"""
import sys
import heapq
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
AB = []
for i in range(n):
    a,b = map(int,readline().split())
    AB.append([a,-b])

AB.sort()
hp = []
heapq.heapify(hp)
now = 0
ans = 0
for i in range(1,n+1):
    while True:
        if now >= len(AB):break
        if AB[now][0] > i:break
        heapq.heappush(hp,AB[now][1])
        now += 1
    if hp:
        ans -= heapq.heappop(hp)
    print(ans)