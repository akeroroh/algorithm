dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def map_tracking(start):
    cnt = 0
    stack = [start]

    while stack:
        x, y = stack.pop()
        cnt += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] + 1 == arr[nx][ny]:
                stack.append((nx, ny))

    return cnt

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    result = [9999, 0]
    for i in range(N):
        for j in range(N):
            cnt = map_tracking((i, j))
            if cnt > result[1]:
                result[1] = cnt
                result[0] = arr[i][j]
            elif cnt == result[1]:
                if arr[i][j] < result[0]:
                    result[0] = arr[i][j]

    print(f'#{test_case} {result[0]} {result[1]}')