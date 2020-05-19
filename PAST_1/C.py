#第一回 アルゴリズム実技検定
#C
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
lst1 = list(map(int,readline().split()))
lst1.sort(reverse=True)
print(lst1[2])
