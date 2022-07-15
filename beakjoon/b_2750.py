import sys
sys.setrecursionlimit(10**6)


def partition(start, end, array):
    pivot_index = start
    pivot= array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start < end :
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end

def quick_sort(start, end,array):

    if (start < end):
        p = partition(start,end,array)

        quick_sort(start,p-1,array)
        quick_sort(p + 1, end, array)

n = int(sys.stdin.readline())
num_list = list()
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

quick_sort(0,len(num_list)-1,num_list)


for i in range(len(num_list)):
    print(num_list[i])