T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    arr_lst = []
    for i in range(N-M+1):
        sums = 0
        for j in range(M):
            if i + j < len(lst):
                sums += lst[i+j]
        arr_lst.append(sums)
    print(f'#{test_case} {max(arr_lst)-min(arr_lst)}')