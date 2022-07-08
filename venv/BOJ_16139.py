import sys

def main():
    mystring = sys.stdin.readline().rstrip()

    # add array for all alphabet
    arr = [[0] * 26]

    # count a number of char at each character
    for i in range(len(mystring)):
        arr[i][ord(mystring[i]) - 97] += 1 # ith string, count a number of char in 2-dimensional matrix
        if i==len(mystring)-1: break # At the last, break iteration
        arr.append(arr[-1][:]) # If it it not the last, copy last 2-dimensional matrix

    # iteration
    for i in range(int(sys.stdin.readline())):
        findStr, start, end = sys.stdin.readline().split()
        if int(start)==0:
            print(arr[int(end)][ord(findStr) - 97]) # if start is the first, print only endth value
        else:
            print(arr[int(end)][ord(findStr)-97]-arr[int(start)-1][ord(findStr)-97])

if __name__ == "__main__":
    main()