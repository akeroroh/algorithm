T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    maps = [list(input()) for _ in range(N)]

    secret_num = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if maps[i][j] == '1':
                map_x = i
                map_y = j
                break

    for i in range(56):
        secret_num.append(maps[map_x][map_y-55+i])

    key_dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    result1 = []
    for i in range(0, 56, 7):
        sub_result = []
        for j in range(7):
            sub_result.append(secret_num[i+j])
        result1.append(sub_result)

    result2 = []
    for i in range(8):
        result2.append(''.join(result1[i]))

    result3 = []
    for i in range(8):
        result3.append(key_dic[result2[i]])

    odd_sum = 0
    oddx_sum = 0
    for i in range(8):
        if i%2 == 0:
            odd_sum += result3[i]
        else:
            oddx_sum += result3[i]
    result4 = odd_sum*3+oddx_sum

    if result4%10 == 0:
        print(f'#{test_case} {sum(result3)}')
    else:
        print(f'#{test_case} 0')