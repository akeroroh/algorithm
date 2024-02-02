T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_maps = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(num_maps[N-1-j][i], end='')
        print(' ', end='')
        for j in range(N):
            print(num_maps[N-1-i][N-1-j], end='')
        print(' ', end='')
        for j in range(N):
            print(num_maps[j][N-1-i], end='')
        print(' ', end='')
        print()
