T = int(input())
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
day28 = [2]
for test_case in range(1, T + 1):
    day = ''
    arr = list(map(int, input()))
    num = []
    for i in range(len(arr)):
        num.append(arr[i])
    if int(''.join(map(str, num[4:6]))) in month:
        if int(''.join(map(str, num[4:6]))) in day31:
            if int(''.join(map(str, num[6:8]))) <= 31:
                day = f'{"".join(map(str, num[0:4]))}/{"".join(map(str, num[4:6]))}/{"".join(map(str, num[6:8]))}'
            else:
                day = -1
        if int(''.join(map(str, num[4:6]))) in day30:
            if int(''.join(map(str, num[6:8]))) <= 30:
                day = f'{"".join(map(str, num[0:4]))}/{"".join(map(str, num[4:6]))}/{"".join(map(str, num[6:8]))}'
            else:
                day = -1
        if int(''.join(map(str, num[4:6]))) in day28:
            if int(''.join(map(str, num[6:8]))) <= 28:
                day = f'{"".join(map(str, num[0:4]))}/{"".join(map(str, num[4:6]))}/{"".join(map(str, num[6:8]))}'
            else:
                day = -1
    else:
        day = -1
    print(f'#{test_case} {day}')