import sys
n=int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
f_list = list(map(int, sys.stdin.readline().split()))

cnt = [0]*20000001
for n in num_list:
    cnt[n] += 1
for f in f_list:
    print(cnt[f], end=' ')