#第二回 アルゴリズム実技検定
#C
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
maze = []
for _ in range(n):
    maze += [list(readline().rstrip().decode())]

for i in range(n-2,-1,-1):
    for j in range(2*n-1):
        if maze[i][j] == "#":
            if maze[i+1][j-1] == "X" or \
                maze[i+1][j] == "X" or \
                    maze[i+1][j+1] == "X":
                    maze[i][j] = "X"


for i in maze:
    print("".join(i))