import sys
import math
sys.setrecursionlimit(10**6)

def isprime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def gcd(num1, num2):
    if num1==num2:
        return num1
    if num1 > num2:
        num1, num2 = num2, num1
    mod, rest = num2 // (num2-num1), num2 % (num2- num1)
    if rest==0:
        return gcd(num2 - (mod - 1) * (num2 - num1), num2 - num1)
    else:
        return gcd(num2 - mod* (num2 - num1), num2 - num1)

# 소인수분해해주는 함수, 이것도 버전1보다 약간 향상시켰다. 20자리수의 경우 2배 정도 속도 향상을 보였음.
def factorize2(value):
    num = value  # 원래값을 보존한다.

    divisor_primes = []  # 분해된 인수를 차곡차곡 저장하는 리스트
    factorize_dict = {}  # 리스트의 원소 갯수를 세어 넣는 용도

    # num이 소수라면 (num, 1)을 딕셔너리에 넣어 반환한다.
    # if isprime(num):
    #    factorize_dict[num] = 1
    #    return factorize_dict

    root_val = int(num ** 0.5) + 1
    # 인수분해 루틴은 소수 판정 루틴과는 조금 다르게 접근할 필요가 있다.
    i = 2
    found = False
    while True:
        # 소수 검증 때처럼 num까지 모두 나누어볼 필요는 없고 제곱근값 까지만 나누어보면 된다.
        if i >= root_val: break

        # i가 소수인지 검사해서 소수라면 num을 i로 나눈다
        # i로 나눠서 나머지가 0이라면, 인수분해가 한번 된 것이다.
        if isprime(i) and num % i == 0:
            divisor_primes.append(i)  # 나누는 수를 저장
            num = num // i  # 몫, 가령 24//2 = 12
            # print(f"{i}, {num}")
            root_val = int(num ** 0.5) + 1
            if found == False:
                found = True  # 찾았다는 표시를 함
            # 12는 소수가 아니므로 반복문 계속. 소수가 나오면 그 소수를 저장하고 반복문 종료.
            if isprime(num):
                divisor_primes.append(num)
                break  # return divisor_primes
            # i = 2 # 인수분해를 한번 했으므로 숫자를 다시 2부터 나눠보기로 설정
        else:
            i += 1  # 인수분해가 되지 않으면 젯수(나누는 수)를 1증가
    # print(divisor_primes)

    for n in divisor_primes:
        if n in factorize_dict:
            factorize_dict[n] += 1
        else:
            factorize_dict[n] = 1

    if found == False:  # 소인수를 못 찾았다면 소수이므로
        factorize_dict[value] = 1

    return factorize_dict


# 약수 구하는 함수: 향상된 버전
# 소인수분해 결과를 가지고 약수를 만듦
# 숫자가 클 경우, 속도 면에서 단순한 방식(버전1)보다 훨씬 빠름
# 50234902430546664의 약수를 구했을 때 버전2가 1초 걸리고, 버전1이 35초 걸림.
def getDivisor2(num):
    divisors = []
    res = factorize2(num)  # 예) {2:3, 3:2, 7:1} 형태

    for key, value in res.items():
        divisor = []
        for i in range(value + 1):
            divisor.append(key ** i)
        divisors.append(divisor)
    # divisors : [[2**0, 2**1, 2**2, 2**3], [3**0, 3**1, 3**2], [7**0, 7**1]]
    # divisors : [[1, 2, 4, 8], [1, 3, 9], [1, 7]]

    while True:
        tmp = []  # 리스트 2개 원소를 서로 곱해서 약수를 만들어 임시 저장

        # 리스트를 하나씩 줄여나가는데 리스트가 하나만 남았으면 그것이 약수 집합이므로 종료한다
        if len(divisors) < 2:
            break
        # 리스트 2개의 각 원소를 서로 곱해서 약수를 만들어 저장
        for n in divisors[0]:
            for m in divisors[1]:
                tmp.append(n * m)

        # divisors 안의 리스트는 예에서 3개이고, 리스트[0]과 [1]을 곱해서 약수를 만들고(tmp),
        # 기존 리스트[0]과 리스트 [1]을 삭제하고 1차 약수 리스트인 tmp를 리스트[0] 자리에 끼워넣는다.
        # 한번 실행을 거치면 이제 리스트 목록은 총 2개가 되었다.
        del divisors[0]  # 원래 divisors[0] 삭제
        del divisors[0]  # 원래 divisors[1] 삭제
        divisors.insert(0, tmp)  # 생성된 tmp를 divisors 제일 앞에 끼워넣기

        # 원래는 아래의 인덱싱 방식으로 코딩을 하다가, 그냥 원소를 하나씩 나열해서 처리하는 것이
        # 훨씬 나을 것 같았다. 실제로도 나았고...
        # for j in range(len(divisors[0])):  # 0~3
        #  for k in range(len(divisors[1])): # 0~2
        #    tmp.append(divisors[0][j] * divisors[1][k]) # [0][0] * [1][0]
    return sorted(divisors[0])  # 리스트의 리스트이므로 바깥 대괄호를 제거하고 정렬해서 반환

numbers = []
for i in range(int(sys.stdin.readline())):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)
total_list = []
gcd_list = []
if len(numbers)<2:
    if len(numbers)==0:
        print()
    else:
        pri_list = getDivisor2(numbers[0])
        for p in pri_list:
            if p > 1:
                print(p, end=' ')
else:
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

        pri_list = getDivisor2(gcd_list[0])
        for p in pri_list:
            if p>1:
                print(p, end=' ')
    else:
        pri_list = getDivisor2(total_list[0])
        for p in pri_list:
            if p>1:
                print(p, end=' ')