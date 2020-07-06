#第三回 アルゴリズム実技検定
#L
"""
手前から見れる商品はせいぜい2つであることに注意
input量が多いので実行制限4sec
普通にヒープ管理でいいのかな？

a=1の場合：
hp1から1個取る
hpresにその値を保存
追加操作：
hp1にnowを追加
hp2にnow+1を追加
now+=1する

a=2の場合:
hp2から1個取る
1.もしhpresにその値が存在するならば、これを無視する。hpresからこれを削除する。
なお、この動作もheapを用いて行って良いことが証明できる。
2.これがhp1と等しいならばhp1からもそれを取る
3.どこからとったのかを二次元リストの2つめに格納しておけば高速に追加の操作が行える

追加操作：
1.hp1に同じ値が入っていた場合(手前)：
hp1から同等の値を削除して、hp1にnowをpush,hp2にnow+1をpushしてやる。
その後、now+=1する
2.入っていなかった場合(奥)：
hp1の変更は行わず、hp2にnow+1をpushする。
その後、now +=1する。このとき、hp1は"now"を使わないことになるが
nowは使用済みなので、このように操作を行って構わない。

nowは、hp2において入っているちょうどのところのindexで管理する

a=2で、取った時に、手前なのか奥なのかで扱いが少し違うので注意。

手前→hp1にも入っている：
hp1から同等の値を削除して、hp1にnowをpush,hp2にnow+1をpushしてやる。
その後、now+=1する
奥→hp1には入っていない：
よってhp1の変更は行わず、hp2にnow+1をpushする。
その後、now +=1する。このとき、hp1は"now"を使わないことになるが
nowは使用済みなので、このように操作を行って構わない。

TLE:
whileで回してるのがまずい気もする。
hpresを使わないで解く方法がある？
"""
import sys
import heapq
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
K = []
hp1 = []
hp2 = []
hpres = []
heapq.heapify(hp1)
heapq.heapify(hp2)
heapq.heapify(hpres)
for i in range(n):
    lst1 = list(map(int,readline().split()))
    heapq.heappush(hp1,(-lst1[1],i))
    heapq.heappush(hp2,(-lst1[1],i))
    if lst1[0] >= 2:
        heapq.heappush(hp2,(-lst1[2],i))
    else:
        heapq.heappush(hp2,(0,i))
    K.append(lst1 +[0]*2)

m = int(readline())
A = list(map(int,readline().split())) #1or2
now = [2]*n #hp2にちょうど追加してあるところ(0要素目を考慮)

for i in range(m):
    if A[i] == 1:
        val,index = heapq.heappop(hp1) #値,index
        print(-val)

        heapq.heappush(hpres,val)
        heapq.heappush(hp1,(-K[index][now[index]],index))
        heapq.heappush(hp2,(-K[index][now[index]+1],index))
        now[index] += 1
    
    else:
        while True: #hp1で消化済みだった場合ループする
            val,index = heapq.heappop(hp2) #値,index
            if not hpres:
                break
            res_val = heapq.heappop(hpres)
            if val == res_val:
                continue
            else: #違うなら戻しておく
                heapq.heappush(hpres,res_val)
                break
        print(-val)
        hp1_val,hp1_idx = heapq.heappop(hp1)
        #hp1に入っているかいないかで分岐
        if hp1_val != val: #入っていなかった場合
            heapq.heappush(hp1,(hp1_val,hp1_idx))
            heapq.heappush(hp2,(-K[index][now[index]+1],index))
            now[index] += 1
        
        else:
            heapq.heappush(hp1,(-K[index][now[index]],index))
            heapq.heappush(hp2,(-K[index][now[index]+1],index))
            now[index] += 1