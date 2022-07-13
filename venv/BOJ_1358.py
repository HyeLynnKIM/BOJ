import sys
import math

# get widht, height, x, y, the number of people
width, height, x, y, person = map(int, sys.stdin.readline().split())

# cnt_people
cnt_person = 0
radius = int(height / 2)

# iteration for 'person' times
for i in range(person):
    p_x, p_y = map(int, sys.stdin.readline().split())

    # if p_x is less than first x coordinate (in left hemisphere)
    if p_x <= x:
        if math.sqrt(math.pow((x-p_x), 2) + math.pow(((y + radius)-p_y), 2)) <= radius:
            cnt_person += 1
    # if p_x is less than x + width and more than x (in rectangle)
    elif x < p_x < (x+width):
        if y <= p_y <= y+height:
            cnt_person += 1
    # if p_x is more than x + width (in right hemisphere)
    else:
        if math.sqrt(math.pow(((x + width)-p_x), 2) + math.pow(((y + radius)-p_y), 2)) <= radius:
            cnt_person += 1
print(cnt_person)