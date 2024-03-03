arr = [list(map(int, input().split())) for _ in range(9)]

max_result = -1
result_index = (0, 0)
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_result:
            max_result = arr[i][j]
            result_index = (i+1, j+1)

print(max_result)
print(*result_index)