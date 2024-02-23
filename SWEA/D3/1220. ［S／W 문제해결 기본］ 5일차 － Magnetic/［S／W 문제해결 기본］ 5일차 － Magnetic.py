T = 10
for test_case in range(1, T+1):
    length = input()
    maps = [list(map(int, input().split())) for _ in range(100)]

    map2 = []
    for i in range(100):
        sum_lst = []
        for j in range(100):
            if maps[j][i] > 0:
                sum_lst.append(maps[j][i])
        map2.append(sum_lst)

    result = 0
    for i in range(len(map2)):
        for j in range(len(map2[i])-1):
            if map2[i][j] == 1 and map2[i][j+1] == 2:
                result += 1

    print(f'#{test_case} {result}')
