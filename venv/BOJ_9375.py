import sys

# count tc case
tc = int(sys.stdin.readline())

# iterate for tc times
for i in range(tc):

    # count a number of clothes
    clothes = int(sys.stdin.readline())
    # make cloth dict
    cloth = {}

    # iterate for appending dict
    for i in range(clothes):
        in_cloth = list(sys.stdin.readline().split())
        cloth_value = []
        if in_cloth[1] not in cloth.keys():
            cloth[in_cloth[1]] = cloth_value
            cloth[in_cloth[1]].append(in_cloth[0])
        else: cloth[in_cloth[1]].append(in_cloth[0])

    # count all cases
    if len(cloth.keys())==1:
        for i in cloth.keys():
            print(len(cloth[i]))
            break
    else:
        cnt = 1
        for i in cloth.keys():
            cnt *= len(cloth[i])+1
        # 각 wear마다 안입음+하나라도 입는 경우의수 모두 곱하고 알몸인 경우 1빼기
        print(cnt-1)

