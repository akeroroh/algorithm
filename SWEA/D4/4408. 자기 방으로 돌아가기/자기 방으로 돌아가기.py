T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    room_lst = [list(map(int, input().split())) for _ in range(N)]

    go_lst = [0] * 201
    for room in room_lst:
        start = min(room[0], room[1])
        end = max(room[0], room[1])
        for i in range((start+1)//2, (end+1)//2+1):
            go_lst[i] += 1

    print(f'#{test_case} {max(go_lst)}')