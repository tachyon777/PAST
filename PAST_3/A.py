#第三回 アルゴリズム実技検定
#A
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')
t = readline().rstrip().decode('utf-8')

if s == t:
    print("same")
elif s.lower() == t.lower():
    print("case-insensitive")
else:
    print("different")