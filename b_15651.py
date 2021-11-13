result = []

inputNum = list(map(int, input().split()))
N = inputNum[0]
M = inputNum[1]

def backtracking(stepNum,tempStr):
    # 첫번째 인자 : 몇번째 문자를 고르는 중인지?
    # 두번째 인자 : 지금까지 골라놓은 string 을 저장해놓은 것

    if(len(tempStr) >= 2*M-1):
        result.append(tempStr)
        return

    for i in range(1,N+1):
        backtracking(stepNum+1,tempStr+str(i)+" ")



backtracking(0,"")
for i in range(len(result)):
    print(result[i])