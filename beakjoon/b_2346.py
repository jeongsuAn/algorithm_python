import sys

n = int(sys.stdin.readline().strip())
paper_num = list(map(int,sys.stdin.readline().strip().split(" ")))

n_list = []
len_list = n
index = 0
result_list = [1]

for i in range(2, n + 1):
    n_list.append(i)
paper = paper_num[0]
del paper_num[0]

for i in range(2, n + 1):
    len_list -= 1
    if paper >= 0 :
        index = (index + paper - 1) % len_list
    else :
        index = (index + paper) % len_list
    paper = paper_num[index]
    result_list.append(n_list[index])

    del n_list[index]
    del paper_num[index]


result = list(map(str, result_list))
result = " ".join(result)

print(result)