T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ele_info = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(1, N):
            if i+j < N and ele_info[i][0] < ele_info[i+j][0] and ele_info[i][1] > ele_info[i+j][1] :
                result += 1
            elif i+j < N and ele_info[i][0] > ele_info[i + j][0] and ele_info[i][1] < ele_info[i + j][1]:
                result += 1
                
    print(f'#{test_case} {result}')