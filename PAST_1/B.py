#第一回 アルゴリズム実技検定
#B
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(int(readline()))

for i in range(1,n):
    res = lst1[i]-lst1[i-1]
    if res==0:
        print("stay")
    elif res>0:
        print("up",res)
    else:
        print("down",-res)
