import sys

n = int(sys.stdin.readline())

list_n = [0,1,2]

if n > 2 :
    for i in range(1,n):
        list_n.append(list_n[i]+list_n[i+1])

print(list_n[n]%10007)