#第一回 アルゴリズム実技検定
#J
"""
まず迷路はグラフとして良い
左下隅:S
右下隅:G1
右上隅:G2
とした時に、
ある一点をP定めて
(P-S)+(P-G1)+(P-G2)のパスの合計の最小値が答えとなる。
これは三点が必ず一点で交差する場合が最適であることから言える
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
#迷路plane
h,w = map(int,readline().split())
n = h*w
maze = []
for _ in range(h):
    maze += [list(map(int,readline().split()))]

#迷路にindexを振るため、リストを作成
#0 1 2
#3 4 5
#6 7 8 のように
idx_lst = []
idx = 0
for i in range(h):
    res = []
    for j in range(w):
        res.append(idx)
        idx += 1
    idx_lst.append(res)

def make_graph(h,w,maze):
    g = [[] for _ in range(n)] #n:h*w
    
    #実際に迷路を隣接リスト化
    for i in range(h):
        for j in range(w):
            for k,l in ([1, 0], [-1, 0], [0, 1], [0, -1]): #4近傍について探索
                new_h, new_w = i+k,j+l
                if new_h < 0 or new_h >= h or \
                new_w < 0 or new_w >= w: #リスト外でないならelif条件へ
                    continue
                g[idx_lst[i][j]].append([maze[new_h][new_w],idx_lst[new_h][new_w]]) #ダイクストラ法(heapq)でそのまま扱えるようにweight firstにしてある

    return g

graph = make_graph(h,w,maze)

#ダイクストラ法通常版
#O(ElogV)
import heapq
def dijkstra_heap(s,edge):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist): #キューから値が無くなるまで
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]: #既に最小距離が確定しているなら
            continue
        v = minedge[1] #vに頂点を代入
        d[v] = minedge[0] #その頂点のコストに重みを代入
        used[v] = False #vには最小距離が入っていることが証明できる(ヒープキューを使用しているため)
        for e in edge[v]: #頂点vから伸びている辺の先をヒープキューに入れてく
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d #回しきったらreturn(たどり着けなかった頂点はinf.)

res1 = dijkstra_heap(idx_lst[h-1][0],graph)
res2 = dijkstra_heap(idx_lst[0][w-1],graph)
res3 = dijkstra_heap(idx_lst[h-1][w-1],graph)
res4 = 10**18
for i in range(n):
    if res4 >= res1[i]+res2[i]+res3[i]-2*maze[i//w][i%w]:
        res4 = res1[i]+res2[i]+res3[i]-2*maze[i//w][i%w]

print(res4)
