import sys

n = int(sys.stdin.readline())

list_n = []



for i in range(n):
    list_n.append([])
    list_n[i] = list(map(int,sys.stdin.readline().strip().split(" ")))

for i in range(1,n):
    for j in range(len(list_n[i])):
        if j==0 :
            list_n[i][j] = list_n[i-1][0]+list_n[i][j]
        elif j == len(list_n[i])-1:
            list_n[i][j] = list_n[i-1][len(list_n[i])-2]+list_n[i][j]
        else :
            list_n[i][j] = max(list_n[i-1][j-1],list_n[i-1][j])+list_n[i][j]


print(max(list_n[i]))