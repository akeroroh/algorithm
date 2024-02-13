def dfs(S, G):
    stack = []
    stack.append(S)

    while stack:
        v = stack.pop()

        if visited[v] == 0:
            visited[v] = 1

            for w in range(1, 101):
                if graph[v][w] == 1 and visited[w] == 0:
                    if w == G:
                        return 1
                    stack.append(w)
    return 0

T = 10
for test_case in range(1, T+1):
    tc, road_num = map(int, input().split())

    arr = list(map(int, input().split()))
    visited = [0 for _ in range(101)]
    graph = [[0 for _ in range(101)] for _ in range(101)]

    for i in range(road_num):
        n1, n2 = arr[i*2], arr[i*2+1]
        graph[n1][n2] = 1

    print(f'#{test_case} {dfs(0, 99)}')