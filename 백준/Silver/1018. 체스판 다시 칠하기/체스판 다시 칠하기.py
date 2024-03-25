N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

result = []

for p in range(0, N-7):
    for q in range(0, M-7):
        result1 = 0
        for i in range(8):
            for j in range(8):
                if (p+i)%2 == 0 and (q+j)%2 == 0 and board[p+i][q+j] == 'W':
                    result1 += 1
                elif (p+i)%2 == 1 and (q+j)%2 == 1 and board[p+i][q+j] == 'W':
                    result1 += 1
                elif (p+i)%2 == 0 and (q+j)%2 == 1 and board[p+i][q+j] == 'B':
                    result1 += 1
                elif (p+i)%2 == 1 and (q+j)%2 == 0 and board[p+i][q+j] == 'B':
                    result1 += 1
        result.append(result1)
        result2 = 0
        for i in range(8):
            for j in range(8):
                if (p+i)%2 == 0 and (q+j)%2 == 0 and board[p+i][q+j] == 'B':
                    result2 += 1
                elif (p+i)%2 == 1 and (q+j)%2 == 1 and board[p+i][q+j] == 'B':
                    result2 += 1
                elif (p+i)%2 == 0 and (q+j)%2 == 1 and board[p+i][q+j] == 'W':
                    result2 += 1
                elif (p+i)%2 == 1 and (q+j)%2 == 0 and board[p+i][q+j] == 'W':
                    result2 += 1
        result.append(result2)

print(min(result))