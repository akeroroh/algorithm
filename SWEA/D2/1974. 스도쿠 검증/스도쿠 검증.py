T = int(input())
for test_case in range(1, T + 1):
    maps = [list(map(int, input().split())) for _ in range(9)]

    cnt = 0
    for i in range(9):
        if len(set(maps[i])) == 9:
            cnt += 1

    for j in range(9):
        maps_sudoku = []
        for i in range(9):
            maps_sudoku.append(maps[i][j])
        if len(set(maps_sudoku)) == 9:
            cnt += 1

    for i in 0, 3, 6:
        for j in 0, 3, 6:
            maps_sudoku2 = []
            for p in range(3):
                for q in range(3):
                    maps_sudoku2.append(maps[p][q])
            if len(set(maps_sudoku2)) == 9:
                cnt += 1

    result = 0
    if cnt == 27:
        result =1

    print(f'#{test_case} {result}')
