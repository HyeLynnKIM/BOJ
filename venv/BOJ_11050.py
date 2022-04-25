import sys
a, b = map(int, sys.stdin.readline().split())

top1, top2 = 1, 1
bot = 1
if a-b<b: b=a-b
for i in range(a, a-b, -1):
    top1*=i
    # top2*=i
    top1//=bot
    # top2/=bot # 나누기로 하면 부동소수점 때문에 답이 많이 달라짐
    bot+=1
    # print(top1, top2)
print(int(top1%10007))