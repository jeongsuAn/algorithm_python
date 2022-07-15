import sys

n_list = list(map(int,sys.stdin.readline().strip().split(" ")))
goal = n_list[1]
coin_list = []
result = 0
coin_index = 0

for i in range(n_list[0]):
    coin_list.append(int(sys.stdin.readline()))

coin_index = len(coin_list) - 1
while goal != 0 :
    if coin_list[coin_index]>goal:
        coin_index -= 1
    else :
        result += int(goal / coin_list[coin_index])
        goal = goal % coin_list[coin_index]

print(result)