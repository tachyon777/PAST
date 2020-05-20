#第二回 アルゴリズム実技検定
#D
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
ord_comma = 46
s = readline().rstrip().decode('utf-8')
n = len(s)
kijun = ord("a")
lst1 = [i for i in range(kijun,kijun+26)]
lst1 = [ord_comma] + lst1
ans = 0

def func(s,t):
    flag = 1
    for i in range(len(s)):
        if s[i] == ".":
            continue
        elif s[i] != t[i]:
            flag = 0
    return flag
for i in lst1:
    res = chr(i)
    for j in range(n):
        if func(res,s[j]):
            ans += 1
            break
for i in lst1:
    for j in lst1:
        res = chr(i)+chr(j)
        for k in range(n-1):
            if func(res,s[k:k+2]):
                ans+=1
                break
for i in lst1:
    for j in lst1:
        for k in lst1:
            res = chr(i)+chr(j)+chr(k)
            for l in range(n-2):
                if func(res,s[l:l+3]):
                    ans+=1
                    break

print(ans)