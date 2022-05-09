import sys
# time complexity: O(log(N))
def bi_search(target, n_list):
    sta = 0;
    end = len(n_list)-1

    while(sta<=end):
        mid = (sta+end) // 2

        if n_list[mid]==target:
            return 1
        elif n_list[mid]<target:
            sta = mid + 1
        else:
            end = mid - 1
    return 0

n = int(sys.stdin.readline())
s_list = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for index, target_number in enumerate(m_list):
    if bi_search(target_number, s_list): print("1", end=" ")
    else: print("0", end=" ")