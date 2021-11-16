#bottom up 방식을 사용한다.

# 3차원 배열 선언
result = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]


for i in range(21):
    for j in range(21):
        result[0][i][j] = 1
        result[i][0][j] = 1
        result[i][j][0] = 1

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i<j and j<k:
                result[i][j][k] = result[i][j][k-1]+result[i][j-1][k-1]-result[i][j-1][k]
            else:
                result[i][j][k] = result[i-1][j][k]+result[i-1][j-1][k]+result[i-1][j][k-1]-result[i-1][j-1][k-1]


while True:
    numList=list(map(int,input().split()))
    if numList[0]==-1 and numList[1]==-1 and numList[2]==-1:
        break
    elif numList[0]<=0 or numList[1]<=0 or numList[2]<=0:
        print("w("+str(numList[0])+", "+str(numList[1])+", "+str(numList[2])+") = 1")
    elif numList[0]>20 or numList[1]>20 or numList[2]>20:
        print("w(" + str(numList[0]) + ", " + str(numList[1]) + ", " + str(numList[2]) + ") = "+str(result[20][20][20]))
    else :
        print("w(" + str(numList[0]) + ", " + str(numList[1]) + ", " + str(numList[2]) + ") = " + str(result[numList[0]][numList[1]][numList[2]]))