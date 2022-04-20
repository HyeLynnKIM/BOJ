import sys
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    min = b-a if a>b-a else a
    top=1
    for i in range(b, b-min, -1):
        top*=i
    for i in range(min, 1, -1):
        top/=i
    print(int(top))