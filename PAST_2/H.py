#第二回 アルゴリズム実技検定
#H
"""
マンハッタン距離でグラフを構築してダイクストラ
"""
import sys
sys.setrecursionlimit(10**7)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())
maze = [[] for _ in range(11)]
for i in range(n):
    s = readline().rstrip().decode('utf-8')
    for j,t in enumerate(s):
        if t == "S":maze[0].append((i,j))
        elif t == "G":maze[-1].append((i,j))
        else:maze[int(t)].append((i,j))

#ダイクストラ法通常版
#O(ElogV)
import heapq
def dijkstra_heap(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * (n*m)
    used = [True] * (n*m) #True:未確定
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

edge = [[] for i in range(n*m)]
#edge[i] : iから出る道の[重み,行先]の配列

for i in range(10):
    for x,y in maze[i]:
        for x2,y2 in maze[i+1]:
            dist = abs(x-x2)+abs(y-y2)
            edge[x*m+y].append([dist,x2*m+y2])
ans = dijkstra_heap(maze[0][0][0]*m+maze[0][0][1])
ans = ans[maze[-1][0][0]*m+maze[-1][0][1]]
print(ans if ans < float("inf") else -1) #引数が始点,戻り値が各頂点への最短路(リスト型)