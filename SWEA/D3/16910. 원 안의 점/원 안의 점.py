T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if i**2 + j**2 <= N**2:
                count += 1
    print(f'#{test_case} {count*4+(N*4)+1}')