T = int(input())
for test_case in range(1, T+1):
    N, P = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(N)]

    birus_lst = []

    for i in range(N):
        for j in range(N):
            birus_num = 0
            birus_num += maps[i][j]
            for p in range(1, P+1):
                if 0 <= i+p < N:
                    birus_num += maps[i+p][j]
            for p in range(1, P + 1):
                if 0 <= i-p < N:
                    birus_num += maps[i-p][j]
            for p in range(1, P + 1):
                if 0 <= j+p < N:
                    birus_num += maps[i][j+p]
            for p in range(1, P + 1):
                if 0 <= j-p < N:
                    birus_num += maps[i][j-p]
            birus_lst.append(birus_num)

    print(f'#{test_case} {max(birus_lst)}')