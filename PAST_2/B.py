#第二回 アルゴリズム実技検定
#B
import sys
from collections import defaultdict
dic1 = defaultdict(int)
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

s = readline().rstrip().decode('utf-8')

for i in s:
    dic1[i] += 1
res = 0
ans = ""
for i,j in dic1.items():
    if j > res:
        ans = i
        res = j
print(ans)