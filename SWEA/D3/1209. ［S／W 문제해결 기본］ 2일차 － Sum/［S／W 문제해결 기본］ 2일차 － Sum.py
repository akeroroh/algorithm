T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_num = []
    for i in range(100):
        sum_num.append(sum(arr[i]))

    for z in range(100):
        col_sum = 0
        for p in range(100):
            col_sum += arr[p][z]
        sum_num.append(col_sum)

    cross_sum = 0
    for q in range(100):
        cross_sum += arr[q][q]
    sum_num.append(cross_sum)

    uncross_sum = 0
    for w in range(100):
        uncross_sum += arr[w][99-w]
    sum_num.append(uncross_sum)

    max_num = max(sum_num)

    print(f'#{tc} {max_num}')