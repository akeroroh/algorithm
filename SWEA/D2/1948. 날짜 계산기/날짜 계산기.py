T = int(input())
for test_case in range(1, T + 1):
    M1, D1, M2, D2 = list(map(int, input().split()))

    day_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    days = 0
    if M2-M1 == 0:
        days = D2 - D1 + 1
    elif M2-M1 == 1:
        days = D2 + (day_dic[M1]-D1) + 1
    else:
        days = D2 + (day_dic[M1]-D1) + 1
        for i in range(M1+1, M2):
            days += day_dic[i]

    print(f'#{test_case} {days}')