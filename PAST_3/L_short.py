#第三回 アルゴリズム実技検定
#L(書き直し)
"""
優先度付きキューのリストを3つ用意することでこの問題は解くことができる。
1.手前から1個だけ見たとき(a=1)のheap(hp1)
2.手前から2個見たとき(a=2)のheap(hp2)
3.hp1から使用されたものであって、hp2にはまだあるもの(hpres)
もう一つ、以下のヒープがあってもよいが、無いほうが簡単のため省略
(4.hp2から使用されたものであって、hp1にはまだあるもの)

場合分けをしっかり考えないと、辻褄が合わなくなるので注意。
"""
import sys
import heapq
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
hpify = heapq.heapify
push = heapq.heappush
pop = heapq.heappop
n = int(readline())
K = []
hp1 = []
hp2 = []
hpres = []
hpify(hp1)
hpify(hp2)
hpify(hpres)
for i in range(n):
    lst1 = list(map(int,readline().split()))
    push(hp1,(-lst1[1],i))
    push(hp2,(-lst1[1],i))
    if lst1[0] >= 2:
        push(hp2,(-lst1[2],i))
    else:
        push(hp2,(0,i))
    K.append(lst1 +[0]*2)

m = int(readline())
A = list(map(int,readline().split()))
now = [2]*n #hp2にちょうど追加してあるところ(0要素目の要素数を考慮)

for i in range(m):
    if A[i] == 1:
        val,idx = pop(hp1)

        print(-val)

        push(hpres,val)
        push(hp1,(-K[idx][now[idx]],idx))
        push(hp2,(-K[idx][now[idx]+1],idx))
        now[idx] += 1
    
    else:
        while True: #hp1で消化済みだった場合ループする
            val,idx = pop(hp2)
            if not hpres:
                break
            res_val = pop(hpres)
            if val == res_val:
                continue
            else:
                push(hpres,res_val)
                break
        
        print(-val)

        hp1_val,hp1_idx = pop(hp1)

        #hp1に入っているかいないかで分岐
        if hp1_val != val:
            push(hp1,(hp1_val,hp1_idx))
            push(hp2,(-K[idx][now[idx]+1],idx))
            now[idx] += 1
        
        else:
            push(hp1,(-K[idx][now[idx]],idx))
            push(hp2,(-K[idx][now[idx]+1],idx))
            now[idx] += 1