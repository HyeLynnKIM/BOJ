import sys

def search(target, s):
    sta=0
    end=len(s)-1

    while(sta<=end):
        mid = (sta+end)//2
        if s[mid]==target:
            return 1
        elif s[mid]<target:
            sta=mid+1
        else: end=mid-1
    return 0

n, m = map(int, sys.stdin.readline().split())
s = []
check = []
sum=0

for i in range(n):
    s.append(sys.stdin.readline().rstrip())
s.sort()
for i in range(m):
    check.append(sys.stdin.readline().rstrip())
check.sort()

for i in check:
    if search(i, s): sum+=1
print(sum)