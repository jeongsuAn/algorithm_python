import sys

n = int(sys.stdin.readline().strip())
n_list = list(map(int, sys.stdin.readline().strip().split(" ")))
result = 0
temp_num = 0
n_list.sort()

for i in range(0, len(n_list)):
    temp_num = n_list[i]+temp_num
    result += temp_num

print(result)
