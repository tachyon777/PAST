#第一回 アルゴリズム実技検定
#A
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

try:
    n = int(readline())
    print(n*2)
except:
    print("error")