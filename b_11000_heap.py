import sys
import heapq

n = int(sys.stdin.readline())
time_table = list()

for i in range(n):
    time_table.append(tuple(map(int,sys.stdin.readline().strip().split())))
time_table.sort()


result_list = []
heapq.heappush(result_list,time_table[0][1])
result_num = 1
for i in range(1,n):
    if result_list[0] <= time_table[i][0] :
        heapq.heappop(result_list)
        heapq.heappush(result_list,time_table[i][1])
    elif result_list[0] > time_table[i][0]:
        heapq.heappush(result_list,time_table[i][1])
        result_num += 1

print(result_num)

# [] Result_list
# [3 4 5]