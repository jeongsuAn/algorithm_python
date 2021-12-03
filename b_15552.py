import sys

n = int(sys.stdin.readline())
result = list()

for i in range(n):
    list= sys.stdin.readline().strip().split(" ")
    result.append(int(list[0])+int(list[1]))

for i in result:
    print(i)
