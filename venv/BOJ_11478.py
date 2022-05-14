import sys

s = sys.stdin.readline().rstrip()
part = [s]

for i in range(1,len(s)):
    for j in range(len(s)-i+1):
        part.append(s[j:j+i])
        
print(len(set(part)))
