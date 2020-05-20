#第二回 アルゴリズム実技検定
#A
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
lst1 = [ "B1","B2","B3","B4","B5","B6",
"B7","B8","B9","1F","2F","3F","4F","5F","6F","7F","8F","9F" ]
lst2 = lst1[8::-1] + lst1[9:]
a,b = readline().rstrip().decode('utf-8').split()

i,j = 0,0
for idx,k in enumerate(lst2):
    if a == k:
        i = idx
    if b == k:
        j = idx

print(abs(i-j))