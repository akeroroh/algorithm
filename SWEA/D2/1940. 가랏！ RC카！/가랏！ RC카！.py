T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    command_list = [list(map(int, input().split())) for _ in range(N)]

    move = 0
    ms = 0
    for i in range(N):
        if command_list[i][0] == 0:
            move += ms
        elif command_list[i][0] == 1:
            ms += command_list[i][1]
            move += ms
        else:
            if ms < command_list[i][1]:
                ms = 0
            else:
                ms -= command_list[i][1]
                move += ms

    print(f'#{test_case} {move}')