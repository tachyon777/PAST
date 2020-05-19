#第一回 アルゴリズム実技検定
#D
import sys
from collections import defaultdict
dic1 = defaultdict(int)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n):
    dic1[int(readline())] += 1

ans = [0,0]
flag = 0
for i in range(1,n+1):
    if dic1[i] != 1:
        flag = 1
        if dic1[i] == 0:
            ans[1] = i
        else:
            ans[0] = i 

if flag:
    print(*ans)
else:
    print("Correct")