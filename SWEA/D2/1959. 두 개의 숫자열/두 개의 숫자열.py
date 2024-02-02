T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    max_list = []
    if len(a_list) > len(b_list):
        for i in range(N-M+1):
            x_list = []
            for j in range(M):
                x_list.append(a_list[i+j] * b_list[j])
            max_list.append(sum(x_list))
    elif len(a_list) < len(b_list):
        for i in range(M - N + 1):
            y_list = []
            for j in range(N):
                y_list.append(a_list[j] * b_list[i+j])
            max_list.append(sum(y_list))
    else:
        for i in range(N):
            z_list = []
            z_list.append(a_list[i] * b_list[i])
            max_list.append(sum(z_list))

    result = max(max_list)

    print(f'#{test_case} {result}')