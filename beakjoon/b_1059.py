import sys

size_of_S = int(sys.stdin.readline())
list_S = list(map(int,sys.stdin.readline().strip().split(" ")))
list_S.sort()

essential_num = int(sys.stdin.readline())
start_num = 0
end_num = 0
result = 0

for i in range(len(list_S)):
    if list_S[0] > essential_num:
        start_num = 1
        end_num = list_S[0]-1
        break
    if list_S[i] == essential_num:
        start_num = 0
        end_num = 0
        break
    if list_S[i] > essential_num:
        end_num = list_S[i]-1
        if i >= 1:
            start_num = list_S[i-1]+1
        elif i==0:
            start_num = 0
        break

if start_num==0 and end_num==0:
    result = 0
else:
    result = (end_num-essential_num+1)*(essential_num-start_num)+end_num-essential_num

print(result)