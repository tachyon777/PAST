#第二回 アルゴリズム実技検定
#J
"""
再帰的解法
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
s = readline().rstrip().decode('utf-8')

def func(res,s):
    if s == "":
        return res
    if s[0] == ")":
        return [res+res[::-1],s[1:]]
    elif s[0] == "(":
        res2 = func("",s[1:])
        return func(res + res2[0],res2[1])
    else:
        return func(res+s[0],s[1:])
    return res

print(func("",s))