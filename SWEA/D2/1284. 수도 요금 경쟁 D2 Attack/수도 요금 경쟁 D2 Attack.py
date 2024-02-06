T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = list(map(int, input().split()))

    water_list = []

    water_list.append(W * P)

    if W > R:
        water_list.append(Q + (W-R) * S)
    else:
        water_list.append(Q)

    min_water = min(water_list)

    print(f'#{test_case} {min_water}')