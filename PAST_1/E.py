#第一回 アルゴリズム実技検定
#E
"""
問題：
n頂点の有向グラフとq個のクエリが与えられるので、最終的な隣接行列を出力せよ
クエリ1:頂点aから頂点bに対して辺を張る
クエリ2:頂点aに向かって辺を張っている全頂点に対してaから辺を張る(無向グラフ化)
クエリ3:頂点aから張っている全頂点xに対して、そのxから辺を張っている頂点に対してaから辺を張る
        言い換えると、頂点aからの距離が2であるような辺に対してその距離を1にする。
解法：
n,qの制約が少ないので、貪欲で良い
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,q = map(int,readline().split())

#隣接行列
g = [[float("inf")]*n for i in range(n)]
for i in range(n):
    g[i][i] = 0 #自分自身への距離は0とする

for i in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "1":
        com,a,b = map(int,s.split())
        a,b = a-1,b-1
    else:
        com,a = map(int,s.split())
        a = a-1
    if com == 1:
        g[a][b] = 1
    elif com == 2:
        for i in range(n):
            if i == a:
                continue
            if g[i][a] == 1:
                g[a][i] = 1
    else:
        q = []
        for i in range(n):
            if i == a:continue
            if g[a][i] == 1:
                for j in range(n):
                    if j == a:continue
                    if g[i][j] == 1:
                        q.append([a,j])
        for i,j in q:
            g[i][j] = 1

#output process
for i in g:
    res = ""
    for j in i:
        if j == 1:
            res += "Y"
        else:
            res += "N"
    print(res)
