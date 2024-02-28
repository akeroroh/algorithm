def min_route(x, y, sum_route, cnt):
    global result

    if cnt == len(son_house):
        sum_route += abs(x-home[0]) + abs(y-home[1])
        if result > sum_route:
            result = sum_route
        return

    elif result < sum_route:
        return

    for i in range(len(son_house)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        min_route(son_house[i][0], son_house[i][1], sum_route + abs(x-son_house[i][0]) + abs(y-son_house[i][1]), cnt+1)
        visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    office = arr[:2]
    home = arr[2:4]
    son_house = []
    for i in range(2, N+2):
        son_house.append([arr[2*i], arr[2*i+1]])
    visited = [0] * (N+1)

    result = 999999

    min_route(office[0], office[1], 0, 0)

    print(f'#{test_case} {result}')