#第三回 アルゴリズム実技検定
#F
"""
一行につき一文字とって回文を作成するという問題
N<=500
S[i] == s[n-i]となる文字が存在するかどうかを判定していけば良い。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
lst1 = []
for i in range(n):
    lst1.append(set(list(readline().rstrip().decode('utf-8'))))
ans = [0]*n
for i in range(n//2):
    flag = 0
    for j in lst1[i]:
        for k in lst1[n-(i+1)]:
            if j == k:
                ans[i] = j
                ans[n-(i+1)] = j
                flag = 1
                break
        if flag:break
    if not flag:
        print(-1)
        exit()

if not even(n):
    for i in lst1[n//2]:
        ans[n//2] = i
        break

print("".join(ans))


