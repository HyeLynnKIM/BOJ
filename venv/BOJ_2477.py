import sys

def fineMainIdx(dir_line: list, num: list):
    # init idx variable
    idx = 0

    # if-else: at each 6-angles rectangels case
    if num[0]==2:
        if num[2]==2: #1 - 423131 (one 4, one 2, two 3 and 1)
            for i in range(len(dir_line)):
                if dir_line[i][0] == 4:
                    idx = i
        else: #2 - 231414 (one 2, one 3, two 4 and 1)
            for i in range(len(dir_line)):
                if dir_line[i][0] == 2:
                    idx = i
    else:
        if num[3]==1: #3 - 142323 (one 1, one 4, two 2 and 3)
            for i in range(len(dir_line)):
                if dir_line[i][0] == 1:
                    idx = i
        else: #4 - 314242 (one 3, one 1, two 4 and 2)
            for i in range(len(dir_line)):
                if dir_line[i][0] == 3:
                    idx = i
    return idx

def main():
    # how many melon in 1 m^2
    oriental_melon = int(sys.stdin.readline())

    # store drawing line (direction, length)
    dir_line = []
    number = [0 , 0, 0 , 0]

    for i in range(6): # 6-angles
        dir, line = map(int, sys.stdin.readline().split())
        dir_line.append([dir, line])
        number[dir-1] += 1

    # find Main Index
    idx = fineMainIdx(dir_line, number)

    # The line that only one comes out is the maximum width
    long_wid, long_hei = dir_line[idx][1], 0
    if idx + 1 > 5: long_hei = dir_line[0][1]
    else: long_hei = dir_line[idx + 1][1]

    # The area that should be subtracted from the main index by a certain distance
    sub_wid, sub_hei = dir_line[idx - 2][1], 0

    if idx > 2: sub_hei= dir_line[idx - 3][1]
    else: sub_hei = dir_line[idx + 3][1]

    print(oriental_melon*(long_wid * long_hei-sub_wid * sub_hei))

if __name__=='__main__':
    main()