T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N+1)]

    center = []
    village_map = []
    for i in range(N+1):
        for j in range(N+1):
            if maps[i][j] == 2:
                center.append([i, j])
            elif maps[i][j] == 1:
                village_map.append([i, j])

    width_lst = []
    for i in village_map:
        width_lst.append(((i[0]-center[0][0])**2)+((i[1]-center[0][1])**2))

    result = 1
    while result**2 < max(width_lst):
        result += 1

    print(f'#{test_case} {result}')