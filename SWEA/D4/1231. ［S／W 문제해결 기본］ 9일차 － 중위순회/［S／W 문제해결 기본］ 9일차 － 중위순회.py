def mid_order(T):
    global result_num_list
    if T:
        mid_order(left[T])
        result_num_list.append(T)
        mid_order((right[T]))

T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    left = [0]*(N+1)
    right = [0]*(N+1)

    word_dic = {}
    for i in range(N):
        word_dic[arr[i][0]] = arr[i][1]

    for i in range(N):
        len_arr = len(arr[i])
        if len_arr == 4:
            left[int(arr[i][0])] = int(arr[i][2])
            right[int(arr[i][0])] = int(arr[i][3])
        if len_arr == 3:
            left[int(arr[i][0])] = int(arr[i][2])

    result_num_list = []
    mid_order(int(1))
    sub_result = []
    for i in range(N):
        sub_result.append(word_dic[str(result_num_list[i])])
    result = ''.join(sub_result)
    print(f'#{test_case}', end=' ')
    print(result)