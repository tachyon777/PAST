#第二回 アルゴリズム実技検定
#G
"""
ランレングス符号化を用いて高速にクエリを消化すれば良い
"""
import sys
from collections import deque
from collections import defaultdict
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
deq = deque([])
for i in range(n):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "1":
        com,c,x = s.split()
        x = int(x)
    else:
        com,d = s.split()
        d = int(d)
    if com == "1":
        deq.append([c,x])
    else:
        dic1 = defaultdict(int)
        while d > 0:
            if not deq:break
            s,ct = deq.popleft()
            if ct > d: #余るなら
                deq.appendleft([s,ct-d])
                dic1[s] += d
            else:dic1[s] += ct
            d -= ct
        res = 0
        for j in dic1.values():
            res += j**2
        print(res)