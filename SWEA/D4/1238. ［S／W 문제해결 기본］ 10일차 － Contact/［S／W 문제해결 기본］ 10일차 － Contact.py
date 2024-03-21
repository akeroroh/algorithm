def bfs(start):
    counts = 1
    queue = [[start, 1]]
    visited[start][0] = 1

    while queue:
        v, counts = queue.pop(0)

        for i in graph[v]:
            if not visited[i][0]:
                visited[i][0] = 1
                visited[i][1] = counts + 1
                queue.append([i, counts + 1])

T = 10
for test_case in range(1, T+1):
    L, S = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        n1, n2 = lst[i], lst[i+1]
        graph[n1].append(n2)
    visited = [[0, 0] for _ in range(101)]

    bfs(S)

    max_num = 0
    result = 0

    for i in range(1, 101):
        if max_num <= visited[i][1]:
            max_num = visited[i][1]
            result = i

    print(f'#{test_case} {result}')
