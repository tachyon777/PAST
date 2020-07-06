#第三回 アルゴリズム実技検定
#K
"""
多分親を管理するような解き方をするはず。
根からの"距離"によってクエリを完全に消化できる。
机の直上にあるコンテナを根として、その距離を0とする。
また、根のコンテナの番号を管理するリストを保持する。
コンテナをある机に積み替えるとき、根のコンテナが存在するならば、
距離を"そのコンテナに既に積み上げられているものの個数"として、
その一要素(上にどれだけ積まれていても関係ない)を変更(根の要素、根からの距離)する。

amount = 今そのコンテナに何個積まれているか
roots = その机の一番下の要素はなにか(何も乗ってないなら-1にでも。)

最後に全要素の祖先の番号を出力することでこの問題が解ける。
(このとき、最悪O(N)かかるので、つなぎ直す工夫が必要)
↓
visitedでN個回せば(dfs)いいかも？
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,q = map(int,readline().split())
roots = [i for i in range(n)]
tops = [i for i in range(n)]
g = [ 0 for _ in range(n)]
for i in range(n):
    g[i] = -(i+1) #根の要素(-1なら自分が根),根からの距離
for _ in range(q):
    f,t,x = map(int,readline().split())
    f,t,x = f-1,t-1,x-1
    con = g[x]
    res = tops[f]
    if con < 0:
        roots[f] = -1
        tops[f] = -1
    else:
        tops[f] = con
    if tops[t] == -1:
        g[x] = -(t+1)
    else:
        g[x] = tops[t]
    tops[t] = res

#ここまでで一回デバッグ
#ok

#あとは根につなぎ直しながらansに埋め込む
ans = [-1]*n
for i in range(n):
    if ans[i] == -1:
        stack = []
        now = i
        while True:
            if g[now] < 0:
                desk = - g[now]
                stack.append(now)
                break
            else:
                stack.append(now)
            now = g[now] #親
        for j in stack:
            ans[j] = desk

for i in ans:
    print(i)