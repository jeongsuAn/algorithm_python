result = []

result.append(0)
result.append(1)
result.append(2)

num = int(input())
for i in range(3,num+1):
    result[i%3]=((result[(i-1)%3]+result[(i-2)%3])%15746)

print(result[num%3]%15746)