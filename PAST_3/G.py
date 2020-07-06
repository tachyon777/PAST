#第三回 アルゴリズム実技検定
#G
"""
移動方法がちょっと特殊な幅優先探索。
初期位置:0,0
ゴール:x,y
障害物:n個
すぬけくんが障害物に囲まれていない以上は必ずゴールできる。
"""
import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,Gx,Gy = map(int,readline().split())

visited = [[0]*411 for _ in range(411)]
maze = [[0]*411 for _ in range(411)]
for i in range(n):
    x,y = map(int,readline().split())
    maze[y+205][x+205] = 1

deq = deque([(205,205,0)])
visited[205][205] = 1
ans = -1
while deq:
    y,x,ct = deq.popleft()
    if y == Gy+205 and x == Gx+205:
        ans = ct
        break
    for i,j in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,0)]:
        if 0 <= y+i < 411 and 0 <= x+j < 411:
            if not visited[y+i][x+j] and not maze[y+i][x+j]:
                visited[y+i][x+j] = 1
                deq.append((y+i,x+j,ct+1))

print(ans)