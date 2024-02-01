T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(N)]

    flower_list = []
    for i in range(N):
        for j in range(M):
            bomb_num = maps[i][j]
            basic_flower_sum = maps[i][j]
            p = 1
            if j+p <M:
                basic_flower_sum += maps[i][j+p]
            if j-p >= 0:
                basic_flower_sum += maps[i][j-p]
            if i+p < N:
                basic_flower_sum += maps[i+p][j]
            if i-p >= 0:
                basic_flower_sum += maps[i-p][j]
            flower_list.append(basic_flower_sum)

    max_flower = max(flower_list)

    print(f'#{test_case} {max_flower}')