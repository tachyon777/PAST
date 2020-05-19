#第一回 アルゴリズム実技検定
#K
"""
問題：
木構造が与えられる。
その後、q個のクエリが与えられるので、
aの祖先がbであるか求めよ
解法：
根付き木を創り、a,bの最小共通祖先がbならばyes,そうでないならno
根付き木の作り方に少し工夫が必要で、作成順番を気をつける必要がある。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())

g = [[] for _ in range(n)] #隣接リスト
for i in range(n):
    a = int(readline())
    if a == -1:
        root = i
    else:
        g[a-1].append(i)

#親、子の関係を完全保存(どちらからでも辿れる)
child = [[] for i in range(n)] #それぞれの頂点の子を入れる
parent = [-1]*n
used = [False]*n
tank = [root]

while tank:
    q = tank.pop() #q:親
    used[q] = True
    for e in g[q]: #e:子
        if not used[e]: #eが使われていないなら
            child[q].append(e) #qの子にeを追加
            tank.append(e)
            parent[e] = q #eの親はq

N = 2*n-1
#RMQ - Indexed
def init_min(init_min_val):
    #set_val
    for i in range(N):
        seg_min[i+num_min-1]=init_min_val[i]*N + i    
    #built
    for i in range(num_min-2,-1,-1) :
        seg_min[i]=min(seg_min[2*i+1],seg_min[2*i+2]) 
    
def query_min(p,q):
    if q<=p:
        return ide_ele_min
    p += num_min-1
    q += num_min-2
    res=ide_ele_min
    while q-p>1:
        if p&1 == 0:
            res = min(res,seg_min[p])
        if q&1 == 1:
            res = min(res,seg_min[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = min(res,seg_min[p])
    else:
        res = min(min(res,seg_min[p]),seg_min[q])
    return res


#####単位元######
ide_ele_min = 10**18

#num_min:N以上の最小の2のべき乗
num_min =2**(N-1).bit_length()
seg_min=[ide_ele_min]*2*num_min

#Euler Tour
#eulerTour : 訪れた順番の頂点の配列
#left[i] : 初めて頂点 i に訪れたときのeulerTourのIndex
#right[i] :  最後に頂点 i に訪れたときのeulerTourのIndex
#depth[i] : 頂点 i の深さ
tank = [root]
eulerTour = []
left = [0]*n
right = [-1]*n
depth = [-1]*n

eulerNum = -1
de = -1

while tank:
    q = tank.pop()
    if q >= 0:
        #first time
        eulerNum += 1
        eulerTour.append(q)
        left[q] = eulerNum
        right[q] = eulerNum
        tank.append(~q)
        de += 1
        depth[q] = de #深さ
        for ch in child[q]:
            tank.append(ch)
    else: #すべての頂点は必ず2度通るので、ifで引っかからなければ帰り道
        de -= 1
        if ~q != root: #ビット反転(反転を反転)したものが根である場合は既に処理済みなので飛ばす
            eulerTour.append(parent[~q]) #親=bit反転したもの
            eulerNum += 1 #オイラー路の順番
            right[parent[~q]] = eulerNum #オイラー路の順番をrightに格納
        
init_min([depth[e] for e in eulerTour])

def getLCA(u,v): # 最小共通祖先を求める
    g = query_min(min(left[u],left[v]),max(right[u],right[v])+1)
    return eulerTour[g%N] #セグ木の構造上、N(=2*n-1)でmodを取るとそのLCAが求まる

#ここまでがテンプレート

q = int(readline())
for i in range(q):
    a,b = map(int,readline().split())
    a,b = a-1,b-1
    LCA = getLCA(a,b)
    print("Yes" if LCA == b else "No")
