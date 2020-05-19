#第一回 アルゴリズム実技検定
#M
"""
求めるのは
魔力の和/質量の和　の最大値
よって、魔力の最大化、質量の最小化を目指せば良い。

sum(魔力)/sum(質量)の最大値の求め方は、
ある値Xを決め打った時に、それ(Xより大きい)を達成できるかどうかの二分探索により求まる。
式
sum(魔力)/sum(質量) >= Xを変形して、
sum(魔力) >= sum(質量)*X
これを
sum(魔力) >= sum(質量*X)として、
sigma(魔力i-質量i*X) >= 0
を達成できるかどうかを判定する。

"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m = map(int,readline().split())
AB = []
for i in range(n):
    a,b = map(int,readline().split())
    AB.append([a,b,0])
for j in range(m):
    c,d = map(int,readline().split())
    AB.append([c,d,1])

#nが入る場所(すでにあるならその左)のindexを返す

def func(mid): #ここが関数部分
    res = []
    for a,b,f in AB:
        res.append([b - a*mid,f])
    res.sort(reverse=True)
    flag = 0
    count = 0
    ret = 0
    i = 0
    while True:
        if count >= 5:
            break
        if flag and res[i][1]:
            i += 1
            continue
        if res[i][1]:
            flag = 1
            count += 1
            ret += res[i][0]
        else:
            count += 1
            ret += res[i][0]
        i += 1
    return True if ret >= 0 else False


def binary_search(): #2分探索
    ok = -1
    ng = 10**10
    for i in range(100):
        mid = (ok+ng)/2
        if func(mid):
            ok = mid
        else:
            ng = mid

    return ok

print(binary_search())
