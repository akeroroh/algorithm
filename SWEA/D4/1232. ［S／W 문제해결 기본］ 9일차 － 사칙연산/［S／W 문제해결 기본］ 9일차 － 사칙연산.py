T = 10
for test_case in range(1, T+1):
    N = int(input())
    num_arr = [list(input().split()) for _ in range(N)]
    for i in range(N-1, -1, -1):
        if num_arr[i][1] == '+':
            num_arr[i][1] = int(num_arr[int(num_arr[i][2])-1][1]) + int(num_arr[int(num_arr[i][3])-1][1])
        elif num_arr[i][1] == '-':
            num_arr[i][1] = int(num_arr[int(num_arr[i][2])-1][1]) - int(num_arr[int(num_arr[i][3])-1][1])
        elif num_arr[i][1] == '*':
            num_arr[i][1] = int(num_arr[int(num_arr[i][2])-1][1]) * int(num_arr[int(num_arr[i][3])-1][1])
        elif num_arr[i][1] == '/':
            num_arr[i][1] = int(num_arr[int(num_arr[i][2])-1][1]) / int(num_arr[int(num_arr[i][3])-1][1])

    print(f'#{test_case} {int(num_arr[0][1])}')