N = int(input())

result = []
for i in range(1667):
    for j in range(1001):
        if 3*i + 5*j == N and i+j < 9999:
            result.append(i+j)

if result:
    print(min(result))
else:
    print(-1)