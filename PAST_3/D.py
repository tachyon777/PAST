#第三回 アルゴリズム実技検定
#D
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())

dic1 = {
    "####.##.##.####":0,
    ".#.##..#..#.###":1,
    "###..#####..###":2,
    "###..####..####":3,
    "#.##.####..#..#":4,
    "####..###..####":5,
    "####..####.####":6,
    "###..#..#..#..#":7,
    "####.#####.####":8,
    "####.####..####":9
}

ans = [[] for _ in range(n)]
lst1 = []
for _ in range(5):
    lst1.append(readline().rstrip().decode('utf-8'))
for i in range(5):
    for j in range(n):
        ans[j].append(lst1[i][4*j+1:4*j+4])
ans2 = ""
for i in ans:
    res = ""
    for j in i:
        res += j
    ans2 += str(dic1[res])

print(ans2)