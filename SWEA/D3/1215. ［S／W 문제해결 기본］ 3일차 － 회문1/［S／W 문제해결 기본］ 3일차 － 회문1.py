T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]


    count = 0
    for i in range(8):
        for j in range(8-N+1):
            palindrome_check = []
            for q in range(N):
                palindrome_check.append(arr[i][j+q])
            if palindrome_check == palindrome_check[::-1]:
                count += 1

    for i in range(8):
        for j in range(8-N+1):
            palindrome_check = []
            for q in range(N):
                palindrome_check.append(arr[j+q][i])
            if palindrome_check == palindrome_check[::-1]:
                count += 1

    print(f'#{test_case} {count}')