import sys
n, m = map(int, sys.stdin.readline().split())
cnt_listen, cnt_see= {}, {}

for i in range(n):
    cnt_listen[i] = sys.stdin.readline().rstrip()
for i in range(m):
    cnt_see[sys.stdin.readline().rstrip()] = i

common=[]
for i in cnt_listen:
    try:
        tmp = cnt_see[cnt_listen[i]]
    except Exception as e:
        continue
    common.append(cnt_listen[i])

common.sort()
print(len(common))
for i in common:
    print(i)