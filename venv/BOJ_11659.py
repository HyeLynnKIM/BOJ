import sys
n, m = map(int, sys.stdin.readline().split())
num_lsit = list(map(int, sys.stdin.readline().split()))
sum=0
sum_list = []

## 각 구간 합 구하기
for i in range(n+1):
    sum_list.append(sum)
    if i==n: break
    sum+=num_lsit[i]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum_list[b]-sum_list[a-1])