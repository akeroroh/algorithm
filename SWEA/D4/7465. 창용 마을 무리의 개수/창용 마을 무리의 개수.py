def find_set(x, parents):
    if parents[x] == x:
        return x
    return find_set(parents[x], parents)

def union(x, y, parents):
    x = find_set(x, parents)
    y = find_set(y, parents)

    if x == y:
        pass

    if x < y:
        for i in range(len(parents)):
            if parents[i] == y:
                parents[i] = x
    else:
        for i in range(len(parents)):
            if parents[i] == x:
                parents[i] = y


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    parents = [i for i in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        union(x, y, parents)

    parents.remove(0)
    result = set(parents)

    print(f'#{test_case} {len(result)}')