T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr_list = [list(map(int, input().split())) for _ in range(M)]

    maps = [[0] * N for i in range(N)]
    maps[N//2-1][N//2-1] = 2
    maps[N//2][N//2] = 2
    maps[N//2-1][N//2] = 1
    maps[N//2][N//2-1] = 1

    direct = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while arr_list:
        x, y, c = arr_list.pop(0)
        maps[y-1][x-1] = c

        for dy, dx in direct:
            ny, nx = y - 1 + dy, x - 1 + dx
            change = [[ny, nx]]

            while -1 < nx < N and -1 < ny < N and maps[ny][nx] != 0 and c != maps[ny][nx]:
                ny, nx = ny + dy, nx + dx
                change.append([ny, nx])

            if len(change) > 1 and -1 < nx < N and -1 < ny < N and maps[ny][nx] != 0:
                for i, j in change:
                    maps[i][j] = c

    black_stone = 0
    white_stone = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                black_stone += 1
            elif maps[i][j] == 2:
                white_stone += 1

    print(f'#{test_case} {black_stone} {white_stone}')