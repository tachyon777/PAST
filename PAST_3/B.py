#第三回 アルゴリズム実技検定
#B
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,q = map(int,readline().split())
prob = [n]*m
user = [[0]*m for _ in range(n)]
for _ in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "1":
        com,a = s.split()
        a = int(a)
        a -= 1
    else:
        com,a,b = s.split()
        a,b = int(a),int(b)
        a,b = a-1,b-1
    
    if com == "1":
        res = 0
        for i in range(m):
            if user[a][i] == 1:
                res += prob[i]
        print(res)
    else:
        prob[b] -= 1
        user[a][b] = 1
