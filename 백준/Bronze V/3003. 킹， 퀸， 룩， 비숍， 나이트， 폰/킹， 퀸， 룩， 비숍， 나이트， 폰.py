white_chess = list(map(int, input().split()))

right_chess = [1, 1, 2, 2, 2, 8]

result = []
for i in range(6):
    result.append(right_chess[i]-white_chess[i])

print(*result)