from collections import deque

def bfs(start):
    counts = 1

    queue = deque([[start, counts]])
    visited[start][0] = 1

    while queue:
        v, counts = queue.popleft()

        for i in graph[v]:
            if not visited[i][0]:
                visited[i][0] = 1
                visited[i][1] = counts + 1
                queue.append([i, counts + 1])

T = 10
for test_case in range(1, T + 1):
    N, S = map(int, input().split())
    num_lst = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        n1, n2 = num_lst[i], num_lst[i+1]
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
