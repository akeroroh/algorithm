from heapq import heappush, heappop


def prim(start):
    pq = [(0, start)]
    MST = [0] * N
    sum_weight = 0

    while pq:
        weight, now = heappop(pq)

        if MST[now] == 1:
            continue

        if sum(MST) == N:
            break

        MST[now] = 1
        sum_weight += weight

        for to, weight in graph[now]:
            if not MST[to]:
                heappush(pq, (weight, to))

    return sum_weight

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    X_lst = list(map(int, input().split()))
    Y_lst = list(map(int, input().split()))
    E = float(input())

    graph = [[0] * N for _ in range(N)]
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j :
                graph[i].append((j, (X_lst[i]-X_lst[j])**2 + (Y_lst[i]-Y_lst[j])**2))

    print(f'#{test_case} {round(prim(0)*E)}')