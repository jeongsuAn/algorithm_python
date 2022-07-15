#결과값을 놓아둘 list
result_0 = []
result_1 = []

#bottom up 방식으로 문제를 해결할 예정

num = int(input())
numList = []
for i in range(num):
    numList.append(int(input()))
maxNum = max(numList)

# result_0 초기화
result_0.append(1) #result_0[0] = 1
result_0.append(0) #result_0[1] = 0

# result_1 초기화
result_1.append(0)
result_1.append(1)

for i in range(2,maxNum+1):
    result_0.append(result_0[i-2]+result_0[i-1])
    result_1.append(result_1[i-2]+result_1[i-1])

for i in numList:
    print(str(result_0[i])+" "+str(result_1[i]))