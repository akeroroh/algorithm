T = 10
for test_case in range(1, T + 1):
    N = int(input())
    dump_lst = list(map(int, input().split()))
    for i in range(N):
        max_index = dump_lst.index(max(dump_lst))
        min_index = dump_lst.index(min(dump_lst))
        dump_lst[max_index] -= 1
        dump_lst[min_index] += 1

    print(f'#{test_case} {max(dump_lst) - min(dump_lst)}')