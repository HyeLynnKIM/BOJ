import sys
a, b = map(int, sys.stdin.readline().split())
a_list = set(list(map(int, sys.stdin.readline().split())))
b_list = set(list(map(int, sys.stdin.readline().split())))

com_list = a_list & b_list
print(len(a_list - com_list)+len(b_list - com_list))