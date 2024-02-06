T = int(input())
for test_case in range(1, T + 1):
    arr_list = [list(map(str, input())) for _ in range(5)]

    test_list = [['*'] * 5 for _ in range(15)]
    for i in range(15):
        for j in range(15):
            try:
                test_list[i][j] = arr_list[j][i]
            except:
                pass

    result = [''.join(test_list[_]) for _ in range(15)]
    result2 = ''.join(result)
    result3 = result2.replace('*','')

    print(f'#{test_case} {result3}')