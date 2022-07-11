import sys
import math

def distance(a, b, c, x1, x2, r):
    dis = abs(a*x1+b*x2+c)/math.sqrt(math.pow(a, 2)+math.pow(b, 2))
    if dis>=r:
        return False
    else:
        return True

for i in range(int(sys.stdin.readline())):

    # count entrance
    entrance = 0

    # input x1, y1, x2, y2
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    # input coefficients of line-equation , a b c
    a, b, c = (y2-y1), (x1-x2), (x2*y1-x1*y1+x1*y1-x1*y2)

    for j in range(int(sys.stdin.readline())):
        # input circle's coordinates and diameter

        tmp_x, tmp_y, tmp_r = map(int,sys.stdin.readline().split())

        # if start == end
        if (x1 == x2) and (y1 == y2):
            continue

        # check 2 intersection points
        is_in_planet = distance(a, b, c, tmp_x, tmp_y, tmp_r)
        # is true
        if is_in_planet:
            start_line = math.sqrt(math.pow(tmp_x-x1, 2)+math.pow(tmp_y-y1, 2))
            end_line = math.sqrt(math.pow(tmp_x - x2, 2)+math.pow(tmp_y - y2, 2))
            if (start_line <= tmp_r) and (end_line <= tmp_r):
                pass
            elif (start_line >= tmp_r) and (end_line >= tmp_r):
                pass
            else:
                entrance += 1
    print(entrance)

