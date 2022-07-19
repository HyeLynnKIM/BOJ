import sys

# counting def for 2 and 5
def counting(tmp: int, num: int):
    cnt = 0
    while tmp>=num:
        cnt += tmp//num
        tmp//=num
    return cnt

n, m = map(int, sys.stdin.readline().split())
print(min(counting(n, 2)-(counting(m, 2) + counting(n-m, 2)), counting(n, 5)-(counting(m, 5) + counting(n-m, 5))))