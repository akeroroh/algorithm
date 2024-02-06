T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    num_dic = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}

    mul = 1
    while sum(num_dic.values()) < 10:
        num_list = list(map(int, str(N * mul)))

        for i in num_list:
            num_dic[i] = 1

        mul += 1

    print(f'#{test_case} {(mul-1)*N}')