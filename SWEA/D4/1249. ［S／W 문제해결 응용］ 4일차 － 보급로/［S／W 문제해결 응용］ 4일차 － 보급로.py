from heapq import heappush, heappop
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]

    direct = (0, 1), (1, 0), (-1, 0), (0, -1)

    queue = []
    heappush(queue, (0, 0, 0))
    distance[0][0] = 0

    while queue:
        weight, x, y = heappop(queue)

        if distance[x][y] < weight:
            continue

        for dir in direct:
            nx = x + dir[0]
            ny = y + dir[1]

            if 0 <= nx < N and 0 <= ny < N:
                new_weight = weight + graph[nx][ny]

                if new_weight >= distance[nx][ny]:
                    continue

                distance[nx][ny] = new_weight
                heappush(queue, (new_weight, nx, ny))

    print(f'#{test_case} {distance[N-1][N-1]}')