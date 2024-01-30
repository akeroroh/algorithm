T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = input()


    if num_list.count('0') == N:
        counts = 0
    elif num_list.count('1') == N:
        counts = N
    else:
        num = list(map(len, num_list.split('0')))
        counts = max(num)

    print(f'#{test_case} {counts}')