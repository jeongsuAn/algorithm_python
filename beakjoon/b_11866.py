import sys

n, k = map(int, sys.stdin.readline().strip().split(" "))

n_list = []
len_list = n
index = 0
result_list = []

for i in range(1, n + 1):
    n_list.append(i)
print(n_list)

for i in range(1, n + 1):
    index = (index + k - 1) % len_list
    result_list.append(n_list[index])
    len_list -= 1
    del n_list[index]

result = list(map(str, result_list))
result = ", ".join(result)
result = "<" + result + ">"

print(result)
