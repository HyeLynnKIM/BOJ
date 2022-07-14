import sys
import copy

def gcd(num1, num2):
    if num1==num2:
        return num1
    if num1 > num2:
        num1, num2 = num2, num1
    mod, rest = num2 // (num2-num1), num2 % (num2- num1)
    if rest==0:
        return gcd(num2-(mod-1)*(num2-num1), num2-num1)
    else:
        return gcd(num2 - mod* (num2 - num1), num2 - num1)

numbers = []
for i in range(int(sys.stdin.readline())):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)
total_list = []
gcd_list = []

for i in range(0, len(numbers)):
    for t in range(i+1, len(numbers)):
        total_list.append(numbers[t] - numbers[i])

if len(total_list)!=1:
    for i in range(len(total_list)-1):
        gcd_list.append(gcd(total_list[i], total_list[i+1]))

    while(len(gcd_list)!=1):
        temp_list = [j for j in gcd_list]
        gcd_list = list()
        for i in range(len(temp_list)-1):
            gcd_list.append(gcd(temp_list[i], temp_list[i+1]))

    for i in range(2, gcd_list[0]+1):
        if gcd_list[0]%i==0:
            print(i, end=' ')
else:
    for i in range(2, total_list[0] + 1):
        if gcd_list[0] % i == 0:
            print(i, end=' ')