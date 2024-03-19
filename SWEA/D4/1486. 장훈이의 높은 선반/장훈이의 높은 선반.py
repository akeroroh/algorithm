def dfs(wichi, sum_ki):
    global result
    if wichi == N:
        if sum_ki >= B and sum_ki-B < result:
            result = sum_ki-B
        return

    visited[wichi] = True
    dfs(wichi+1, sum_ki+lst[wichi])
    visited[wichi] = False
    dfs(wichi+1, sum_ki)


T = int(input())
for test_case in range(1, T+1):
    N, B = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    visited = [False] * (N+1)
    result = 9999
    dfs(0, 0)

    print(f'#{test_case} {result}')