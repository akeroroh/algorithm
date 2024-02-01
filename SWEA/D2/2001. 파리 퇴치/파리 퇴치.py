T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(N)]

    sum_lst = []
    for i in range(N-M+1):
        for z in range(N-M+1):
            kill_fly = 0
            for q in range(i, i+M):
                for p in range(z, z+M):
                    kill_fly += maps[q][p]
                sum_lst.append(kill_fly)

    max_kill = max(sum_lst)

    print(f'#{test_case} {max_kill}')