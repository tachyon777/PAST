#第三回 アルゴリズム実技検定
#E
"""
n頂点m辺の無向グラフが与えられる。
初め頂点iは色cで塗られている。
クエリ1が与えられると、その頂点に隣接する頂点がその色で上書きされる。
クエリ2が与えられると、その頂点を色yで上書きする。
特に凝った解法は無いので、単純にクエリを消化すれば良い。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,q = map(int,readline().split())
g = [[] for i in range(n)]
for i in range(m):
    x,y = map(int,readline().split())
    x,y = x-1,y-1
    g[x].append(y)
    g[y].append(x)
C = list(map(int,readline().split()))

for _ in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "1":
        com,fr = s.split()
        fr = int(fr)
        fr = fr-1
    else:
        com,fr,y = s.split()
        fr,y = int(fr),int(y)
        fr = fr-1
    color = C[fr]
    print(color)
    if com == "1":
        for go in g[fr]:
            C[go] = color
    else:
        C[fr] = y
        
        