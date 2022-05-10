import sys
n, m = map(int, sys.stdin.readline().split())
pokemon1 = {} # key: index, value: pokemon
pokemon2 = {} # key: pokemon, value: index
quiz = []
for i in range(1,n+1):
    tmp = sys.stdin.readline().rstrip()
    pokemon1[i] = tmp# 그냥 readline() 하면 개행문자 포함
    pokemon2[tmp] = i

for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    try:
        tmp = int(tmp)
        print(pokemon1[tmp])
    except Exception as e:
        print(pokemon2[tmp])