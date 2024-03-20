def dfs(cnt, point):
    global result

    if point <= result:
        return

    if cnt == N:
        result = max(point, result)
        return

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            dfs(cnt+1, point * (lst[cnt][i]/100))
            visited[i] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    result = 0
    dfs(0, 1)

    print(f'#{test_case} {result*100:.6f}')