#第三回 アルゴリズム実技検定
#I
"""
行列に対しクエリを消化する
行列自体を変更するのは論外なので、
与えられた行列は一度も変更せずにindex管理で解く。

行列は
0 1 2 3
4 5 6 7
8 9 10 11
12 13 14 15

のようなN*Nの行列

#1
元の位置がiである行がどこに行っているのかを保持することで消化する

#2
1と同じく、元の位置がjであるような列がどこにあるのかを保持
#3
転置したときにどのようなindexの法則があるのか不明。シュミレーションする。
→rowとcolに入れるindexを反転すればok
このとき行列のindexが崩れないか？→大丈夫

#4
lst[a][b] を出力
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
q = int(readline())
row = [i for i in range(n)]
col = [i for i in range(n)]
T = 0 #0:元の形,1:転置中
for _ in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "3":
        T = 1-T
        continue
    else:
        com,a,b = s.split()
        a,b = int(a),int(b)
        a,b = a-1,b-1
    if com == "1":
        if not T:
            row[a],row[b] = row[b],row[a]
        else:
            col[a],col[b] = col[b],col[a]
    elif com == "2":
        if not T:
            col[a],col[b] = col[b],col[a]
        else:
            row[a],row[b] = row[b],row[a]
    else:
        if not T:
            print(n*row[a]+col[b])
        else:
            print(n*row[b]+col[a])