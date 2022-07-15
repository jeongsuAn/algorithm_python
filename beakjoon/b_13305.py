import sys
n = int(sys.stdin.readline())
range_list = list(map(int, sys.stdin.readline().split(" ")))
oil_cost_list = list(map(int, sys.stdin.readline().split(" ")))
cur = 0
result = 0

for i in range(1,n-1):
    if oil_cost_list[cur]<=oil_cost_list[i]:
        result += range_list[i]*oil_cost_list[i]
    else :
        result += range_list[i] * oil_cost_list[i]
        cur = i

print(result)