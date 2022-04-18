import sys
n = int(sys.stdin.readline())

numlist = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    numlist[i][0], numlist[i][1], numlist[i][2] = map(int, sys.stdin.readline().split())

sum_table = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    for j in range(3):
        if  i==0:
            sum_table[i][j] = numlist[i][j]
        else:
            sum_table[i][j] = min(sum_table[i-1][(j+1)%3], sum_table[i-1][(j+2)%3]) + numlist[i][j]
print(min(sum_table[-1]))