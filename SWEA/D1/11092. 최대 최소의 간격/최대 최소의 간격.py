T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))

    max_p = 0
    min_p = 0

    for i in range(len(num_lst)):
        if num_lst[max_p] <= num_lst[i]:
            max_p = i
        if num_lst[min_p] > num_lst[i]:
            min_p = i

    print(f'#{test_case} {abs(max_p - min_p)}')