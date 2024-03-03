N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maps = [[0]*100 for _ in range(100)]

for i in range(N):
    for j in range(arr[i][0], arr[i][0]+10):
        for p in range(arr[i][1], arr[i][1]+10):
            maps[j][p] = 1

result = 0
for i in range(100):
    for j in range(100):
        if maps[i][j] > 0:
            result += 1

print(result)