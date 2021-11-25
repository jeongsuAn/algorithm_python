import sys

stack = []
result = []
_str = ""

while True:
    _str = sys.stdin.readline()
    if _str == ".\n":
        break
    yes_or_no = 1 # 1 == yes, 0 == no
    for i in range(len(_str)):
        if _str[i] == "("  or _str[i] == "[" :
            stack.append(_str[i])
        if _str[i] == ")" or _str[i] == "]" :
            if stack:
                temp = stack.pop()
            else:
                yes_or_no = 0
                break
            if temp == "(" and _str[i] == ")":
                continue
            elif temp == "[" and _str[i] == "]":
                continue
            else:
                yes_or_no = 0
                break
    if stack: #stack에 남아있는 경우 no , ex) '('만 있는 경우
        yes_or_no = 0
        stack=[]
    if yes_or_no == 0:
        result.append("no")
    else:
        result.append("yes")
for i in result:
    print(i)