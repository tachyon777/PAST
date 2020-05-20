#第二回 アルゴリズム実技検定
#I
"""
比較、格納を繰り返す
"""
import sys
from copy import deepcopy
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = 2**int(readline())
lst1 = list(map(int,readline().split()))
lst2 = []
for i in range(n):
    lst2.append([i,lst1[i]])
ans = [0]*n
count = 1
lst3 = []
while True:
    if len(lst2) == 2:
        ans[lst2[0][0]] = count
        ans[lst2[1][0]] = count
        break
    for i in range(0,len(lst2),2):
        if lst2[i][1] < lst2[i+1][1]:
            ans[lst2[i][0]] = count
            lst3.append(lst2[i+1])
        else:
            ans[lst2[i+1][0]] = count
            lst3.append(lst2[i])
    lst2 = deepcopy(lst3)
    lst3 = []
    
    count += 1

for i in ans:
    print(i)