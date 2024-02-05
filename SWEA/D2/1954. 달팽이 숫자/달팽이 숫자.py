T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    maps = [[0] * N for _ in range(N)]
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]

    d = 0
    r = 0
    c = 0
    for i in range(1, N**2+1):
        maps[r][c] = i
        nrow = r + row[d]
        ncol = c + col[d]
        if 0 <= nrow < N and 0 <= ncol < N and maps[nrow][ncol] == 0:
            r = nrow
            c = ncol
        else:
            d = d+1 if d < 3 else 0
            r = r + row[d]
            c = c + col[d]

    print(f'#{test_case}')
    for i in range(N):
        print(*maps[i])