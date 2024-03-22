from heapq import heappush, heappop

T = int(input())
for test_case in range(1, T+1):
    N, M, X = map(int, input().split())

    graph1 = [[] for _ in range(N+1)]
    graph2 = [[] for _ in range(N+1)]
    for i in range(M):
        x, y, c = map(int, input().split())
        graph1[x].append((y, c))
        graph2[y].append((x, c))

    INF = int(11e9)
    distance1 = [INF] * (N+1)

    queue1 = []
    heappush(queue1, (X, 0))
    distance1[X] = 0

    while queue1:
        now, weight = heappop(queue1)
        if distance1[now] < weight:
            continue

        for to in graph1[now]:
            next_node = to[0]
            next_weight = to[1]

            new_weight = weight + next_weight
            if new_weight >= distance1[next_node]:
                continue

            distance1[next_node] = new_weight
            heappush(queue1, (next_node, new_weight))

    distance2 = [10001] * (N+1)

    queue2 = []
    heappush(queue2, (X, 0))
    distance2[X] = 0

    while queue2:
        now, weight = heappop(queue2)
        if distance2[now] < weight:
            continue

        for to in graph2[now]:
            next_node = to[0]
            next_weight = to[1]

            new_weight = weight + next_weight
            if new_weight >= distance2[next_node]:
                continue

            distance2[next_node] = new_weight
            heappush(queue2, (next_node, new_weight))

    result = 0
    for i in range(1, N+1):
        result = max(result, (distance1[i]+distance2[i]))

    print(f'#{test_case} {result}')