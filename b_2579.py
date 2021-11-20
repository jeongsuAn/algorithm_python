import sys

n = int(sys.stdin.readline())
point_list = [0]
result_list = [0]
two_step = [False]

for i in range(n):
    point_list.append(int(sys.stdin.readline()))

result_list.append(point_list[1])
two_step.append(False)
if n>1:
    result_list.append(point_list[1]+point_list[2])
    two_step.append(True)
if n>2:
    if point_list[2]+point_list[3]>point_list[1]+point_list[3]:
        result_list.append(point_list[2] + point_list[3])
        two_step.append(True)
if n>3:
    for i in range(4,n+1):
        if result_list[i-2] >= result_list[i-1] :
            result_list.append(result_list[i-2]+point_list[i])
            two_step.append(False)
        elif two_step[i-1] == True :
            result_list.append(result_list[i - 2] + point_list[i])
            two_step.append(False)
        else :
            result_list.append(result_list[i - 1] + point_list[i])
            two_step.append(True)

print(result_list[n])