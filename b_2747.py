import sys

n = int(sys.stdin.readline())

list_n = [0,1]

if n > 1 :
    for i in range(1,n):
        list_n.append(list_n[i-1]+list_n[i])

print(list_n[n])