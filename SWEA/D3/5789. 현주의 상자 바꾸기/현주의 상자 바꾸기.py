T = int(input())
for test_case in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    lr_list = [list(map(int, input().split())) for _ in range(Q)]

    box_list = [0] * N
    for i in range(Q):
        for j in range(lr_list[i][0]-1, lr_list[i][1]):
            box_list[j] = i+1

    print(f'#{test_case}', end=' ')
    for i in range(N):
        print(box_list[i], end=' ')
    print()