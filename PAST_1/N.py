#第一回 アルゴリズム実技検定
#N
"""
開けるべき幅Cの左端を固定して考えた時、障害物とかぶ(り始め)るようなに+pして、
かぶらなくなるような座標で-pする。
座標が10**10と非常に大きいので、
座標順にソートしてイベント的に処理する。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,w,c = map(int,readline().split())
event = []
for i in range(n):
    l,r,p = map(int,readline().split())
    event.append([max(l-c+1,0),p])
    event.append([r,-p])
event.sort()
ans = 10**18
event_now = 0
now = 0
res = 0
while event_now < 2*n:
    now = event[event_now][0]
    if now > w-c:break
    res += event[event_now][1]
    if event_now+1 < 2*n and now != event[event_now+1][0]:
        ans = min(ans,res)
    event_now += 1
ans = min(ans,res)
print(ans)