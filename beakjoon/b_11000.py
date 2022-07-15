import sys

n = int(sys.stdin.readline())
time_table = list()

for i in range(n):
    time_table.append(tuple(map(int,sys.stdin.readline().strip().split())))
time_table.sort()
print(time_table)

result_list = [0 for i in range(n)]
result_num = 0
for i in range(n):
    for j in range(len(result_list)):
        if i>=1 and time_table[i-1][0] == time_table[i][0]:
            result_list[result_num] = time_table[i][1]
            result_num += 1
            break
        if result_list[j] == 0 :
            result_list[j] = time_table[i][1]
            result_num += 1
            break
        if result_list[j] <= time_table[i][0]:
            result_list[j] = time_table[i][1]
            break
# [0 0 0 0 0] Result_list
# [4 3 2 0 0]

print(result_num)