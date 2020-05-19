#第一回 アルゴリズム実技検定
#F
"""
大文字で始まって大文字で終わるような長さ2以上の文字列で区切る
その後、大文字、小文字を区別しないソートを行った後につなげて出力
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')

kijun = ord("a")
ans = []
res = ""
count = 0
for i in s:
    if ord(i) < kijun and count >= 1:
        res += i
        ans.append([res.lower(),res])
        res = ""
        count = 0
    else:
        res += i
        count += 1
ans.sort()
res = ""
for i,j in ans:
    res += j
print(res)
