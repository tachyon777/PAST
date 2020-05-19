#第一回 アルゴリズム実技検定
#H
"""
問題：
リストが与えられる。与えられるクエリを消化し、
(元のリストの合計値-最終的なリストの合計値)を求めよ。
クエリ1:x番目の要素からa引く
クエリ2:リストの奇数番目全てをa引く
クエリ3:リストの全要素からa引く
但し、上記のクエリはリストの要素がマイナスとなり得る場合は行わない

解法：
そのクエリを消化できるか/できないかを
最小値の保持で高速に求められれば良い。
与えられたリスト自体の操作は一回も行わず、
・各要素から引かれた数のリスト(lst2)
・奇数番目の要素から引かれた数(odd)
・全要素から引かれた数(al)
を保持することによって、最小値をO(1)で求められるようにする
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = list(map(int,readline().split()))
q = int(readline())
one = 0
odd = 0
al = 0
odd_min = min(lst1[::2]) #0-indexedでは偶数番目になるので注意
al_min = min(lst1)
for i in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "1":
        com,x,a = map(int,s.split())
        x = x-1
    else:
        com,a = map(int,s.split())
    if com == 1:
        if even(x):
            if lst1[x] - al - odd >= a:
                lst1[x] -= a
                one += a
                odd_min = min(odd_min,lst1[x])
                al_min = min(al_min,lst1[x])
        else:
            if lst1[x] - al >= a:
                lst1[x] -= a
                one += a
                al_min = min(al_min,lst1[x])
    elif com == 2:
        if odd_min >= a:
            odd_min -= a
            al_min = min(al_min,odd_min)
            odd += a
    else:
        if al_min >= a:
            al_min -= a
            odd_min -= a
            al += a

print(one + ((n+1)//2)*odd + n*al )